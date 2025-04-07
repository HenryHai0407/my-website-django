from django.shortcuts import render
from product.models import ProductModel

# Create your views here.
def product(request):

    product_list = ProductModel.objects.all()

    return render(request, 'product/index.html', {'product_list': product_list})

def detail(request, id):

    # data get from db

    product = ProductModel.objects.get(pk=id)

    return render(request, 'product/detail.html', { 'product': product })