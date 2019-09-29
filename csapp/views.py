# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from scrap import scrape_car_models, scrape_car_maker
# Create your views here.

def index(request):
    
    return render(request, 'csapp/index.html')

def makers(request):

    return JsonResponse(scrape_car_maker(), safe=False)
    
def makers_req(request, num):

    return JsonResponse(scrape_car_models(num), safe=False)