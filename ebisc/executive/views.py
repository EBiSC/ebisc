import csv
import hashlib
import requests
from datetime import datetime

from django import forms

from django.db import IntegrityError
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.html import format_html
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import permission_required
from django.forms import ModelForm, inlineformset_factory
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.db.models import Q
from django.db.models.functions import Lower

from ebisc.site.views import render
from ebisc.celllines.models import Cellline, CelllineStatus, CelllineBatch, CelllineInformationPack, CelllineAliquot, Disease, Organization, BatchCultureConditions, CelllineBatchImages


class BiosamplesError(Exception):
    pass


@permission_required('auth.can_view_executive_dashboard')
def dashboard(request):

    '''Display a list of all cell lines. Provide paging and sorting.'''

    COLUMNS = [
        ('cellLineName', 'Cell line Name', 'name'),
        ('disease', 'Disease', 'diseases'),
        ('depositor', 'Depositor', 'generator__name'),
        ('validated', 'Validated', 'validated'),
        ('batches', 'Batches', None),
        ('quantity', 'QTY', None),
        ('status', 'Status', 'current_status__status'),
        ('forSale', 'For Sale', 'available_for_sale_at_ecacc'),
    ]

    SORT_COLUMNS = dict([(x[0], x[2]) for x in COLUMNS])

    cellline_objects = Cellline.objects.all()

    # Search
    search_query = request.GET.get('q', None)

    if search_query:
        cellline_objects = cellline_objects.filter(Q(name__icontains=request.GET.get('q')) | Q(ecacc_id__icontains=request.GET.get('q')) | Q(biosamples_id__icontains=request.GET.get('q')) | Q(alternative_names__icontains=request.GET.get('q')) | Q(batches__biosamples_id__icontains=request.GET.get('q')) | Q(batches__aliquots__biosamples_id__icontains=request.GET.get('q')) | Q(donor__biosamples_id__icontains=request.GET.get('q')) | Q(donor__provider_donor_ids__icontains=request.GET.get('q'))).distinct()

    # Filters
    filters = {
        'status': request.GET.get('status', None),
        'depositor': request.GET.get('depositor', None),
        'disease': request.GET.get('disease', None),
    }

    status = CelllineStatus.STATUS_CHOICES
    depositors = Organization.objects.filter(generator_of_cell_lines__isnull=False).distinct()
    diseases = Disease.objects.filter(name__isnull=False).order_by(Lower('name'))

    if filters['status']:
        cellline_objects = cellline_objects.filter(current_status__status=request.GET.get('status', None))

    if filters['depositor']:
        cellline_objects = cellline_objects.filter(generator__name=request.GET.get('depositor', None))

    if filters['disease']:
        cellline_objects = cellline_objects.filter(Q(diseases__disease__name=request.GET.get('disease', None)) | Q(donor__diseases__disease__name=request.GET.get('disease', None)))

    # Select related
    cellline_objects = cellline_objects.select_related('generator', 'donor')
    cellline_objects = cellline_objects.prefetch_related('batches', 'diseases', 'diseases__disease', 'donor__diseases', 'donor__diseases__disease')

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
        'status': status,
        'depositors': depositors,
        'diseases': diseases,
        'filters': filters,
        'search_query': search_query,
        'celllines': celllines,
        'celllines_registered': Cellline.objects.count(),
        'celllines_validated': Cellline.objects.filter(validated__lt=3).count(),
        'celllines_at_ecacc': Cellline.objects.filter(current_status__status='at_ecacc').count(),
        'celllines_expand_to_order': Cellline.objects.filter(current_status__status='expand_to_order').count(),
        'celllines_restricted_distribution': Cellline.objects.filter(current_status__status='restricted_distribution').count(),
        'celllines_recalled': Cellline.objects.filter(current_status__status='recalled').count(),
        'celllines_withdrawn': Cellline.objects.filter(current_status__status='withdrawn').count(),
    })


class CelllineInformationPackForm(ModelForm):
    class Meta:
        model = CelllineInformationPack
        fields = ['version', 'clip_file']


class CelllineStatusForm(ModelForm):
    class Meta:
        model = CelllineStatus
        fields = ['status', 'comment']

    def clean(self):
        cleaned_data = super(CelllineStatusForm, self).clean()
        new_status = cleaned_data.get('status')

        if new_status == 'recalled' or new_status == 'withdrawn':
            if not cleaned_data.get('comment'):
                raise forms.ValidationError(
                    'You must provide a reason for withdrawing/recalling a line in the Comment field.'
                )


@permission_required('auth.can_view_executive_dashboard')
def cellline(request, name):

    '''Display complete information for the selected cell line. Allow CLIP uploads for administrators.'''

    cellline = get_object_or_404(Cellline, name=name)

    same_donor_lines = Cellline.objects.filter(donor=cellline.donor).exclude(name=cellline.name).exclude(name__regex='(-\d+)$').order_by('name')

    if cellline.derived_from:
        same_donor_lines = same_donor_lines.exclude(name=cellline.derived_from.name)

    # Relatives
    relatives = [related_donor for related_donor in cellline.donor.relatives.all()]

    if not request.user.has_perm('auth.can_manage_executive_dashboard'):
        return render(request, 'executive/cellline.html', {
            'cellline': cellline,
        })

    if request.method == 'POST':

        if 'clip' in request.POST:
            clip_form = CelllineInformationPackForm(request.POST, request.FILES, prefix='clip')
            if clip_form.is_valid():
                clip = clip_form.save(commit=False)
                clip.cell_line = cellline
                clip.md5 = hashlib.md5(clip.clip_file.read()).hexdigest()
                try:
                    clip.save()
                    messages.success(request, format_html(u'A new CLIP <code>{0}</code> has been sucessfully added.', clip.version))
                except IntegrityError:
                    messages.error(request, format_html(u'CLIP version {0} for cell line {1} already exists.', clip.version, cellline.name))

                return redirect('.')
            else:
                messages.error(request, format_html(u'Invalid CLIP data submitted. Please check below.'))
            status_form = CelllineStatusForm(prefix='status')

        elif 'status' in request.POST:
            status_form = CelllineStatusForm(request.POST, prefix='status')
            if status_form.is_valid():
                new_status = status_form.cleaned_data['status']
                if new_status == 'withdrawn' or new_status == 'not_available':
                    cellline.available_for_sale = False
                else:
                    cellline.available_for_sale = True
                cellline.save()

                status = status_form.save(commit=False)
                status.cell_line = cellline
                status.user = request.user
                status.save()

                messages.success(request, format_html(u'Status for cell line <code>{0}</code> has been sucessfully changed to <code>{1}</code>.', cellline.name, cellline.current_status.status))
                return redirect('.')
            else:
                messages.error(request, format_html(u'Invalid status data submitted. Please check below.'))
            clip_form = CelllineInformationPackForm(prefix='clip')

        elif 'delete_clip' in request.POST:
            delete_clip_ids = request.POST.getlist('delete-clip')

            for clip_id in delete_clip_ids:
                try:
                    clip = CelllineInformationPack.objects.get(cell_line=cellline, id=clip_id)
                    clip.delete()
                    messages.success(request, format_html(u'CLIP version <code><strong>{0}</strong></code> for cell line <code><strong>{1}</strong></code> has been sucessfully deleted.', clip.version, cellline.name))

                except CelllineInformationPack.DoesNotExist:
                    messages.error(request, format_html(u'The CLIP you are trying to delete does not exist.'))

            return redirect('.')
            clip_form = CelllineInformationPackForm(prefix='clip')
            status_form = CelllineStatusForm(prefix='status')

    else:
        clip_form = CelllineInformationPackForm(prefix='clip')
        status_form = CelllineStatusForm(prefix='status', initial={'status': cellline.current_status})

    return render(request, 'executive/cellline.html', {
        'cellline': cellline,
        'clip_form': clip_form,
        'status_form': status_form,
        'same_donor_lines': same_donor_lines,
        'relatives': relatives,
    })


BATCH_TYPE_CHOICES = (
    ('central_facility', 'Central Facility Expansion'),
    ('depositor', 'Depositor Expansion'),
)


class NewBatchForm(forms.Form):
    cellline_name = forms.CharField(label='Cell line name', max_length=15, widget=forms.TextInput(attrs={'readonly': True}))
    cellline_biosample_id = forms.CharField(label='Cell line Biosample ID', max_length=100, widget=forms.TextInput(attrs={'readonly': True}))
    batch_id = forms.CharField(
        label='Batch ID', max_length=5, help_text='ex. P001', widget=forms.TextInput(attrs={'class': 'small'}),
        validators=[RegexValidator('^[a-zA-Z]{1}[0-9]{3}$', message='Batch ID is not in the correct format (letter + 3 digits)')]
    )
    batch_type = forms.CharField(label='Batch Type', max_length=50, widget=forms.Select(choices=BATCH_TYPE_CHOICES), help_text=format_html(u'<div class="tooltip-item"><span class="glyphicon glyphicon-question-sign"></span><div class="tooltip"><p><b>Depositor expansion batch:</b> A batch-worth of empty vials are sent to the depositor, with EBiSC labels and EBiSC vial IDs. The depositor fills the vials and ships them back to central facility.</p><p><b>Central facility expansion batch:</b> Central facility expand the batch and then fill EBiSC vials with EBiSC vial labels. The batch is expanded from a small number of unlabeled vials sent by depositor or from vials already banked at CF.</p></div></div>'))
    number_of_vials = forms.IntegerField(label='Number of vials in batch', min_value=1, widget=forms.TextInput(attrs={'class': 'small'}))
    derived_from = forms.CharField(label='Derived from', max_length=100, help_text='BiosampleID of cell line or vial ID that the batch was derived from')

    def clean(self):
        cleaned_data = super(NewBatchForm, self).clean()
        cellline_biosample_id = cleaned_data.get('cellline_biosample_id')
        batch_id = cleaned_data.get('batch_id')
        derived_from = cleaned_data.get('derived_from')

        cellline = Cellline.objects.get(biosamples_id=cellline_biosample_id)

        if cellline_biosample_id and batch_id:
            existing_batch_ids = set([b.batch_id for b in CelllineBatch.objects.filter(cell_line__biosamples_id=cellline_biosample_id)])

            if batch_id in existing_batch_ids:
                raise forms.ValidationError(
                    'A batch with this Batch ID for cell line %(cellline_name)s already exists.',
                    params={'cellline_name': cellline.name}
                )

        if cellline_biosample_id and derived_from:
            existing_vial_ids = set([v.biosamples_id for v in CelllineAliquot.objects.filter(batch__cell_line__biosamples_id=cellline_biosample_id)])

            if derived_from != cellline.biosamples_id and derived_from not in existing_vial_ids:
                raise forms.ValidationError(
                    'Derived from Biosamples ID: %(derived_from)s does not match the cell line ID or any vial IDs from this cell line.',
                    params={'derived_from': derived_from}
                )


@permission_required('auth.can_view_executive_dashboard')
def new_batch(request, name):

    cellline = get_object_or_404(Cellline, name=name)

    if cellline.donor:
        donor_biosamples_id = cellline.donor.biosamples_id
    else:
        donor_biosamples_id = ''

    if request.method != 'POST':
        new_batch_form = NewBatchForm(initial={'cellline_name': cellline.name, 'cellline_biosample_id': cellline.biosamples_id})
    else:
        new_batch_form = NewBatchForm(request.POST)
        if not new_batch_form.is_valid():
            messages.error(request, format_html(u'Invalid batch data submitted. Please check below.'))
        else:
            data = new_batch_form.cleaned_data

            cellline_name = data['cellline_name']
            cellline_biosample_id = data['cellline_biosample_id']
            batch_type = data['batch_type']
            batch_id = data['batch_id']
            number_of_vials = data['number_of_vials']
            derived_from = data['derived_from']

            full_batch_id = cellline_name + "_" + batch_id

            # Store vial numbers, and full vial IDs
            vials = []
            for i in list(range(1, number_of_vials + 1)):
                vial_number = str(i).zfill(4)
                vials.append((vial_number, full_batch_id + "_" + vial_number))

            # Save batch
            batch = CelllineBatch(
                cell_line=cellline,
                biosamples_id=full_batch_id,    # not an actual biosamples ID anymore
                batch_id=batch_id,
                batch_type=batch_type,
            )
            batch.save()

            # Save vials
            for v in vials:
                CelllineAliquot(
                    batch=batch,
                    biosamples_id=v[1], # not an actual biosamples ID anymore
                    name='%s %s vial %s' % (cellline_name, batch_id, v[0]),
                    number=v[0],
                    derived_from=derived_from,
                ).save()

            messages.success(request, format_html(u'A new batch <code><strong>{0}</strong></code> for cell line <code><strong>{1}</strong></code> has been sucessfully created.', batch_id, cellline_name))
            return redirect('executive:cellline', cellline_name)

    return render(request, 'executive/batches/new-batch.html', {
        'cellline': cellline,
        'new_batch_form': new_batch_form,
    })


class UpdateBatchDataForm(forms.ModelForm):

    class Meta:
        model = CelllineBatch
        fields = ['certificate_of_analysis', 'vials_at_roslin', 'vials_shipped_to_ecacc', 'vials_shipped_to_fraunhoffer']


class UpdateBatchCultureConditionsForm(forms.ModelForm):

    class Meta:
        model = BatchCultureConditions
        exclude = ['batch']


@permission_required('auth.can_view_executive_dashboard')
def update_batch(request, name, batch_biosample_id):

    cellline = get_object_or_404(Cellline, name=name)
    batch = get_object_or_404(CelllineBatch, biosamples_id=batch_biosample_id)

    try:
        batch_culture_conditions = BatchCultureConditions.objects.get(batch=batch)
    except BatchCultureConditions.DoesNotExist:
        batch_culture_conditions = None

    ImageFormSet = inlineformset_factory(CelllineBatch, CelllineBatchImages, fields=('image', 'magnification', 'time_point'), max_num=4, extra=4)

    if request.method != 'POST':
        update_batch_form = UpdateBatchDataForm(instance=batch)
        update_batch_culture_conditions_form = UpdateBatchCultureConditionsForm(instance=batch_culture_conditions)
        image_formset = ImageFormSet(instance=batch)
    else:
        update_batch_form = UpdateBatchDataForm(request.POST, request.FILES, instance=batch)
        update_batch_culture_conditions_form = UpdateBatchCultureConditionsForm(request.POST, instance=batch_culture_conditions)
        image_formset = ImageFormSet(request.POST, request.FILES, instance=batch)

        if not update_batch_form.is_valid() or not update_batch_culture_conditions_form.is_valid() or not image_formset.is_valid():
            messages.error(request, format_html(u'Invalid batch data submitted. Please check below.'))
        else:
            # Save batch culture conditions
            batch_culture_conditions = update_batch_culture_conditions_form.save(commit=False)
            batch_culture_conditions.batch = batch
            batch_culture_conditions.save()

            # Save inventory and CoA
            batch = update_batch_form.save(commit=False)
            batch.cell_line = cellline
            batch.biosamples_id = batch.biosamples_id
            batch.batch_id = batch.batch_id
            batch.batch_type = batch.batch_type
            if batch.certificate_of_analysis:
                batch.certificate_of_analysis_md5 = hashlib.md5(batch.certificate_of_analysis.read()).hexdigest()
            else:
                batch.certificate_of_analysis_md5 = None
            batch.save()

            # Save images
            instances = image_formset.save()
            for instance in instances:
                if instance.image:
                    instance.md5 = hashlib.md5(instance.image.read()).hexdigest()
                else:
                    instance.md5 = None
                instance.save()

            messages.success(request, format_html(u'Batch data for batch <code><strong>{0}</strong></code> / <code><strong>{1}</strong></code> has been successfuly updated.', cellline.name, batch.batch_id))
            return redirect('executive:cellline', name)

    return render(request, 'executive/batches/update-batch.html', {
        'cellline': cellline,
        'batch': batch,
        'update_batch_form': update_batch_form,
        'update_batch_culture_conditions_form': update_batch_culture_conditions_form,
        'image_formset': image_formset,
    })


@permission_required('auth.can_view_executive_dashboard')
def batch_data(request, name, batch_biosample_id):

    '''Return batch data as CSV file.'''

    batch = get_object_or_404(CelllineBatch, biosamples_id=batch_biosample_id, cell_line__name=name)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}_{}.csv"'.format(batch.cell_line.name, batch.batch_id)

    writer = csv.writer(response)

    writer.writerow(['Cell line alternative names', 'Cell line name', 'ECACC Cat. no.', 'Batch ID', 'Full Batch ID', 'Vial number', 'Vial ID'])

    for aliquot in batch.aliquots.all():

        if batch.cell_line.alternative_names:
            cell_line_name = batch.cell_line.alternative_names.replace(",", ";").encode('utf-8')
        else:
            cell_line_name = batch.cell_line.name

        writer.writerow([cell_line_name, batch.cell_line.name, batch.cell_line.ecacc_id, batch.batch_id, batch.biosamples_id, 'Vial %s' % aliquot.number, aliquot.biosamples_id])

    return response


@permission_required('auth.can_view_executive_dashboard')
def cell_line_ids(request):

    '''Return cell line IDs as CSV file.'''

    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="ebisc_cell_line_ids-{}.csv"'.format(datetime.date(datetime.now()))

    writer = csv.writer(response)

    writer.writerow(['hPSCreg name', 'Depositor', 'Owner',
                     'Alternative names',
                     'EBiSC status',
                     'BioSamples Cell line ID', 'ECACC Cat. No',
                     'Depositor Donor ID', 'BioSamples Donor ID',
                     'Sex', 'Age', 'Donor Diseases',
                     'Batches', 'Line Diseases', 'Genetics',
                     'Primary Cell Type', 'Derivation', 'Passage', 'Culture Conditions', 'notes'])

    for cell_line in Cellline.objects.all():

        if cell_line.alternative_names:
            cell_line_alternative_names = cell_line.alternative_names.replace(",", ";").encode('utf-8')
        else:
            cell_line_alternative_names = ''

        if cell_line.donor:
            donor_biosamples_id = cell_line.donor.biosamples_id
            donor_sex = cell_line.donor.gender

            if cell_line.donor.provider_donor_ids:
                donor_depositor_names = '; '.join([str(n) for n in cell_line.donor.provider_donor_ids])
            else:
                donor_depositor_names = ''
        else:
            donor_biosamples_id = ''
            donor_depositor_names = ''
            donor_sex = ''

        if cell_line.donor_diseases:
            donor_disease_list = "; ".join(cell_line.donor_diseases).encode('utf-8')
        else:
            donor_disease_list = ''

        if cell_line.cellline_diseases:
            line_disease_list = "; ".join(cell_line.cellline_diseases).encode('utf-8')
        else:
            line_disease_list = ''

        if cell_line.search_terms_genetics:
            genetics = "; ".join(cell_line.search_terms_genetics).encode('utf-8')
        else:
            genetics = ''

        if hasattr(cell_line, "derivation") and cell_line.derivation.primary_cell_type:
            primary_cell_type = cell_line.derivation.primary_cell_type.name
        else:
            primary_cell_type = ''

        if cell_line.search_terms_derivation:
            derivation = "; ".join(cell_line.search_terms_derivation).encode('utf-8')
        else:
            derivation = ''

        if cell_line.public_notes:
            notes = cell_line.public_notes.replace(",", ";").encode('utf-8')
        else:
            notes = ''

        culture_conditions = ''
        if hasattr(cell_line, "celllinecultureconditions"):
            cc = cell_line.celllinecultureconditions
            passage = cc.passage_number_banked
            if cc.surface_coating:
                culture_conditions = cc.surface_coating
            if cc.culture_medium:
                if cc.culture_medium == "other" and hasattr(cc, 'culture_medium_other'):
                    if cc.culture_medium_other.base:
                        culture_conditions += "; " + cc.culture_medium_other.base
                        if cc.culture_medium_other.protein_source:
                            culture_conditions += " + " + cc.culture_medium_other.protein_source
                else:
                    culture_conditions += "; " + cc.culture_medium
            culture_conditions = culture_conditions.replace("&trade;", u"\u2122")
            culture_conditions = culture_conditions.replace("&#8482;", u"\u2122")
            culture_conditions = culture_conditions.replace("&reg;", u"\u00ae")
            culture_conditions = culture_conditions.encode('utf-8')
        else:
            passage = ''

        batches = cell_line.batches.all();
        batch_ids = []
        if batches:
            for batch in batches:
                if batch.batch_id:
                    batch_ids.append(batch.batch_id)
        batches_list = "; ".join(batch_ids)

        writer.writerow([cell_line.name, cell_line.generator, cell_line.owner,
                         cell_line_alternative_names,
                         cell_line.current_status.status,
                         cell_line.biosamples_id, cell_line.ecacc_id,
                         donor_depositor_names, donor_biosamples_id,
                         donor_sex, cell_line.donor_age, donor_disease_list,
                         batches_list, line_disease_list, genetics,
                         primary_cell_type, derivation, passage, culture_conditions, notes])

    return response


@permission_required('auth.can_view_executive_dashboard')
def batch_ids(request):

    '''Return batch IDs as CSV file.'''

    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="ebisc_batch_ids-{}.csv"'.format(datetime.date(datetime.now()))

    writer = csv.writer(response)

    writer.writerow(['Cell line name', 'Cell line BioSamples ID', 'Batch No', 'Full Batch ID', 'Batch type', 'Medium', "Vials Central", "Vials to ECACC", "Vials to FH"])

    for batch in CelllineBatch.objects.all().order_by('cell_line__name'):

        medium = ''
        if hasattr(batch, 'batchcultureconditions') and batch.batchcultureconditions.culture_medium:
            medium = batch.batchcultureconditions.culture_medium.encode('utf-8')

        writer.writerow((
            batch.cell_line.name,
            batch.cell_line.biosamples_id,
            batch.batch_id,
            batch.biosamples_id,
            batch.batch_type,
            medium,
            batch.vials_at_roslin,
            batch.vials_shipped_to_ecacc,
            batch.vials_shipped_to_fraunhoffer
        ))

    return response
