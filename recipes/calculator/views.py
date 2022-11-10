from django.shortcuts import render

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

}

   
def recipe(request, dish):
    persons = int(request.GET.get('servings', 1))
    recipe = {}
    if dish in DATA.keys():
        for ing, amount in DATA[dish].items():
            recipe[ing] = amount * persons
    context = {
        'recipe': recipe
    }
    return render(request, "calculator/index.html", context)

