from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.transaction_home, name='transaction_home'),
    # path('transactions/list/', views.transaction_list, name='transaction_list'),
    path('transactions/add/', views.add_transaction, name='add_transaction'),
    path('transactions/<int:transaction_id>/', views.transaction_detail, name='transaction_detail'),
    path('transactions/<int:transaction_id>/update/', views.update_transaction, name='update_transaction'),
    path('transactions/<int:transaction_id>/delete/', views.delete_transaction, name='delete_transaction'),
    
]