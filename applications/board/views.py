from django.contrib.auth.models import User
from django.shortcuts import render
from applications.user.views import Users

# Create your views here.
from django.views.generic import TemplateView


class dashBoard(TemplateView):
    def get(self, request, *args, **kwargs):
        contexto={}
        url = ''

        try:
            email = request.session['emailUser']
            user = User.objects.get(username=email)
            users = Users.objects.get(user=user)
            authentication = True
            context = {'authentication': authentication, 'email': email}
            url = 'dashBoard.html'
        except:
            url='login.html'
        return render(request, url,contexto)