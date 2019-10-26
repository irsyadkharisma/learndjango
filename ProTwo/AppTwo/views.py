from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse('<em>My Second App</em>')

def index(keduwa):
    cobatemplatehelp = {'help' : "INI HELP PAGE"}
    return render(keduwa, 'help.html', context = cobatemplatehelp) 