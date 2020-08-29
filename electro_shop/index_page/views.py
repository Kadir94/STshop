from django.shortcuts import render
import json
import requests
from .forms import SearchForm
from .get_search_selenium import search_selenium


def search_views(request):
    array1 = []
    array2 = []
    # search_result = None

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            search_result = search_selenium(form.cleaned_data['search'])
            response = requests.get('https://api.exchangeratesapi.io/latest?base=USD%27')
            data = json.loads(response.text)
            rate = data['rates']
            print(rate)
            for x in rate:
             array1.append(round(rate[x], 3))
             array2.append(x)
    else:
        form = SearchForm()

    context = {
        'liste': array1,
        'sth': array2,
        'form':form,
        'search_result':search_result,}

    return render(request, 'homepage.html', context)
