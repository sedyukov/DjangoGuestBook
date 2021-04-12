from django.shortcuts import render
from django.http import HttpResponse
from .models import Review
from .models import Category
# Create your views here.


def index(request):
    reviews = Review.objects.all()
    category = Category.objects.all()
    return render(request, 'main/index.html', {'reviews': reviews, 'categories': category, 'title': "Гостевая книга"})
