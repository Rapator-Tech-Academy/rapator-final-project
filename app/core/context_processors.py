from core.models import Category, Product, City


def latest_products(request):
    product = Product.objects.all()
    return {'latest_products': product}


def cities(request):
    cities = City.objects.all().order_by('name')

    return {
        'cities': cities
    }
