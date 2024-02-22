from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def demo(request):
    return HttpResponse("hello milan!")

def demo1(request):
    return JsonResponse({'1': 'Hi bro', '2': 'milan','A': 23})