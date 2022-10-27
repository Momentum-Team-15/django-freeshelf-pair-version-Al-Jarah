from django.shortcuts import render, redirect, get_object_or_404
from .models import Resource, Category, Favorite
from . forms import NameForm
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    resources = Resource.objects.all()
    return render(request, 'core/home.html', {'resources': resources})

@login_required
def resource_detail(request, pk):
    resources = Resource.objects.get(pk=pk)
    return render(request, 'core/resource_detail.html', {'resource': resources})

@login_required
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    return render(request, 'core/categories_detail.html', {'category': category, 'resources':category.resources.all(), 'categories': category})

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else: 
        form = NameForm()

    return render(request, 'core/registration_form.html', {'form': form})

@login_required
def edit(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if request.method == "POST":
        form = NameForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            form = form.save()
            form.user = request.user
            form.created_at = timezone.now()
            return redirect('home', pk=form.pk)
    else:
        form = NameForm(instance=resource)
    return render(request, 'core/edit.html', {'form': form})

@login_required
def delete(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if request.method == "POST":
        form = NameForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            form = form.save()
            form.user = request.user
            form.created_at = timezone.now()
            return redirect('home', pk=form.pk)
    else:
        form = NameForm(instance=resource)
    return render(request, 'core/delete.html', {'form': form})

@login_required
def add_favorite(request, res_pk):
    resource = get_object_or_404(Resource, pk=res_pk)
    unfavorited = False
    for favorite in request.user.favorites.all():
        if resource == favorite.resource:
            favorite.delete()
            unfavorite = True
        if not unfavorite:
            favorite = Favorite.objects.create(resource=resource, user=request.user)
            favorite.save()
        return redirect('home')
