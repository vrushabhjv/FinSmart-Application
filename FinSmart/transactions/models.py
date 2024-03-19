from django.db import models
from django.contrib.auth.models import User
from goals.models import Goal

# Create your models here.
class TransactionCategory(models.Model):
    name = models.CharField(max_length=100)
    type = models.BooleanField(default=True) # True for income, False for expense
    
    class Meta:
        verbose_name_plural = 'Transaction Categories'
    def __str__(self):
        return self.name
    
    
class Transaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.BooleanField(default=True) # True for income, False for expense
    goal = models.ForeignKey(Goal, on_delete=models.SET_NULL, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Transactions'
        
    def __str__(self):
        return self.user.username+ ' - ' +self.category.name + ' - ' + self.description
''' def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.goal:
           # If a goal is associated with the transaction, update its current progress
            self.goal.current_progress += self.amount
            self.goal.save()'''
    