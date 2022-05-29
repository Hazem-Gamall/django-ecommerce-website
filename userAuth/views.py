from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm 

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=username, password=password)
        print(username,password, user)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Logged in Successfully'))
            return redirect('/')
        else:
            messages.error(request, ('Invalid login'))
            return redirect('/auth/user_login')
    else:
        return render(request, 'views/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, ('You Logged out Successfully'))
    return(redirect('/'))

def user_register(request):
    if request.method == 'POST':
        print(request.POST['username'], request.POST['password1'])
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Register successful')
            return redirect('/')
        else:
            messages.error(request, 'Register Failed')          
            return render(request, 'views/register.html', {'form':form})
    else:
        form = UserRegisterForm()
        return  render(request, 'views/register.html', {'form':form})