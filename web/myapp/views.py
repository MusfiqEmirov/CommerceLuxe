import datetime
import os
import random
from django.shortcuts import render,redirect,render,get_object_or_404
from django.http.response import HttpResponse,HttpResponseRedirect,HttpResponseNotFound,Http404
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from .models import Product, UploadModel
from django.db.models import Avg, Min, Max
from .forms import ProductCreateForm, ProductEditForm, UploadForm

def index(request):
    
    products = Product.objects.filter(isActive=True).order_by("-price")
    # product_count = Product.objects.filter(isActive=True).count()
    # avg_price = Product.objects.filter(isActive=True).aggregate(Avg("price"))
    context = {
        "products":products,
        # "product_count":product_count,
        # "avg_price":avg_price
    }
    return render(request, 'my_app/index.html', context)

@login_required(login_url="/account/login")
def list(request):
    
    if "q" in  request.GET and request.GET.get("q"):
        q = request.GET["q"]
        products = Product.objects.filter(name__contains=q)
    else:
        products = Product.objects.all().order_by("-price")
    context = {
        "products":products,
    }
    return render(request, 'my_app/list.html', context)

@login_required(login_url="/account/login")
def create(request):
    if request.method == "POST":
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
       form = ProductCreateForm()


    return render(request, "my_app/create.html",{
        "form":form
    })

@login_required(login_url="/account/login")
def edit(request,id):
    product = get_object_or_404(Product,pk=id)

    if request.method == "POST":
        form = ProductEditForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect("list")
        
    else:
        form = ProductEditForm(instance=product)

    return render(request,"my_app/edit.html",{
        "form":form
    })  

@login_required(login_url="/account/login")
def delete(request,id):
    product = get_object_or_404(Product,pk=id)
    
    if request.method == "POST":
        product.delete()
        return redirect("list")
    return render(request,"my_app/delete_confirm.html",{
        "product":product
    })


@login_required(login_url="/account/login")
def detalis(request,slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        "product":product
    }

    return render(request,"my_app/detalis.html",context)

# def handle_uploaded(file):
#     number = random.randint(10000, 99999)
#     file_name, file_extension = os.path.splitext(file.name)
#     name = file_name +"-"+ str(number) + file_extension

#     with open("temp/" + name, "wb+") as destination:
#         for chunk in file.chunks():
#             destination.write(chunk)


@login_required(login_url="/account/login")
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            model = UploadModel(image = request.FILES["image"])
            model.save()
            return render(request, "my_app/success.html")
    else:
        form = UploadForm()
    return render(request, "my_app/upload.html", {
        "form":form
    })























































# def getByTelefonId(request,category):

#     data_keys_list = list(data.keys())
#     if category > len(data_keys_list):
#         return HttpResponseNotFound("bu id haqqinda melumat yoxdur")
#     redirect_text = data_keys_list[category - 1]

#     redirect_path = reverse("product_name",args=[redirect_text])
#     return redirect(redirect_path)

# def getByTelefon(request, category):
#     # data_keys = list(data.keys())
#     try:
#         product = data[category]
#         return render(request,"products.html",{
#             "products":product,
#             "category":category,
#             "now":datetime.datetime.now()
            
#         })
#     except:
#         return HttpResponseNotFound("bu id haqqinda melumat yoxdur")




