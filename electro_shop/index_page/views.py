from django.shortcuts import render

from .forms import SearchForm
from .get_search_selenium import search_selenium
from .Currency_json import get_json

def search_views(request):

    search_result = None
    json_results = get_json()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            search_result = search_selenium(form.cleaned_data['search'])


    else:
        form = SearchForm()

    context = {
        'form': form,
        'search_result': search_result,
        'json_results': json_results,
          }

    return render(request, 'homepage.html', context)

