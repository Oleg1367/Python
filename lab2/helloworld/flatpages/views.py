#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
#    return HttpResponse(u'Привет, мир!', mimetype=u"text/plain; charset=utf-8")
     return render(request, 'static_handler.html', {})

