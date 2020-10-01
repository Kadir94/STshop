import json
import requests


def get_json():
    array1 = []
    array2 = []
    response = requests.get('https://api.exchangeratesapi.io/latest?base=USD')
    data = json.loads(response.text)
    rate = data['rates']
    for x in rate:
        array1.append(round(rate[x], 3))
        array2.append(x)
    json_data = dict(zip(array2, array1))
    return json_data

