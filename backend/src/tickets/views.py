from django.shortcuts import render
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    return render(request, 'tickets/home.html')


