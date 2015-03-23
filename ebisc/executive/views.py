from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.http import Http404

from ebisc.celllines.models import Cellline


def dashboard(request):

    return render(request, 'executive/dashboard.html', {
        'celllines': Cellline.objects.all()
    })


def cellline(request, biosamples_id):

    return render(request, 'executive/cellline.html', {
        'cellline': get_object_or_404(Cellline, biosamplesid=biosamples_id)
    })


@require_POST
def accept(request, biosamples_id):

    '''
    Perform one of the following transitions:
        Pending -> Pending | Accepted | Rejected
        Rejected -> Accepted
    '''

    cellline = get_object_or_404(Cellline, biosamplesid=biosamples_id)

    action = request.POST.get('action', None)

    print cellline
    print request.POST

    if action == 'pendng' and cellline.celllineaccepted == 'pending':
        pass
    elif action == 'accepted':
        cellline.celllineaccepted = 'accepted'
    elif action == 'rejected' and cellline.celllineaccepted == 'pending':
        cellline.celllineaccepted = 'rejected'
    else:
        raise Http404

    cellline.save()

    return redirect('executive:dashboard')
