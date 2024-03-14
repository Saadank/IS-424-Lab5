from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

people = []

def add_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        new_person = Person(username=username, password=password)
        people.append(new_person)
        return HttpResponseRedirect(reverse('default'))
    return render(request, 'myapp/add.html')

def default_view(request):
    return render(request, 'myapp/default.html', {'people': people})
