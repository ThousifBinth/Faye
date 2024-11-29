from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request,'seller/home.html')


def login(request):
    return render(request,'seller/login.html')

# def addproducts(request):
#     return render(request,'seller/addproducts.html')

def login(request):
    if request.method == 'POST':
        name=request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if Sellerregistration.objects.filter(name=name, email=email, password=password).exists():
            return redirect('seller:dashboard')
        else:
            return render(request, 'seller/login.html', {'msg': 'Invalid email or password'})
    return render(request, 'seller/login.html')

def dashboard(request):
    return render(request,'seller/dashboard.html')

def viewproducts(request):
    return render(request,'seller/viewproducts.html')

def maincat(request):
    if request.method == 'POST':
        selected_category_id = request.POST.get('pdt_category')
        return redirect('seller:addproducts', category_id=selected_category_id)  # Redirect to addproduct with category_id

    categories = Category.objects.all()  # Fetch all categories for the dropdown
    return render(request, 'seller/maincat.html', {'categories':categories})


def addproducts(request, category_id):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES['image']
        category = Category.objects.get(id=category_id)
        subcategory = Subcategory.objects.get(id=request.POST['pdt_subcategory'])
        product = Product(name=name, category=category, subcategory=subcategory, price=price, description=description, image=image)
        product.save()
        return redirect('seller:viewproducts')
    categories = Category.objects.all()
    subcategories = Subcategory.objects.filter(category=category_id)
    return render(request, 'seller/addproducts.html', {'categories': categories, 'subcategories':subcategories})            


def viewproducts(request):
        products = Product.objects.all()
        return render(request,'seller/viewproducts.html',{'products': products})


def deleteproducts(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('seller:viewproducts')

def editproducts(request, id):
    product = Product.objects.get(id=id)
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('pdt_name')
        price = request.POST.get('pdt_price')
        description = request.POST.get('pdt_description')
        category1 = request.POST.get('pdt_category')
        image = request.FILES.get('pdt_image')

        # Get the category object by id
        cat = Category.objects.get(id=category1)

        # Update the product
        product.name = name
        product.price = price
        product.description = description
        product.category = cat
        if image:
            product.image = image
        product.save()

        return redirect('seller:viewproducts')
    return render(request, 'seller/editproducts.html', {'product': product, 'categories':categories})