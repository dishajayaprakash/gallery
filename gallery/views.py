from gallery.models import gallery
from django.shortcuts import render


def disp(request):
    results=gallery.objects.all()
    return render(request, 'pictures.html', {'gallery': results})

def home_page(request):
    context = {"title": "Home Page"}
    return render(request, "home.html", context)

