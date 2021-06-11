from main.models import Category


def categories_list(request):
    queryset = Category.objects.all()
    return {'categories': queryset}