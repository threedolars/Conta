# flake8: noqa
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from contact.forms import RegisterForm, RegisterUpdateForm
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


@login_required(login_url="contact:login")
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form.save()
    return redirect('contact:login')


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


@login_required(login_url="contact:login")
def logout_view(request):
    auth.logout(request)
    return redirect("contact:index")
