from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'ruthik'})

def add(request):
    val1 = request.POST['num1'] # the num1 is the variable name we defined in the frontend, we get the value from the link now.
    val2 = request.POST['num2']
    res = int(val1) + int(val2)
    return render(request, 'result.html', {'result':res}) # whichever the data you want to pass to html page from render, it should be always in the dictionary format{key:value}