# In goals/forms.py

from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    GOAL_CATEGORIES = [
        ('Goal category', '--Goal-category--'),
        ('Health and Fitness Goals', 'Health and Fitness Goals'),
        ('Career and Education Goals', 'Career and Education Goals'),
        ('Personal Development Goals', 'Personal Development Goals'),
        ('Spiritual and Well-being Goals', 'Spiritual and Well-being Goals'),
        ('Travel Goals', 'Travel Goals'),

        # Add more choices as needed
    ]

    DEFAULT_GOAL_CATEGORY = 'finance'  # Set the default goal category here

    goal_category = forms.ChoiceField(choices=GOAL_CATEGORIES, initial=DEFAULT_GOAL_CATEGORY)

    class Meta:
        model = Goal
        fields = ['name', 'target_amount', 'target_date','goal_category']
        widgets = {
            'target_date': forms.DateInput(attrs={'type': 'date'}),
        }
