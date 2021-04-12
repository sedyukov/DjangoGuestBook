from django.shortcuts import render
from django.http import HttpResponse
from .models import Review
# Create your views here.


def index(request):
    reviews = Review.objects.all()
    return render(request, 'main/index.html', {'reviews': reviews, 'title': "Гостевая книга"})