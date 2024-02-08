from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def login_view(request):
    set_cookies = {}
    response = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.POST.get('next')
        remember_me = request.POST.get('remember_me') == "1"
        if remember_me:
            set_cookies['xsp_username'] = username
            set_cookies['remember_me'] = "1"
        else:
            set_cookies['xsp_username'] = None
            set_cookies['remember_me'] = None
        user = authenticate(request, username=username, password=password)
        if user is None:
            response = redirect(f"{reverse('login')}?err=login_failed")
        else:
            login(request, user)
            if next_url:
                response = redirect(next_url)
            else:
                response = redirect('/documentation/versions')
    else:
        ctx = {
            "err": request.GET.get('err'),
            "username": request.COOKIES.get("xsp_username"),
            "remember_me": request.COOKIES.get("remember_me")
        }
        response = render(request, 'auth/login.html', ctx)

    for k, v in set_cookies.items():
        if v is not None:
            response.set_cookie(k, v)
        else:
            response.delete_cookie(k)

    return response


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/auth/login')