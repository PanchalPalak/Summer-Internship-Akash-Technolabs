from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepageview(request):
    return render(request,'home.html',{'name':'pal','surname':'panchal'})

def about(request):
    return render(request,'about.html',{'name':'pal','surname':'panchal'})    