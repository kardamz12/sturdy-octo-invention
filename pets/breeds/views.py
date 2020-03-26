from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Breed

# Create your views here.

def get_breedlist(request):
    queryset = Breed.objects.all()
    return render(request, 'get_breedlist.html', {'profiles':queryset})

def post_breedlist(request):
    if request.method == 'POST':
        name = request.POST['name']
        size = request.POST['size']
        friendliness = request.POST['friendliness']
        trainability = request.POST['trainability']
        sheddingamount = request.POST['sheddingamount']
        exerciseneeds = request.POST['exerciseneeds']

        user = User.objects.create_user(name=name, size=size, friendliness=friendliness, trainability=trainability, sheddingamount=sheddingamount,
                                        exerciseneeds=exerciseneeds)
        user.save();
        messages.info(request, 'Breed details added.')
        return redirect('get_breedlist')
    else:
        messages.info(request, 'Breed details not added.')
        return render(request, 'get_breedlist')

def get_breeddetail(request):
    queryset = Breed.objects.get(id=2)
    return render(request, 'get_breed.html', {'profile': queryset})

def put_breeddetail(request):
    queryset = Breed.objects.get(id=1)
    queryset.name = "abc"
    queryset.save()
    return render(request, 'get_breed.html', {'profile': queryset})

def delete_breeddetail(request):
    queryset = Breed.objects.get(name='abc')
    queryset.delete()
    queryset = Breed.objects.all()
    return render(request, 'get_breedlist.html', {'profiles': queryset})