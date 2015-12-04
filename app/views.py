"""
Definition of views.
"""
from login.forms import *
from django.shortcuts import render_to_response 
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.views.decorators.csrf import csrf_project
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    assert isinstance(request, HttpRequest)

    email = ""
    password=""
    errors = []
    user_info = {}
    if request.user.is_authenticated():
        if request.user:
            user_info["name"] = request.user 
        else:
            user_info["name"] = "hao"

        return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'errors': errors,
            "user_info":user_info,
            "flag_login":1
        })
    )
        # return render_to_response('app/index.html',{'errors': errors,"user_info":user_info,"flag_login":1})

    user= None
    flag_login = 0
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                user_info["name"] = email
                login(request, user)
                flag_login = 1
            else:
                errors.append("Not a active user")
        else:
            errors.append("Email or Password wrong")
    
    return render(
    request,
    'app/index.html',
    context_instance = RequestContext(request,
    {
            'title':'Home Page',
            'year':datetime.now().year,
            'errors': errors,
            "user_info":user_info,
            "flag_login":flag_login
    })
    )
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password1'],
            email = form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'registration/register.html',
    variables,
    )

def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
