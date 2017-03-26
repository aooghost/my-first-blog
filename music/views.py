from django.http import Http404
from django.shortcuts import render
#from django.http import HttpResponse
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums' : all_albums,}
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("This album does not exists")
    return render(request, 'music/detail.html', {'album' : album})

def contact(request):
    return render(request, 'music/contact.html')

def cover(request):
    return render(request, 'music/cover.html')
