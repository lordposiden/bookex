from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == "POST":
        user = Usermodel(
            username=request.POST['username'],
            password=request.POST['password'],
            user_image=request.FILES.get('user_image')
        )
        user.save()
        return redirect('login')
    return render(request, "register.html")



def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        try:
            user = Usermodel.objects.get(username=username)
            if user.password == password:
                request.session['user_id'] = user.user_id
                return redirect('index')
            else:
                messages.error(request,"invalid password or username")
                return redirect('login')
        except Usermodel.DoesNotExist:
            messages.error(request,"invalid username or password")
            return redirect('login')
    return render(request,'login.html')
