from django.urls import path
from . import views

app_name = 'complist'

urlpatterns = [
    # /complist/
    path('', views.IndexView.as_view(), name='index'),
    # /complist/x/
    path('<int:pk>/', views.DetailView.as_view(), name='compinfo'),

    path('register/', views.UserFormView.as_view(), name='register'),
]