from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.template import loader
from .models import (Fertilizer, Fertilizer_Detail, 
Fertilizer_Element, Fertilizer_Amount, Fertilizer_Price, Fertilizer_Cost, UploadedImage, Fertilizer_Recycle)
from django.db.models import Q
from .forms import NewUserForm
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
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm
from django.utils import timezone
import logging
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from .decorators import public_view, login_exempt


def regenerate_csrf_token(request):
    if request.method == 'GET':
        csrf_token = get_token(request)
        return HttpResponse(csrf_token)


def register_view(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)

        if signup_form.is_valid():
            username = signup_form.cleaned_data['username']
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password']
            
            # Check if the username is unique
            if User.objects.filter(username=username).exists():
                signup_form.add_error('username', 'This username is already taken.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('login')  # Redirect to the desired URL after successful signup
    else:
        signup_form = SignupForm()

    return render(request, 'accounts/register.html', {'signup_form': signup_form})
    


logger = logging.getLogger(__name__)

logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            logger.warning(
                f"Login Successful at {timezone.now()} by username: {request.POST.get('username')}"
            )
            messages.success(request, f"Login Successful at {timezone.now()} by username: {request.POST.get('username')}")
            return redirect('dashboard')  # Redirect to the dashboard or desired URL
        else:
            logger.warning(
                f"Login attempt failed at {timezone.now()} by username: {request.POST.get('username')}"
            )
            messages.error(request, f"Login attempt failed at {timezone.now()} by username: {request.POST.get('username')}")

    else:
        login_form = AuthenticationForm()

    signup_form = SignupForm(request.POST)  # Pass the POST data to the signup form

    if request.method == 'POST' and signup_form.is_valid():
        username = signup_form.cleaned_data['username']
        email = signup_form.cleaned_data['email']
        password = signup_form.cleaned_data['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, f"This Username {request.POST.get('username')} is already in taken!")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, f"SignUp Successful at {timezone.now()} by username: {request.POST.get('username')}")
            return redirect('login')

    password_reset_form = PasswordResetForm(request.POST or None)

    if request.method == 'POST' and password_reset_form.is_valid():
        user_email = password_reset_form.cleaned_data['email']
        password_reset_form.save(
            request=request,
            from_email=None,  # Use the default email backend configured in settings
            email_template_name='accounts/password_reset.html',
        )
        messages.success(request, f"A password reset email has been sent to {user_email}.")
        return redirect('login')

    context = {
        'login_form': login_form,
        'signup_form': signup_form,
        'password_reset_form': password_reset_form,
    }
    return render(request, 'accounts/login.html', context)




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

def delete_fertilizers_recycle(request, id):
  member = Fertilizer_Recycle.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse("Fertilizers_recycle"))

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

def delete_ppm(request, id):
  member = Fertilizer_Amount.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse("ppm"))

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

@public_view
def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

@login_exempt
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
  