from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.

class Users(TemplateView):
    def get(self,request,*args, **kwargs):
        context ={}
        return render(request, 'log.html', context)

