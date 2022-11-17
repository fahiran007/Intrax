from django.shortcuts import render,redirect
from IPassApp.models import Item
from IPassApp import idx_gen
# Create your views here.
def addingItem(request):
    try:
        token = request.GET.get('token')
    except:
        pass
    if request.method == "POST":
        platform = request.POST.get('platform')
        username = request.POST.get('username')
        password = request.POST.get('password')
        idx = idx_gen.token_gen()
        l = Item(platform=platform,username=username,password=password,idx=idx)
        l.save()
        return redirect('/IPassApp')
    data = Item.objects.all()
    context = {
        'data':data
    }
    return render(request, 'IdandPassword/index.html',context)
def editItem(request):
    idx = request.GET.get('token')
    data = Item.objects.get(idx=idx)   
    if request.method == "POST":
        platform = request.POST.get('platform')
        username = request.POST.get('username')
        password = request.POST.get('password')
        data.platform = platform
        data.username = username
        data.password = password
        data.save()
        return redirect('/IPassApp')
    context = {
        'data':data
    }
    return render(request, 'IdandPassword/editinfo.html',context)