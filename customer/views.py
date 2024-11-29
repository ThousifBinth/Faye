from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from seller.models import *
from django.contrib import messages
# Create your views here.

def home(request):
    cust=request.session.get('customer') 
    return render(request,'customer/home.html',{'cust':cust})


def signup(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customerregistration(name=name,email=email,password=password)
        customer.save()
        return redirect('customer:login')
    return render(request, 'customer/signup.html')

def login(request):
    if 'customer_id' in request.session:
        return redirect('customer:dashboard')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        try:
            cust=Customerregistration.objects.get(email=email, password=password, name=name)
            request.session['customer_id'] = cust.id
            request.session['customer_name'] = cust.name
            return redirect('customer:dashboard')
        except Customerregistration.DoesNotExist:
            return render(request, 'customer/login.html', {'msg':'Invalid Credentials'})
    return render(request, 'customer/login.html')
        # if Customerregistration.objects.filter(name=name,email=email, password=password).exists():
        #     return redirect('customer:dashboard')
        # else:
        #     return render(request, 'customer/login.html', {'msg': 'Invalid email or password'})

def dashboard(request):
     if 'customer_id' in request.session:
        customer_name = request.session.get('customer_name')
        products = Product.objects.all()
        return render(request,'customer/dashboard.html', {'products':products,'username': customer_name})
     else:
        return render(request, 'customer/login.html')

         



# def viewproducts(request):
#      # if 'customer' in request.session:

#     products = Product.objects.all()
#     return render(request,'customer/viewproducts.html', {'products':products})

def viewproducts(request):
    return render(request,'customer/viewproducts.html')


def cart(request):
    # if 'customer' in request.session:
    if 'customer_id' in request.session:
        # customer_id = request.session['customer_id']
        
    # Get all items in the cart
        cart_items = Cart.objects.all()
    
    # Calculate the total price and total quantity
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        total_quantity = sum(item.quantity for item in cart_items)
    
    # Prepare a list to store the total price per item
        total_price_per_item = []
        grand_total = 0
    
    # Loop through the cart items and calculate totals
        for item in cart_items:
            item_total = item.product.price * item.quantity
            total_price_per_item.append({'item': item, 'total': item_total})
            grand_total += item_total



# Render the cart template with the cart items, totals, and total quantity
        return render(request, 'customer/cart.html', {
            'cart_items': cart_items,
            'grand_total': grand_total,
            'total_price': total_price,
            'total_price_per_item': total_price_per_item,
            'total_quantity': total_quantity  
        })
    # else:
    #     return render(request, 'customer/home.html')
    


def add_to_cart(request, product_id):
    if 'customer_id in request.session':
        customer_id = request.session['customer_id']
    product = Product.objects.get(id=product_id)
    cart_item,created = Cart.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item.quantity = 1
        cart_item.save()
    cart_item.save()
    # add success message
    messages.success(request,'Product added to cart successfully!!!')
    return redirect('customer:dashboard')

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item = Cart.objects.get(product=product)
    cart_item.delete()
    return redirect('customer:cart')


def search(request):
    products = None
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(description__icontains=keyword)
    
    return render(request, 'customer/viewproducts.html', {'products':products})


def logout(request):
    if 'customer' in request.session:
        del request.session['customer']
        return redirect('customer:home')
    else:
      return render(request, 'customer/logout.html')