from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Breed

# Create your views here.

def get_breedlist(request):
    try:
        queryset = Breed.objects.all()
        return render(request, 'get_breedlist.html', {'profiles':queryset})
    except queryset.DoesNotExist:
        messages.info(request, "Couldn't fetch the Breed list.")

def post_breedlist(request):
    try:
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
            messages.info(request, 'Breed details added. Please find the updated Breed list below:')
            queryset = Breed.objects.all()
            return render(request, 'get_breedlist.html', {'profiles': queryset})
        else:
            messages.info(request, 'Breed details not added.')
            queryset = Breed.objects.all()
            return render(request, 'get_breedlist.html', {'profiles': queryset})
    except:
        messages.info(request, 'Breed details not added(Inside except)')

def get_breeddetail(request):
    try:
        queryset = Breed.objects.get(id=2)
        return render(request, 'get_breed.html', {'profile': queryset})
    except queryset.DoesNotExist:
        messages.info(request, "Couldn't fetch the Breed details.")

def put_breeddetail(request):
    try:
        queryset = Breed.objects.get(id=2)
        queryset.name = "Jackie"
        queryset.save()
        return render(request, 'get_breed.html', {'profile': queryset})
    except queryset.DoesNotExist:
        messages.info(request, "Couldn't update a Breed details.")

def delete_breeddetail(request):
    try:
        queryset = Breed.objects.get(name='abc')
        queryset.delete()
        queryset = Breed.objects.all()
        return render(request, 'get_breedlist.html', {'profiles': queryset})
    except queryset.DoesNotExist:
        messages.info(request, "Couldn't delete a Breed details.")