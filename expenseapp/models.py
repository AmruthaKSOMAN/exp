from django.db import models

# Create your models here.

class Expense(models.Model):
    Item=models.CharField(max_length=50)
    Amount=models.BigIntegerField()
    
    def __str__(self):
        return self.Item
    
class Balance(models.Model):
    Current_Balance=models.BigIntegerField()
    
    def __int__(self):
        return self.Current_Balance
