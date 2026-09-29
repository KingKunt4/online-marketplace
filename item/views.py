from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import newItemForm

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'detail.html', {
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

    return render(request, 'newlisting.html', {
        'form':form,
        'title':'New Listing',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')
