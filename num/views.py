from django.shortcuts import render
import pyttsx3
import inflect
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.


def Index(request):
    try:
     
        return render(request, "index.html")
        
    except Exception as e:
        print(e)

def Response(request):
    try:
        if request.method == "POST":
            number=request.POST['number']
            p = inflect.engine()
            num=p.number_to_words(number)
            num=num.capitalize()           
            print(num)
            engine = pyttsx3.init()
            engine.say(num)
            engine.runAndWait()
            engine.stop()
         
        return JsonResponse ({'data':num})
        
    except Exception as e:
        print(e)




