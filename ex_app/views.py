from django.shortcuts import render
from django.http import JsonResponse
import requests

def test_api(request):
    url = "https://api.github.com/events"
    nxt = request.GET.get('n')
    prv = request.GET.get('p')

    if nxt:
        response = requests.get(nxt).json()
    elif prv:
        response = requests.get(prv).json()
    else:
        response = requests.get(url).json()
        
    context = {
    'responses': response,
    }
    return render(request, 'api.html', context)


def api_detail(request):
    url = request.GET.get('detail')
    response = requests.get(url).json()
    context = {
    'response': response,
    }
    return render(request,'api_detail.html', context)