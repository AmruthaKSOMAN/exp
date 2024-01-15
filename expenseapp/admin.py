from django.contrib import admin
from .models import Balance,Expense

# Register your models here.
# admin.site.register(Balance)
# admin.site.register(Expense)

class ExpenseAdmin(admin.ModelAdmin):
    list_display=('Item','Amount')
    ordering=('Item',)
    search_fields=('Item','Amount')
    
admin.site.register(Expense,ExpenseAdmin)
    
class BalanceAdmin(admin.ModelAdmin):
    list_display=('id','Current_Balance')
    ordering=('id',)
    search_fields=('id',)
    
admin.site.register(Balance,BalanceAdmin)
    


