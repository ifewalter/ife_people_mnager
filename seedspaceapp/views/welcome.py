from django.shortcuts import render

__author__ = 'ife'


#maps to /
def welcome(request):
    return render(request, 'welcome.html')
