from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import User


def index_page(request):
    data = User.objects.all()
    context = {'data': data}
    return render(request, "index.html", context)


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        idnumber = request.POST.get('idnumber')
        genre = request.POST.get('genre')
        password = request.POST.get('password')
        verificationcode = request.POST.get('verificationcode')
