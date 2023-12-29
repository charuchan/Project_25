from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def create_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']

        TO=Topics.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        QLTO=Topics.objects.all()
        d={'topic':QLTO}
        return render(request,'display_topic.html',d)
    return render(request,'create_topic.html')    

def create_web(request):
    QLTO=Topics.objects.all()
    d={'topic':QLTO}
    if request.method=='POST':
        n=request.POST['n']
        tn=request.POST['tn']
        u=request.POST['u']
        em=request.POST['em']
        TO=Topics.objects.get(topic_name=tn)
        wo=Webpage.objects.get_or_create(name=n,topic_name=TO,url=u,email=em)[0]
        wo.save()
        QLWO=Webpage.objects.all()
        d1={'QLWO':QLWO}
        return render(request,'display_web.html',d1)
    return render(request,'create_web.html',d)


def select_multiple_web(request):
    QLTO=Topics.objects.all()
    d={'Topics':QLTO}
    if request.method=='POST':

        Topics_list=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for topic_name in Topics_list:
            QLWO=QLWO|Webpage.objects.filter(topic_name=topic_name)
        d1={'QLWO':QLWO}
        return render(request,'display_web.html',d1)
    return render(request,'select_multiple_web.html',d)
        