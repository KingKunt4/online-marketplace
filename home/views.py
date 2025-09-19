from django.shortcuts import render, redirect
from django.http import HttpResponse
from items.models import Category, Items
from . forms import signupForm, LoginForm

def index(request):
    item = Items.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'categories': categories,
        'items': item,
    })

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')    
    else: 
        form = signupForm()
    return render(request, 'signup.html', {
        'form': form,
    })