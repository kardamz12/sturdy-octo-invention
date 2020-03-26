from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Dog


# Create your views here.
class DogDetail(APIView):
    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DogList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'display_dog.html'

    def get(self, request):
        queryset = Dog.objects.all()
        return Response({'profiles': queryset})
        #return render(request, 'display_dog.html', {'queryset':queryset})

    def post(self, request):
        if request.method == 'POST':
            name = request.POST['name']
            age = request.POST['age']
            breed = request.POST['breed']
            gender = request.POST['gender']
            color = request.POST['color']
            favoritefood = request.POST['favoritefood']
            favoritetoy = request.POST['favoritetoy']

            user = User.objects.create_user(name=name, age=age, breed=breed, gender=gender, color=color, favoritefood=favoritefood, favoritetoy=favoritetoy)
            user.save();
            messages.info(request, 'Dog details added.')
            return redirect('display_dog')
        else:
            messages.info(request, 'Dog details not added.')
            return redirect('display_dog')
