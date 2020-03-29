from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Dog, Breed

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
            post_data = request.POST

            name = post_data.get('name')
            age = post_data.get('age')
            breed_name = post_data.get('breed_name')
            gender = post_data.get('gender')
            color = post_data.get('color')
            favoritefood = post_data.get('favoritefood')
            favoritetoy = post_data.get('favoritetoy')

            if name and age and breed_name and gender and color and favoritefood and favoritetoy:
                instance_dog = Dog()
                instance_dog.name = name
                instance_dog.age = age
                instance_dog.breed_name = breed_name
                instance_dog.gender = gender
                instance_dog.color = color
                instance_dog.favoritefood = favoritefood
                instance_dog.favoritetoy = favoritetoy
                instance_dog.save()

                messages.info(request, 'Dog details added. Please find the updated Dog list below:')
                queryset = Dog.objects.all()
                return render(request, 'get_doglist.html', {"profiles": queryset})
        else:
            return render(request, 'post_doglist.html')
    except:
        messages.info(request, 'Dog details not added(Inside except)')

def get_dogdetail(request):
    try:
        if request.method == 'POST':
            queryset = Dog.objects.get(id=request.POST.get('id'))
            return render(request, 'get_dog.html', {'profile': queryset})
        else:
            return render(request, 'get_dogdetail.html')
    except:
        messages.info(request, "Couldn't fetch the Dog details.")

#curl "http://127.0.0.1:8000/post_doglist"  --data "name=Jonny1^&age=2^&breed=Poodle^&gender=Male^&color=Black^&favoritefood=Pedigree^&favoritetoy=Toy+bone"

def put_dogdetail(request):
    try:
        if request.method == 'POST':
            queryset = Dog.objects.get(id=request.POST.get('id'))
            queryset.name = request.POST.get('name')
            queryset.save()
            queryset = Dog.objects.all()
            return render(request, 'get_doglist.html', {'profiles': queryset})
        else:
            return render(request, 'put_dogdetail.html')
    except queryset.DoesNotExist:
        messages.info(request, "Couldn't update a Dog details.")

def delete_dogdetail(request):
    try:
        if request.method == 'POST':
            queryset = Dog.objects.get(id=request.POST.get('id'))
            queryset.delete()
            queryset = Dog.objects.all()
            return render(request, 'get_doglist.html', {'profiles': queryset})
        else:
            return render(request, 'delete_dogdetail.html')
    except:
        messages.info(request, "Couldn't delete a Dog details.")


def get_breedlist(request):
    try:
        queryset = Breed.objects.all()
        return render(request, 'get_breedlist.html', {'profiles':queryset})
    except queryset.DoesNotExist:
        messages.info(request, "Couldn't fetch the Breed list.")

def post_breedlist(request):
    try:
        if request.method == 'POST':
            post_data = request.POST

            breed_name = post_data.get('breed_name')
            size = post_data.get('size')
            friendliness = post_data.get('friendliness')
            trainability = post_data.get('trainability')
            sheddingamount = post_data.get('sheddingamount')
            exerciseneeds = post_data.get('exerciseneeds')

            if breed_name and size and friendliness and trainability and sheddingamount and exerciseneeds:
                instance_breed = Breed()
                instance_breed.breed_name = breed_name
                instance_breed.size = size
                instance_breed.friendliness = friendliness
                instance_breed.trainability = trainability
                instance_breed.sheddingamount = sheddingamount
                instance_breed.exerciseneeds = exerciseneeds
                instance_breed.save()

                messages.info(request, 'Breed details added. Please find the updated Breed list below:')
                queryset = Breed.objects.all()
                return render(request, 'get_breedlist.html', {'profiles': queryset})
        else:
            return render(request, 'post_breedlist.html')
    except:
        messages.info(request, 'Breed details not added(Inside except)')

def get_breeddetail(request):
    try:
        if request.method == 'POST':
            queryset = Breed.objects.get(id=request.POST.get('id'))
            return render(request, 'get_breed.html', {'profile': queryset})
        else:
            return render(request, 'get_breeddetail.html')
    except:
        messages.info(request, "Couldn't fetch the Breed details.")

def put_breeddetail(request):
    try:
        if request.method == 'POST':
            queryset = Breed.objects.get(id=request.POST.get('id'))
            queryset.name = request.POST.get('name')
            queryset.save()
            queryset = Breed.objects.all()
            return render(request, 'get_breedlist.html', {'profiles': queryset})
        else:
            return render(request, 'put_breeddetail.html')
    except queryset.DoesNotExist:
        messages.info(request, "Couldn't update a Breed details.")

def delete_breeddetail(request):
    try:
        if request.method == 'POST':
            queryset = Breed.objects.get(id=request.POST.get('id'))
            queryset.delete()
            queryset = Breed.objects.all()
            return render(request, 'get_breedlist.html', {'profiles': queryset})
        else:
            return render(request, 'delete_breeddetail.html')
    except:
        messages.info(request, "Couldn't delete a Breed details.")