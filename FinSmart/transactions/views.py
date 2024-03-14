from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
from .models import Transaction, TransactionCategory
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

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
        # 'transactions': transactions,
        'page_obj':page_obj,
    }
    
    return render(request, 'transactions/transactions.html',context)

'''
def transaction_list(request):
    transactions = Transaction.objects.all()

    # Retrieve categories from the database
    categories = TransactionCategory.objects.all()  # Assuming you have a Category model
    
    # Pass categories data to the template context
    context = {
        'categories': categories,
        'transactions': transactions,
    }
    
    # Filtering based on query parameters
    # category = request.GET.get('category')
    # if category:
    #     transactions = transactions.filter(category=category)

    paginator = Paginator(transactions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'transactions/transactions.html', {'page_obj': page_obj}, context)
'''

'''def transaction_detail(request, transaction_id):
   transaction = Transaction.objects.get(id=transaction_id)
    return render(request, 'transaction_detail.html', {'transaction': transaction})'''

def view_transaction(request, transaction_id):
    # Fetch the goal details from the database based on the goal_id
    # Assuming you have a method to retrieve the goal details, replace the placeholders with your actual implementation
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    
    # Pass the goal details to the template
    context = {'transaction': transaction}
    
    # Render the template
    return render(request, 'transaction_detail.html', context)

    # Handle form submission to create a new transaction
def add_transaction(request):
    # Handle form submission to create a new transaction
    if request.method == 'POST':
        #To display only the categories according to selected transaction_type
        #handles when this executes {onchange="this.form.submit()"}, in the add_transaction.html, only type will be selected and no other attributes will be entered, so check if category is None 
        if request.POST.get('category') == None:
            print(request.POST['type'])
            if request.POST['type'] == 'income':
                type = True
            elif request.POST['type'] == 'expense':
                type = False
            print(type)
            categories = TransactionCategory.objects.all()  # Assuming you have a Category model
    
            # Pass categories data to the template context
            context = {
                'categories': categories,
                'transaction_type':type,
            }
            return render(request, 'transactions/add_transaction.html', context)
            
        #handles when the form is submitted with all the attributes
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
        # Create a new transaction object and save it to the database
        print(category)
        transaction = Transaction(date=date, description=description, amount=amount, category=category, type=type, user=user)
        transaction.save()
        messages.success(request, f'Transaction added successfully')
        return redirect('transaction_home')
    else:
        print(request.user)
        categories = TransactionCategory.objects.all()  # Assuming you have a Category model
    
        # Pass categories data to the template context
        context = {
            'categories': categories,
            'transaction_type':None,
        }
        return render(request, 'transactions/add_transaction.html', context)

def update_transaction(request, transaction_id):
    # Handle form submission to update an existing transaction
    pass

def delete_transaction(request, transaction_id):
    # Handle deletion of an existing transaction
    # Retrieve the transaction object
    try:
        transaction = Transaction.objects.get(id=transaction_id)
    except Transaction.DoesNotExist:
        # Handle the case where the transaction does not exist
        messages.error(request, "Transaction does not exist.")
        return redirect('transaction_list')  # Redirect to transaction list page or any other appropriate page

    if request.method == 'POST':
        # Delete the transaction
        transaction.delete()
        messages.success(request, "Transaction deleted successfully.")
        return redirect('transaction_home')  # Redirect to transaction list page or any other appropriate page

