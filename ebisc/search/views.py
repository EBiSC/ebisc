from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required

from ebisc.site.views import render
from ebisc.celllines.models import Cellline


# @permission_required('site.can_view_cell_lines', raise_exception=True)
@permission_required('site.can_view_cell_lines')
def search(request):

    return render(request, 'search/search.html', {})


# @permission_required('site.can_view_cell_lines', raise_exception=True)
@permission_required('site.can_view_cell_lines')
def cellline(request, biosamples_id):

    return render(request, 'search/cellline.html', {
        'cellline': get_object_or_404(Cellline, biosamples_id=biosamples_id)
    })
