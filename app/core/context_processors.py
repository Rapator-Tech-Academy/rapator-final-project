from core.models import City

def cities(request):
    cities = City.objects.all().order_by('name')

    return {
        'cities': cities
    }