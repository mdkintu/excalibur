from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Message
from .forms import  ProfileForm
from django.db.models import Q

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
        username=request.POST['username']
        password=request.POST['password']
        form = LoginForm(data=request.POST, request=request)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            form = LoginForm()
    else:
        form = LoginForm()
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
    return HttpResponse('This is the Job Post View')

@login_required(login_url='login')  # Ensure user is logged in
def post_find(request):
    return HttpResponse('This is the  Job Search View')

@login_required(login_url='login')  # Ensure user is logged in
def inbox_new(request):
    profile=request.user.profile
    messageRequests=profile.messages.all()
    unreadCount=messageRequests.filter(is_read=False).count
    context={'messageRequests':messageRequests, 'unreadCount':unreadCount}
    return render(request, 'accounts/inbox.html', context)

@login_required(login_url='login')
def viewMessage(request, pk):
    profile=request.user.profile
    message=profile.message.get(id=pk)
    context={'message':message}
    return render (request, 'accounts/message.html', context)

@login_required
def view_profile(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'accounts/view_profile.html', context)

@login_required(login_url='login')
def update_profile(request):
    # if request.method == 'POST':
    #     # Process form data to update profile (we'll cover the form soon)
    #     profile = request.user.profile 
    #     # ... update profile fields ...
    #     profile.save()
    #     return redirect('view_profile')  # Redirect to view profile after update
    # else:  # GET request
    #     profile = request.user.profile
    #     context = {'profile': profile}
        profile=request.user.profile
        form=ProfileForm(instance=profile)

        if request.method=='POST':
            form=ProfileForm(request.POST, instance=request.user.profile)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Profile Updated Successfully for {}'.format(username))
                return redirect('view_profile')
        context={'form':form}
        return render(request, 'accounts/update_profile.html', context)
