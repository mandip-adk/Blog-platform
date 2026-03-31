from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("login")
        else:
            messages.error(request, "Please enter the correct information as asked.")
    else:

        form = UserCreationForm()

    return render(request, "accounts/registration.html", {'form':form})
