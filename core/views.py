from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
import random


systems = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

last_damaged_system = None

def status_view(request):
    global last_damaged_system
    last_damaged_system = random.choice(list(systems.keys()))
    return JsonResponse({"damaged_system": last_damaged_system})

def repair_bay_view(request):
    if not last_damaged_system:
        return HttpResponseBadRequest("Call /status first")
    code = systems[last_damaged_system]
    html = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Repair</title></head>
    <body><div class="anchor-point">{code}</div></body>
    </html>
    """
    return HttpResponse(html)

def teapot_view(request):
    return HttpResponse("I'm a teapot", status=418)