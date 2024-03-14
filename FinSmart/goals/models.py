from django.db import models
from django.contrib.auth.models import User

class GoalCategory(models.Model):
    name = models.CharField(max_length=100)
    type = models.BooleanField(default=True) 
    
    class Meta:
        verbose_name_plural = 'Goal Categories'
    def __str__(self):
        return self.name

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    target_date = models.DateField()
    current_progress = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    goal_category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    #class Meta:
     #   app_label = 'goals'
# Create your models here.
