from django.conf.urls import url
from first_app import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'first_app', views.index, name='index'),
    
    
    
]