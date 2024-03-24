from django.urls import path
from . import views

# app_name = 'goals'

urlpatterns = [
    path('', views.goal_home, name='goal_home'),
    path('add/', views.add_goal, name='add_goal'),
    path('goals/<int:goal_id>/', views.view_goal, name='view_goal'),
    path('goals/<int:goal_id>/delete/', views.delete_goal, name='delete_goal'),
    

]