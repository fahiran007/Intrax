from django.shortcuts import render,redirect
import pyttsx3
# Create your views here.
def Home(request):
    try:
        spell = request.GET.get("spelling")
    except:
        pass
    if spell == None:
        spell = ""
    return render(request, 'TTS/index.html',{"spell":spell})
def speech(request):
    spelling = request.GET.get('spelling')
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    engine.say(spelling)
    engine.runAndWait()
    return redirect(f'/TTS/Home?spelling={spelling}')
def speechs(request):
    spelling = request.GET.get('spelling')
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    for i in range(100):
        engine.say(spelling)
        engine.runAndWait()
    return redirect(f'/TTS/Home?spelling={spelling}')