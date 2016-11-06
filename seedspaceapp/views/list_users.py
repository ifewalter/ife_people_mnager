from django.shortcuts import render
from seedspaceapp.models import Person

__author__ = 'ife'


#maps to /list
def list(request):
    persons = Person.objects.all()
    return render(request, "list.html",{'persons':persons})