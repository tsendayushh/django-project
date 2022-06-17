from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def get_greetings(request):
    print(request.GET.get('param1', ''))
    return HttpResponse("Working")

