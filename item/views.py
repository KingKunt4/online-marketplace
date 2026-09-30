from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Item, Category
from .forms import newItemForm, editItemForm

def index(request):
    query = request.GET.get('query', '')
    item = Item.objects.filter(is_sold=False)
    category = Category.objects.all()
    category_id = request.GET.get('category', 0)

    if category_id:
        item = item.filter(category_id=category_id)
    if query:
        item = item.filter(Q(name__icontains=query)|Q(description__icontains=query))
        
    return render(request, 'item/index.html', {
        'item':item,
        'query':query,
        'categories':category,
        'category_id': int(category_id)
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {
        'item': item,
        'related': related
    })

@login_required
def newListing(request):
    if request.method=='POST':
        form = newItemForm(request.POST, request.FILES)

        if form.is_valid:
            item = form.save(commit=False)
            item.created_by = request.user
    
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = newItemForm()

    return render(request, 'item/newlisting.html', {
        'form':form,
        'title':'New Listing',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method=='POST':
        form = editItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid:    
            form.save()
            return redirect('item:detail', pk=item.id)
            
    else:
        form = editItemForm(instance=item)

    return render(request, 'item/newlisting.html', {
        'form':form,
        'title':'Edit Listing',
    })