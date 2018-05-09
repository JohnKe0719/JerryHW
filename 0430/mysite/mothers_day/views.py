from django.shortcuts import render
from .models import *
# Create your views here.
def MotherDay(request):
    if request.method=='POST':
        say = request.POST.get('say')
        postIt.objects.create(words=say)
        return render(request,'mothers_day.html',{'say':say})
    return render(request,'mothers_day.html')
