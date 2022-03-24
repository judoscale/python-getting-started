from django.shortcuts import render
from django.http import HttpResponse
import time

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def sleep(request):
    milliseconds = request.GET.get("ms", "1000")
    time.sleep(int(milliseconds) / 1000)
    return HttpResponse("😴 Slept for {} milliseconds".format(milliseconds))


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
