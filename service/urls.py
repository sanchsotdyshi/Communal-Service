from django.urls import path
from . import views

app_name = 'service'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('new_application/', views.create_application, name='create_application'),
    path('login/', views.login, name='login'),
    path('worker_page/', views.worker_page, name='worker_page'),
]