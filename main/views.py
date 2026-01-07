from django.shortcuts import render


def home(request):
    context = {
        'name': 'Hudson Matheus',
        'rank': 'Faixa Marrom',
        'quote': '"Disciplina, honra e respeito."',
        'active': 'conquistas',
    }
    return render(request, 'main/docs/index.html', context)
