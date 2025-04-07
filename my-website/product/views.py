from django.shortcuts import render
# from product.models import ProductModel
import requests

# Create your views here.
def product(request):
    response = requests.get("http://localhost:8000/api/products")
    print(response)
    product_list = response.json()
    # product_list = []

    return render(request, 'product/index.html', {'product_list': product_list})

def detail(request, id):

    # data get from db
    response = requests.get(f"http://localhost:8000/api/products/{id}")
    product = {}

    return render(request, 'product/detail.html', { 'product': product })