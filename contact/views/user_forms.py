
from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    form = RegisterForm()

    if request.method == "GET":
        messages.info(request, "Create your User")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User registred')
            return redirect('contact:login')

    return render(request=request,
                  template_name="contact/register.html",
                  context={
                      "form": form
                  })


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, "Login sucess")
            return redirect('contact:index')
        else:
            messages.error(request, 'Login Error')

    return render(request, 'contact/login.html',
                  {
                      "form": form
                  }
                  )


def logout_view(request):
    auth.logout(request)
    return redirect("contact:index")
