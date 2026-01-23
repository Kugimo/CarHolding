from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .forms import CarCreateForm
from .models import Car, Category


def index_view(request):
    cars = Car.objects.all()

    if 'search' in request.GET:
        search = request.GET['search']

        cars = cars.filter(title__icontains=search)

    return render(request, 'app/index.html', {'cars': cars})


def car_detail_view(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'app/car_detail.html', {'car': car})


def car_create_view(request):
    categories = Category.objects.all()


    if request.method == 'POST':
        title = request.POST['title']
        category_id = request.POST['category_id']
        model = request.POST['model']
        year = request.POST['year']
        price = request.POST['price']
        image = request.FILES['image']

        category = Category.objects.get(id=category_id)

        car = Car(title=title, category = category, model=model, year=year, price=price, image=image)
        car.save()

        return redirect("index")

    return render(request, 'app/car_create.html', {'categories': categories})


def car_update_view(request, car_id):
    categories = Category.objects.all()
    car = Car.objects.get(id=car_id)

    if request.method == 'POST':
        title = request.POST['title']
        category_id = request.POST['category_id']
        model = request.POST['model']
        year = request.POST['year']
        price = request.POST['price']
        image = request.FILES['image']

        category = Category.objects.get(id=category_id)

        car.title = title
        car.category = category
        car.model = model
        car.year = year
        car.price = price
        car.image = image

        car.save()

        return redirect("index")

    return render(request=request, template_name='app/car_update.html', context={'categories': categories, 'car': car})

def car_delete_view(request, car_id):
    car = Car.objects.get(id=car_id)
    car.delete()

    return redirect("index")

def car_create_2(request):
    if request.method == 'POST':
        form = CarCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("index")
    form = CarCreateForm()
    return render(request, 'app/car_create_2.html', {'form': form})

def user_register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Вы успешно создали аккаунт')
            return redirect("index")

        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f'{error}')
    form = UserCreationForm()
    return render(request, 'app/user_register.html', context={'form': form})

def user_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему')
            return redirect("index")
        messages.error(request, 'Неправильный логин или пароль')

    return render(request, 'app/user_login.html')


