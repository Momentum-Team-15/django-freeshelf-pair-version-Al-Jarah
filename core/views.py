from django.shortcuts import render, redirect, get_object_or_404
from .models import Resources
from . forms import NameForm
from django.http import HttpResponseRedirect
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'core/home.html', {})
    
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else: 
        form = NameForm()

    return render(request, 'core/registration_form.html', {'form': form})

def edit(request, pk):
    resources = get_object_or_404(Resources, pk=pk)
    if request.method == "POST":
        form = NameForm(request.POST, request.FILES, instance=resources)
        if form.is_valid():
            form = form.save()
            form.user = request.user
            form.created_at = timezone.now()
            return redirect('home', pk=form.pk)
    else:
        form = NameForm(instance=resources)
    return render(request, 'core/edit.html', {'form': form})

def delete(request, pk):
    resources = get_object_or_404(Resources, pk=pk)
    if request.method == "POST":
        form = NameForm(request.POST, request.FILES, instance=resources)
        if form.is_valid():
            form = form.save()
            form.user = request.user
            form.created_at = timezone.now()
            return redirect('home', pk=form.pk)
    else:
        form = NameForm(instance=resources)
    return render(request, 'core/delete.html', {'form': form})
