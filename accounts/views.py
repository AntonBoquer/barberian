from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout



from .models import *

@login_required(login_url='login')
def home(request):
    return render(request,'accounts/dashboard.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def addproduct(request):
    products = beverage.objects.all()
    return render(request,'accounts/addproduct.html',{'products': products})

@login_required(login_url='login')
def removeproduct(request):
    products = beverage.objects.all()
    return render(request,'accounts/removeproduct.html',{'products': products})

@login_required(login_url='login')
def addservice(request):
    service = supplie.objects.all()
    return render(request,'accounts/addservice.html', {'supplie': service})

@login_required(login_url='login')
def removeservice(request):
    service = supplie.objects.all()
    return render(request,'accounts/removeservice.html', {'supplie': service})

@login_required(login_url='login')
def products(request):
    products = beverage.objects.all()
    return render(request,'accounts/products.html',{'products': products})

@login_required(login_url='login')
def service(request):
    service = supplie.objects.all()
    return render(request,'accounts/service.html', {'supplie': service})

@login_required(login_url='login')
def inventory(request):
    products = beverage.objects.all()
    service = supplie.objects.all()
    context = {'products': products, 'supplie': service}
    return render(request,'accounts/inventory.html', context)
  
@login_required(login_url='login')
def update(request, id):
  mymember = supplie.objects.get(id=id)
  template = loader.get_template('accounts/addservice.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def updaterecord(request, id):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        member = get_object_or_404(supplie, id=id)
        member.amount = amount
        member.save()
        return redirect('service')  # Redirect to 'addservice' URL after updating the value
    elif request.method == 'GET':
        # If it's a GET request, you should render the addservice.html template with the form
        mymember = get_object_or_404(supplie, id=id)
        return render(request, 'accounts/addservice.html', {'mymember': mymember})
    else:
        return HttpResponse("Invalid request method")

@login_required(login_url='login')
def updateDrink(request, id):
    mymember = beverage.objects.get(id=id)
    template = loader.get_template('accounts/addproduct.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def updaterecordDrink(request, id):
    if request.method == 'POST':
        amount = request.POST['amount']
        member = beverage.objects.get(id=id)
        member.amount = amount
        member.save()
        return redirect('products')
    else:
        return HttpResponse("Invalid request method")
# Create your views here.
