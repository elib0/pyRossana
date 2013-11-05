from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gallery.models import Album


def home(request):
    if request.is_ajax():
        albums = Album.objects.all()
        p = Paginator(albums, 1, allow_empty_first_page=True)

        page = request.GET.get('page')
        try:
            album = p.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            album = p.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            album = p.page(p.num_pages)

        return render(request, 'gallery/index.html', {"album": album})
