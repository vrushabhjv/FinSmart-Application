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
    # The __str__method in Django models is used to provide a human-readable string representation of the model instance. It is a special method in Python that is called when you try to convert an object to a string, such as when printing the object or using it in a template.
    # For example, if you have a `Transaction` model, the `__str__` method can be used to display the transaction details in a more user-friendly way, such as `"John Doe - Groceries - Bought milk"` instead of the default string representation, which might be something like `"<Transaction object (1)>"`.

# By providing a meaningful string representation of the model instance, the `__str__` method can greatly improve the readability and usability of your Django application, especially when working with large datasets or complex models.
    
    
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
    