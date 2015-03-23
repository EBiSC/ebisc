from django.shortcuts import render, get_object_or_404

from ebisc.celllines.models import Cellline


def search(request):

    return render(request, 'search/search.html', {
        'celllines': Cellline.objects.filter(celllineaccepted='accepted'),
    })


def cellline(request, biosamples_id):

    return render(request, 'search/cellline.html', {
        'cellline': get_object_or_404(Cellline, biosamplesid=biosamples_id)
    })
