from django.shortcuts import render
from .models import Expense, Balance

# Create your views here.


def base(request):
    return render(request, 'base.html')


def addexpense(request):

    response = {}
    try:
        it = request.POST.get('items')
        am = request.POST.get('amount')
        cbl = Balance.objects.get(id=1)
        if cbl.Current_Balance >= int(am):
            exp = Expense.objects.all()
            cpy = 0
            for i in exp:
                if i.Item == it:
                    cpy = 1
            if cpy == 0:
                datas = Expense(Item=it, Amount=am)
                datas.save()
                response['msg1'] = 'Expense Added'

                crb = Balance.objects.get(id=1)
                am = request.POST.get('amount')
                cb = crb.Current_Balance-int(am)
                Balance.objects.filter(
                    Current_Balance=crb.Current_Balance).update(Current_Balance=cb)

            else:
                it = request.POST.get('items')
                am = request.POST.get('amount')
                exp = Expense.objects.get(Item=it)
                amt = exp.Amount+int(am)
                Expense.objects.filter(Item=it).update(Amount=amt)
                response['msg1'] = 'Expense Added'

                crb = Balance.objects.get(id=1)
                am = request.POST.get('amount')
                cb = crb.Current_Balance-int(am)

                Balance.objects.filter(
                    Current_Balance=crb.Current_Balance).update(Current_Balance=cb)

            return render(request, 'addexpense.html', response)
        else:
            response['msg1'] = 'Insufficient Balance'
            return render(request, 'addexpense.html', response)
    except Exception as e:
        print(e)
        response['msg1'] = 'Expense Not Added'
        return render(request, 'addexpense.html', response)


def creditamount(request):

    try:
        crb = Balance.objects.get(id=1)
        crd = request.POST.get('crdtamnt')
        cb = crb.Current_Balance+int(crd)
        Balance.objects.filter(
            Current_Balance=crb.Current_Balance).update(Current_Balance=cb)
        return render(request, 'creditamount.html', {'bal': 'Amount Credited'})
    except Exception as e:
        print(e)
        return render(request, 'creditamount.html', {'bal': 'Amount Not Credited'})


def balance(request):
    bal = Balance.objects.all()
    return render(request, 'balance.html', {'bl': bal})


def expense(request):
    exp = Expense.objects.all()
    return render(request, 'expense.html', {'ex': exp})
