from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.shortcuts import render, redirect
from django.utils.timezone import datetime
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Replace the existing home function with the one below
def home(request):
    return render(request, 'hello/home.html')

def account(request):
    return render(request, 'hello/account.html')

def subjects(request):
    return render(request, 'hello/subjects.html')

def hello_there(request, name):
    return render(
        request,
        'hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "log_message.html", {"form": form})

def account(request):
    return render(request, 'account.html')

def subjects(request):
    return render(request, 'subjects.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'home-user.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('profile')
        else:
            messages.info(request, 'Password Not Matched')
            return redirect('register')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect(request, '/')