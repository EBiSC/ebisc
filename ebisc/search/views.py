from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from ebisc.celllines.models import Cellline


@login_required
def search(request):

    return render(request, 'search/search.html', {
        'celllines': Cellline.objects.filter(celllineaccepted='accepted'),
    })


@login_required
def search_develop(request):

    return render(request, 'search/develop.html', {
        # 'celllines': Cellline.objects.filter(celllineaccepted='accepted'),
    })


@login_required
def cellline(request, biosamples_id):

    return render(request, 'search/cellline.html', {
        'cellline': get_object_or_404(Cellline, biosamplesid=biosamples_id)
    })
