from django.urls import path
from .import views

urlpatterns = [
    path('', views.base, name="base"),
    path('addexpense', views.addexpense, name="addexpense"),
    path('creditamount', views.creditamount, name="creditamount"),
    path('balance', views.balance, name="balance"),
    path('expense', views.expense, name="expense"),
]
