from django.http import HttpResponse
from django.shortcuts import render
from .models import GiftModel as Gift, CategoryModel as Category

def root_view(request):
    # Получаем базовый QuerySet всех товаров
    gifts = Gift.objects.all()
    categories = Category.objects.all()

    # 1. ФИЛЬТРАЦИЯ ПО КАТЕГОРИЯМ
    category_id = request.GET.get('category')
    if category_id:
        # Предполагается, что в модели Gift есть связь с Category (например, category_id)
        gifts = gifts.filter(category_id=category_id)

    # 2. ФИЛЬТРАЦИЯ ПО ДИАПАЗОНУ ЦЕН
    price_range = request.GET.get('price_range')
    if price_range == 'under_25':
        gifts = gifts.filter(price__lt=25)
    elif price_range == '25_50':
        gifts = gifts.filter(price__gte=25, price__lte=50)
    elif price_range == '50_100':
        gifts = gifts.filter(price__gte=50, price__lte=100)
    elif price_range == 'over_100':
        gifts = gifts.filter(price__gt=100)

    # 3. СОРТИРОВКА
    sort_by = request.GET.get('sort')
    if sort_by == 'price_asc':
        gifts = gifts.order_by('price')
    elif sort_by == 'price_desc':
        gifts = gifts.order_by('-price')
    elif sort_by == 'newest':
        gifts = gifts.order_by('-created_at')  # Поменяйте 'created_at' на ваше поле даты создания

    context = {
        'gifts': gifts,
        'categories': categories,
    }
    return render(request, 'catalog.html', context)
