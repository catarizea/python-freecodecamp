from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.


def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis'

    return render(request, 'index.html', {'feature': feature1})


def counter(request):
    words = request.POST['text']
    counter = len(words.split())
    return render(request, 'counter.html', {'counter': counter})
