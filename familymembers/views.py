from django.shortcuts import render, redirect

from familymembers.models import FamilyMembers, Expenses


# Create your views here.
def home(request):
    return render(request,'home.html')


def addmemberlogic(request):
    f1=FamilyMembers()
    f1.name=request.POST["MemberName"]
    f1.mobile=request.POST['MemberMobile']
    f1.occupation=request.POST['MemberOccupation']
    f1.income=request.POST['MemberIncome']
    f1.save()
    return render(request,'addmember.html')




def f1(request):
    return render(request,'addmember.html')


def f2(request):
    data=FamilyMembers.objects.all()
    return render(request,'display.html',{'x':data})


def updatefunction(request,id):
    m1=FamilyMembers.objects.get(id=id)

    if request.method=="POST":
        m1.name = request.POST["MemberName"]
        m1.mobile = request.POST['MemberMobile']
        m1.occupation = request.POST['MemberOccupation']
        m1.income = request.POST['MemberIncome']
        m1.save()
        return redirect('show')
    return render(request, 'editing.html', {'x': m1})



def deletefunction(request,id):
    m1=FamilyMembers.objects.get(id=id)
    m1.delete()
    return redirect('show')


def addexpensefunction(request):
    family=FamilyMembers.objects.all()
    return render(request,'addexpense.html',{'x':family})


def saveexpensedatafunction(request):
    exp=Expenses()
    exp.membername_id=request.POST['name']
    exp.purpose=request.POST['purpose']
    exp.expense=request.POST['expense']
    exp.save()
    return render(request,'addexpense.html',{'x':FamilyMembers.objects.all()})


def showexpensefunction(request):
    expenses_data=Expenses.objects.all()
    family_data=FamilyMembers.objects.all()
    return render(request,'showexpenses.html',{'x':expenses_data,'y':family_data})


def editexpensefunction(request,id):
    exp = Expenses.objects.get(id=id)
    if request.method=='POST':
        exp.membername_id = request.POST['membername_id']
        exp.purpose = request.POST['purpose']
        exp.expense = request.POST['expense']
        exp.save()
        return redirect('showexpense')
    return render(request, 'editexpense.html', {'x': exp})


def deleteexpensefunction(request,id):
    exp_del=Expenses.objects.get(id=id)
    exp_del.delete()
    return redirect('showexpense')