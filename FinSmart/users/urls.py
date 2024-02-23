from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('transactions/', views.transactions, name='transactions'),
    # path('logout/', views.logout, name='logout'),
    # path('profile/', views.profile, name='profile'),
    # path('edit_profile/', views.edit_profile, name='edit_profile'),
    # path('change_password/', views.change_password, name='change_password'),
    # path('delete_profile/', views.delete_profile, name='delete_profile'),
]