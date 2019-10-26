from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

# def index(request):
#     return HttpResponse('<html><h1>It Works!!!!</h1></html>')


def index(request):
    kunam = {'asu' : '<html>werweiurbcsjkhfcb<html>'}
    return render(request, 'first_app/index.html', context=kunam)