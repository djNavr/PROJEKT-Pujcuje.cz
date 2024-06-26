from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .models import Item
from .models import *
from .forms import *

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def category(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'blog/category.html', context)

def category_list(request,category_id):

    test = Item.objects.filter(category=category_id).values()
    print(test)
    context = {
        'categories': Item.objects.filter(category=category_id).values()
    }
    return render(request, 'blog/category_list.html', context)
@login_required
def my_items(request):
    items = Item.objects.all()
    return render(request, 'blog/my_items.html', {'items': items})

@login_required
def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST,
                        request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, f'Your item has been added!')
            return redirect('my_items')
    else:
        form = ItemForm()
    return render(request, 'blog/add_item.html', {'form': form})

@login_required
def remove_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        item.delete()
        messages.success(request, f'Your item has been deleted!')
        return redirect('item_list')
    return render(request, 'blog/remove_item.html', {'item': item})

@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your item has been updated!')
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    print(item.image)
    return render(request, 'blog/edit_item.html', {'form': form, 'item': item})


def rent(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'blog/rent.html', context)
@login_required
def my_orders(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'blog/rent.html', context)
@login_required
def my_diary(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'blog/rent.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
@login_required
def item_list(request):
    items = Item.objects.all()
    return render(request, 'blog/my_items.html', {'items': items})

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

@login_required
def rent_item(request,item_id):
    if request.method == "POST":
        form = DateRangeForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Item has been rented!')
            return redirect('blog-rent')
    else:
        form = DateRangeForm()
    return render(request, 'blog/rent.html', {'form': form})