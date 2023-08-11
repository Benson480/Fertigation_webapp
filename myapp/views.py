from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.template import loader
from .models import (Fertilizer, Fertilizer_Detail, 
Fertilizer_Element, Fertilizer_Amount, Fertilizer_Price, Fertilizer_Cost, UploadedImage, Fertilizer_Recycle)
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
                    Fertilizer_ElementsForm, Fertilizer_Form, ImageUploadForm, Fertilizer_Recycle_Form)
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import get_token
from django.contrib.auth.decorators import login_required
import datetime
from django.http import JsonResponse
# from .decorators import login_required


def regenerate_csrf_token(request):
    if request.method == 'GET':
        csrf_token = get_token(request)
        return HttpResponse(csrf_token)
    
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

def update(request, id):
  mymember = Fertilizer_Amount.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  Date = request.POST['Date']
  amount = request.POST['amount', False]
  member = Fertilizer_Amount.objects.get(id=id)
  member.Date = Date
  # member.amount = amount
  member.save()
  return HttpResponseRedirect(reverse('Fertilizers'))

def update_list(request, id):
  mymember = Fertilizer.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def UpdateFertilizerList(request, id):
  Date = request.POST['Date']
  amount = request.POST['name', False]
  member = Fertilizer.objects.get(id=id)
  member.Date = Date
  # member.amount = amount
  member.save()
  return HttpResponseRedirect(reverse('fertilizer_list'))

def delete(request, id):
  member = Fertilizer_Amount.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse("Fertilizers"))

def delete_fertilizers(request, id):
  member = Fertilizer.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse("fertilizer_list"))

def delete_elements(request, id):
  member = Fertilizer_Element.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse("elements"))


def deleteprice(request, id):
  member = Fertilizer_Price.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse("prices"))

@login_required #(redirect_to='/login/')
def Fertilizers(request):
    context ={}
 
    # create object of form
    mymember = Fertilizer_Amount.objects.all()
    membercost = Fertilizer_Cost.objects.all()
    Fertilizer_list = Fertilizer.objects.all()
    fertform = Fertilizer_AmountForm(request.POST or None, request.FILES or None)
    fertaddform = Fertilizer_Form(request.POST or None, request.FILES or None)
    
     
    # check if form data is valid
    if fertform.is_valid():
        # save the form data to model
        fertform.save()
    context = {
    'form':fertform,
    'mymember': mymember,
    'Fertilizer_list':Fertilizer_list,
    'membercost': membercost, 
    'fertaddform':fertaddform,
  }
    if request.user.is_authenticated:
      request.session['last_activity'] = datetime.datetime.now().isoformat()  # Convert to string

    return render(request, "Fertilizers.html", context)


@login_required #(redirect_to='/login/')
def UvElements(request):
    context ={}
 
    # create object of form
    mymember = Fertilizer_Recycle.objects.all()
    fertform = Fertilizer_Recycle_Form(request.POST or None, request.FILES or None)
    # check if form data is valid
    if fertform.is_valid():
        # save the form data to model
        fertform.save()
    context = {
    'form':fertform,
    'mymember': mymember,
  }
    if request.user.is_authenticated:
      request.session['last_activity'] = datetime.datetime.now().isoformat()  # Convert to string

    return render(request, "UvElements.html", context)

@csrf_protect
@login_required   
def fertilizer_list(request):
    context ={}
 
    # create object of form
    mymember = Fertilizer_Amount.objects.all()
    membercost = Fertilizer_Cost.objects.all()
    Fertilizer_list = Fertilizer.objects.all()
    fertform = Fertilizer_AmountForm(request.POST or None, request.FILES or None)
    fertaddform = Fertilizer_Form(request.POST or None, request.FILES or None)
    
     
    # check if form data is valid
    if fertaddform.is_valid():
        # save the form data to model
        fertaddform.save()
    context = {
    'form':fertform,
    'mymember': mymember,
    'Fertilizer_list':Fertilizer_list,
    'membercost': membercost, 
    'fertaddform':fertaddform,
  }
    if request.user.is_authenticated:
      request.session['last_activity'] = datetime.datetime.now().isoformat()  # Convert to string


    return render(request, "Fertilizers_addition.html", context)

@login_required   
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

@login_required  
def delete_multiple_items(request):
    if request.method == 'GET':
        selected_ids = request.GET.getlist('selected_ids[]')
        
        # Perform the necessary deletion logic using the selected_ids
        # Example: Delete items from the database based on the selected IDs
        Fertilizer_Amount.objects.filter(id__in=selected_ids).delete()

        # Redirect to the appropriate URL after deletion
        return redirect('/Fertilizers')
    
@login_required  
def delete_multiple_fertilizers(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selectedIds[]')
        
        # Check if the user has the necessary permissions to delete the selected items.
        # For example, you can use Django's built-in permissions or any custom checks.
        # Replace 'can_delete_fertilizers' with the appropriate permission.
        if not request.user.has_perm('myapp.can_delete_fertilizers'):
            return JsonResponse({'error': 'Permission denied.'}, status=403)

        # Perform the necessary deletion logic using the selected_ids
        # Example: Delete items from the database based on the selected IDs
        Fertilizer.objects.filter(id__in=selected_ids).delete()

        return JsonResponse({'message': 'Items deleted successfully.'})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@login_required
def ppm(request): 
  mymember = Fertilizer_Amount.objects.all()
  template = loader.get_template('ppm.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

@login_required
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

@login_required
def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

@login_required
def testing(request):
  mymembers= Fertilizer.objects.all().order_by('lastname', '-id').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

@login_required
def template(request):
  template = loader.get_template('template.html')
  return HttpResponse(template.render())

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

@login_required #(redirect_to='/index/')
def dashboard(request):
  template = loader.get_template('dashboard.html')
  # Update user activity in the session
  if request.user.is_authenticated:
    request.session['last_activity'] = datetime.datetime.now().isoformat()  # Convert to string

  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def anouncement(request):
  template = loader.get_template('anouncement.html')
  return HttpResponse(template.render())

def contacts(request):
  #This is the outer contacts page
  template = loader.get_template('contacts.html')
  return HttpResponse(template.render())

def support(request):
  template = loader.get_template('contacts.html')
  return HttpResponse(template.render())

def contact(request):
  """This is the inner file contact page"""
  template = loader.get_template('innercontact.html')
  return HttpResponse(template.render())

@login_required
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


@login_required
def Fertlizer_dealers(request):
  template = loader.get_template('fertilizer_dealers.html')
  return HttpResponse(template.render())

@login_required
def laboratory(request):
  template = loader.get_template('laboratory.html')
  return HttpResponse(template.render())

@login_required
def weather(request):
  template = loader.get_template('weather.html')
  return HttpResponse(template.render())

@login_required
def research(request):
  template = loader.get_template('research.html')
  return HttpResponse(template.render())


@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

@login_required
def image_list(request):
    images = UploadedImage.objects.all()
    return render(request, 'image_list.html', {'images': images})

def deleteimages(request, id):
  member = UploadedImage.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse("image_list"))
  