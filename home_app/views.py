from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from home_app.forms import ImageForm
from . import models
from . import forms


def index(request):
    return render(request, 'home_app/base1.html')


def get_all_products(request):
    products = models.Product.objects.all()
    return render(request, 'home_app/products.html', {'products': products})


def change_product(request, product_id):
    product = models.Product.objects.filter(pk=product_id).first()
    form = forms.ProductForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        image = form.cleaned_data['image']
        if isinstance(image, bool):
            image = None
        if image is not None:
            fs = FileSystemStorage()
            fs.save(image.name, image)
        product.name = form.cleaned_data['name']
        product.description = form.cleaned_data['description']
        product.price = form.cleaned_data['price']
        product.amount = form.cleaned_data['amount']
        product.image = image
        product.save()
        return redirect('products')
    else:
        form = forms.ProductForm(initial={'name': product.name, 'description': product.description,
                                          'price': product.price, 'amount': product.amount, 'image': product.image})

    return render(request, 'home_app/change_product.html', {'form': form})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES) # request.POST ����� �������� ��������� ���������� , request.FILES ����� �������� �����
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()  # FileSystemStorage ��������� ��������� �������� � �������
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'home_app/upload_ima