from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import User


def index_page(request):
    data = User.objects.all()
    context = {'data': data}
    return render(request, "index.html", context)


def edit_page(request):
    return render(request, "edit.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        idnumber = request.POST.get('idnumber')
        ticketprice = request.POST.get('ticketprice')
        ticketnumber = request.POST.get('ticketnumber')
        date = request.POST.get('date')

        query = User(name=name, idnumber=idnumber, ticketprice=ticketprice, ticketnumber=ticketnumber, date=date)
        query.save()
        return redirect("index")
    return render(request, "index.html")
