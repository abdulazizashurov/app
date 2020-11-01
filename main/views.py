from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PupilsForm

def home(request):
    return render(request,'main/base.html',context={'subjects':Subject.objects.all(),
                                                    'teachers':Teacher.objects.all(),
                                                    'socials': SocialNetwork.objects.all(),
                                                    })

def news(request):
    return render(request,'main/new.html',context={'news': New.objects.all(),})




def register(request):
    form = PupilsForm()
    if request.method == 'POST':
        form = PupilsForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
        else:
            form = PupilsForm(request.POST)
    return render(request, 'main/register.html', {'form': form})