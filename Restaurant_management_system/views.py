# I have created this file - Darshan
from django.http import HttpResponse
from django.shortcuts import render



##connects views
#loginform
def loginconnects(request):
    return render(request,"connects/form.html")

#register
def registerconnects(request):
    return render(request,"connects/register.html")

#home
def home(request):
    return render(request,"connects/home.html")

#khata
def khataconnects(request):
    return render(request,"connects/khata.html")

#khatatable
def khatatable(request):
    return render(request,"connects/khatainner.html")

#statements
def statementsconnects(request):
    return render(request,"connects/statements.html")

#E-Restura
def index(request):
    return render(request, 'index.html')

