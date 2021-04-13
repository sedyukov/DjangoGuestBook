from django.shortcuts import render
from django.http import HttpResponse
from .models import Review
from .models import Category
from .forms import ReviewForm
# Create your views here.


def index(request):
    reviews = Review.objects.all()
    category = Category.objects.all()
    return render(request, 'main/index.html', {'reviews': reviews, 'categories': category, 'title': "Гостевая книга"})


def personal(request):
    reviews = Review.objects.filter(category=1)
    category = Category.objects.all()
    return render(request, 'main/index.html', {'reviews': reviews, 'categories': category, 'title': "Гостевая книга"})


def cowork(request):
    reviews = Review.objects.filter(category=3)
    category = Category.objects.all()
    return render(request, 'main/index.html', {'reviews': reviews, 'categories': category, 'title': "Гостевая книга"})


def optimization(request):
    reviews = Review.objects.filter(category=4)
    category = Category.objects.all()
    return render(request, 'main/index.html', {'reviews': reviews, 'categories': category, 'title': "Гостевая книга"})


def other(request):
    reviews = Review.objects.filter(category=5)
    category = Category.objects.all()
    return render(request, 'main/index.html', {'reviews': reviews, 'categories': category, 'title': "Гостевая книга"})
