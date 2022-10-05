from django.shortcuts import render,redirect
from TimeRules.models import Creates,timestamps
from TimeRules.timerules import Dictionary,times
from django.http import HttpResponse
from datetime import date as dat
from datetime import date as dat2
from TimeRules.settime import serialNum
# Create your views here
def home(request):
    today = dat.today()
    if Creates.objects.filter(ListingDate=today).first():
        pass
    else:
        return redirect('/Routine/Create')
    dates = Creates.objects.get(ListingDate=today)
    data = timestamps.objects.filter(collage=dates.collage,writting=dates.writting)
    time = serialNum(dates.collage, dates.writting)
    return render(request, 'Timerules/index.html',{"data":data,"time":time})
def Create(request):
    if request.method == 'POST':
        timestamps.objects.all().delete()
        collage = "no"
        writting = "yes"
        data = Dictionary(collage, writting)
        s = 1
        for i in range(len(data)):
            l = timestamps(title=data[f"d{i}"]["title"],serialNumber=s,fromTime=data[f"d{i}"]["from"],toTime=data[f"d{i}"]["to"],collage=collage,writting=writting,minutes=data[f"d{i}"]["hour"])
            l.save()
            s = s + 1
        collage = "yes"
        writting = "yes"
        data = Dictionary(collage, writting)
        s = 1
        for i in range(len(data)):
            l = timestamps(title=data[f"d{i}"]["title"],serialNumber=s,fromTime=data[f"d{i}"]["from"],toTime=data[f"d{i}"]["to"],collage=collage,writting=writting,minutes=data[f"d{i}"]["hour"])
            l.save()
            s = s + 1
        collage = "yes"
        writting = "no"
        data = Dictionary(collage, writting)
        s = 1
        for i in range(len(data)):
            l = timestamps(title=data[f"d{i}"]["title"],serialNumber=s,fromTime=data[f"d{i}"]["from"],toTime=data[f"d{i}"]["to"],collage=collage,writting=writting,minutes=data[f"d{i}"]["hour"])
            l.save()
            s = s + 1
        collage = "no"
        writting = "no"
        data = Dictionary(collage, writting)
        s = 1
        for i in range(len(data)):
            l = timestamps(title=data[f"d{i}"]["title"],serialNumber=s,fromTime=data[f"d{i}"]["from"],toTime=data[f"d{i}"]["to"],collage=collage,writting=writting,minutes=data[f"d{i}"]["hour"])
            l.save()
            s = s + 1
        wakeup = request.POST.get('wakeup')
        collage = request.POST.get('collage')
        writting = request.POST.get('writting')
        today = dat2.today()
        l = Creates(ListingDate=today,writting=writting,collage=collage)
        l.save()
        return redirect('/Routine/Home')
    return render(request, 'Timerules/index.html')