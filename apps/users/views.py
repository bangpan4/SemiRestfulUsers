from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    return render(request, 'users/index.html', {'users': User.objects.all()})

def add(request):
    return render(request, 'users/add.html')

def create(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/users/add')
        else:
            newuser = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
            newuser.save()
    return redirect('/users')

def show(request, id):
    if request.method == 'GET':
        return render(request, 'users/show.html', {'user': User.objects.get(id=id)})

def edit(request, id):
    if request.method == 'GET':
        return render(request, 'users/edit.html', {'user': User.objects.get(id=id)})

def update(request,id):
    if request.method == 'POST':
        newupdate = request.POST
        newuser = User.objects.get(id=id)
        newuser.first_name = newupdate['first_name']
        newuser.last_name = newupdate['last_name']
        newuser.email = newupdate['email']
        newuser.save()
    return redirect('/users')
    

def delete(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users')