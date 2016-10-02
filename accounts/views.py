from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit = False)

            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            messages.success(request,"User Created!")
            new_user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request,new_user)
            return redirect('users:user_new')
    else:
        form = UserRegistrationForm()

    context = {
        "form":form,
        }
    return render(request,"accounts/register.html",context)
