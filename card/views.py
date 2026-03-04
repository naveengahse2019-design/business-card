import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.core.cache import cache




def home(request):
    return render(request,"mangalla.html")

def metal_rates(request):
    url = "https://api.metals.dev/v1/latest"

    params = {
        "api_key": settings.METALS_API_KEY,
        "currency": "INR",
        "unit": "toz"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        return JsonResponse(data)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)