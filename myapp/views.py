from django.shortcuts import render,redirect
# from .models import *
from myapp.models import SliderModel,AboutModel,BlogModel,ClientModel,ContactModel


# Create your views here.

def HomeSection(request):
    if request.method == "GET":

        slider = SliderModel.objects.all().order_by('-created_at')
        about = AboutModel.objects.all().order_by('-created_at')
        blog = BlogModel.objects.all().order_by('-created_at')[:2]
        client = ClientModel.objects.all()
        return render(request, 'index.html', {'slider':slider, 'about':about, 'blog':blog, 'client':client})
    if request.method == "POST":
        contact = ContactModel.objects.create(
            name = request.POST.get('name'),
            phone = request.POST.get('phone'),
            email = request.POST.get('email'),
            meassage = request.POST.get('message'),
        )
        return redirect('/app/home/')

def AboutSection(request):
    if request.method == "GET":
        about = AboutModel.objects.all()
        return render(request, 'about.html', {'about':about})
    if request.method == "POST":
        contact = ContactModel.objects.create(
            name = request.POST.get('name'),
            phone = request.POST.get('phone'),
            email = request.POST.get('email'),
            meassage = request.POST.get('message'),
        )
        return redirect('/app/home/')

def BlogSection(request):
    if request.method == "GET":
        blog = BlogModel.objects.all()
        return render(request, 'blog.html', {'blog':blog})
    if request.method == "POST":
        contact = ContactModel.objects.create(
            name = request.POST.get('name'),
            phone = request.POST.get('phone'),
            email = request.POST.get('email'),
            meassage = request.POST.get('message'),
        )
        return redirect('/app/home/')