from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Review
from .models import Category
from .forms import ReviewForm
# Create your views here.


def index(request):
    reviews = Review.objects.order_by('-date')
    category = Category.objects.all()
    return render(request, 'main/index.html', {'reviews': reviews,
                                               'categories': category,
                                               'title': "Гостевая книга"})


def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            error = "Форма была некорректно заполнена"

    reviews = Review.objects.all()
    category = Category.objects.all()
    form = ReviewForm()
    return render(request, 'main/create.html', {'reviews': reviews,
                                               'categories': category,
                                               'title': "Гостевая книга",
                                               'form': form})


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


def bydate(request):
    reviews = Review.objects.order_by('date')
    category = Category.objects.all()
    return render(request, 'main/index.html', {'reviews': reviews,
                                               'categories': category,
                                               'title': "Гостевая книга"})


def byalphauth(request):
    reviews = Review.objects.order_by('author')
    category = Category.objects.all()
    return render(request, 'main/index.html', {'reviews': reviews,
                                               'categories': category,
                                               'title': "Гостевая книга"})


def byalphtext(request):
    reviews = Review.objects.order_by('text')
    category = Category.objects.all()
    return render(request, 'main/index.html', {'reviews': reviews,
                                               'categories': category,
                                               'title': "Гостевая книга"})