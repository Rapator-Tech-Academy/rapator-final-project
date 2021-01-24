from core.models import Category, Product

def latest_posts(request):
    post = Product.objects.all()[:2]
    return {'latest_posts': post}
from core.models import City


def cities(request):
    cities = City.objects.all().order_by('name')

    return {
        'cities': cities
    }
