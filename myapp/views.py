from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import (Fertilizer, Fertilizer_Detail, 
Fertilizer_Element, Fertilizer_Amount, Fertilizer_Price, Fertilizer_Cost)
from django.db.models import Q
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Sum
import itertools
from .forms import (Fertilizer_AmountForm, DeleteFertilizerForm, Fertilizer_PricesForm, 
                    Fertilizer_ElementsForm)
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

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
            return redirect('/dashboard/')
        
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

def dashboard(request):
  template = loader.get_template('dashboard.html')
  return HttpResponse(template.render())
  

def update(request, id):
  mymember = Fertilizer_Amount.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  Date = request.POST['Date']
  # amount = request.POST['amount', False]
  member = Fertilizer_Amount.objects.get(id=id)
  member.Date = Date
  # member.amount = amount
  member.save()
  return HttpResponseRedirect(reverse('Fertilizers'))

def delete(request, id):
  member = Fertilizer_Amount.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse("Fertilizers"))

def deleteprice(request, id):
  member = Fertilizer_Price.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse("prices"))


def Fertilizers(request):
    context ={}
 
    # create object of form
    mymember = Fertilizer_Amount.objects.all()
    membercost = Fertilizer_Cost.objects.all()
    fertform = Fertilizer_AmountForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if fertform.is_valid():
        # save the form data to model
        fertform.save()
    context = {
    'form':fertform,
    'mymember': mymember,
    'membercost': membercost, 
  }


    return render(request, "Fertilizers.html", context)
  


def elements(request):
    context ={}
    # create object of form
    mymember = Fertilizer_Element.objects.all()
    fertelementform = Fertilizer_ElementsForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if fertelementform.is_valid():
        # save the form data to model
        fertelementform.save()
    context = {
    'fertelementform':fertelementform,
    'mymember': mymember,
  }


    return render(request, "elements.html", context)
  


def ppm(request): 
  mymember = Fertilizer_Element.objects.all()
  template = loader.get_template('ppm.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())


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

def dashboard(request):
  template = loader.get_template('dashboard.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def anouncement(request):
  template = loader.get_template('anouncement.html')
  return HttpResponse(template.render())

def contacts(request):
  template = loader.get_template('contacts.html')
  return HttpResponse(template.render())

def prices(request):
    context ={}
 
    # create object of form
    mymember = Fertilizer_Price.objects.all()
    fertpriceform = Fertilizer_PricesForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if fertpriceform .is_valid():
        # save the form data to model
        fertpriceform .save()
    context = {
    'form':fertpriceform ,
    'mymember': mymember,
  }


    return render(request, "prices.html", context)



def Fertlizer_dealers(request):
  template = loader.get_template('fertilizer_dealers.html')
  return HttpResponse(template.render())

def laboratory(request):
  template = loader.get_template('laboratory.html')
  return HttpResponse(template.render())

def weather(request):
  template = loader.get_template('weather.html')
  return HttpResponse(template.render())

def research(request):
  template = loader.get_template('research.html')
  return HttpResponse(template.render())
  