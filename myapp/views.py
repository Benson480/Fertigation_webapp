from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Fertilizer, Fertilizer_Detail, Fertilizer_Element, Fertilizer_Amount
from django.db.models import Q
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Sum
import itertools

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {"form": form}
    return render(request, "accounts/register.html", context)

# Create your views here.
def login_view(request):
    # future -> ?next=/articles/create/
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            messages.success(request, "Login successful.")
            login(request, user)
            return redirect('/members/')
        
    else:
        messages.success(request, "Login not Sucessful try again!")
        form = AuthenticationForm(request)
        
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html", {})

def members(request):
  mymembers = Fertilizer.objects.all()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
 

def details(request, id):
  mymember = Fertilizer_Detail.objects.all()
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def elements(request): 
  mymember = Fertilizer_Element.objects.all()
  template = loader.get_template('elements.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def home(request):
  mymembers = Fertilizer.objects.all()
  template = loader.get_template('home.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def testing(request):
  mymembers= Fertilizer.objects.all().order_by('lastname', '-id').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def template(request):
  template = loader.get_template('template.html')
  return HttpResponse(template.render())

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())