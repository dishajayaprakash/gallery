from django.shortcuts import render
from gallery.models import gallery

def disp(request):
    results=gallery.objects.all()
    return render(request, 'pictures.html', {'gallery': results})
