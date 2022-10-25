from django.shortcuts import render, redirect, get_object_or_404
from .forms import NameForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    user=request.user
    return render(request, 'core/home.html', {})
    
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else: 
        form = NameForm()

    return render(request, 'core/registration_form.html', {'form': form})
