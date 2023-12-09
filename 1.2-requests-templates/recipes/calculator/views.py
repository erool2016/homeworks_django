from django.shortcuts import render
from django.http import HttpResponse, Http404

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

def start_page(request):
    return HttpResponse(DATA.items())

def choice(request):
    name = request.GET.get('name')
    quant = request.GET.get('quant')
    print(name, quant)
    context = {
        'recipe': DATA[name],
        'quant': quant
    }
    return HttpResponse(f'{DATA[name]} {quant}', )
def omlet(request):
    recipie = request.GET.get('name')
    quant = int(request.GET.get('quant',1))
    print(recipie, quant)
    if recipie:
        calc = {}
        for key in DATA[recipie].keys():
            calc[key] = DATA[recipie][key] * quant
        print(calc)
        context = {
            'recipe': calc
        }
    return render(request, 'calculator/index.html', context)
# def pasta(request):
#     return render(request, 'calculator/index.html', context)
#
# def buter(request):
#     return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
