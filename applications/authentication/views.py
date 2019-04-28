from django.views.generic import TemplateView
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .forms import  getRegister
from applications.user.models import Users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
class login(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        print("Dentro del post")
        email = request.POST['email']
        password = request.POST['password']
        context = {}
        user = authenticate(username=email, password=password)
        if user is not None:
            userAuth_p = User.objects.get(email=email)
            authentication = True
            #name = userAuth_p.name
            request.session['emailUser'] = user.email
            #request.session['name'] = name
            context = {'authentication':authentication,'email':email}
            url = 'base.html'
            return render(request,url,context)
        else:
            context = {'messageT':True, 'message':"User or pass invalid."}
            return render(request, 'login.html', context)

class registerPage(TemplateView):
    def get(self, request, *args, **kwargs):
        form = getRegister()
        context = {'form':form}
        return render(request, 'register.html', context)

    def post(self, request, *args, **kwargs):
        print("Dentro del post")
        message = ""
        messageB = True
        form = getRegister(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            if(pass1 == pass2):
                email = request.POST['email']
                try:
                    userAuth_p = User.objects.get(email=email)
                    message = "The email it was used"

                except:
                    name = request.POST['name']
                    last_name = request.POST['last_name']
                    numberID = request.POST['numberID']
                    user = User(password=pass1, first_name=name, email=email,last_name=last_name,username=email)
                    user.set_password(pass1)
                    user.save()
                    users = Users(user=user, id_number=numberID)
                    users.save()
                    message = "Success user create, Login please"
                    context = {'messageB':messageB, 'message':message}
                    return render(request, 'login.html', context)

            else:
                message = "Passwords do not match"

        else:
            message = "Please fill in all information"
        return render(request, 'register.html', {'form':form, 'message':message, 'messageB':messageB})