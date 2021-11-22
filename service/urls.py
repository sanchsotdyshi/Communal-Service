from django.urls import path
from . import views

app_name = 'service'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('error/<int:code>/', views.error, name='error'),
    path('new_application/', views.create_application, name='create_application'),
    path('login/', views.login, name='login'),
    path('worker_page/', views.worker_page, name='worker_page_post'),
    path('worker_page/<int:mode>/<int:id>/', views.worker_page, name='worker_page'),
    path('complete/<int:id>/<int:worker_id>/', views.complete_app, name='complete_app'),
]