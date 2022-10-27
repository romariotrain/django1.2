from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
omlet = DATA['omlet']



def omlet_recipe(request):
    servings = int(request.GET.get('servings', 1))
    omlet = DATA['omlet']
    for ingredients in omlet:
        omlet[ingredients] = omlet[ingredients] * servings
    context = {'recipe': omlet}
    return render(request, 'calculator/index.html', context)


def pasta_recipe(request):
    servings = int(request.GET.get('servings', 1))
    pasta = DATA['pasta']
    for ingredients in pasta:
        pasta[ingredients] = pasta[ingredients] * servings
    context = {'recipe': pasta}
    pasta = DATA['pasta']
    return render(request, 'calculator/index.html', context)

def buter_recipe(request):
    servings = int(request.GET.get('servings', 1))
    buter = DATA['buter']
    for ingredients in buter:
        buter[ingredients] = buter[ingredients] * servings
    context = {'recipe': buter}
    buter = DATA['buter']
    return render(request, 'calculator/index.html', context)







# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

