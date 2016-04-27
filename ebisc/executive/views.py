import csv
import hashlib

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.html import format_html
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import permission_required
from django.forms import ModelForm

from ebisc.site.views import render
from ebisc.celllines.models import Cellline, CelllineBatch, CelllineInformationPack


@permission_required('auth.can_view_executive_dashboard')
def dashboard(request):

    '''Display a list of all cell lines. Provide paging and sorting.'''

    COLUMNS = [
        ('cellLineName', 'Cell line Name', 'name'),
        # ('cellLineAlternativeNames', 'Alternative Names', 'alternative_names'),
        ('disease', 'Disease', 'primary_disease'),
        ('depositor', 'Depositor', 'generator__name'),
        ('validated', 'Validated', 'validated'),
        ('batches', 'Batches', None),
        ('quantity', 'QTY', None),
        ('sold', 'Sold', None),
        ('availability', 'Availability', 'availability'),
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

    paginator = Paginator(cellline_objects, 50)

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
        'celllines_validated': Cellline.objects.filter(validated__lt=3),
        'celllines_at_ecacc': Cellline.objects.filter(availability='at_ecacc'),
        'celllines_expand_to_order': Cellline.objects.filter(availability='expand_to_order'),
        'celllines_restricted_distribution': Cellline.objects.filter(availability='restricted_distribution'),
    })


class CelllineInformationPackForm(ModelForm):
    class Meta:
        model = CelllineInformationPack
        fields = ['version', 'clip_file']


@permission_required('auth.can_view_executive_dashboard')
def cellline(request, name):

    '''Display complete information for the selected cell line. Allow CLIP uploads for administrators.'''

    cellline = get_object_or_404(Cellline, name=name)

    if not request.user.has_perm('auth.can_manage_executive_dashboard'):
        return render(request, 'executive/cellline.html', {
            'cellline': cellline,
        })

    if request.method == 'POST':
        clip_form = CelllineInformationPackForm(request.POST, request.FILES)
        if clip_form.is_valid():
            clip = clip_form.save(commit=False)
            clip.cell_line = cellline
            clip.md5 = hashlib.md5(clip.clip_file.read()).hexdigest()
            clip.save()
            messages.success(request, format_html(u'A new CLIP <code>{0}</code> has been sucessfully added.', clip.version))
            return redirect('.')
        else:
            messages.error(request, format_html(u'Invalid CLIP data submitted. Please check below.'))
    else:
        clip_form = CelllineInformationPackForm()

    return render(request, 'executive/cellline.html', {
        'cellline': cellline,
        'clip_form': clip_form,
    })


@permission_required('auth.can_view_executive_dashboard')
def batch_data(request, name, batch_biosample_id):

    '''Return batch data as CSV file.'''

    batch = get_object_or_404(CelllineBatch, biosamples_id=batch_biosample_id, cell_line__name=name)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}_{}.csv"'.format(batch.cell_line.name, batch.batch_id)

    writer = csv.writer(response)

    writer.writerow(['Cell line alternative names', 'Cell line name', 'ECACC Cat. no.', 'Batch ID', 'Batch Biosample ID', 'Vial number', 'Vial Biosample ID'])

    for aliquot in batch.aliquots.all():

        if batch.cell_line.alternative_names:
            cell_line_name = batch.cell_line.alternative_names.replace(",", ";")
        else:
            cell_line_name = batch.cell_line.name

        aliquot_number = aliquot.number.zfill(3)

        writer.writerow([cell_line_name, batch.cell_line.name, batch.cell_line.ecacc_id, batch.batch_id, batch.biosamples_id, 'vial %s' % aliquot_number, aliquot.biosamples_id])

    return response


@permission_required('auth.can_manage_executive_dashboard')
@require_POST
def accept(request, name):

    '''
    Perform one of the following transitions:
        Pending -> Pending | Accepted | Rejected
        Rejected -> Accepted
    '''

    cellline = get_object_or_404(Cellline, name=name)

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


@permission_required('auth.can_manage_executive_dashboard')
@require_POST
def availability(request, name):

    '''
    Perform one of the following transitions:
        Not available -> Not available | Stocked at ECACC | Expand to order
        Stocked at ECACC -> Not available | Stocked at ECACC | Expand to order
        Expand to order -> Not available | Stocked at ECACC | Expand to order
    '''

    cellline = get_object_or_404(Cellline, name=name)

    action = request.POST.get('action', None)
    redirect_to = redirect(request.POST.get('next', None) and request.POST.get('next') or 'executive:dashboard')

    if action == 'not_available' and cellline.availability == 'not_available':
        pass
    elif action == 'at_ecacc':
        messages.success(request, format_html(u'Status for cell line <code><strong>{0}</strong></code> changed form <code><strong>{1}</strong></code> to <code><strong>{2}</strong></code>.', cellline.name, cellline.availability, action))
        cellline.availability = 'at_ecacc'
        cellline.available_for_sale = True
    elif action == 'expand_to_order':
        messages.success(request, format_html(u'Status for cell line <code><strong>{0}</strong></code> changed form <code><strong>{1}</strong></code> to <code><strong>{2}</strong></code>.', cellline.name, cellline.availability, action))
        cellline.availability = 'expand_to_order'
        cellline.available_for_sale = True
    elif action == 'restricted_distribution':
        messages.success(request, format_html(u'Status for cell line <code><strong>{0}</strong></code> changed form <code><strong>{1}</strong></code> to <code><strong>{2}</strong></code>.', cellline.name, cellline.availability, action))
        cellline.availability = 'restricted_distribution'
        cellline.available_for_sale = True
    elif action == 'not_available':
        messages.success(request, format_html(u'Status for cell line <code><strong>{0}</strong></code> changed form <code><strong>{1}</strong></code> to <code><strong>{2}</strong></code>.', cellline.name, cellline.availability, action))
        cellline.availability = 'not_available'
        cellline.available_for_sale = False
    else:
        return redirect_to

    cellline.save()

    return redirect_to
