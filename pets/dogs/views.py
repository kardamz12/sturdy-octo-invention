from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Dog

# Create your views here.
def base(request):
    return render(request, 'base.html')

def get_doglist(request):
    queryset = Dog.objects.all()
    return render(request, 'get_doglist.html', {'profiles':queryset})

def post_doglist(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        breed = request.POST['breed']
        gender = request.POST['gender']
        color = request.POST['color']
        favoritefood = request.POST['favoritefood']
        favoritetoy = request.POST['favoritetoy']

        user = User.objects.create_user(name=name, age=age, breed=breed, gender=gender, color=color,
                                        favoritefood=favoritefood, favoritetoy=favoritetoy)
        user.save();
        messages.info(request, 'Dog details added.')
        return redirect('get_doglist')
    else:
        messages.info(request, 'Dog details not added.')
        return render(request, 'get_doglist')

def get_dogdetail(request):
    queryset = Dog.objects.get(id=2)
    return render(request, 'get_dog.html', {'profile': queryset})

def put_dogdetail(request):
    queryset = Dog.objects.get(id=1)
    queryset.name = "Neelu"
    queryset.save()
    return render(request, 'get_dog.html', {'profile': queryset})

def delete_dogdetail(request):
    queryset = Dog.objects.get(name='aa')
    queryset.delete()
    queryset = Dog.objects.all()
    return render(request, 'get_doglist.html', {'profiles': queryset})