from django.shortcuts import render
from datetime import date

def index(request):
    context = {
        'hoje': date.today()
    }
    return render(request, 'index.html', context)
