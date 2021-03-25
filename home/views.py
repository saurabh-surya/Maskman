from django.shortcuts import render, HttpResponse
from .models import Product
from home.models import Contact

products = Product.objects.all()
# Create your views here.
def index(request):
    print(products)
    par = { 'product': products}
    return render(request, 'index.html', par)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name =request.POST.get('name')
        email =request.POST.get('email')
        desc =request.POST.get('desc')
        contact=Contact(name=name,email=email,desc=desc)
        contact.save()
    return render(request, 'contact.html')

def detail(request,mod):
    det = {}
    print(mod)
    for i in products:
        if(i.model==mod):
            det = { 'details' : i}
    return render(request, 'detail.html',det)
