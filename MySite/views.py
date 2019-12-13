from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    file = open("D:\coding\Python\django\MySite\Static\cek.html", "r")
    return HttpResponse(file)