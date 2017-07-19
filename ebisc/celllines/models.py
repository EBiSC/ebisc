import os
import uuid
import datetime
from dirtyfields import DirtyFieldsMixin

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
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

    name = models.CharField(_(u'Cell type'), max_length=300, unique=True)
    purl = models.URLField(_(u'Purl'), max_length=500, null=True, blank=True)

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

    name = models.CharField(u'name', max_length=200)
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

    VALIDATION_CHOICES = (
        ('1', _(u'Validated, visible')),
        ('2', _(u'Validated, not visible')),
        ('3', _(u'Unvalidated')),
        ('5', _(u'Name registered, no data')),
    )

    validated = models.CharField(_(u'Cell line data validation'), max_length=50, choices=VALIDATION_CHOICES, default='5')
    available_for_sale = models.NullBooleanField(_(u'Available for sale'))
    available_for_sale_at_ecacc = models.BooleanField(_(u'Available for sale on ECACC'), default=False)
    current_status = models.ForeignKey('CelllineStatus', null=True, blank=True)

    name = models.CharField(_(u'Cell line name'), unique=True, max_length=16)
    alternative_names = models.CharField(_(u'Cell line alternative names'), max_length=500, null=True, blank=True)

    biosamples_id = models.CharField(_(u'Biosamples ID'), unique=True, max_length=100)
    hescreg_id = models.CharField(_(u'hESCreg ID'), unique=True, max_length=10, null=True, blank=True)
    ecacc_id = models.CharField(_(u'ECACC ID'), unique=True, max_length=10, null=True, blank=True)

    donor = models.ForeignKey('Donor', verbose_name=_(u'Donor'), null=True, blank=True)
    donor_age = models.ForeignKey(AgeRange, verbose_name=_(u'Age'), null=True, blank=True)

    generator = models.ForeignKey('Organization', verbose_name=_(u'Generator'), related_name='generator_of_cell_lines')
    owner = models.ForeignKey('Organization', verbose_name=_(u'Owner'), null=True, blank=True, related_name='owner_of_cell_lines')
    derivation_country = models.ForeignKey('Country', verbose_name=_(u'Derivation country'), null=True, blank=True)

    has_diseases = models.NullBooleanField(_(u'Has diseases'))
    disease_associated_phenotypes = ArrayField(models.CharField(max_length=500), verbose_name=_(u'Disease associated phenotypes'), null=True, blank=True)
    non_disease_associated_phenotypes = ArrayField(models.CharField(max_length=700), verbose_name=_(u'Non-disease associated phenotypes'), null=True, blank=True)

    has_genetic_modification = models.NullBooleanField(_(u'Genetic modification flag'))

    derived_from = models.ForeignKey('Cellline', verbose_name=_(u'Derived from cell line'), null=True, blank=True, related_name='derived_cell_lines')
    comparator_cell_line = models.ForeignKey('Cellline', verbose_name=_(u'Comparator cell line'), null=True, blank=True, related_name='comparator_cell_lines')
    comparator_cell_line_relation = models.CharField(_(u'Comparator cell line relation'), max_length=100, null=True, blank=True)

    access_and_use_agreement = models.FileField(_(u'Access and use agreement (AUA)'), upload_to=upload_to, null=True, blank=True)
    access_and_use_agreement_md5 = models.CharField(_(u'Access and use agreement md5'), max_length=100, null=True, blank=True)

    access_and_use_agreement_participant = models.FileField(_(u'Access and use agreement for participants (prAUA)'), upload_to=upload_to, null=True, blank=True)
    access_and_use_agreement_participant_md5 = models.CharField(_(u'Access and use agreement for participants md5'), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line')
        verbose_name_plural = _(u'Cell lines')
        ordering = ['name']

    def __unicode__(self):
        return u'%s' % (self.biosamples_id,)

    @property
    def ecacc_url(self):
        return 'http://www.phe-culturecollections.org.uk/products/celllines/ipsc/detail.jsp?refId=%s&collection=ecacc_ipsc' % self.ecacc_id

    @property
    def primary_disease(self):
        diseases = []

        # Check if any donor/cell line diseases are primary
        if self.donor:
            for disease in self.donor.diseases.all():
                if disease.primary_disease is True:
                    return disease
                else:
                    diseases.append(disease)

        for disease in self.diseases.all():
            if disease.primary_disease is True:
                return disease
            else:
                diseases.append(disease)

        # If not, return the first one that is not 'normal' on the list
        if diseases == []:
            return None
        else:
            for ds in diseases:
                if ds.disease and ds.disease.xpurl != 'http://purl.obolibrary.org/obo/PATO_0000461':
                    return ds
            return diseases[0]

    @property
    def donor_diseases(self):

        donor_diseases = []

        if self.donor:
            for disease in self.donor.diseases.all():
                if disease.disease:
                    donor_diseases.append(disease.disease.name)

        return donor_diseases

    @property
    def cellline_diseases(self):

        cellline_diseases = []

        for disease in self.diseases.all():
            if disease.disease:
                cellline_diseases.append(disease.disease.name)

        return cellline_diseases

    @property
    def all_genes(self):

        genes = []

        for disease in self.diseases.all():
            for mod in disease.genetic_modification_cellline_disease_gene_knock_out.all():
                if mod.gene:
                    genes.append(mod.gene.name)
            for mod in disease.genetic_modification_cellline_disease_gene_knock_in.all():
                if mod.target_gene:
                    genes.append(mod.target_gene.name)
                if mod.transgene:
                    genes.append(mod.transgene.name)
            for mod in disease.genetic_modification_cellline_disease_transgene_expression.all():
                if mod.gene:
                    genes.append(mod.gene.name)
            for mod in disease.genetic_modification_cellline_disease_isogenic.all():
                if mod.gene:
                    genes.append(mod.gene.name)
            for variant in disease.genetic_modification_cellline_disease_variants.all():
                if mod.gene:
                    genes.append(variant.gene.name)
        if self.donor:
            for disease in self.donor.diseases.all():
                for variant in disease.donor_disease_variants.all():
                    if variant.gene:
                        genes.append(variant.gene.name)
        for mod in self.genetic_modification_cellline_gene_knock_out.all():
            if mod.gene:
                genes.append(mod.gene.name)
        for mod in self.genetic_modification_cellline_gene_knock_in.all():
            if mod.target_gene:
                genes.append(mod.target_gene.name)
            if mod.transgene:
                genes.append(mod.transgene.name)
        for mod in self.genetic_modification_cellline_transgene_expression.all():
            if mod.gene:
                genes.append(mod.gene.name)
        for mod in self.genetic_modification_cellline_isogenic.all():
            if mod.gene:
                genes.append(mod.gene.name)
        for variant in self.genetic_modification_cellline_variants.all():
            if variant.gene:
                genes.append(variant.gene.name)

        return genes

    @property
    def all_diseases(self):

        return list(set(self.donor_diseases + self.cellline_diseases))

    def to_elastic(self):

        '''
        Facets
        - Disease
        - Donor sex
        - Donor age
        - Primary cell type
        - Depositor

        Searching
        - Disease
        - Donor sex
        - Primary cell type
        - Depositor
        - Alternative name
        - Biosamples ID
        '''

        return {
            'biosamples_id': self.biosamples_id,
            'name': self.name,
            'primary_disease': self.primary_disease.disease.name if self.primary_disease.disease else None,
            'donor_disease': self.donor_diseases if self.donor_diseases else None,
            'genetic_modification_disease': self.cellline_diseases if self.cellline_diseases else _(u'/'),
            'all_diseases': self.all_diseases if self.all_diseases else None,
            'primary_disease_synonyms': [s.strip() for s in self.primary_disease.disease.synonyms.split(',')] if self.primary_disease and self.primary_disease.disease.synonyms else None,
            'disease_associated_phenotypes': self.disease_associated_phenotypes if self.disease_associated_phenotypes else None,
            'non_disease_associated_phenotypes': self.non_disease_associated_phenotypes if self.non_disease_associated_phenotypes else None,
            'depositor': self.generator.name,
            'primary_cell_type': self.derivation.primary_cell_type.name if self.derivation.primary_cell_type else None,
            'alternative_names': self.alternative_names,
            'donor_sex': self.donor.gender.name if self.donor and self.donor.gender else _(u'Not known'),
            'donor_age': self.donor_age.name if self.donor_age else None,
            'all_genes': self.all_genes if self.all_genes else None,
        }

    def get_latest_batch(self):
        batches = self.batches.all()
        active_batch_ids = []

        if batches:
            for batch in batches:
                if batch.batch_id and not batch.batch_id.startswith('SAME'):
                    active_batch_ids.append(batch.batch_id)

            if active_batch_ids:
                latest_batch_id = sorted(active_batch_ids, lambda a, b: cmp(int(b[1:]), int(a[1:])) != 0 or cmp(a[0], b[0]))[0]
                return self.batches.get(batch_id=latest_batch_id)
            else:
                return None

        else:
            return None

    def get_latest_clip(self):
        clips = self.clips.all()
        clips_versions = []

        if clips:
            for clip in clips:
                clips_versions.append(clip.version)

            if clips_versions:
                latest_version = sorted(clips_versions, lambda a, b: cmp(int(b[1:]), int(a[1:])) != 0 or cmp(a[0], b[0]))[0]
                return self.clips.get(version=latest_version)
            else:
                return None

        else:
            return None


class CelllineStatus(models.Model):

    STATUS_CHOICES = (
        ('not_available', _(u'Not available')),
        ('at_ecacc', _(u'Stocked by ECACC')),
        ('expand_to_order', _(u'Expand to order')),
        ('restricted_distribution', _(u'Restricted distribution')),
        ('recalled', _(u'Recalled')),
        ('withdrawn', _(u'Withdrawn')),
    )

    cell_line = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), related_name='statuses')

    status = models.CharField(_(u'Status'), max_length=50, choices=STATUS_CHOICES, default='not_available')
    comment = models.TextField(_(u'Comment'), null=True, blank=True, help_text='Optional unless you are recalling or withdrawing a line. In that case you must provide a reason for the recall/withdrawal.')

    user = models.ForeignKey(User, null=True, blank=True)
    updated = models.DateTimeField(u'Updated', auto_now=True)

    class Meta:
        verbose_name = _(u'Cell line status')
        verbose_name_plural = _(u'Cell line statuses')
        ordering = ['-updated']

    def __unicode__(self):
        return self.status

    def save(self, *args, **kwargs):
        super(CelllineStatus, self).save(*args, **kwargs)
        self.cell_line.current_status = self
        self.cell_line.save()

    def delete(self, *args, **kwargs):
        if self.cell_line.current_status == self:
            self.cell_line.current_status = None
            self.cell_line.save()
        super(CelllineStatus, self).delete(*args, **kwargs)


class CelllineInformationPack(models.Model):

    cell_line = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), related_name='clips')

    version = models.CharField(_(u'CLIP version'), max_length=10, help_text='e.g. "v1"')
    created = models.DateTimeField(u'Created', auto_now_add=True)
    updated = models.DateTimeField(u'Updated', auto_now=True)

    clip_file = models.FileField(_(u'CLIP file'), upload_to=upload_to, help_text='File name e.g. "UKBi005-A.CLIP.v1.pdf"')
    md5 = models.CharField(_(u'CLIP md5'), max_length=100)

    class Meta:
        verbose_name = _(u'Cell line information pack')
        verbose_name_plural = _(u'Cell line information packs')
        ordering = ['-updated']
        unique_together = (('cell_line', 'version'))

    def __unicode__(self):
        return u'%s' % (self.id,)

    def filename(self):
        return os.path.basename(self.clip_file.name)


# -----------------------------------------------------------------------------
# Batch: Cellline -> Batch(es) -> Aliquot(s)

class CelllineBatch(models.Model):

    BATCH_TYPE_CHOICES = (
        ('depositor', _(u'Depositor Expansion')),
        ('central_facility', _(u'Central Facility Expansion')),
        ('unknown', _(u'Unknown')),
    )

    cell_line = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), related_name='batches')
    biosamples_id = models.CharField(_(u'Biosamples ID'), max_length=100, unique=True)

    batch_id = models.CharField(_(u'Batch ID'), max_length=12)
    batch_type = models.CharField(_(u'Batch type'), max_length=50, choices=BATCH_TYPE_CHOICES, default='unknown')

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
    image = models.ImageField(_(u'Image'), upload_to=upload_to)
    md5 = models.CharField(_(u'MD5'), max_length=100)
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
    biosamples_id = models.CharField(_(u'Biosamples ID'), max_length=100, unique=True)
    name = models.CharField(_(u'Name'), max_length=50, null=True, blank=True)
    number = models.CharField(_(u'Number'), max_length=10, null=True, blank=True)
    derived_from = models.CharField(_(u'Biosamples ID of sample from which the vial was derived'), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line aliquot')
        verbose_name_plural = _(u'Cell line aliquotes')
        ordering = ['name']

    def __unicode__(self):
        return u'%s' % (self.biosamples_id,)


# -----------------------------------------------------------------------------
# Donor

class Donor(DirtyFieldsMixin, models.Model):

    biosamples_id = models.CharField(_(u'Biosamples ID'), max_length=100, unique=True)
    gender = models.ForeignKey(Gender, verbose_name=_(u'Gender'), null=True, blank=True)

    provider_donor_ids = ArrayField(models.CharField(max_length=200), verbose_name=_(u'Provider donor ids'), null=True)
    country_of_origin = models.ForeignKey('Country', verbose_name=_(u'Country of origin'), null=True, blank=True)
    ethnicity = models.CharField(_(u'Ethnicity'), max_length=100, null=True, blank=True)
    family_history = models.CharField(_(u'Family history'), max_length=500, null=True, blank=True)
    medical_history = models.CharField(_(u'Medical history'), max_length=500, null=True, blank=True)
    clinical_information = models.CharField(_(u'Clinical information'), max_length=500, null=True, blank=True)

    karyotype = models.CharField(_(u'Karyotype'), max_length=500, null=True, blank=True)
    karyotype_method = models.CharField(_(u'Karyotype method'), max_length=100, null=True, blank=True)
    karyotype_file = models.FileField(_(u'File'), upload_to=upload_to, null=True, blank=True)
    karyotype_file_enc = models.CharField(_(u'File enc'), max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Donor')
        verbose_name_plural = _(u'Donors')
        ordering = ['biosamples_id']

    def __unicode__(self):
        return u'%s' % (self.biosamples_id,)


class DonorGenomeAnalysis(DirtyFieldsMixin, models.Model):

    donor = models.ForeignKey('Donor', verbose_name=_(u'Donor'), related_name='donor_genome_analysis')
    analysis_method = models.CharField(_(u'Analysis method'), max_length=300, null=True, blank=True)
    link = models.URLField(u'Link', null=True, blank=True)

    class Meta:
        verbose_name = _(u'Donor genome analysis')
        verbose_name_plural = _(u'Donor genome analysis')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class DonorGenomeAnalysisFile(models.Model):

    genome_analysis = models.ForeignKey('DonorGenomeAnalysis', verbose_name=_(u'Donor genome analysis'), related_name='donor_genome_analysis_files')
    vcf_file = models.FileField(_(u'VCF File'), upload_to=upload_to)
    vcf_file_enc = models.CharField(_(u'VCF File enc'), max_length=300)
    vcf_file_description = models.CharField(_(u'VCF File description'), max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Donor genome analysis file')
        verbose_name_plural = _(u'Donor genome analysis files')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


# -----------------------------------------------------------------------------
# Disease

class Disease(models.Model):

    # purl = models.URLField(_(u'Purl'), unique=True)
    xpurl = models.URLField(_(u'Purl'))
    name = models.CharField(_(u'Name'), max_length=200, null=True, blank=True)
    synonyms = models.CharField(_(u'Synonyms'), max_length=2000, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Disease')
        verbose_name_plural = _(u'Diseases')
        ordering = ['xpurl']

    def __unicode__(self):
        return u'%s' % self.xpurl


class Variant(models.Model):

    gene = models.ForeignKey(Molecule, verbose_name=_(u'Gene'), related_name='variant_gene', null=True, blank=True)

    chromosome_location = models.CharField(_(u'Chromosome location'), max_length=500, null=True, blank=True)
    nucleotide_sequence_hgvs = models.CharField(_(u'Nucleotide sequence HGSV'), max_length=1000, null=True, blank=True)
    protein_sequence_hgvs = models.CharField(_(u'Protein sequence HGSV'), max_length=1000, null=True, blank=True)
    zygosity_status = models.CharField(_(u'Zygosity status'), max_length=200, null=True, blank=True)
    clinvar_id = models.CharField(_(u'ClinVar ID'), max_length=200, null=True, blank=True)
    dbsnp_id = models.CharField(_(u'dbSNP ID'), max_length=200, null=True, blank=True)
    dbvar_id = models.CharField(_(u'dbVar ID'), max_length=200, null=True, blank=True)
    publication_pmid = models.CharField(_(u'PubMed ID'), max_length=200, null=True, blank=True)
    notes = models.CharField(_(u'Brief explanation'), max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Variant')
        verbose_name_plural = _(u'Variants')
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.id,)


# Donor diseases and disease variants
class DonorDisease(models.Model):

    donor = models.ForeignKey(Donor, verbose_name=_(u'Donor'), related_name='diseases')
    disease = models.ForeignKey('Disease', verbose_name=_(u'Diagnosed disease'), null=True, blank=True)
    disease_not_normalised = models.CharField(_(u'Disease name - not normalised'), max_length=500, null=True, blank=True)

    primary_disease = models.BooleanField(_(u'Primary disease'), default=False)

    disease_stage = models.CharField(_(u'Disease stage'), max_length=1000, null=True, blank=True)
    affected_status = models.CharField(_(u'Affected status'), max_length=12, null=True, blank=True)
    carrier = models.CharField(_(u'Carrier'), max_length=12, null=True, blank=True)

    notes = models.TextField(_(u'Notes'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Donor disease')
        verbose_name_plural = _(u'Donor diseases')
        unique_together = [('donor', 'disease', 'disease_not_normalised')]
        ordering = ['disease']

    def __unicode__(self):
        return u'%s - %s' % (self.donor, self.disease)


class DonorDiseaseVariant(DirtyFieldsMixin, Variant):

    variant_id = models.IntegerField(_(u'Variant ID'), null=True, blank=True)
    donor_disease = models.ForeignKey(DonorDisease, verbose_name=_(u'Donor disease'), related_name="donor_disease_variants")

    class Meta:
        verbose_name = _(u'Donor disease variant')
        verbose_name_plural = _(u'Donor disease variants')
        unique_together = [('donor_disease', 'variant_id')]
        ordering = ['donor_disease']

    def __unicode__(self):
        return u'%s' % (self.donor_disease,)


# Genetic modifications (associated and not associated to diseases)
class CelllineDisease(models.Model):

    cell_line = models.ForeignKey(Cellline, verbose_name=_(u'Cell line'), related_name='diseases')
    disease = models.ForeignKey('Disease', verbose_name=_(u'Diagnosed disease'), null=True, blank=True)
    disease_not_normalised = models.CharField(_(u'Disease name - not normalised'), max_length=500, null=True, blank=True)
    primary_disease = models.BooleanField(_(u'Primary disease'), default=False)
    notes = models.TextField(_(u'Notes'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line disease')
        verbose_name_plural = _(u'Cell line diseases')
        unique_together = [('cell_line', 'disease', 'disease_not_normalised')]
        ordering = ['disease']

    def __unicode__(self):
        return u'%s - %s' % (self.cell_line, self.disease)


class ModificationVariantDisease(DirtyFieldsMixin, Variant):

    modification_id = models.IntegerField(_(u'Modification ID'), null=True, blank=True)
    cellline_disease = models.ForeignKey(CelllineDisease, verbose_name=_(u'Cell line disease'), related_name="genetic_modification_cellline_disease_variants")

    class Meta:
        verbose_name = _(u'Genetic modification - Disease associated variant')
        verbose_name_plural = _(u'Genetic modifications - Disease associated variants')
        unique_together = [('cellline_disease', 'modification_id')]
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.id,)


class ModificationVariantNonDisease(DirtyFieldsMixin, Variant):

    modification_id = models.IntegerField(_(u'Modification ID'), null=True, blank=True)
    cell_line = models.ForeignKey(Cellline, verbose_name=_(u'Cell line'), related_name="genetic_modification_cellline_variants")

    class Meta:
        verbose_name = _(u'Genetic modification - Variant non disease')
        verbose_name_plural = _(u'Genetic modifications - Variant non disease')
        unique_together = [('cell_line', 'modification_id')]
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.id,)


class ModificationIsogenic(models.Model):

    gene = models.ForeignKey(Molecule, verbose_name=_(u'Gene'), related_name='modification_isogenic_gene', null=True, blank=True)

    chromosome_location = models.CharField(_(u'Chromosome location'), max_length=500, null=True, blank=True)
    nucleotide_sequence_hgvs = models.CharField(_(u'Nucleotide sequence HGSV'), max_length=1000, null=True, blank=True)
    protein_sequence_hgvs = models.CharField(_(u'Protein sequence HGSV'), max_length=1000, null=True, blank=True)
    zygosity_status = models.CharField(_(u'Zygosity status'), max_length=200, null=True, blank=True)
    modification_type = models.CharField(_(u'Target locus modification type'), max_length=1000, null=True, blank=True)
    notes = models.CharField(_(u'Brief explanation'), max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Genetic modification - Isogenic modification')
        verbose_name_plural = _(u'Genetic modifications - Isogenic modification')
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.id,)


class ModificationIsogenicDisease(DirtyFieldsMixin, ModificationIsogenic):

    modification_id = models.IntegerField(_(u'Modification ID'), null=True, blank=True)
    cellline_disease = models.ForeignKey(CelllineDisease, verbose_name=_(u'Cell line disease'), related_name="genetic_modification_cellline_disease_isogenic")

    class Meta:
        verbose_name = _(u'Genetic modification - Isogenic modification disease related')
        verbose_name_plural = _(u'Genetic modifications - Isogenic modification disease related')
        unique_together = [('cellline_disease', 'modification_id')]
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.id,)


class ModificationIsogenicNonDisease(DirtyFieldsMixin, ModificationIsogenic):

    modification_id = models.IntegerField(_(u'Modification ID'), null=True, blank=True)
    cell_line = models.ForeignKey(Cellline, verbose_name=_(u'Cell line'), related_name='genetic_modification_cellline_isogenic')

    class Meta:
        verbose_name = _(u'Genetic modification - Isogenic modification non disease')
        verbose_name_plural = _(u'Genetic modifications - Isogenic modification non disease')
        unique_together = [('cell_line', 'modification_id')]
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.id,)


class ModificationTransgeneExpression(models.Model):

    gene = models.ForeignKey(Molecule, verbose_name=_(u'Gene'), related_name='modification_transgene_expression_gene', null=True, blank=True)

    chromosome_location = models.CharField(_(u'Chromosome location'), max_length=500, null=True, blank=True)
    delivery_method = models.CharField(_(u'Delivery method'), max_length=1000, null=True, blank=True)
    virus = models.ForeignKey(Virus, verbose_name=_(u'Virus'), null=True, blank=True)
    transposon = models.ForeignKey(Transposon, verbose_name=_(u'Transposon'), null=True, blank=True)
    notes = models.CharField(_(u'Brief explanation'), max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Genetic modification - Transgene expression')
        verbose_name_plural = _(u'Genetic modifications - Transgene expression')
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.id,)


class ModificationTransgeneExpressionDisease(DirtyFieldsMixin, ModificationTransgeneExpression):

    modification_id = models.IntegerField(_(u'Modification ID'), null=True, blank=True)
    cellline_disease = models.ForeignKey(CelllineDisease, verbose_name=_(u'Cell line disease'), related_name="genetic_modification_cellline_disease_transgene_expression")

    class Meta:
        verbose_name = _(u'Genetic modification - Transgene expression disease related')
        verbose_name_plural = _(u'Genetic modifications - Transgene expression disease related')
        unique_together = [('cellline_disease', 'modification_id')]
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.id,)


class ModificationTransgeneExpressionNonDisease(DirtyFieldsMixin, ModificationTransgeneExpression):

    modification_id = models.IntegerField(_(u'Modification ID'), null=True, blank=True)
    cell_line = models.ForeignKey(Cellline, verbose_name=_(u'Cell line'), related_name='genetic_modification_cellline_transgene_expression')

    class Meta:
        verbose_name = _(u'Genetic modification - Transgene expression non disease')
        verbose_name_plural = _(u'Genetic modifications - Transgene expression non disease')
        unique_together = [('cell_line', 'modification_id')]
        ordering = ['gene']

    def __unicode__(self):
        return u'%s' % (self.id,)


class ModificationGeneKnockOut(models.Model):

    gene = models.ForeignKey(Molecule, verbose_name=_(u'Gene'), related_name='modification_gene_knock_out_gene', null=True, blank=True)

    chromosome_location = models.CharField(_(u'Chromosome location'), max_length=500, null=True, blank=True)
    delivery_method = models.CharField(_(u'Delivery method'), max_length=200, null=True, blank=True)
    virus = models.ForeignKey(Virus, verbose_name=_(u'Virus'), null=True, blank=True)
    transposon = models.ForeignKey(Transposon, verbose_name=_(u'Transposon'), null=True, blank=True)
    notes = models.CharField(_(u'Brief explanation'), max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Genetic modification - Gene knock-out')
        verbose_name_plural = _(u'Genetic modifications - Gene knock-out')
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.id,)


class ModificationGeneKnockOutDisease(DirtyFieldsMixin, ModificationGeneKnockOut):

    modification_id = models.IntegerField(_(u'Modification ID'), null=True, blank=True)
    cellline_disease = models.ForeignKey(CelllineDisease, verbose_name=_(u'Cell line disease'), related_name="genetic_modification_cellline_disease_gene_knock_out")

    class Meta:
        verbose_name = _(u'Genetic modification - Gene knock-out disease related')
        verbose_name_plural = _(u'Genetic modifications - Gene knock-out disease related')
        unique_together = [('cellline_disease', 'modification_id')]
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.id,)


class ModificationGeneKnockOutNonDisease(DirtyFieldsMixin, ModificationGeneKnockOut):

    modification_id = models.IntegerField(_(u'Modification ID'), null=True, blank=True)
    cell_line = models.ForeignKey(Cellline, verbose_name=_(u'Cell line'), related_name='genetic_modification_cellline_gene_knock_out')

    class Meta:
        verbose_name = _(u'Genetic modification - Gene knock-out non disease')
        verbose_name_plural = _(u'Genetic modifications - Gene knock-out non disease')
        unique_together = [('cell_line', 'modification_id')]
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.id,)


class ModificationGeneKnockIn(models.Model):

    target_gene = models.ForeignKey(Molecule, verbose_name=_(u'Target gene'), related_name='modification_gene_knock_in_target_gene', null=True, blank=True)
    chromosome_location = models.CharField(_(u'Chromosome location - target gene'), max_length=500, null=True, blank=True)

    transgene = models.ForeignKey(Molecule, verbose_name=_(u'Transgene'), related_name='modification_gene_knock_in_transgene', null=True, blank=True)
    chromosome_location_transgene = models.CharField(_(u'Chromosome location - transgene'), max_length=500, null=True, blank=True)

    delivery_method = models.CharField(_(u'Delivery method'), max_length=200, null=True, blank=True)
    virus = models.ForeignKey(Virus, verbose_name=_(u'Virus'), null=True, blank=True)
    transposon = models.ForeignKey(Transposon, verbose_name=_(u'Transposon'), null=True, blank=True)
    notes = models.CharField(_(u'Brief explanation'), max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Genetic modification - Gene knock-in')
        verbose_name_plural = _(u'Genetic modifications - Gene knock-in')
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.id,)


class ModificationGeneKnockInDisease(DirtyFieldsMixin, ModificationGeneKnockIn):

    modification_id = models.IntegerField(_(u'Modification ID'), null=True, blank=True)
    cellline_disease = models.ForeignKey(CelllineDisease, verbose_name=_(u'Cell line disease'), related_name="genetic_modification_cellline_disease_gene_knock_in")

    class Meta:
        verbose_name = _(u'Genetic modification - Gene knock-in disease related')
        verbose_name_plural = _(u'Genetic modifications - Gene knock-in disease related')
        unique_together = [('cellline_disease', 'modification_id')]
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.id,)


class ModificationGeneKnockInNonDisease(DirtyFieldsMixin, ModificationGeneKnockIn):

    modification_id = models.IntegerField(_(u'Modification ID'), null=True, blank=True)
    cell_line = models.ForeignKey(Cellline, verbose_name=_(u'Cell line'), related_name='genetic_modification_cellline_gene_knock_in')

    class Meta:
        verbose_name = _(u'Genetic modification - Gene knock-in non disease')
        verbose_name_plural = _(u'Genetic modifications - Gene knock-in non disease')
        unique_together = [('cell_line', 'modification_id')]
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.id,)


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

    passage_number_banked = models.CharField(_(u'Passage number banked (pre-EBiSC)'), max_length=100, null=True, blank=True)
    number_of_vials_banked = models.CharField(_(u'No. Vials banked (pre-EBiSC)'), max_length=10, null=True, blank=True)
    passage_history = models.NullBooleanField(_(u'Passage history (back to reprogramming)'), default=None, null=True, blank=True)
    culture_history = models.NullBooleanField(_(u'Culture history (methods used)'), default=None, null=True, blank=True)

    rock_inhibitor_used_at_passage = models.CharField(u'Rock inhibitor (Y27632) used at passage', max_length=10, choices=EXTENDED_BOOL_CHOICES, default='unknown')
    rock_inhibitor_used_at_cryo = models.CharField(u'Rock inhibitor (Y27632) used at cryo', max_length=10, choices=EXTENDED_BOOL_CHOICES, default='unknown')
    rock_inhibitor_used_at_thaw = models.CharField(u'Rock inhibitor (Y27632) used at thaw', max_length=10, choices=EXTENDED_BOOL_CHOICES, default='unknown')

    class Meta:
        verbose_name = _(u'Cell line culture conditions')
        verbose_name_plural = _(u'Cell line culture conditions')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class BatchCultureConditions(DirtyFieldsMixin, models.Model):

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

    base = models.CharField(_(u'Culture medium base'), max_length=200, blank=True)
    protein_source = models.CharField(_(u'Protein source'), max_length=200, null=True, blank=True)
    serum_concentration = models.IntegerField(_(u'Serum concentration'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Culture medium')
        verbose_name_plural = _(u'Culture mediums')
        ordering = ['base', 'protein_source', 'serum_concentration']

    def __unicode__(self):
        return u'%s / %s / %s' % (self.base, self.protein_source, self.serum_concentration)


class CelllineCultureMediumSupplement(DirtyFieldsMixin, models.Model):

    cell_line_culture_conditions = models.ForeignKey(CelllineCultureConditions, verbose_name=_(u'Cell line culture conditions'), related_name='medium_supplements')

    supplement = models.CharField(_(u'Supplement'), max_length=200)
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
    primary_cell_type_not_normalised = models.CharField(_(u'Primary cell type name - not normalised'), max_length=100, null=True, blank=True)
    primary_cell_developmental_stage = models.CharField(_(u'Primary cell developmental stage'), max_length=45, null=True, blank=True)
    tissue_procurement_location = models.CharField(_(u'Location of primary tissue procurement'), max_length=200, null=True, blank=True)
    tissue_collection_date = models.DateField(_(u'Tissue collection date'), null=True, blank=True)
    reprogramming_passage_number = models.CharField(_(u'Passage number reprogrammed'), max_length=100, null=True, blank=True)

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

    detectable = models.CharField(u'Is reprogramming vector detectable', max_length=10, choices=EXTENDED_BOOL_CHOICES, default='unknown')
    methods = ArrayField(models.CharField(max_length=200), verbose_name=_(u'Methods used'), null=True, blank=True)
    detectable_notes = models.TextField(u'Notes on reprogramming vector detection', null=True, blank=True)

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

    silenced = models.CharField(u'Have the reprogramming vectors been silenced', max_length=10, choices=EXTENDED_BOOL_CHOICES, default='unknown')
    methods = ArrayField(models.CharField(max_length=200), verbose_name=_(u'Methods used'), null=True, blank=True)
    silenced_notes = models.TextField(u'Notes on reprogramming vector silencing', null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line integrating vector')
        verbose_name_plural = _(u'Cell line integrating vectors')

    def __unicode__(self):
        return unicode(self.vector)


class VectorFreeReprogrammingFactor(models.Model):

    name = models.CharField(_(u'Vector free reprogram factor'), max_length=200, unique=True)

    class Meta:
        verbose_name = _(u'Vector free reprogram factor')
        verbose_name_plural = _(u'Vector free reprogram factors')
        ordering = ['name']

    def __unicode__(self):
        return u'%s' % (self.name,)


class CelllineVectorFreeReprogrammingFactors(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'), related_name='vector_free_reprogramming_factors')
    factors = models.ManyToManyField(VectorFreeReprogrammingFactor, verbose_name=_(u'Vector-free reprogramming factor'), blank=True)

    class Meta:
        verbose_name = _(u'Cell line Vector-free Programming Factor')
        verbose_name_plural = _(u'Cell line Vector-free Programming Factors')

    def __unicode__(self):
        return u'%s' % (self.id,)


# -----------------------------------------------------------------------------
# Cell line Characterization

# Microbiology/Virology Screening

class CelllineCharacterization(DirtyFieldsMixin, models.Model):

    SCREENING_CHOICES = (
        ('positive', u'Positive'),
        ('negative', u'Negative'),
        ('not_done', u'Not done'),
    )

    cell_line = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'))

    certificate_of_analysis_flag = models.NullBooleanField(_(u'Certificate of analysis flag'))
    certificate_of_analysis_passage_number = models.CharField(_(u'Certificate of analysis passage number'), max_length=10, null=True, blank=True)

    virology_screening_flag = models.NullBooleanField(_(u'Virology screening flag'))
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


# Analysis of Undifferentiated Cells

# Depositor provided files
class DepositorDataFile(models.Model):

    file_doc = models.FileField(_(u'File'), upload_to=upload_to, null=True, blank=True)
    file_enc = models.CharField(_(u'File enc'), max_length=300, null=True, blank=True)
    file_description = models.TextField(_(u'File description'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Depositor data file')
        verbose_name_plural = _(u'Depositor data files')
        ordering = ['file_enc']

    def __unicode__(self):
        return unicode(self.id)

    def filename(self):
        return os.path.basename(self.file_doc.name)

    def extension(self):
        name, extension = os.path.splitext(self.file_doc.name)
        return extension


# Marker expression
class CelllineCharacterizationMarkerExpression(DirtyFieldsMixin, models.Model):

    cell_line = models.ForeignKey(Cellline, verbose_name=_(u'Cell line'), related_name='undifferentiated_marker_expression')

    marker_id = models.IntegerField(_(u'Marker ID'), default=0)
    marker = models.CharField(_(u'Marker'), max_length=100)
    expressed = models.NullBooleanField(_(u'Expressed'))

    class Meta:
        verbose_name = _(u'Undifferentiated cells - marker expression')
        verbose_name_plural = _(u'Undifferentiated cells - marker expressions')
        ordering = ['cell_line']

    def __unicode__(self):
        return '%s (%s)' % (self.marker, self.cell_line)


class CelllineCharacterizationMarkerExpressionMethod(DirtyFieldsMixin, models.Model):

    marker_expression = models.ForeignKey(CelllineCharacterizationMarkerExpression, verbose_name=_(u'Marker expression'), related_name='marker_expression_method')

    name = models.CharField(_(u'Method name'), max_length=500)

    class Meta:
        verbose_name = _(u'Marker expression method')
        verbose_name_plural = _(u'Marker expression methods')
        ordering = ['name']

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.marker_expression)


class CelllineCharacterizationMarkerExpressionMethodFile(DepositorDataFile):

    marker_expression_method = models.ForeignKey(CelllineCharacterizationMarkerExpressionMethod, verbose_name=_(u'Marker expression method'), related_name='marker_expression_method_files')

    class Meta:
        verbose_name = _(u'Marker expression method file')
        verbose_name_plural = _(u'Marker expression method files')
        ordering = ['marker_expression_method']

    def __unicode__(self):
        return unicode(self.marker_expression_method)


# Morphology images
class CelllineCharacterizationUndifferentiatedMorphologyFile(DepositorDataFile):

    cell_line = models.ForeignKey(Cellline, verbose_name=_(u'Cell line'), related_name='undifferentiated_morphology_files')

    class Meta:
        verbose_name = _(u'Cell line undifferentiated cells morphology file')
        verbose_name_plural = _(u'Cell line undifferentiated cells morphology files')
        ordering = ['cell_line']

    def __unicode__(self):
        return unicode(self.cell_line)


# Pluritest
class CelllineCharacterizationPluritest(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'))

    pluritest_flag = models.NullBooleanField(_(u'Pluritest flag'))
    pluripotency_score = models.CharField(_(u'Pluripotency score'), max_length=10, null=True, blank=True)
    novelty_score = models.CharField(_(u'Novelty score'), max_length=10, null=True, blank=True)
    microarray_url = models.URLField(_(u'Microarray data link'), max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line characterization Pluritest')
        verbose_name_plural = _(u'Cell line characterization Pluritests')
        ordering = ['cell_line']

    def __unicode__(self):
        return unicode(self.cell_line)


class CelllineCharacterizationPluritestFile(DepositorDataFile):

    pluritest = models.ForeignKey(CelllineCharacterizationPluritest, verbose_name=_(u'Cell line pluritest'), related_name='pluritest_files')

    class Meta:
        verbose_name = _(u'Cell line Pluritest file')
        verbose_name_plural = _(u'Cell line Pluritest files')
        ordering = ['pluritest']

    def __unicode__(self):
        return unicode(self.pluritest)


# EpiPluriScore
class CelllineCharacterizationEpipluriscore(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'))

    epipluriscore_flag = models.NullBooleanField(_(u'EpiPluriScore flag'))
    score = models.CharField(_(u'Pluripotency score'), max_length=10, null=True, blank=True)
    marker_mcpg = models.NullBooleanField(_(u'Marker mCpG'))
    marker_OCT4 = models.NullBooleanField(_(u'Marker OCT4'))

    class Meta:
        verbose_name = _(u'Cell line characterization Epipluri score')
        verbose_name_plural = _(u'Cell line characterization Epipluri scores')
        ordering = ['cell_line']

    def __unicode__(self):
        return unicode(self.cell_line)


class CelllineCharacterizationEpipluriscoreFile(DepositorDataFile):

    epipluriscore = models.ForeignKey(CelllineCharacterizationEpipluriscore, verbose_name=_(u'Cell line EpiPluriScore'), related_name='epipluriscore_files')

    class Meta:
        verbose_name = _(u'Cell line EpiPluriScore file')
        verbose_name_plural = _(u'Cell line EpiPluriScore files')
        ordering = ['epipluriscore']

    def __unicode__(self):
        return unicode(self.epipluriscore)


# hPSC Scorecard
class CelllineCharacterizationHpscScorecard(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'))

    self_renewal = models.NullBooleanField(_(u'Self renewal'))
    endoderm = models.NullBooleanField(_(u'Endoderm'))
    mesoderm = models.NullBooleanField(_(u'Mesoderm'))
    ectoderm = models.NullBooleanField(_(u'Ectoderm'))

    class Meta:
        verbose_name = _(u'Cell line hPSC Scorecard')
        verbose_name_plural = _(u'Cell line hPSC Scorecards')
        ordering = ['cell_line']

    def __unicode__(self):
        return unicode(self.cell_line)


class CelllineCharacterizationHpscScorecardReport(DepositorDataFile):

    hpsc_scorecard = models.ForeignKey(CelllineCharacterizationHpscScorecard, verbose_name=_(u'Cell line hPSC Scorecard'), related_name='hpsc_scorecard_reports')

    class Meta:
        verbose_name = _(u'Cell line hPSC Scorecard report')
        verbose_name_plural = _(u'Cell line hPSC Scorecard reports')
        ordering = ['hpsc_scorecard']

    def __unicode__(self):
        return unicode(self.hpsc_scorecard)


class CelllineCharacterizationHpscScorecardScorecard(DepositorDataFile):

    hpsc_scorecard = models.ForeignKey(CelllineCharacterizationHpscScorecard, verbose_name=_(u'Cell line hPSC Scorecard'), related_name='hpsc_scorecard_files')

    class Meta:
        verbose_name = _(u'Cell line hPSC Scorecard scorecard')
        verbose_name_plural = _(u'Cell line hPSC Scorecard scorecards')
        ordering = ['hpsc_scorecard']

    def __unicode__(self):
        return unicode(self.hpsc_scorecard)


# RNA Sequencing
class CelllineCharacterizationRNASequencing(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'))
    data_url = models.CharField(_(u'RNA Sequencing data link'), max_length=500, blank=True, default='')

    class Meta:
        verbose_name = _(u'Link to RNA Sequencing data')
        verbose_name_plural = _(u'Links to RNA Sequencing data')
        ordering = ['data_url']

    def __unicode__(self):
        return u'%s' % (self.data_url,)


# Gene Expression Array
class CelllineCharacterizationGeneExpressionArray(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'))
    data_url = models.CharField(_(u'Gene Expression Array data link'), max_length=500, blank=True, default='')

    class Meta:
        verbose_name = _(u'Link to Gene Expression Array data')
        verbose_name_plural = _(u'Links to Gene Expression Array data')
        ordering = ['data_url']

    def __unicode__(self):
        return u'%s' % (self.data_url,)


# Differentiation potency
class CelllineCharacterizationDifferentiationPotency(DirtyFieldsMixin, models.Model):

    GERMLAYER_CHOICES = (
        ('endoderm', _(u'Endoderm')),
        ('mesoderm', _(u'Mesoderm')),
        ('ectoderm', _(u'Ectoderm')),
    )

    cell_line = models.ForeignKey(Cellline, verbose_name=_(u'Cell line'), related_name='differentiation_potency_germ_layers')
    germ_layer = models.CharField(_(u'Germ layer'), max_length=20, choices=GERMLAYER_CHOICES)

    class Meta:
        verbose_name = _(u'Germ layer')
        verbose_name_plural = _(u'Germ layers')
        ordering = ['germ_layer']

    def __unicode__(self):
        return u'%s' % (self.germ_layer,)


class CelllineCharacterizationDifferentiationPotencyCellType(DirtyFieldsMixin, models.Model):

    germ_layer = models.ForeignKey(CelllineCharacterizationDifferentiationPotency, verbose_name=_(u'Germ layer'), related_name='germ_layer_cell_types')
    name = models.CharField(_(u'Name'), max_length=200, default='')
    in_vivo_teratoma_flag = models.NullBooleanField(_(u'In vivo teratoma'))
    in_vitro_spontaneous_differentiation_flag = models.NullBooleanField(_(u'In vitro spontaneous differentiation'))
    in_vitro_directed_differentiation_flag = models.NullBooleanField(_(u'In vitro directed differentiation'))
    scorecard_flag = models.NullBooleanField(_(u'Scorecard'))
    other_flag = models.NullBooleanField(_(u'Other'))
    transcriptome_data = models.CharField(_(u'Link to transcriptome data'), max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Diferentiation potency cell type')
        verbose_name_plural = _(u'Diferentiation potency cell types')
        ordering = ['name']

    def __unicode__(self):
        return u'%s' % (self.name,)


class CelllineCharacterizationDifferentiationPotencyCellTypeMarker(DirtyFieldsMixin, models.Model):

    cell_type = models.ForeignKey(CelllineCharacterizationDifferentiationPotencyCellType, verbose_name=_(u'Cell type'), related_name='germ_layer_cell_type_markers')
    name = models.CharField(_(u'Name'), max_length=100, default='')
    expressed = models.NullBooleanField(_(u'Expressed'))

    class Meta:
        verbose_name = _(u'Diferentiation potency cell type marker')
        verbose_name_plural = _(u'Diferentiation potency cell type markers')
        ordering = ['name']

    def __unicode__(self):
        return u'%s' % (self.name,)


class CelllineCharacterizationDifferentiationPotencyMorphologyFile(DepositorDataFile):

    cell_type = models.ForeignKey(CelllineCharacterizationDifferentiationPotencyCellType, verbose_name=_(u'Cell type'), related_name='germ_layer_cell_type_morphology_files')

    class Meta:
        verbose_name = _(u'Diferentiation potency cell type morphology file')
        verbose_name_plural = _(u'Diferentiation potency cell type morphology files')
        ordering = ['cell_type']

    def __unicode__(self):
        return u'%s' % (self.cell_type, )


class CelllineCharacterizationDifferentiationPotencyProtocolFile(DepositorDataFile):

    cell_type = models.ForeignKey(CelllineCharacterizationDifferentiationPotencyCellType, verbose_name=_(u'Cell type'), related_name='germ_layer_cell_type_protocol_files')

    class Meta:
        verbose_name = _(u'Diferentiation potency cell type protocol file')
        verbose_name_plural = _(u'Diferentiation potency cell type protocol files')
        ordering = ['cell_type']

    def __unicode__(self):
        return u'%s' % (self.cell_type, )


# Characterisation (Old fields)
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

class UndifferentiatedMorphologyMarkerImune(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=u'Cell line', related_name='undifferentiated_morphology_marker_imune')
    passage_number = models.CharField(u'Passage number', max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Markerd Undiff - Imune')
        verbose_name_plural = _(u'Markerd Undiff - Imune')


class UndifferentiatedMorphologyMarkerImuneMolecule(DirtyFieldsMixin, MarkerMoleculeBase):

    marker = models.ForeignKey(UndifferentiatedMorphologyMarkerImune, verbose_name=u'Marker', related_name='molecules')


class UndifferentiatedMorphologyMarkerRtPcr(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=u'Cell line', related_name='undifferentiated_morphology_marker_rtpcr')
    passage_number = models.CharField(u'Passage number', max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Markerd Undiff - RtPcr')
        verbose_name_plural = _(u'Markerd Undiff - RtPcr')


class UndifferentiatedMorphologyMarkerRtPcrMolecule(DirtyFieldsMixin, MarkerMoleculeBase):

    marker = models.ForeignKey(UndifferentiatedMorphologyMarkerRtPcr, verbose_name=u'Marker', related_name='molecules')


class UndifferentiatedMorphologyMarkerFacs(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=u'Cell line', related_name='undifferentiated_morphology_marker_facs')
    passage_number = models.CharField(u'Passage number', max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Markerd Undiff - Facs')
        verbose_name_plural = _(u'Markerd Undiff - Facs')


class UndifferentiatedMorphologyMarkerFacsMolecule(DirtyFieldsMixin, MarkerMoleculeBase):

    marker = models.ForeignKey(UndifferentiatedMorphologyMarkerFacs, verbose_name=u'Marker', related_name='molecules')


class UndifferentiatedMorphologyMarkerMorphology(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=u'Cell line', related_name='undifferentiated_morphology_marker_morphology')
    passage_number = models.CharField(u'Passage number', max_length=10, null=True, blank=True)
    description = models.TextField(u'Description', null=True, blank=True)
    data_url = models.URLField(u'URL', null=True, blank=True)

    class Meta:
        verbose_name = _(u'Markerd Undiff - Morphology')
        verbose_name_plural = _(u'Markerd Undiff - Morphology')


class UndifferentiatedMorphologyMarkerExpressionProfile(DirtyFieldsMixin, models.Model):

    cell_line = models.OneToOneField(Cellline, verbose_name=u'Cell line', related_name='undifferentiated_morphology_marker_expression_profile')
    method = models.CharField(u'Method', max_length=100, null=True, blank=True)
    passage_number = models.CharField(u'Passage number', max_length=10, null=True, blank=True)
    data_url = models.URLField(u'Data URL', null=True, blank=True)
    uploaded_data_url = models.URLField(u'Uploaded data URL', null=True, blank=True)

    class Meta:
        verbose_name = _(u'Markerd Undiff - Expression profile')
        verbose_name_plural = _(u'Markerd Undiff - Expression profile')


class UndifferentiatedMorphologyMarkerExpressionProfileMolecule(DirtyFieldsMixin, MarkerMoleculeBase):

    marker = models.ForeignKey(UndifferentiatedMorphologyMarkerExpressionProfile, verbose_name=u'Marker', related_name='molecules')


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

    name = models.CharField(_(u'Organization name'), max_length=500, unique=True, null=True, blank=True)
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

class CelllinePublication(DirtyFieldsMixin, models.Model):

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

    # Higly suspect!
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
    karyotype_file = models.FileField(_(u'File'), upload_to=upload_to, null=True, blank=True)
    karyotype_file_enc = models.CharField(_(u'File enc'), max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line karyotype')
        verbose_name_plural = _(u'Cell line karyotypes')
        ordering = []

    def __unicode__(self):
        return unicode(self.karyotype)


# Genome-Wide Assays
class CelllineHlaTyping(DirtyFieldsMixin, models.Model):

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


class CelllineStrFingerprinting(DirtyFieldsMixin, models.Model):

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


class CelllineGenomeAnalysis(DirtyFieldsMixin, models.Model):

    cell_line = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), related_name='genome_analysis')
    analysis_method = models.CharField(_(u'Analysis method'), max_length=300, null=True, blank=True)
    link = models.URLField(u'Link', null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line genome analysis')
        verbose_name_plural = _(u'Cell line genome analysis')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class CelllineGenomeAnalysisFile(models.Model):

    genome_analysis = models.ForeignKey('CelllineGenomeAnalysis', verbose_name=_(u'Cell line genome analysis'), related_name='genome_analysis_files')
    vcf_file = models.FileField(_(u'VCF File'), upload_to=upload_to)
    vcf_file_enc = models.CharField(_(u'VCF File enc'), max_length=300)
    vcf_file_description = models.CharField(_(u'VCF File description'), max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line genome analysis file')
        verbose_name_plural = _(u'Cell line genome analysis files')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


# -----------------------------------------------------------------------------
# TODO Cell line differentation 2


class Germlayer(models.Model):

    germlayer = models.CharField(_(u'Germ layer'), max_length=100, blank=True)

    class Meta:
        verbose_name = _(u'Germ layer')
        verbose_name_plural = _(u'Germ layers')
        ordering = ['germlayer']

    def __unicode__(self):
        return u'%s' % (self.germlayer,)


class Marker(models.Model):

    name = models.CharField(_(u'Marker'), max_length=200, blank=True)

    class Meta:
        verbose_name = _(u'Marker')
        verbose_name_plural = _(u'Markers')
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Morphologymethod(models.Model):

    morphologymethod = models.CharField(_(u'Morphology method'), max_length=200, blank=True)

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

    passage_number = models.CharField(_(u'Passage number'), max_length=10, blank=True)
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
