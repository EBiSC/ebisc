import csv
import hashlib
import requests
from sets import Set

from django import forms

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.html import format_html
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import permission_required
from django.forms import ModelForm
from django.core.validators import RegexValidator

from django.conf import settings

from ebisc.site.views import render
from ebisc.celllines.models import Cellline, CelllineBatch, CelllineInformationPack, CelllineAliquot


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


BATCH_TYPE_CHOICES = (
    ('depositor', 'Depositor Expansion'),
    ('central_facility', 'Central Facility Expansion'),
)


class NewBatchForm(forms.Form):
    cellline_name = forms.CharField(label='Cell line name', max_length=15, widget=forms.TextInput(attrs={'readonly': True}))
    cellline_biosample_id = forms.CharField(label='Cell line Biosample ID', max_length=20, widget=forms.TextInput(attrs={'readonly': True}))
    batch_id = forms.CharField(
        label='Batch ID', max_length=5, help_text='ex. P001', widget=forms.TextInput(attrs={'class': 'small'}),
        validators=[RegexValidator('^[a-zA-Z]{1}[0-9]{3}$', message='Batch ID is not in the correct format (letter + 3 digits)')]
    )
    batch_type = forms.CharField(label='Batch Type', max_length=50, widget=forms.Select(choices=BATCH_TYPE_CHOICES))
    number_of_vials = forms.IntegerField(label='Number of vials in batch', min_value=1, widget=forms.TextInput(attrs={'class': 'small'}))
    derived_from = forms.CharField(label='Derived from', max_length=20, help_text='BiosampleID of cellline or vial that the batch was derived from')

    # def clean_cellline_name(self):
    #     return self.initial.cellline_name
    #
    # def clean_cellline_biosample_id(self):
    #     return self.initial.cellline_biosample_id

    def clean(self):
        cleaned_data = super(NewBatchForm, self).clean()
        cellline_biosample_id = cleaned_data.get('cellline_biosample_id')
        batch_id = cleaned_data.get('batch_id')

        cellline = Cellline.objects.get(biosamples_id=cellline_biosample_id)

        if cellline_biosample_id and batch_id:
            existing_batch_ids = Set([b.batch_id for b in CelllineBatch.objects.filter(cell_line__biosamples_id=cellline_biosample_id)])

            if batch_id in existing_batch_ids:
                raise forms.ValidationError(
                    'A batch with this Batch ID for cell line %(cellline_name)s already exists.',
                    params={'cellline_name': cellline.name}
                )


@permission_required('auth.can_manage_executive_dashboard')
def new_batch(request, name):

    cellline = get_object_or_404(Cellline, name=name)

    if request.method == 'POST':
        new_batch_form = NewBatchForm(request.POST)
        if new_batch_form.is_valid():
            data = new_batch_form.cleaned_data

            cellline_name = data['cellline_name']
            cellline_biosample_id = data['cellline_biosample_id']
            batch_type = data['batch_type']
            batch_id = data['batch_id']
            number_of_vials = data['number_of_vials']
            derived_from = data['derived_from']

            biosamples_url = settings.BIOSAMPLES.get('url')
            biosamples_key = settings.BIOSAMPLES.get('key')

            vials = []

            for i in list(range(1, number_of_vials + 1)):
                vial_number = str(i).zfill(4)

                # Request Biosample IDs for vial
                url = '%s/sampletab/api/v2/source/EBiSCIMS/sample?apikey=%s' % (biosamples_url, biosamples_key)
                headers = {'Accept': 'text/plain', 'Content-Type': 'application/xml'}
                xml = """<?xml version="1.0" encoding="UTF-8"?><BioSample xmlns="http://www.ebi.ac.uk/biosamples/SampleGroupExport/1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" submissionReleaseDate="2115/03/04" xsi:schemaLocation="http://wwwdev.ebi.ac.uk/biosamples/assets/xsd/v1.0/BioSDSchema.xsd"><Property class="Sample Name" characteristic="true" comment="false" type="STRING"><QualifiedValue><Value>%s %s vial %s</Value></QualifiedValue></Property><derivedFrom>%s</derivedFrom></BioSample>""" % (cellline_name, batch_id, vial_number, derived_from)

                r = requests.post(url, data=xml, headers=headers)

                print 'Status code: %s' % r.status_code

                # Save vial number, vial BioSample ID
                if r.status_code == 202:
                    vials.append((vial_number, r.text))
                    print 'Vial ID: %s' % r.text
                else:
                    messages.error(request, format_html(u'There was a problem requesting the BioSampleID. Please try again.'))
                    return redirect('.')

            # Request Biosample ID for batch
            vial_list = ''

            for v in vials:
                vial_list += '<Id>%s</Id>' % v[1]

            url = '%s/sampletab/api/v2/source/EBiSCIMS/group?apikey=%s' % (biosamples_url, biosamples_key)
            headers = {'Accept': 'text/plain', 'Content-Type': 'application/xml'}
            xml = """<?xml version="1.0" encoding="UTF-8"?><BioSampleGroup xmlns="http://www.ebi.ac.uk/biosamples/SampleGroupExport/1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.ebi.ac.uk/biosamples/SampleGroupExport/1.0 http://www.ebi.ac.uk/biosamples/assets/xsd/v1.0/BioSDSchema.xsd"><Property class="Group Name" characteristic="true" comment="false" type="STRING"><QualifiedValue><Value>%s batch %s</Value></QualifiedValue></Property><SampleIds>%s</SampleIds></BioSampleGroup>""" % (cellline_name, batch_id, vial_list)

            r = requests.post(url, data=xml, headers=headers)

            if r.status_code == 202:
                batch_biosamples_id = r.text
                print 'Batch ID: %s' % r.text
            else:
                messages.error(request, format_html(u'There was a problem requesting the BioSampleID. Please try again.'))
                return redirect('.')

            # Save batch
            batch = CelllineBatch(
                cell_line=cellline,
                biosamples_id=batch_biosamples_id,
                batch_id=batch_id,
                batch_type=batch_type,
            )
            batch.save()

            # Save vials
            for v in vials:
                vial = CelllineAliquot(
                    batch=batch,
                    biosamples_id=v[1],
                    name='%s %s vial %s' % (cellline_name, batch_id, v[0]),
                    number=v[0],
                    # derived_from_aliqot=derived_from,
                )
                vial.save()

            return redirect('.')
        else:
            messages.error(request, format_html(u'Invalid batch data submitted. Please check below.'))
    else:
        new_batch_form = NewBatchForm(initial={'cellline_name': cellline.name, 'cellline_biosample_id': cellline.biosamples_id})

    return render(request, 'executive/create-batch/new-batch.html', {
        'cellline': cellline,
        'new_batch_form': new_batch_form,
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
