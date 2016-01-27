from django.shortcuts import get_object_or_404

from ebisc.site.views import render
from ebisc.celllines.models import Cellline


def search(request):
    return render(request, 'search/search.html', {})


def cellline(request, name):
    return render(request, 'search/cellline.html', {
        'cellline': get_object_or_404(Cellline, name=name)
    })
