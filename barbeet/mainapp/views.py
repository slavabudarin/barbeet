from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Pixels

def edit(request, id):
    pixels = Pixels.objects.get(id=id)

    if request.method == "POST":
            pixels.id  = request.POST.get("id")
            pixels.color = request.POST.get("color")
            pixels.save()
            return HttpResponseRedirect("/1")
    else:
            dolbaeb = Pixels.objects.all()
            return render(request, "edit.html", {"pixels": pixels,"dolbaeb": dolbaeb})
