from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.html import format_html
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from ebisc.celllines.models import Cellline


@login_required
def dashboard(request):

    paginator = Paginator(Cellline.objects.all(), 20)

    page = request.GET.get('page')

    try:
        celllines = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        page = 1
        celllines = paginator.page(page)
    except EmptyPage:
        # if page is out of range, deliver first page
        page = 1
        celllines = paginator.page(page)

    return render(request, 'executive/dashboard.html', {
        'page': int(page),
        'celllines': celllines,
    })


def cellline(request, biosamples_id):

    return render(request, 'executive/cellline.html', {
        'cellline': get_object_or_404(Cellline, biosamplesid=biosamples_id)
    })


@login_required
@require_POST
def accept(request, biosamples_id):

    '''
    Perform one of the following transitions:
        Pending -> Pending | Accepted | Rejected
        Rejected -> Accepted
    '''

    cellline = get_object_or_404(Cellline, biosamplesid=biosamples_id)

    action = request.POST.get('action', None)

    if action == 'pendng' and cellline.celllineaccepted == 'pending':
        pass
    elif action == 'accepted':
        messages.success(request, format_html(u'Status for cell line <code>{0}</code> changed form <code>{1}</code> to <code>{2}</code>.', cellline.biosamplesid, cellline.celllineaccepted, action))
        cellline.celllineaccepted = 'accepted'
    elif action == 'rejected' and cellline.celllineaccepted == 'pending':
        messages.success(request, format_html(u'Status for cell line <code>{0}</code> changed form <code>{1}</code> to <code>{2}</code>.', cellline.biosamplesid, cellline.celllineaccepted, action))
        cellline.celllineaccepted = 'rejected'
    else:
        return redirect('executive:dashboard')

    cellline.save()

    return redirect('executive:dashboard')
