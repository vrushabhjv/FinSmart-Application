from django.urls import path
from . import views

urlpatterns = [
    path('', views.transaction_home, name='transaction_home'),
    # path('transactions/list/', views.transaction_list, name='transaction_list'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('<int:transaction_id>/', views.view_transaction, name='view_transaction'),
    path('<int:transaction_id>/update/', views.update_transaction, name='update_transaction'),
    path('<int:transaction_id>/delete/', views.delete_transaction, name='delete_transaction'),
    
]