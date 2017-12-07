from django.conf.urls import url
from . import views

app_name = 'myapp'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^budget', views.budget, name="budget"),
    url(r'^selectcpu', views.selectcpu, name="selectcpu"),
    url(r'^selectram', views.selectram, name="selectram"),
    url(r'^selectps', views.selectps, name="selectps"),
    url(r'^detail$', views.detail, name="detail"),
]
