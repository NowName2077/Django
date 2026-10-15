from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .SignUpForm import SignUpForm

def home(request):
    context = {}
    return render(request, 'myapp/home.html', context)
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "myapp/signup.html", {"form": form})
