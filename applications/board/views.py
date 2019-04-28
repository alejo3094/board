from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class dashBoard(TemplateView):
    def get(self, request, *args, **kwargs):
        contexto={}
        url = ''

        try:
            email = request.session['emailUser']
            user = User.objects.get(email=email)
            authentication = True
            context = {'authentication': authentication, 'email': email}
            url = 'login.html'
        except:
            url='login.html'
        return render(request, url,contexto)