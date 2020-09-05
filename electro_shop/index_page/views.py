from django.shortcuts import render

from .forms import SearchForm
from .get_search_selenium import search_selenium
from .Currency_json import get_json


def search_views(request):
    search_result = None
    json_results = None

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            search_result = search_selenium(form.cleaned_data['search'])
            json_results = get_json()
    else:
        form = SearchForm()

    context = {
        'form': form,
        'search_result': search_result,
        'json_data': json_results,}

    return render(request, 'homepage.html', context)

#search_views()
# def json_views(request):
#     if request.method == 'POST':
#         form = JsonForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     else:
#         form = JsonForm()
#
#     context = {
#         'form': form,
#         'json_results': json_results,
#     }
#     return render(request, 'homepage.html', context)
