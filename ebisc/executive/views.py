import csv

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.html import format_html
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import permission_required

from ebisc.site.views import render
from ebisc.celllines.models import Cellline, CelllineBatch


@permission_required('auth.can_view_executive_dashboard')
def dashboard(request):

    '''Display a list of all cell lines. Provide paging and sorting.'''

    COLUMNS = [
        # ('biosamplesID', 'Biosamples ID', 'biosamples_id'),
        ('cellLineName', 'Cell line Name', 'name'),
        ('cellLineAlternativeNames', 'Alternative Names', 'alternative_names'),
        ('disease', 'Disease', 'primary_disease'),
        ('depositor', 'Depositor', 'generator__name'),
        ('batches', 'Batches', None),
        ('quantity', 'QTY', None),
        ('sold', 'Sold', None),
        ('status', 'Status', None),
        # ('accepted', 'Accepted', 'accepted'),
    ]

    SORT_COLUMNS = dict([(x[0], x[2]) for x in COLUMNS])

    cellline_objects = Cellline.objects.all()

    # Sorting

    sort_column = request.GET.get('sc', None)
    sort_order = request.GET.get('so', 'asc')

    if sort_column in SORT_COLUMNS.keys() and SORT_COLUMNS[sort_column] is not None:
        if sort_order == 'asc':
            cellline_objects = cellline_objects.order_by(SORT_COLUMNS[sort_column])
        else:
            cellline_objects = cellline_objects.order_by('-' + SORT_COLUMNS[sort_column])
    else:
        sort_column = COLUMNS[0][0]

    # Pagination

    paginator = Paginator(cellline_objects, 20)

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
        'columns': COLUMNS,
        'sort_column': sort_column,
        'sort_order': sort_order,
        'page': int(page),
        'celllines': celllines,
        'celllines_registered': Cellline.objects.all(),
        'celllines_for_sale': Cellline.objects.filter(available_for_sale=True),
    })


@permission_required('auth.can_view_executive_dashboard')
def cellline(request, biosamples_id):

    '''Display complete information for the selected cell line.'''

    return render(request, 'executive/cellline.html', {
        'cellline': get_object_or_404(Cellline, biosamples_id=biosamples_id)
    })


@permission_required('auth.can_view_executive_dashboard')
def batch_data(request, biosamples_id, batch_biosample_id):

    '''Return batch data as CSV file.'''

    batch = get_object_or_404(CelllineBatch, biosamples_id=batch_biosample_id, cell_line__biosamples_id=biosamples_id)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}_{}.csv"'.format(batch.cell_line.name, batch.batch_id)

    writer = csv.writer(response)

    writer.writerow(['Cell line Biosample ID', 'Cell line name', 'Batch Biosample ID', 'Batch ID', 'Vial Biosample ID'])

    for aliquot in batch.aliquots.all():
        writer.writerow([batch.cell_line.biosamples_id, batch.cell_line.name, batch.biosamples_id, batch.batch_id, aliquot.biosamples_id])

    return response


@permission_required('auth.can_manage_executive_dashboard')
@require_POST
def accept(request, biosamples_id):

    '''
    Perform one of the following transitions:
        Pending -> Pending | Accepted | Rejected
        Rejected -> Accepted
    '''

    cellline = get_object_or_404(Cellline, biosamples_id=biosamples_id)

    action = request.POST.get('action', None)
    redirect_to = redirect(request.POST.get('next', None) and request.POST.get('next') or 'executive:dashboard')

    if action == 'pending' and cellline.accepted == 'pending':
        pass
    elif action == 'accepted':
        messages.success(request, format_html(u'Status for cell line <code><strong>{0}</strong></code> changed form <code><strong>{1}</strong></code> to <code><strong>{2}</strong></code>.', cellline.biosamples_id, cellline.accepted, action))
        cellline.accepted = 'accepted'
    elif action == 'rejected' and cellline.accepted == 'pending':
        messages.success(request, format_html(u'Status for cell line <code><strong>{0}</strong></code> changed form <code><strong>{1}</strong></code> to <code><strong>{2}</strong></code>.', cellline.biosamples_id, cellline.accepted, action))
        cellline.accepted = 'rejected'
    else:
        return redirect_to

    cellline.save()

    return redirect_to
