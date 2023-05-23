from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    
    elif request.method == 'POST':
        user_id = request.POST.get('id', '')
        user_pw = request.POST.get('pswd1', '')
        user_pw_confirm = request.POST.get('pswd2', '')
        user_name = request.POST.get('name', '')
        user_phone = request.POST.get('phone', '')
        user_email = request.POST.get('email', '')

        if (user_id or user_pw or user_pw_confirm or user_name or user_email or user_phone) == '':
            return redirect('register')
        elif user_pw != user_pw_confirm:
            return redirect('register')
        else:
            user = User(
                user_id=user_id,
                user_pw=user_pw,
                user_name=user_name,
                user_phone=user_phone,
                user_email=user_email
            )
            user.save()
        return redirect('/login')
