from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def pepe(request):
    return JsonResponse({"message": "hello"})
