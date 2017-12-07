from django.shortcuts import render
from . models import GPU, CPU, RAM, PS
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import datetime


def index(request):
    return render(request, 'myapp/index.html',)


def budget(request):
    if request:
        global bdgt
        ip = request.POST['Budget']
        bdgt = int(ip)
        global best_gpu
        best_gpu = GPU.objects.filter(cost__lte=bdgt)

    else:
        return render(request, 'myapp/index.html', {'err_m': "Error"})

    return render(request, 'myapp/index.html', {'gpu': best_gpu})


def selectcpu(request):

    if request:
        best_gpu = GPU.objects.get(name=request.POST['GPU_name'])
        final_name = best_gpu.name
        request.session['final_name'] = final_name
        global checkcost
        checkcost = int(bdgt-best_gpu.cost)
        request.session['checkcost'] = checkcost
        global best_cpu
        if checkcost:
            best_cpu = CPU.objects.filter(cost__lte=checkcost)

    else:
        return render(request, 'myapp/index.html', {'err_m': "Error"})

    return render(request, 'myapp/index.html', {'cpu': best_cpu})


def selectram(request):
    if request:
        checkcost = request.session['checkcost']
        best_cpu = CPU.objects.get(name=request.POST['CPU_name'])
        checkcost -= best_cpu.cost
        best_ram = RAM.objects.filter(cost__lte=checkcost)

    else:
        return render(request, 'myapp/index.html', {'err_m': "Error"})

    return render(request, 'myapp/index.html', {'ram': best_ram})


def selectps(request):
    if request:
        checkcost = request.session['checkcost']
        best_ram = RAM.objects.get(name=request.POST['RAM_name'])
        checkcost -= best_ram.cost
        best_ps = PS.objects.filter(cost__lte=checkcost)

    else:
        return render(request, 'myapp/index.html', {'err_m': "Error"})

    return render(request, 'myapp/index.html', {'ps': best_ps})


def detail(request):
    if request:
        final_name = request.session['final_name']
        best_gpu = GPU.objects.get(name=final_name)
        driver = webdriver.PhantomJS()
        driver.get('https://exmo.com/en/exchange')

        html = driver.page_source
        soup = BeautifulSoup(html)

        # check out the docs for the kinds of things you can do with 'find_all'
        # this (untested) snippet should find tags with a specific class ID
        # see: http://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class
        for tag in soup.find_all('div', class_='top_exch_rate'):
            m = re.search(r'(d*)+.+(d*)', tag.text, )
            s = m.group()
        price = s
        global pr
        pr = ''
        for li in price:
            if li.isnumeric():
                pr += str(li)
            elif li == '.':
                break
        current_price = pr[1:]
        value = int(current_price)

        driver = webdriver.PhantomJS()
        driver.get('https://blockchain.info/stats')

        html = driver.page_source
        soup = BeautifulSoup(html)

        # check out the docs for the kinds of things you can do with 'find_all'
        # this (untested) snippet should find tags with a specific class ID
        # see: http://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class
        for tag in soup.find_all('td', id='difficulty'):
            m = re.search(r'(.*)(,.*)*', tag.text, )
            s = m.group()
        price = s
        pr = ''
        for li in price:
            if li.isnumeric():
                pr += str(li)
        difficulty = pr[:]
        D = int(difficulty)
        day1 = datetime.date(2009, 3, 1)
        day2 = datetime.date.today()
        period = (day2-day1).days
        x = period*144
        h = best_gpu.hashing_rate
        t = 86400
        R = (50*value)/(x/210000)*2
        B = (h*t*R) / ((2**32)*D)
        final_answer = B * (10 ** 6)
        driver.save_screenshot('screen.png')

    else:
        return render(request, 'myapp/index.html', {'error_message': "Invalid input"})

    return render(request, 'myapp/index.html', {'result': final_answer})
