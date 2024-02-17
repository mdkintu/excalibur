from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

# this view didnt have a form to login
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')  # Replace 'home' with appropriate redirect 
#         else:
#             messages.error(request, 'Username or password is incorrect.')
#     return render(request, 'accounts/login.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(data=request.POST, request=request)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
    else:
        form = LoginForm()
        messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('index')

@login_required(login_url='login')  # Ensure user is logged in
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@login_required(login_url='login')  # Ensure user is logged in
def post_job(request):
    return HttpResponse('This is the  Post Job View')

@login_required(login_url='login')  # Ensure user is logged in
def inbox_new(request):
    return HttpResponse('This is the new messages View')
