import os
import uuid
import datetime
from dirtyfields import DirtyFieldsMixin

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.postgres.fields import ArrayField


# -----------------------------------------------------------------------------
# Utilities

EXTENDED_BOOL_CHOICES = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('unknown', 'Unknown'),
)


def upload_to(instance, filename):
    date = datetime.date.today()
    return os.path.join('celllines', '%d/%02d/%02d' % (date.year, date.month, date.day), str(uuid.uuid4()), filename)


# -----------------------------------------------------------------------------
# Indexes

class AgeRange(models.Model):

    name = models.CharField(_(u'Age range'), max_length=10, unique=True)

    class Meta:
        verbose_name = _(u'Age range')
        verbose_name_plural = _(u'Age ranges')
        ordering = ['name']

    def __unicode__(self):
        return self.name


class CellType(models.Model):

    name = models.CharField(_(u'Cell type'), max_length=100, unique=True)

    class Meta:
        verbose_name = _(u'Cell type')
        verbose_name_plural = _(u'Cell types')
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Country(models.Model):

    name = models.CharField(_(u'Country'), max_length=45, unique=True)
    code = models.CharField(_(u'Country code'), max_length=3, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Country')
        verbose_name_plural = _(u'Countries')
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Gender(models.Model):

    name = models.CharField(_(u'Gender'), max_length=10, unique=True)

    class Meta:
        verbose_name = _(u'Gender')
        verbose_name_plural = _(u'Genders')
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Molecule(models.Model):

    KIND_CHOICES = (
        ('gene', u'Gene'),
        ('protein', u'Protein'),
    )

    name = models.CharField(u'name', max_length=20)
    kind = models.CharField(u'Kind', max_length=20, choices=KIND_CHOICES)

    class Meta:
        verbose_name = _(u'Molecule')
        verbose_name_plural = _(u'Molecules')
        unique_together = [('name', 'kind')]
        ordering = ['name', 'kind']

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.kind)


class MoleculeReference(models.Model):

    CATALOG_CHOICES = (
        ('entrez', u'Entrez'),
        ('ensembl', u'Ensembl'),
    )

    molecule = models.ForeignKey(Molecule, verbose_name='Molecule')
    catalog = models.CharField(u'Molecule ID source', max_length=20, choices=CATALOG_CHOICES)
    catalog_id = models.CharField(u'ID', max_length=20)

    class Meta:
        verbose_name = _(u'Molecule reference')
        verbose_name_plural = _(u'Molecule references')
        ordering = ['molecule', 'catalog']
        unique_together = [('molecule', 'catalog')]

    def __unicode__(self):
        return '%s %s in %s' % (self.molecule, self.catalog_id, self.catalog)


class Virus(models.Model):

    name = models.CharField(_(u'Virus'), max_length=100, unique=True)

    class Meta:
        verbose_name = _(u'Virus')
        verbose_name_plural = _(u'Viruses')
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Transposon(models.Model):

    name = models.CharField(_(u'Transposon'), max_length=100, unique=True)

    class Meta:
        verbose_name = _(u'Transposon')
        verbose_name_plural = _(u'Transposons')
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Unit(models.Model):

    name = models.CharField(_(u'Units'), max_length=20, unique=True)

    class Meta:
        verbose_name = _(u'Units')
        verbose_name_plural = _(u'Units')
        ordering = ['name']

    def __unicode__(self):
        return self.name


# -----------------------------------------------------------------------------
# Cell line

class Cellline(DirtyFieldsMixin, models.Model):

    ACCEPTED_CHOICES = (
        ('pending', _(u'Pending')),
        ('accepted', _(u'Accepted')),
        ('rejected', _(u'Rejected')),
    )

    accepted = models.CharField(_(u'Cell line accepted'), max_length=10, choices=ACCEPTED_CHOICES, default='pending')
    status = models.ForeignKey('CelllineStatus', verbose_name=_(u'Cell line status'), null=True, blank=True)

    name = models.CharField(_(u'Cell line name'), unique=True, max_length=15)
    alternative_names = models.CharField(_(u'Cell line alternative names'), max_length=500, null=True, blank=True)

    biosamples_id = models.CharField(_(u'Biosamples ID'), unique=True, max_length=12)
    hescreg_id = models.CharField(_(u'hESCreg ID'), unique=True, max_length=10, null=True, blank=True)
    ecacc_id = models.CharField(_(u'ECACC ID'), unique=True, max_length=10, null=True, blank=True)

    donor = models.ForeignKey('Donor', verbose_name=_(u'Donor'), null=True, blank=True)
    donor_age = models.ForeignKey(AgeRange, verbose_name=_(u'Age'), null=True, blank=True)

    generator = models.ForeignKey('Organization', verbose_name=_(u'Generator'), related_name='generator_of_cell_lines')
    owner = models.ForeignKey('Organization', verbose_name=_(u'Owner'), null=True, blank=True, related_name='owner_of_cell_lines')
    derivation_country = models.ForeignKey('Country', verbose_name=_(u'Derivation country'), null=True, blank=True)

    primary_disease = models.ForeignKey('Disease', verbose_name=_(u'Diagnosed disease'), null=True, blank=True)
    primary_disease_diagnosis = models.CharField(_(u'Disease diagnosis'), max_length=12, null=True, blank=True)
    primary_disease_stage = models.CharField(_(u'Disease stage'), max_length=100, null=True, blank=True)
    disease_associated_phenotypes = ArrayField(models.CharField(max_length=500), verbose_name=_(u'Disease associated phenotypes'), null=True)
    affected_status = models.CharField(_(u'Affected status'), max_length=12, null=True, blank=True)
    family_history = models.CharField(_(u'Family history'), max_length=500, null=True, blank=True)
    medical_history = models.CharField(_(u'Medical history'), max_length=500, null=True, blank=True)
    clinical_information = models.CharField(_(u'Clinical information'), max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line')
        verbose_name_plural = _(u'Cell lines')
        ordering = ['biosamples_id']

    def __unicode__(self):
        return u'%s' % (self.biosamples_id,)

    @property
    def ecacc_url(self):
        return 'https://www.phe-culturecollections.org.uk/products/celllines/generalcell/detail.jsp?refId=%s&collection=ecacc_gc' % self.ecacc_id

    def to_elastic(self):

        if self.primary_disease and self.primary_disease_diagnosis != '0':
            disease = self.primary_disease.disease
        elif self.primary_disease_diagnosis == '0':
            disease = 'normal'
        else:
            disease = None

        return {
            'biosamples_id': self.biosamples_id,
            'name': self.name,
            'primary_disease': disease,
            'primary_disease_synonyms': [s.strip() for s in self.primary_disease.synonyms.split(',')] if self.primary_disease and self.primary_disease.synonyms else None,
            'depositor': self.generator.name,
            'primary_cell_type': self.derivation.primary_cell_type.name if self.derivation.primary_cell_type else None,
            'alternative_names': self.alternative_names,
        }


class CelllineStatus(models.Model):

    status = models.CharField(_(u'Cell line status'), max_length=50, unique=True)

    class Meta:
        verbose_name = _(u'Cell line status')
        verbose_name_plural = _(u'Cell line statuses')
        ordering = ['status']

    def __unicode__(self):
        return self.status


# -----------------------------------------------------------------------------
# Batch: Cellline -> Batch(es) -> Aliquot(s)

class CelllineBatch(models.Model):

    cell_line = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), related_name='batches')
    biosamples_id = models.CharField(_(u'Biosamples ID'), max_length=12, unique=True)

    batch_id = models.CharField(_(u'Batch ID'), max_length=12)

    vials_at_roslin = models.IntegerField(_(u'Vials at Central facility'), null=True, blank=True)
    vials_shipped_to_ecacc = models.IntegerField(_(u'Vials shipped to ECACC'), null=True, blank=True)
    vials_shipped_to_fraunhoffer = models.IntegerField(_(u'Vials shipped to Fraunhoffer'), null=True, blank=True)

    certificate_of_analysis = models.FileField(_(u'Certificate of analysis'), upload_to=upload_to, null=True, blank=True)
    certificate_of_analysis_md5 = models.CharField(_(u'Certificate of analysis md5'), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line batch')
        verbose_name_plural = _(u'Cell line batches')
        ordering = ['biosamples_id']
        unique_together = (('cell_line', 'batch_id'))

    def __unicode__(self):
        return u'%s' % (self.biosamples_id,)


class CelllineBatchImages(models.Model):

    batch = models.ForeignKey('CelllineBatch', verbose_name=_(u'Cell line Batch images'), related_name='images')
    image_file = models.FileField(_(u'Image file'), upload_to=upload_to)
    image_md5 = models.CharField(_(u'Image file md5'), max_length=100)
    magnification = models.CharField(_(u'Magnification'), max_length=10, null=True, blank=True)
    time_point = models.CharField(_(u'Time point'), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line batch image')
        verbose_name_plural = _(u'Cell line batch images')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class CelllineAliquot(models.Model):

    batch = models.ForeignKey('CelllineBatch', verbose_name=_(u'Cell line'), related_name='aliquots')
    biosamples_id = models.CharField(_(u'Biosamples ID'), max_length=12, unique=True)

    derived_from_aliqot = models.ForeignKey('self', verbose_name=_(u'Derived from aliquot'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line aliquot')
        verbose_name_plural = _(u'Cell line aliquotes')
        ordering = ['biosamples_id']

    def __unicode__(self):
        return u'%s' % (self.biosamples_id,)


# -----------------------------------------------------------------------------
# Donor

class Donor(models.Model):

    biosamples_id = models.CharField(_(u'Biosamples ID'), max_length=12, unique=True)
    gender = models.ForeignKey(Gender, verbose_name=_(u'Gender'), null=True, blank=True)

    provider_donor_ids = ArrayField(models.CharField(max_length=20), verbose_name=_(u'Provider donor ids'), null=True)
    country_of_origin = models.ForeignKey('Country', verbose_name=_(u'Country of origin'), null=True, blank=True)
    ethnicity = models.CharField(_(u'Ethnicity'), max_length=100, null=True, blank=True)
    phenotypes = ArrayField(models.CharField(max_length=100), verbose_name=_(u'Phenotypes'), null=True)

    karyotype = models.CharField(_(u'Karyotype'), max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Donor')
        verbose_name_plural = _(u'Donors')
        ordering = ['biosamples_id']

    def __unicode__(self):
        return u'%s' % (self.biosamples_id,)


# -----------------------------------------------------------------------------
# Disease

class Disease(models.Model):

    icdcode = models.CharField(_(u'DOID'), max_length=30, unique=True, null=True, blank=True)
    purl = models.URLField(_(u'Purl'), max_length=300, unique=True, null=True, blank=True)
    disease = models.CharField(_(u'Disease'), max_length=45, blank=True)
    synonyms = models.CharField(_(u'Synonyms'), max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Disease')
        verbose_name_plural = _(u'Diseases')
        ordering = ['disease']

    def __unicode__(self):
        return u'%s' % (self.disease,)


# -----------------------------------------------------------------------------
# Cell line and batch culture conditions

class CelllineCultureConditions(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'))

    surface_coating = models.CharField(_(u'Surface coating'), max_length=100, null=True, blank=True)
    feeder_cell_type = models.CharField(_(u'Feeder cell type'), max_length=45, null=True, blank=True)
    feeder_cell_id = models.CharField(_(u'Feeder cell id'), max_length=45, null=True, blank=True)
    passage_method = models.CharField(_(u'Passage method'), max_length=100, null=True, blank=True)
    enzymatically = models.CharField(_(u'Enzymatically'), max_length=45, null=True, blank=True)
    enzyme_free = models.CharField(_(u'Enzyme free'), max_length=45, null=True, blank=True)
    o2_concentration = models.IntegerField(_(u'O2 concentration'), null=True, blank=True)
    co2_concentration = models.IntegerField(_(u'Co2 concentration'), null=True, blank=True)
    other_culture_environment = models.CharField(_(u'Other culture environment'), max_length=100, null=True, blank=True)

    culture_medium = models.CharField(_(u'Culture medium'), max_length=45, null=True, blank=True)

    passage_number_banked = models.CharField(_(u'Passage number banked (pre-EBiSC)'), max_length=10, null=True, blank=True)
    number_of_vials_banked = models.CharField(_(u'No. Vials banked (pre-EBiSC)'), max_length=10, null=True, blank=True)
    passage_history = models.NullBooleanField(_(u'Passage history (back to reprogramming)'), default=None, null=True, blank=True)
    culture_history = models.NullBooleanField(_(u'Culture history (methods used)'), default=None, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line culture conditions')
        verbose_name_plural = _(u'Cell line culture conditions')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class BatchCultureConditions(models.Model):

    batch = models.OneToOneField(CelllineBatch, verbose_name=_(u'Batch'))

    culture_medium = models.CharField(_(u'Medium'), max_length=100, null=True, blank=True)
    passage_method = models.CharField(_(u'Passage method'), max_length=100, null=True, blank=True)
    matrix = models.CharField(_(u'Matrix'), max_length=100, null=True, blank=True)
    o2_concentration = models.CharField(_(u'O2 Concentration'), max_length=12, null=True, blank=True)
    co2_concentration = models.CharField(_(u'CO2 Concentration'), max_length=12, null=True, blank=True)
    temperature = models.CharField(_(u'Temperature'), max_length=12, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Batch culture conditions')
        verbose_name_plural = _(u'Batch culture conditions')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class CultureMediumOther(DirtyFieldsMixin, models.Model):

    cell_line_culture_conditions = models.OneToOneField(CelllineCultureConditions, verbose_name=_(u'Cell line culture conditions'), related_name='culture_medium_other')

    base = models.CharField(_(u'Culture medium base'), max_length=45, blank=True)
    protein_source = models.CharField(_(u'Protein source'), max_length=45, null=True, blank=True)
    serum_concentration = models.IntegerField(_(u'Serum concentration'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Culture medium')
        verbose_name_plural = _(u'Culture mediums')
        ordering = ['base', 'protein_source', 'serum_concentration']

    def __unicode__(self):
        return u'%s / %s / %s' % (self.base, self.protein_source, self.serum_concentration)


class CelllineCultureMediumSupplement(DirtyFieldsMixin, models.Model):

    cell_line_culture_conditions = models.ForeignKey(CelllineCultureConditions, verbose_name=_(u'Cell line culture conditions'), related_name='medium_supplements')

    supplement = models.CharField(_(u'Supplement'), max_length=45)
    amount = models.CharField(_(u'Amount'), max_length=45, null=True, blank=True)
    unit = models.ForeignKey('Unit', verbose_name=_(u'Unit'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line culture supplements')
        verbose_name_plural = _(u'Cell line culture supplements')
        ordering = ['supplement']

    def __unicode__(self):
        if self.amount and self.unit:
            return '%s - %s %s' % (self.supplement, self.amount, self.unit)
        else:
            return unicode(self.supplement)


# -----------------------------------------------------------------------------
# Cell line Derivation

class CelllineDerivation(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'), related_name='derivation')

    primary_cell_type = models.ForeignKey('CellType', verbose_name=_(u'Primary cell type'), null=True, blank=True)
    primary_cell_developmental_stage = models.CharField(_(u'Primary cell developmental stage'), max_length=45, null=True, blank=True)
    tissue_procurement_location = models.CharField(_(u'Location of primary tissue procurement'), max_length=45, null=True, blank=True)
    tissue_collection_date = models.DateField(_(u'Tissue collection date'), null=True, blank=True)
    reprogramming_passage_number = models.CharField(_(u'Passage number reprogrammed'), max_length=10, null=True, blank=True)

    selection_criteria_for_clones = models.TextField(_(u'Selection criteria for clones'), null=True, blank=True)
    xeno_free_conditions = models.NullBooleanField(_(u'Xeno free conditions'), default=None, null=True, blank=True)
    derived_under_gmp = models.NullBooleanField(_(u'Derived under gmp'), default=None, null=True, blank=True)
    available_as_clinical_grade = models.NullBooleanField(_(u'Available as clinical grade'), default=None, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line derivation')
        verbose_name_plural = _(u'Cell line derivations')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


# Reprogramming method

class NonIntegratingVector(models.Model):

    name = models.CharField(_(u'Non-integrating vector'), max_length=100, unique=True)

    class Meta:
        verbose_name = _(u'Non-integrating vector')
        verbose_name_plural = _(u'Non-integrating vectors')
        ordering = ['name']

    def __unicode__(self):
        return self.name


class IntegratingVector(models.Model):

    name = models.CharField(_(u'Integrating vector'), max_length=100, unique=True)

    class Meta:
        verbose_name = _(u'Integrating vector')
        verbose_name_plural = _(u'Integrating vectors')
        ordering = ['name']

    def __unicode__(self):
        return self.name


class CelllineNonIntegratingVector(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'), related_name='non_integrating_vector')
    vector = models.ForeignKey(NonIntegratingVector, verbose_name=_(u'Non-integrating vector'), null=True, blank=True)

    genes = models.ManyToManyField(Molecule, blank=True)

    class Meta:
        verbose_name = _(u'Cell line non integrating vector')
        verbose_name_plural = _(u'Cell line non integrating vectors')

    def __unicode__(self):
        return unicode(self.vector)


class CelllineIntegratingVector(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'), related_name='integrating_vector')
    vector = models.ForeignKey(IntegratingVector, verbose_name=_(u'Integrating vector'), null=True, blank=True)

    virus = models.ForeignKey(Virus, verbose_name=_(u'Virus'), null=True, blank=True)
    transposon = models.ForeignKey(Transposon, verbose_name=_(u'Transposon'), null=True, blank=True)

    excisable = models.NullBooleanField(_(u'Excisable'), default=None, null=True, blank=True)
    absence_reprogramming_vectors = models.NullBooleanField(_(u'Absence of reprogramming vector(s)'), default=None, null=True, blank=True)

    genes = models.ManyToManyField(Molecule, blank=True)

    class Meta:
        verbose_name = _(u'Cell line integrating vector')
        verbose_name_plural = _(u'Cell line integrating vectors')

    def __unicode__(self):
        return unicode(self.vector)


class VectorFreeReprogrammingFactor(models.Model):

    vector_free_reprogramming_factor = models.CharField(_(u'Vector free reprogram factor'), max_length=15, blank=True)
    reference_id = models.CharField(_(u'Referenceid'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Vector free reprogram factor')
        verbose_name_plural = _(u'Vector free reprogram factors')
        ordering = ['vector_free_reprogramming_factor']

    def __unicode__(self):
        return u'%s' % (self.vector_free_reprogramming_factor,)


class CelllineVectorFreeReprogrammingFactors(models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'), related_name='vector_free_reprogramming_factors')
    factor = models.ForeignKey(VectorFreeReprogrammingFactor, verbose_name=_(u'Vector-free reprogramming factor'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line Vector-free Programming Factor')
        verbose_name_plural = _(u'Cell line Vector-free Programming Factors')

    def __unicode__(self):
        return unicode(self.factor)


# -----------------------------------------------------------------------------
# Cell line Characterization

class CelllineCharacterization(models.Model):

    SCREENING_CHOICES = (
        ('positive', u'Positive'),
        ('negative', u'Negative'),
        ('not_done', u'Not done'),
    )

    cell_line = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'))

    certificate_of_analysis_passage_number = models.CharField(_(u'Certificate of analysis passage number'), max_length=10, null=True, blank=True)

    screening_hiv1 = models.CharField(_(u'Hiv1 screening'), max_length=20, choices=SCREENING_CHOICES, null=True, blank=True)
    screening_hiv2 = models.CharField(_(u'Hiv2 screening'), max_length=20, choices=SCREENING_CHOICES, null=True, blank=True)

    screening_hepatitis_b = models.CharField(_(u'Hepatitis b'), max_length=20, choices=SCREENING_CHOICES, null=True, blank=True)
    screening_hepatitis_c = models.CharField(_(u'Hepatitis c'), max_length=20, choices=SCREENING_CHOICES, null=True, blank=True)

    screening_mycoplasma = models.CharField(_(u'Mycoplasma'), max_length=20, choices=SCREENING_CHOICES, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line characterization')
        verbose_name_plural = _(u'Cell line characterizations')
        ordering = ['cell_line']

    def __unicode__(self):
        return unicode(self.cell_line)


class MarkerMoleculeBase(models.Model):

    RESULT_CHOICES = (
        ('+', '+'),
        ('-', '-'),
        ('nd', 'n.d.'),
    )

    # molecule = models.ForeignKey(Molecule) TODO
    molecule = models.CharField(u'Molecule', max_length=25)
    result = models.CharField(u'Result', max_length=5, choices=RESULT_CHOICES)

    class Meta:
        abstract = True
        verbose_name = _(u'Marker molecule')
        verbose_name_plural = _(u'Marker molecules')
        ordering = ['molecule']


# Undifferentiated cells

class UndifferentiatedMorphologyMarkerImune(models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=u'Cell line', related_name='undifferentiated_morphology_marker_imune')
    passage_number = models.CharField(u'Passage number', max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Markerd Undiff - Imune')
        verbose_name_plural = _(u'Markerd Undiff - Imune')


class UndifferentiatedMorphologyMarkerImuneMolecule(MarkerMoleculeBase):

    marker = models.ForeignKey(UndifferentiatedMorphologyMarkerImune, verbose_name=u'Marker', related_name='molecules')


class UndifferentiatedMorphologyMarkerRtPcr(models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=u'Cell line', related_name='undifferentiated_morphology_marker_rtpcr')
    passage_number = models.CharField(u'Passage number', max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Markerd Undiff - RtPcr')
        verbose_name_plural = _(u'Markerd Undiff - RtPcr')


class UndifferentiatedMorphologyMarkerRtPcrMolecule(MarkerMoleculeBase):

    marker = models.ForeignKey(UndifferentiatedMorphologyMarkerRtPcr, verbose_name=u'Marker', related_name='molecules')


class UndifferentiatedMorphologyMarkerFacs(models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=u'Cell line', related_name='undifferentiated_morphology_marker_facs')
    passage_number = models.CharField(u'Passage number', max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Markerd Undiff - Facs')
        verbose_name_plural = _(u'Markerd Undiff - Facs')


class UndifferentiatedMorphologyMarkerFacsMolecule(MarkerMoleculeBase):

    marker = models.ForeignKey(UndifferentiatedMorphologyMarkerFacs, verbose_name=u'Marker', related_name='molecules')


class UndifferentiatedMorphologyMarkerMorphology(models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=u'Cell line', related_name='undifferentiated_morphology_marker_morphology')
    passage_number = models.CharField(u'Passage number', max_length=10, null=True, blank=True)
    description = models.TextField(u'Description', null=True, blank=True)
    data_url = models.URLField(u'URL', null=True, blank=True)

    class Meta:
        verbose_name = _(u'Markerd Undiff - Morphology')
        verbose_name_plural = _(u'Markerd Undiff - Morphology')


class UndifferentiatedMorphologyMarkerExpressionProfile(models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=u'Cell line', related_name='undifferentiated_morphology_marker_expression_profile')
    method = models.CharField(u'Method', max_length=100, null=True, blank=True)
    passage_number = models.CharField(u'Passage number', max_length=10, null=True, blank=True)
    data_url = models.URLField(u'Data URL', null=True, blank=True)
    uploaded_data_url = models.URLField(u'Uploaded data URL', null=True, blank=True)

    class Meta:
        verbose_name = _(u'Markerd Undiff - Expression profile')
        verbose_name_plural = _(u'Markerd Undiff - Expression profile')


class UndifferentiatedMorphologyMarkerExpressionProfileMolecule(MarkerMoleculeBase):

    marker = models.ForeignKey(UndifferentiatedMorphologyMarkerExpressionProfile, verbose_name=u'Marker', related_name='molecules')


# -----------------------------------------------------------------------------
# Cell line Ethics

class CelllineEthics(DirtyFieldsMixin, models.Model):

    ACCESS_POLICY_CHOICES = (
        ('open_access', 'Open access'),
        ('controlled_access', 'Controlled access'),
        ('no_information', 'No information'),
    )

    cell_line = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'))

    donor_consent = models.NullBooleanField(_(u'Donor consent'))
    no_pressure_statement = models.NullBooleanField(_(u'No pressure statement'))
    no_inducement_statement = models.NullBooleanField(_(u'No inducement statement'))
    donor_consent_form = models.NullBooleanField(_(u'Copy of consent form'))
    donor_consent_form_url = models.URLField(u'URL of donor consent form', null=True, blank=True)
    known_location_of_consent_form = models.NullBooleanField(_(u'Do you know who holds the consent form'))
    copy_of_consent_form_obtainable = models.NullBooleanField(_(u'Is copy of consent form obtainable'))
    obtain_new_consent_form = models.NullBooleanField(_(u'Is new form obtainable'))
    donor_recontact_agreement = models.NullBooleanField(_(u'Has the donor agreed to be recontacted'))
    consent_anticipates_donor_notification_research_results = models.NullBooleanField(_(u'Consent anticipates the donor will be notified of results of research involving the donated samples or derived cells'))
    donor_expects_notification_health_implications = models.NullBooleanField(_(u'Donor expects to be informed if, during use of donated material, something with significant health implications for the donor is discovered'))
    copy_of_donor_consent_information_english_obtainable = models.NullBooleanField(_(u'Is copy of consent information obtainable in English'))
    copy_of_donor_consent_information_english_url = models.URLField(u'URL of donor consent information in English', null=True, blank=True)
    copy_of_donor_consent_form_english_obtainable = models.NullBooleanField(_(u'Is copy of consent form obtainable in English'))
    copy_of_donor_consent_form_english_url = models.URLField(u'URL of donor consent form in English', null=True, blank=True)

    consent_permits_ips_derivation = models.NullBooleanField(_(u'Consent expressly permits derivation of iPS cells'))
    consent_pertains_specific_research_project = models.NullBooleanField(_(u'Consent pertains to one specific research project'))
    consent_permits_future_research = models.NullBooleanField(_(u'Consent permits unforeseen future research'))
    future_research_permitted_specified_areas = models.NullBooleanField(_(u'Future research is permitted only in relation to specified areas or types of research'))
    future_research_permitted_areas = models.TextField(_(u'Future research permitted areas or types'), null=True, blank=True)
    consent_permits_clinical_treatment = models.NullBooleanField(_(u'Consent permits uses for clinical treatment or human applications'))
    formal_permission_for_distribution = models.NullBooleanField(_(u'Formal permission from the owner for distribution'))
    consent_permits_research_by_academic_institution = models.NullBooleanField(_(u'Consent permits research by academic institution'))
    consent_permits_research_by_org = models.NullBooleanField(_(u'Consent permits research by public organization'))
    consent_permits_research_by_non_profit_company = models.NullBooleanField(_(u'Consent permits research by non-profit company'))
    consent_permits_research_by_for_profit_company = models.NullBooleanField(_(u'Consent permits research by for-profit company'))
    consent_permits_development_of_commercial_products = models.NullBooleanField(_(u'Consent permits development of commercial products'))
    consent_expressly_prevents_commercial_development = models.NullBooleanField(_(u'Consent expressly prevents commercial development'))
    consent_expressly_prevents_financial_gain = models.NullBooleanField(_(u'Consent expressly prevents financial gain'))
    further_constraints_on_use = models.NullBooleanField(_(u'Any further constraints on use'))
    further_constraints_on_use_desc = models.TextField(_(u'Further constraints on use'), null=True, blank=True)

    consent_expressly_permits_indefinite_storage = models.NullBooleanField(_(u'Consent expressly permits indefinite storage'))
    consent_prevents_availiability_to_worldwide_research = models.NullBooleanField(_(u'Consent prevents availiability to worldwide research'))

    consent_permits_genetic_testing = models.NullBooleanField(_(u'Consent permits genetic testing'))
    consent_permits_testing_microbiological_agents_pathogens = models.NullBooleanField(_(u'Consent permits testing for microbiological agents pathogens'))
    derived_information_influence_personal_future_treatment = models.NullBooleanField(_(u'Derived information may influence personal future treatment'))

    donor_data_protection_informed = models.NullBooleanField(_(u'Donor informed about data protection'))
    donated_material_code = models.NullBooleanField(_(u'Donated material is coded'))
    donated_material_rendered_unidentifiable = models.NullBooleanField(_(u'Donated material has been rendered unidentifiable'))
    donor_identity_protected_rare_disease = models.CharField(u'Donor identity protected', max_length=10, null=True, blank=True, choices=EXTENDED_BOOL_CHOICES)
    genetic_information_exists = models.NullBooleanField(_(u'Is there genetic information associated with the cell line'))
    genetic_information_access_policy = models.CharField(u'Access policy for genetic information derived from the cell line', max_length=50, null=True, blank=True, choices=ACCESS_POLICY_CHOICES)
    genetic_information_available = models.NullBooleanField(_(u'Is genetic information associated with the cell line available'))

    consent_permits_access_medical_records = models.NullBooleanField(_(u'Consent permits access to medical records'))
    consent_permits_access_other_clinical_source = models.NullBooleanField(_(u'Consent permits access to other clinical sources'))
    medical_records_access_consented = models.NullBooleanField(_(u'Access to ongoing medical records has been consented'))
    medical_records_access_consented_organisation_name = models.TextField(_(u'Organisation holding medical records'), null=True, blank=True)

    consent_permits_stop_of_derived_material_use = models.NullBooleanField(_(u'Consent permits stopping the use of derived material'))
    consent_permits_stop_of_delivery_of_information_and_data = models.NullBooleanField(_(u'Consent permits stopping delivery or use of information and data about donor'))

    authority_approval = models.NullBooleanField(_(u'Institutional review board/competent authority approval'))
    approval_authority_name = models.TextField(_(u'Name of accrediting authority'), null=True, blank=True)
    approval_number = models.CharField(_(u'Approval number'), max_length=100, null=True, blank=True)
    ethics_review_panel_opinion_relation_consent_form = models.NullBooleanField(_(u'Ethics review panel provided a favourable opinion in relation of the form of consent'))
    ethics_review_panel_opinion_project_proposed_use = models.NullBooleanField(_(u'Ethics review panel provided a favourable opinion in relation to the project'))

    recombined_dna_vectors_supplier = models.TextField(_(u'Recombined DNA vectors supplier'), null=True, blank=True)
    use_or_distribution_constraints = models.NullBooleanField(_(u'Any use or distribution constraints'))
    use_or_distribution_constraints_desc = models.TextField(_(u'Use or distribution constraints'), null=True, blank=True)
    third_party_obligations = models.NullBooleanField(_(u'Any third party obligations'))
    third_party_obligations_desc = models.TextField(_(u'Third party obligations'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line ethics')
        verbose_name_plural = _(u'Cell line ethics')

    def __unicode__(self):
        return unicode(self.cell_line)


# -----------------------------------------------------------------------------
# Organizations

class CelllineOrganization(models.Model):

    cell_line = models.ForeignKey(Cellline, verbose_name=_(u'Cell line'), related_name='organizations')
    organization = models.ForeignKey('Organization', verbose_name=_(u'Organization'))
    cell_line_org_type = models.ForeignKey('CelllineOrgType', verbose_name=_(u'Cell line org type'))

    class Meta:
        verbose_name = _(u'Cell line organization')
        verbose_name_plural = _(u'Cell line organizations')
        unique_together = ('cell_line', 'organization', 'cell_line_org_type')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Organization(models.Model):

    name = models.CharField(_(u'Organization name'), max_length=100, unique=True, null=True, blank=True)
    short_name = models.CharField(_(u'Organization short name'), unique=True, max_length=6, null=True, blank=True)
    contact = models.ForeignKey('Contact', verbose_name=_(u'Contact'), null=True, blank=True)
    org_type = models.ForeignKey('OrgType', verbose_name=_(u'Organization type'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Organization')
        verbose_name_plural = _(u'Organizations')
        ordering = ['name', 'short_name']

    def __unicode__(self):
        return u' - '.join([x for x in self.short_name, self.name if x])


class CelllineOrgType(models.Model):

    cell_line_org_type = models.CharField(_(u'Cell line organization type'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Cell line org type')
        verbose_name_plural = _(u'Cell line org types')
        ordering = ['cell_line_org_type']

    def __unicode__(self):
        return u'%s' % (self.cell_line_org_type,)


class OrgType(models.Model):

    org_type = models.CharField(_(u'Organization type'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Organization type')
        verbose_name_plural = _(u'Organization types')
        ordering = ['org_type']

    def __unicode__(self):
        return u'%s' % (self.org_type,)


class Contact(models.Model):

    contact_type = models.ForeignKey('ContactType', verbose_name=_(u'Contact type'), null=True, blank=True)
    country = models.ForeignKey('Country', verbose_name=_(u'Country'), db_column='country')
    postcode = models.ForeignKey('Postcode', verbose_name=_(u'Postcode'), db_column='postcode')
    state_county = models.IntegerField(_(u'State county'), null=True, blank=True)
    city = models.CharField(_(u'City'), max_length=45, blank=True)
    street = models.CharField(_(u'Street'), max_length=45, blank=True)
    building_number = models.CharField(_(u'Building number'), max_length=20, blank=True)
    suite_or_apt_or_dept = models.CharField(_(u'Suite or apt or dept'), max_length=10, null=True, blank=True)
    office_phone_country_code = models.ForeignKey('PhoneCountryCode', verbose_name=_(u'Phone country code'), related_name='contacts_officephonecountrycode', null=True, blank=True)
    office_phone = models.CharField(_(u'Office phone'), max_length=20, null=True, blank=True)
    fax_country_code = models.ForeignKey('PhoneCountryCode', verbose_name=_(u'Phone country code'), related_name='contacts_faxcountrycode', null=True, blank=True)
    fax = models.CharField(_(u'Fax'), max_length=20, null=True, blank=True)
    mobile_country_code = models.ForeignKey('PhoneCountryCode', verbose_name=_(u'Phone country code'), related_name='contacts_mobilecountrycode', null=True, blank=True)
    mobile_phone = models.CharField(_(u'Mobile phone'), max_length=20, null=True, blank=True)
    website = models.CharField(_(u'Website'), max_length=45, null=True, blank=True)
    email_address = models.CharField(_(u'Email address'), max_length=45, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Contact')
        verbose_name_plural = _(u'Contacts')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class ContactType(models.Model):

    contact_type = models.CharField(_(u'Contact type'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Contact type')
        verbose_name_plural = _(u'Contact types')
        ordering = ['contact_type']

    def __unicode__(self):
        return u'%s' % (self.contact_type,)


class PhoneCountryCode(models.Model):

    phonecountrycode = models.DecimalField(_(u'Phone country code'), max_digits=4, decimal_places=0, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Phone country code')
        verbose_name_plural = _(u'Phone country codes')
        ordering = ['phonecountrycode']

    def __unicode__(self):
        return u'%s' % (self.phonecountrycode,)


class Postcode(models.Model):

    postcode = models.CharField(_(u'Postcode'), max_length=45, blank=True)
    district = models.CharField(_(u'District'), max_length=20)

    class Meta:
        verbose_name = _(u'Postcode')
        verbose_name_plural = _(u'Postcodes')
        ordering = ['postcode', 'district']

    def __unicode__(self):
        return u'%s %s' % (self.postcode, self.district)


class Person(models.Model):

    organization = models.IntegerField(_(u'Organization'), null=True, blank=True)
    last_name = models.CharField(_(u'Person last name'), max_length=20, blank=True)
    first_name = models.CharField(_(u'Person first name'), max_length=45, blank=True)
    contact = models.ForeignKey('Contact', verbose_name=_(u'Contact'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Person')
        verbose_name_plural = _(u'Persons')
        ordering = ['last_name', 'first_name']

    def __unicode__(self):
        return u'%s %s' % (self.last_name, self.first_name)


# -----------------------------------------------------------------------------
# Publications, documents

class CelllinePublication(models.Model):

    REFERENCE_TYPE_CHOICES = (
        ('pubmed', 'PubMed'),
    )

    cell_line = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), null=True, blank=True, related_name='publications')

    reference_type = models.CharField(u'Type', max_length=100, choices=REFERENCE_TYPE_CHOICES)
    reference_id = models.CharField(u'ID', max_length=100, null=True, blank=True)
    reference_url = models.URLField(u'URL')
    reference_title = models.CharField(u'Title', max_length=500)

    class Meta:
        verbose_name = _(u'Cell line publication')
        verbose_name_plural = _(u'Cell line publications')
        unique_together = (('cell_line', 'reference_url'),)
        ordering = ('reference_title',)

    def __unicode__(self):
        return self.reference_title

    @staticmethod
    def pubmed_url_from_id(id):
        return 'http://www.ncbi.nlm.nih.gov/pubmed/%s' % id


class Document(models.Model):

    cell_line = models.IntegerField(_(u'Cell line'), null=True, blank=True)
    title = models.CharField(_(u'Title'), max_length=45, blank=True)
    abstract = models.TextField(_(u'Abstract'), null=True, blank=True)
    document_type = models.ForeignKey('DocumentType', verbose_name=_(u'Document type'), null=True, blank=True)
    depositor = models.IntegerField(_(u'Document depositor'), null=True, blank=True)
    authors = models.TextField(_(u'Authors'), null=True, blank=True)
    owner = models.IntegerField(_(u'Owner'), null=True, blank=True)
    version = models.CharField(_(u'Version'), max_length=5, blank=True)
    access_level = models.IntegerField(_(u'Access level'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Document')
        verbose_name_plural = _(u'Documents')
        ordering = ['title']

    def __unicode__(self):
        return u'%s' % (self.title,)


class DocumentType(models.Model):

    document_type = models.CharField(_(u'Document type'), max_length=30, blank=True)

    class Meta:
        verbose_name = _(u'Document type')
        verbose_name_plural = _(u'Document types')
        ordering = ['document_type']

    def __unicode__(self):
        return u'%s' % (self.document_type,)


# -----------------------------------------------------------------------------
# Cell line value


class CelllineValue(models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'), null=True, blank=True)
    potential_use = models.CharField(_(u'Potential use'), max_length=100, blank=True)
    value_to_society = models.CharField(_(u'Value to society'), max_length=100, blank=True)
    value_to_research = models.CharField(_(u'Value to research'), max_length=100, blank=True)
    other_value = models.CharField(_(u'Other value'), max_length=100, blank=True)

    class Meta:
        verbose_name = _(u'Cell line value')
        verbose_name_plural = _(u'Cell line values')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


# -----------------------------------------------------------------------------
# Genotyping

# Karyotyping
class CelllineKaryotype(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField('Cellline', verbose_name=_(u'Cell line'), related_name='karyotype')

    karyotype = models.CharField(_(u'Karyotype'), max_length=500, null=True, blank=True)
    karyotype_method = models.CharField(_(u'Karyotype method'), max_length=100, null=True, blank=True)

    passage_number = models.CharField(_(u'Passage number'), max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line karyotype')
        verbose_name_plural = _(u'Cell line karyotypes')
        ordering = []

    def __unicode__(self):
        return unicode(self.karyotype)


# Genome-Wide Assays
class CelllineHlaTyping(models.Model):

    cell_line = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), related_name="hla_typing")
    hla_class = models.CharField(_(u'HLA class'), max_length=10, null=True, blank=True)
    hla = models.CharField(_(u'HLA'), max_length=10, null=True, blank=True)
    hla_allele_1 = models.CharField(_(u'Cell line HLA allele 1'), max_length=45, null=True, blank=True)
    hla_allele_2 = models.CharField(_(u'Cell line HLA allele 2'), max_length=45, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line HLA typing')
        verbose_name_plural = _(u'Cell line HLA typing')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class CelllineStrFingerprinting(models.Model):

    cell_line = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), related_name="str_fingerprinting")
    locus = models.CharField(_(u'Locus'), max_length=45, null=True, blank=True)
    allele1 = models.CharField(_(u'Allele 1'), max_length=45, null=True, blank=True)
    allele2 = models.CharField(_(u'Allele 2'), max_length=45, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line STR finger printing')
        verbose_name_plural = _(u'Cell line STR finger printing')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class CelllineGenomeAnalysis(models.Model):

    cell_line = models.OneToOneField('Cellline', verbose_name=_(u'Cell line'), related_name='genome_analysis')
    data = models.CharField(_(u'Data'), max_length=100, null=True, blank=True)
    link = models.URLField(u'Link', null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line genome analysis')
        verbose_name_plural = _(u'Cell line genome analysis')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


# Disease associated genotype
class CelllineDiseaseGenotype(models.Model):

    cell_line = models.OneToOneField('Cellline', verbose_name=_(u'Cell line'), related_name='genotyping_variant')

    allele_carried = models.CharField(_(u'Allele carried through'), max_length=12, null=True, blank=True)
    cell_line_form = models.CharField(_(u'Is the cell line homozygote or heterozygot for this variant'), max_length=12, null=True, blank=True)

    assembly = models.CharField(_(u'Assembly'), max_length=45, null=True, blank=True)
    chormosome = models.CharField(_(u'Chormosome'), max_length=45, null=True, blank=True)
    coordinate = models.CharField(_(u'Coordinate'), max_length=45, null=True, blank=True)
    reference_allele = models.CharField(_(u'Reference allele'), max_length=45, null=True, blank=True)
    alternative_allele = models.CharField(_(u'Alternative allele'), max_length=45, null=True, blank=True)
    protein_sequence_variants = models.CharField(_(u'Protein sequence variants'), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line disease associated genotype')
        verbose_name_plural = _(u'Cell line disease associated genotypes')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class CelllineGenotypingSNP(models.Model):

    disease_genotype = models.ForeignKey('CelllineDiseaseGenotype', verbose_name=_(u'Cell line disease genotype'), related_name='snps', null=True, blank=True)

    gene_name = models.CharField(_(u'SNP gene name'), max_length=45, null=True, blank=True)
    chromosomal_position = models.CharField(_(u'SNP choromosomal position'), max_length=45, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line snp')
        verbose_name_plural = _(u'Cell line snps')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class CelllineGenotypingRsNumber(models.Model):

    disease_genotype = models.ForeignKey('CelllineDiseaseGenotype', verbose_name=_(u'Cell line disease genotype'), related_name='rs_number', null=True, blank=True)

    rs_number = models.CharField(_(u'rs Number'), max_length=12, null=True, blank=True)
    link = models.URLField(u'Link', null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line rs number')
        verbose_name_plural = _(u'Cell line rs numbers')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


# Donor genotyping
class DonorGenotype(models.Model):

    donor = models.OneToOneField('Donor', verbose_name=_(u'Donor'), related_name='donor_genotyping')

    allele_carried = models.CharField(_(u'Allele carried through'), max_length=12, null=True, blank=True)
    homozygous_heterozygous = models.CharField(_(u'Is the donor homozygous or heterozygous for this variant'), max_length=12, null=True, blank=True)

    assembly = models.CharField(_(u'Assembly'), max_length=45, null=True, blank=True)
    chormosome = models.CharField(_(u'Chormosome'), max_length=45, null=True, blank=True)
    coordinate = models.CharField(_(u'Coordinate'), max_length=45, null=True, blank=True)
    reference_allele = models.CharField(_(u'Reference allele'), max_length=45, null=True, blank=True)
    alternative_allele = models.CharField(_(u'Alternative allele'), max_length=45, null=True, blank=True)
    protein_sequence_variants = models.CharField(_(u'Protein sequence variants'), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Donor Genotyping')
        verbose_name_plural = _(u'Donor Genotyping')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class DonorGenotypingSNP(models.Model):

    donor_genotype = models.ForeignKey('DonorGenotype', verbose_name=_(u'Donor Genotype'), related_name='donor_snps')

    gene_name = models.CharField(_(u'SNP gene name'), max_length=45)
    chromosomal_position = models.CharField(_(u'SNP choromosomal position'), max_length=45, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Donor snp')
        verbose_name_plural = _(u'Donor snps')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class DonorGenotypingRsNumber(models.Model):

    donor_genotype = models.ForeignKey('DonorGenotype', verbose_name=_(u'Donor Genotype'), related_name='donor_rs_number')

    rs_number = models.CharField(_(u'rs Number'), max_length=12)
    link = models.URLField(u'Link', null=True, blank=True)

    class Meta:
        verbose_name = _(u'Donor rs number')
        verbose_name_plural = _(u'Donor rs numbers')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


# Genetic modification
class CelllineGeneticModification(models.Model):

    cell_line = models.OneToOneField('Cellline', verbose_name=_(u'Cell line'), related_name='genetic_modification')
    protocol = models.FileField(_(u'Protocol'), upload_to=upload_to, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line genetic modification')
        verbose_name_plural = _(u'Cell line genetic modifications')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class GeneticModificationTransgeneExpression(models.Model):

    cell_line = models.OneToOneField('Cellline', verbose_name=_(u'Cell line'), related_name='genetic_modification_transgene_expression')
    genes = models.ManyToManyField(Molecule, blank=True)
    delivery_method = models.CharField(_(u'Delivery method'), max_length=45, null=True, blank=True)
    virus = models.ForeignKey(Virus, verbose_name=_(u'Virus'), null=True, blank=True)
    transposon = models.ForeignKey(Transposon, verbose_name=_(u'Transposon'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Genetic modification - Transgene Expression')
        verbose_name_plural = _(u'Genetic modifications - Transgene Expression')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class GeneticModificationGeneKnockOut(models.Model):

    cell_line = models.OneToOneField('Cellline', verbose_name=_(u'Cell line'), related_name='genetic_modification_gene_knock_out')
    target_genes = models.ManyToManyField(Molecule, blank=True)
    delivery_method = models.CharField(_(u'Delivery method'), max_length=45, null=True, blank=True)
    virus = models.ForeignKey(Virus, verbose_name=_(u'Virus'), null=True, blank=True)
    transposon = models.ForeignKey(Transposon, verbose_name=_(u'Transposon'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Genetic modification - Gene knock-out')
        verbose_name_plural = _(u'Genetic modifications - Gene knock-out')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class GeneticModificationGeneKnockIn(models.Model):

    cell_line = models.OneToOneField('Cellline', verbose_name=_(u'Cell line'), related_name='genetic_modification_gene_knock_in')
    target_genes = models.ManyToManyField(Molecule, blank=True, related_name='target_genes')
    transgenes = models.ManyToManyField(Molecule, blank=True, related_name='transgenes')
    delivery_method = models.CharField(_(u'Delivery method'), max_length=45, null=True, blank=True)
    virus = models.ForeignKey(Virus, verbose_name=_(u'Virus'), null=True, blank=True)
    transposon = models.ForeignKey(Transposon, verbose_name=_(u'Transposon'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Genetic modification - Gene knock-in')
        verbose_name_plural = _(u'Genetic modifications - Gene knock-in')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class GeneticModificationIsogenic(models.Model):

    cell_line = models.OneToOneField('Cellline', verbose_name=_(u'Cell line'), related_name='genetic_modification_isogenic')
    target_locus = models.ManyToManyField(Molecule, blank=True)
    change_type = models.CharField(_(u'Type of change'), max_length=45, null=True, blank=True)
    modified_sequence = models.CharField(_(u'Modified sequence'), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Genetic modification - Isogenic modification')
        verbose_name_plural = _(u'Genetic modifications - Isogenic modification')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# TODO Cell line differentation 2


class Germlayer(models.Model):

    germlayer = models.CharField(_(u'Germ layer'), max_length=15, blank=True)

    class Meta:
        verbose_name = _(u'Germ layer')
        verbose_name_plural = _(u'Germ layers')
        ordering = ['germlayer']

    def __unicode__(self):
        return u'%s' % (self.germlayer,)


class Marker(models.Model):

    name = models.CharField(_(u'Marker'), max_length=20, blank=True)

    class Meta:
        verbose_name = _(u'Marker')
        verbose_name_plural = _(u'Markers')
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Morphologymethod(models.Model):

    morphologymethod = models.CharField(_(u'Morphology method'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Morphology method')
        verbose_name_plural = _(u'Morphology methods')
        ordering = ['morphologymethod']

    def __unicode__(self):
        return u'%s' % (self.morphologymethod,)


class CellLineMarker(models.Model):

    cell_line = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'))

    marker = models.ForeignKey('Marker', verbose_name=_(u'Marker'), null=True, blank=True)
    morphology_method = models.ForeignKey('Morphologymethod', verbose_name=_(u'Morphology method'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line marker')
        verbose_name_plural = _(u'Cell line markers')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class CellLineDifferentiationPotency(models.Model):

    cell_line = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), null=True, blank=True)

    passage_number = models.CharField(_(u'Passage number'), max_length=5, blank=True)
    germ_layer = models.ForeignKey('Germlayer', verbose_name=_(u'Germ layer'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line differentiation potency')
        verbose_name_plural = _(u'Cell line differentiation potencies')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class CellLineDifferentiationPotencyMarker(models.Model):

    cell_line_differentiation_potency = models.ForeignKey('CellLineDifferentiationPotency', verbose_name=_(u'Cell line differentiation potency'), null=True, blank=True)
    morphology_method = models.ForeignKey('Morphologymethod', verbose_name=_(u'Morphology method'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line differentiation potency marker')
        verbose_name_plural = _(u'Cell line differentiation potency markers')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class CellLineDifferentiationPotencyMolecule(models.Model):

    cell_line_differentiation_potency_marker = models.ForeignKey('CellLineDifferentiationPotencyMarker', verbose_name=_(u'Cell line differentiation potency marker'), null=True, blank=True)
    molecule = models.ForeignKey('Molecule', verbose_name=_(u'Molecule'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line differentiation potency molecule')
        verbose_name_plural = _(u'Cell line differentiation potency molecules')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


# -----------------------------------------------------------------------------
