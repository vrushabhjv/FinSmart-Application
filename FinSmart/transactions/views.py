from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
from .models import Transaction, TransactionCategory
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from goals.models import Goal
from decimal import Decimal

# Create your views here.
def transaction_home(request):
    transactions = Transaction.objects.filter(user=request.user)
    
    # Retrieve categories from the database
    categories = TransactionCategory.objects.all()  # Assuming you have a Category model
    
    paginator = Paginator(transactions, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Pass categories data to the template context
    context = {
        'categories': categories,
        'page_obj':page_obj,
    }
    
    return render(request, 'transactions/transactions.html',context)

def view_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    
    # Pass the transaction details to the template
    context = {'transaction': transaction}
    
    # Render the template
    return render(request, 'transactions/transaction_detail.html', context)

    # Handle form submission to create a new transaction
    #return render(request, 'transaction_detail.html', context)
    
def add_transaction(request):
    if request.method == 'POST':
        if request.POST.get('category') == None:
            # Handle category selection
            if request.POST['type'] == 'income':
                type = True
            elif request.POST['type'] == 'expense':
                type = False
            
            categories = TransactionCategory.objects.all()
            context = {
                'categories': categories,
                'transaction_type':type,
            }
            return render(request, 'transactions/add_transaction.html', context)
        
        # Handle form submission with all attributes
        date = request.POST['date']
        description = request.POST['description']
        amount = request.POST['amount']
        category_id = request.POST['category']
        if request.POST['type'] == 'income':
            type = True
        elif request.POST['type'] == 'expense':
            type = False
        else:
            type = None
        user = request.user

        category = TransactionCategory.objects.get(pk=category_id)
        amount = Decimal(request.POST['amount']) 
        # Create a new transaction object and save it to the database
        transaction = Transaction(date=date, description=description, amount=amount, category=category, type=type, user=user)
         # Handle goal name
        goal_name = request.POST.get('goal_name')
        if goal_name:
            try:
                goal = Goal.objects.get(name=goal_name, user=user)
                goal.current_progress += transaction.amount
                goal.save()
                transaction.goal = goal
            except Goal.DoesNotExist:
                pass  # Handle case where the goal does not exist
        transaction.save()
        messages.success(request, f'Transaction added successfully')
        return redirect('transaction_home')
    else:
        categories = TransactionCategory.objects.all()
        context = {
            'categories': categories,
            'transaction_type':None,
        }
        return render(request, 'transactions/add_transaction.html', context)

def update_transaction(request, transaction_id):
    # Handle form submission to update an existing transaction
    pass

def delete_transaction(request, transaction_id):
    try:
        transaction = Transaction.objects.get(id=transaction_id)
    except Transaction.DoesNotExist:
        messages.error(request, "Transaction does not exist.")
        return redirect('transaction_list')

    if request.method == 'POST':
        transaction.delete()
        messages.success(request, "Transaction deleted successfully.")
        return redirect('transaction_home')
