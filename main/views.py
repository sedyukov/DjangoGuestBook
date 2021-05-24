from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Review
from .models import Category
from .forms import ReviewForm, UserRegistrationForm
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView, DeleteView
# Create your views here.


class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'main/edit.html'
    form_class = ReviewForm


class ReviewDeleteView(DeleteView):
    model = Review
    success_url = '/'
    template_name = 'main/delete.html'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'


def index(request):
    reviews = Review.objects.order_by('-date')
    category = Category.objects.all()
    return render(request, 'main/index.html', {'reviews': reviews,
                                               'categories': category,
                                               'title': "Гостевая книга"})


def logout_view(request):
    logout(request)
    return redirect(index)


def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            error = "Форма была некорректно заполнена"

    reviews = Review.objects.order_by('-date')
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


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/signup.html', {'form': user_form})