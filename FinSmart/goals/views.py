from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required  # Import login_required decorator
from .models import Goal
from .forms import GoalForm
from .models import GoalCategory
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404


def goal_home(request):
    # Query goals belonging to the current user
    goals = Goal.objects.filter(user=request.user)

    # Pagination
    paginator = Paginator(goals, 10)  # Adjust the number of goals per page as needed
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    



    return render(request, 'home1.html' ,context)

@login_required
def add_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, f'A new goal is added successfully')
            return redirect('home')
    else:
        form = GoalForm()
    return render(request, 'add_goal.html', {'form': form})


def view_goal(request, goal_id):
    # Fetch the goal details from the database based on the goal_id
    # Assuming you have a method to retrieve the goal details, replace the placeholders with your actual implementation
    goal = get_object_or_404(Goal, pk=goal_id)
    
    # Pass the goal details to the template
    context = {'goal': goal}
    
    # Render the template
    return render(request, 'goal_detail.html', context)


# Create your views here.
