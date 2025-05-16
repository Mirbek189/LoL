from django.shortcuts import render
from .models import Product

def home(request):
    selected_brands = request.GET.getlist('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    query = request.GET.get('q')

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if selected_brands:
        products = products.filter(brand__in=selected_brands)

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    context = {
        'products': products,
        'brands': Product.objects.values_list('brand', flat=True).distinct(),
        'selected_brands': selected_brands,
        'query': query or "",
        'min_price': min_price or "",
        'max_price': max_price or "",
    }
    return render(request, 'home.html', context)

