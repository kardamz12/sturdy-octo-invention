from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Dog

# Create your views here.
def base(request):
    try:
        return render(request, 'base.html')
    except:
        messages.info(request, "Couldn't render 'base.html'.")

def get_doglist(request):
    try:
        queryset = Dog.objects.all()
        return render(request, 'get_doglist.html', {'profiles':queryset})
    except queryset.DoesNotExist:
        messages.info(request, "Couldn't fetch the Dog list.")

def post_doglist(request):
    try:
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
            messages.info(request, 'Dog details added. Please find the updated Dog list below:')
            queryset = Dog.objects.all()
            return render(request, 'get_doglist.html', {'profiles': queryset})
        else:
            messages.info(request, 'Dog details not added.')
            queryset = Dog.objects.all()
            return render(request, 'get_doglist.html', {'profiles': queryset})
    except:
        messages.info(request, 'Dog details not added(Inside except)')

def get_dogdetail(request):
    try:
        queryset = Dog.objects.get(id=2)
        return render(request, 'get_dog.html', {'profile': queryset})
    except queryset.DoesNotExist:
        messages.info(request, "Couldn't fetch the Dog details.")

def put_dogdetail(request):
    try:
        queryset = Dog.objects.get(id=1)
        queryset.name = "Neel"
        queryset.save()
        return render(request, 'get_dog.html', {'profile': queryset})
    except queryset.DoesNotExist:
        messages.info(request, "Couldn't update a Dog details.")

def delete_dogdetail(request):
    try:
        queryset = Dog.objects.get(name='aa')
        queryset.delete()
        queryset = Dog.objects.all()
        return render(request, 'get_doglist.html', {'profiles': queryset})
    except queryset.DoesNotExist:
        messages.info(request, "Couldn't delete a Dog details.")