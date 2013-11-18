from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gallery.models import Album


def home(request):
    if request.is_ajax():
        albums = Album.objects.all()
        if albums:
            p = Paginator(albums, 1, allow_empty_first_page=True)
            album_page = request.GET.get('page')

            try:
                albums = p.page(album_page)
            except PageNotAnInteger:
                albums = p.page(1)
            except EmptyPage:
                albums = p.page(p.num_pages)

        return render(request, 'gallery/index.html', {"albums": albums})
    else:
        redirect('/')


def album(request, album_id):
    return render(request, 'gallery/album.html')
    

