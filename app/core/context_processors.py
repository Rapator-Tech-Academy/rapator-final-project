from core.models import Category, Product


def latest_posts(request):
    post = Product.objects.all()[:2]
    return {'latest_posts': post}
