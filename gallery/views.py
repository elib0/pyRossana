from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gallery.models import Album


def home(request):
    if request.is_ajax():
        # Paginador Album
        albums = Album.objects.all()
        p = Paginator(albums, 1, allow_empty_first_page=True)
        album_page = request.GET.get('album')

        # Paginador Fotos
        a = p.object_list[0]
        pictures = a.picture_set.all()
        pp = Paginator(pictures, 6)
        picture_page = request.GET.get('page')

        try:
            album = p.page(album_page)
        except PageNotAnInteger:
            album = p.page(1)
        except EmptyPage:
            album = p.page(p.num_pages)

        try:
            picture = pp.page(picture_page)
        except PageNotAnInteger:
            picture = pp.page(1)
        except EmptyPage:
            picture = pp.page(pp.num_pages)

        return render(request, 'gallery/index.html', {"album": album,
                      'pictures': picture})


def ajax_pictures(request):
    if request.is_ajax():
        pass
