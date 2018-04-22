from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Information
# Create your views here.
def index(request):
    informations=Information.objects.all()
    return render_to_response('cms/menu.html',locals())
    #return HttpResponse("Hello mom I'm Here")