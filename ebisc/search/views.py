from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required

from ebisc.site.views import render
from ebisc.celllines.models import Cellline


@permission_required('auth.can_view_cell_lines')
def search(request):

    return render(request, 'search/search.html', {})


@permission_required('auth.can_view_cell_lines')
def cellline(request, name):

    return render(request, 'search/cellline.html', {
        'cellline': get_object_or_404(Cellline, name=name)
    })
