from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from main.models import Product
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.

@csrf_exempt
def login(request):
    try:
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
    except:
        username = request.POST['username']
        password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Login status successful.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login successful!"
                # Add other data if you want to send data to Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed, account is disabled."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed, please check your username or password."
        }, status=401)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password1 = data['password1']
        password2 = data['password2']

        # Check if the passwords match
        if password1 != password2:
            return JsonResponse({
                "status": False,
                "message": "Passwords do not match."
            }, status=400)
        
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "status": False,
                "message": "Username already exists."
            }, status=400)
        
        # Create the new user
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        
        return JsonResponse({
            "username": user.username,
            "status": 'success',
            "message": "User created successfully!"
        }, status=200)
    
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=400)

def product_detail_api(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    
        product.increment_views() 
        
        product_data = {
            "id": str(product.id),
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "product_views": product.product_views, 
            "thumbnail": product.thumbnail,
            "category": product.category,
            "stock": product.stock,
            "created_at": product.created_at.isoformat() if product.created_at else None,
            "is_featured": product.is_featured,

        }

        return JsonResponse(product_data, status=200)

    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def logout(request):
    username = request.user.username
    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logged out successfully!"
        }, status=200)
    except:
        return JsonResponse({
            "status": False,
            "message": "Logout failed."
        }, status=401)