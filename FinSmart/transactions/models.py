from django.db import models
from django.contrib.auth.models import User

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
    
    class Meta:
        verbose_name_plural = 'Transactions'
        
    def __str__(self):
        return self.user.username+ ' - ' +self.category.name + ' - ' + self.description
    