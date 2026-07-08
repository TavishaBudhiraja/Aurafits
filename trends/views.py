from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Contact_Query
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
    
def home(request):
    all_products = Product.objects.all().order_by("id")

    if request.user.is_authenticated:
        paginator = Paginator(all_products, 3)
        page_number = request.GET.get("page")
        product_info = paginator.get_page(page_number)

        return render(request, 'trends/home.html', {
            'product_info': product_info,
            'is_paginated': True,
        })

    else:
        product_info = all_products[:3]

        return render(request, 'trends/home.html', {
            'product_info': product_info,
            'is_paginated': False,
            'warning': 'Please login to view more products.',
            'show_login_prompt': True,
        })

def findproduct(request):
    if request.method == 'POST':
        x = request.POST.get('prod_search')
        #print(x)
        mydata = Product.objects.filter(Q(product_name__icontains= x)| Q(product_category__icontains= x)| Q(product_id__icontains= x))
        #print(mydata)
        if mydata:
                 return render(request,'trends/home.html', {'product_info' :mydata})
        else:
            return render(request,'trends/home.html', {'warning': 'No Record Found'})    

def about(request):
    return render(request, 'trends/about.html')     
   
def contact(request):
    return HttpResponse('Contact Page')

@login_required(login_url="loginuser")
def products(request):
    selected_category = request.GET.get("category", "").strip()

    myproducts = Product.objects.all().order_by("id")

    if selected_category == "Men":
        myproducts = myproducts.filter(
            Q(product_category__icontains="Men") |
            Q(product_category__icontains="Mens") |
            Q(product_category__icontains="Male")
        ).exclude(
            product_category__icontains="Women"
        )

    elif selected_category == "Women":
        myproducts = myproducts.filter(
            Q(product_category__icontains="Women") |
            Q(product_category__icontains="Female") |
            Q(product_category__icontains="Ladies")
        )

    paginator = Paginator(myproducts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "trends/product.html", {
        "page_obj": page_obj,
        "selected_category": selected_category,
    })

def contact(request):
    if request.method == 'GET':
     return render(request,'trends/contact.html') 
    else:
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('message')
        new_data = Contact_Query(name=a, email=b, message=c)
        new_data.save()
        return render(request,'trends/contact.html',{'x': 'Message Sent Successfully'}) 
    
def loginuser(request):
    if request.method == 'GET':
        return render(request,'trends/loginuser.html',{'form': AuthenticationForm()}) 

    else:
        a = request.POST.get('username')
        b = request.POST.get('password')

        user = authenticate(request, username=a, password=b)
        
        if user is None:
            return render(request,'trends/loginuser.html',{'form': AuthenticationForm(), 'error':'Invalid Credentials'})
        else:
            login(request, user)
            return redirect('home')

def signupuser(request):
    if request.method == 'GET':
     return render(request,'trends/signupuser.html',{'form': UserCreationForm()}) 
    else:
        a = request.POST.get('username')
        b = request.POST.get('password1')
        c = request.POST.get('password2')
        if b==c:
                #check whether user name is unique
            if (User.objects.filter(username=a)):
                return render(request,'trends/signupuser.html',{'form': UserCreationForm(),'error': 'User Name Already exists Try again with different username'})
            else:
                user = User.objects.create_user(username = a,password = b)
                user.save()
                login(request,user)
                return redirect('home')
        else:
            # password 1 and 2 do not match
            return render(request,'trends/signupuser.html',{'form': UserCreationForm(),'error': 'Password Mismatch Try Again'})
    
def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')