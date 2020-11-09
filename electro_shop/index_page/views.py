from django.shortcuts import render

from .forms import SearchForm
from .get_search_selenium import search_selenium
from .Currency_json import get_json
import time

def search_views(request):

    search_result = None
    json_results = get_json()
    search_result1 = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            search_result = search_selenium(form.cleaned_data['search'])
            time.sleep(3)
            search_result1 = search_selenium(form.cleaned_data['search'])
            time.sleep(3)

    else:
        form = SearchForm()

    context = {
        'form': form,
        'search_result': search_result,
        'search_result1': search_result1,
        'json_results': json_results,
          }

    return render(request, 'homepage.html', context)

