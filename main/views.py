from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json




def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'stock': product.stock,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)


def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        json_data = {'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'stock': product.stock,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user else None,}

        return JsonResponse(json_data)
    except Product.DoesNotExist:
        return JsonResponse({'detail' : 'Not found'}, status=404)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        product_list = Product.objects.all()
        productstockunder5 = Product.objects.filter(stock__lt=5).values()

    else:
        product_list = Product.objects.filter(user=request.user)

    

    context = {
        'npm' : '2406358636',
        'name': 'Fidel Akilah',
        'class': 'PBP F',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'productstockunder5': productstockunder5,
    }

    return render(request, "main.html", context)

@csrf_exempt
@require_POST
def add_product_ajax(request):
    # Basic validation
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    stock = request.POST.get("stock")

    if not all([name, price, stock]):
        return JsonResponse({'status': 'error', 'message': 'Name, price, and stock are required.'}, status=400)

    try:
        new_product = Product(
            name=name,
            price=price,
            description=strip_tags(request.POST.get("description")),
            stock=stock,
            category=request.POST.get("category"),
            thumbnail=request.POST.get("thumbnail") or None,
            is_featured=request.POST.get("is_featured") == "on",
            user=request.user
        )
        new_product.save()
        
        return JsonResponse({
            'status': 'success', 
            'message': f"Product '{name}' added successfully!"
        }, status=201)

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {str(e)}'}, status=400)


def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        # Add success message
        messages.success(request, f"Product '{product_entry.name}' was created successfully.")
        return redirect('main:show_main')
    context = {'form': form}
    return render(request, "create_product.html", context)

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        saved_product = form.save()
        # Add success message
        messages.success(request, f"Product '{saved_product.name}' was updated successfully.")
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product_name = product.name
    product.delete()
    # Add success message
    messages.success(request, f"Product '{product_name}' was deleted.")
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def register(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'register.html', context)

# NEW: AJAX view for handling registration
@require_POST
def register_ajax(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

    form = UserCreationForm(data)
    if form.is_valid():
        form.save()
        return JsonResponse({
            'status': 'success',
            'message': 'Account created successfully! You can now log in.'
        })
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

# MODIFIED: This view now only displays the login page.
def login_user(request):
   if request.user.is_authenticated:
       return redirect('main:show_main')
   form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

# NEW: AJAX view for handling login
@require_POST
def login_ajax(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    
    form = AuthenticationForm(request, data=data)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        
        response_data = {
            'status': 'success',
            'redirect_url': reverse('main:show_main')
        }
        
        # We create a JsonResponse and then set the cookie on it
        response = JsonResponse(response_data)
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    else:
        # Non-field errors are the main login errors (e.g., "invalid credentials")
        errors = form.non_field_errors()
        return JsonResponse({'status': 'error', 'message': errors[0] if errors else 'Invalid form data.'}, status=400)

def logout_user(request):
    logout(request)
    # Add info message
    messages.info(request, "You have been successfully logged out.")
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
