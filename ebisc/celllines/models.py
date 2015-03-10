from django.db import models
from django.utils.translation import ugettext as _


class Accesslevel(models.Model):
    accesslevel = models.CharField(_(u'Access level'), max_length=20, blank=True)

    class Meta:
        verbose_name = _(u'Access level')
        verbose_name_plural = _(u'Access levels')
        ordering = ['accesslevel']

    def __unicode__(self):
        return u'%s' % (self.accesslevel,)


class Aliquotstatus(models.Model):
    aliquotstatus = models.CharField(_(u'Aliquot status'), max_length=20, blank=True)

    class Meta:
        verbose_name = _(u'Aliquot status')
        verbose_name_plural = _(u'Aliquot statuses')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Approveduse(models.Model):
    approveduse = models.CharField(_(u'Approved use'), max_length=60, blank=True)

    class Meta:
        verbose_name = _(u'Approved use')
        verbose_name_plural = _(u'Approved uses')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Batchstatus(models.Model):
    batchstatus = models.CharField(_(u'Batch status'), max_length=20, blank=True)

    class Meta:
        verbose_name = _(u'Batch status')
        verbose_name_plural = _(u'Batch statuses')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Binnedage(models.Model):
    binnedage = models.CharField(_(u'Binned age'), max_length=5, blank=True)

    class Meta:
        verbose_name = _(u'Binned age')
        verbose_name_plural = _(u'Binned ages')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Cellline(models.Model):
    biosamplesid = models.CharField(_(u'Biosamples id'), unique=True, max_length=12)
    celllinename = models.CharField(_(u'Cell line name'), unique=True, max_length=15)
    celllinedonor = models.ForeignKey('Donor', blank=True, null=True)
    celllineprimarydisease = models.ForeignKey('Disease', blank=True, null=True)
    celllinediseaseaddinfo = models.CharField(_(u'Cell line disease add info'), max_length=100, blank=True)
    celllinestatus = models.ForeignKey('Celllinestatus', blank=True, null=True)
    celllinecelltype = models.ForeignKey('Celltype', blank=True, null=True)
    celllinecollection = models.ForeignKey('Celllinecollection', blank=True, null=True)
    celllinetissuesource = models.ForeignKey('Tissuesource', blank=True, null=True)
    celllinetissuetreatment = models.ForeignKey('Clinicaltreatmentb4Donation', blank=True, null=True)
    celllinetissuedate = models.DateField(blank=True, null=True)
    celllinenamesynonyms = models.TextField(_(u'Cell line name synonyms'), null=True, blank=True)
    depositorscelllineuri = models.CharField(_(u'Depositors cell line uri'), max_length=45, blank=True)
    celllinecomments = models.TextField(_(u'Cell line comments'), null=True, blank=True)
    celllineupdate = models.DateField(blank=True, null=True)
    celllineupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllineupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)
    celllineecaccurl = models.URLField(_(u'Cell line ecacc url'), blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line')
        verbose_name_plural = _(u'Cell lines')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinealiquot(models.Model):
    aliquotcellline = models.ForeignKey(Cellline, blank=True, null=True)
    aliquotstatus = models.ForeignKey(Aliquotstatus, blank=True, null=True)
    aliquotstatusdate = models.CharField(_(u'Aliquot status date'), max_length=20, blank=True)
    aliquotupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line aliquot')
        verbose_name_plural = _(u'Cell line aliquotes')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllineannotation(models.Model):
    annotationcellline = models.ForeignKey(Cellline, blank=True, null=True)
    celllineannotationsource = models.CharField(_(u'Cell line annotation source'), max_length=45, blank=True)
    celllineannotationsourceid = models.CharField(_(u'Cell line annotation source id'), max_length=45, blank=True)
    celllineannotationsourceversion = models.CharField(_(u'Cell line annotation source version'), max_length=45, blank=True)
    celllineannotation = models.TextField(_(u'Cell line annotation'), null=True, blank=True)
    celllineannotationupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllineannotationupdate = models.DateField(blank=True, null=True)
    celllineannotationupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line annotation')
        verbose_name_plural = _(u'Cell line annotations')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinebatch(models.Model):
    batchcellline = models.ForeignKey(Cellline, blank=True, null=True)
    batchstatus = models.ForeignKey(Batchstatus, blank=True, null=True)
    batchstatusdate = models.CharField(_(u'Batch status date'), max_length=20, blank=True)
    batchstatusupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line batch')
        verbose_name_plural = _(u'Cell line batches')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinecharacterization(models.Model):
    characterizationcellline = models.ForeignKey(Cellline, blank=True, null=True)
    certificateofanalysispassage = models.CharField(_(u'Certificate of analysis passage'), max_length=5, blank=True)
    hiv1screening = models.IntegerField(_(u'Hiv1 screening'), blank=True, null=True)
    hiv2screening = models.IntegerField(_(u'Hiv2 screening'), blank=True, null=True)
    hepititusb = models.IntegerField(_(u'Hepititus b'), blank=True, null=True)
    hepititusc = models.IntegerField(_(u'Hepititus c'), blank=True, null=True)
    mycoplasma = models.IntegerField(_(u'Mycoplasma'), blank=True, null=True)
    celllinecharacterizationupdate = models.DateField(blank=True, null=True)
    celllinecharacterizationupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinecharacterizationupdateby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line characterization')
        verbose_name_plural = _(u'Cell line characterizations')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinecollection(models.Model):
    celllinecollectiontotal = models.IntegerField(_(u'Cell line collection total'), blank=True, null=True)
    celllinecollectionupdate = models.DateField(blank=True, null=True)
    celllinecollectionupdatetype = models.IntegerField(_(u'Cell line collection update type'), blank=True, null=True)
    celllinecollectionupdatedby = models.CharField(_(u'Cell line collection updated by'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Cell line collection')
        verbose_name_plural = _(u'Cell line collections')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinecomments(models.Model):
    commentscellline = models.IntegerField(_(u'Comments cell line'), blank=True, null=True)
    celllinecomments = models.TextField(blank=True)
    celllinecommentsupdated = models.DateField(blank=True, null=True)
    celllinecommentsupdatedtype = models.IntegerField(_(u'Cell line comments updated type'), blank=True, null=True)
    celllinecommentsupdatedby = models.IntegerField(_(u'Cell line comments updated by'), blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line comments')
        verbose_name_plural = _(u'Cell line comments')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinecultureconditions(models.Model):
    cultureconditionscellline = models.ForeignKey(Cellline, blank=True, null=True)
    surfacecoating = models.ForeignKey('Surfacecoating', blank=True, null=True)
    feedercelltype = models.CharField(_(u'Feeder cell type'), max_length=45, blank=True)
    feedercellid = models.CharField(_(u'Feeder cell id'), max_length=45, blank=True)
    passagemethod = models.ForeignKey('Passagemethod', blank=True, null=True)
    enzymatically = models.ForeignKey('Enzymatically', blank=True, null=True)
    enzymefree = models.ForeignKey('Enzymefree', blank=True, null=True)
    o2concentration = models.IntegerField(_(u'O2 concentration'), blank=True, null=True)
    co2concentration = models.IntegerField(_(u'Co2 concentration'), blank=True, null=True)
    culturemedium = models.ForeignKey('Culturemedium', blank=True, null=True)
    celllinecultureconditionsupdate = models.DateField(blank=True, null=True)
    celllinecultureconditionsupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinecultureconditionsupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line culture conditions')
        verbose_name_plural = _(u'Cell line culture conditions')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllineculturesupplements(models.Model):
    celllinecultureconditions = models.ForeignKey(Celllinecultureconditions, blank=True, null=True)
    supplement = models.CharField(_(u'Supplement'), max_length=45, blank=True)
    supplementamount = models.CharField(_(u'Supplement amount'), max_length=45, blank=True)
    supplementamountunit = models.ForeignKey('Units', blank=True, null=True)
    celllineculturesupplementsupdated = models.DateField(blank=True, null=True)
    celllineculturesupplementsupdatedtype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllineculturesupplementsupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line culture supplements')
        verbose_name_plural = _(u'Cell line culture supplements')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinederivation(models.Model):
    derivationcellline = models.ForeignKey(Cellline, blank=True, null=True)
    primarycelltypename = models.CharField(_(u'Primary cell type name'), max_length=45, blank=True)
    primarycelltypecellfinderid = models.CharField(_(u'Primary cell type cell finder id'), max_length=45, blank=True)
    primarycelldevelopmentalstage = models.ForeignKey('Primarycelldevelopmentalstage', blank=True, null=True)
    selectioncriteriaforclones = models.TextField(_(u'Selection criteria for clones'), null=True, blank=True)
    xenofreeconditions = models.CharField(_(u'Xeno free conditions'), max_length=4, blank=True)
    derivedundergmp = models.CharField(_(u'Derived under gmp'), max_length=4, blank=True)
    availableasclinicalgrade = models.CharField(_(u'Available as clinical grade'), max_length=4, blank=True)
    celllinederivationupdated = models.DateField(blank=True, null=True)
    celllinederivationupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinederivationupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line derivation')
        verbose_name_plural = _(u'Cell line derivations')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinediffpotency(models.Model):
    diffpotencycellline = models.ForeignKey(Cellline, blank=True, null=True)
    passagenumber = models.CharField(_(u'Passage number'), max_length=5, blank=True)
    germlayer = models.ForeignKey('Germlayer', blank=True, null=True)
    celllinediffpotencyupdated = models.DateField(blank=True, null=True)
    celllinediffpotencyupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinediffpotencyupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line diff potency')
        verbose_name_plural = _(u'Cell line diff potencies')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinediffpotencymarker(models.Model):
    celllinediffpotency = models.ForeignKey(Celllinediffpotency, blank=True, null=True)
    morphologymethod = models.ForeignKey('Morphologymethod', blank=True, null=True)
    celllinediffpotencymarkerupdate = models.DateField(blank=True, null=True)
    celllinediffpotencymarkerupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinediffpotencymarkerupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line diff potency marker')
        verbose_name_plural = _(u'Cell line diff potency markers')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinediffpotencymolecule(models.Model):
    celllinediffpotencymarker = models.IntegerField(_(u'Cell line diff potency marker'), blank=True, null=True)
    diffpotencymolecule = models.ForeignKey('Molecule', blank=True, null=True)
    diffpotencymoleculeupdate = models.DateField(blank=True, null=True)
    diffpotencymoleculeupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    diffpotencymoleculeupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line diff potency molecule')
        verbose_name_plural = _(u'Cell line diff potency molecules')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinegenemutations(models.Model):
    genemutationscellline = models.ForeignKey(Cellline, blank=True, null=True)
    weblink = models.CharField(_(u'Weblink'), max_length=100, blank=True)
    celllinegenemutationsupdate = models.DateField(blank=True, null=True)
    celllinegenemutationsupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinegenemutationsupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line gene mutations')
        verbose_name_plural = _(u'Cell line gene mutations')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinegenemutationsmolecule(models.Model):
    celllinegenemutations = models.ForeignKey(Celllinegenemutations, blank=True, null=True)
    genemutationsmolecule = models.ForeignKey('Molecule', blank=True, null=True)
    celllinegenemutationsmoleculeupdate = models.DateField(blank=True, null=True)
    celllinegenemutationsmoleculeupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinegenemutationsmoleculeupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line gene mutations molecule')
        verbose_name_plural = _(u'Cell line gene mutations molecules')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinegeneticmod(models.Model):
    geneticmodcellline = models.ForeignKey(Cellline, blank=True, null=True)
    celllinegeneticmod = models.CharField(_(u'Cell line genetic mod'), max_length=45, blank=True)
    celllinegeneticmodupdate = models.DateField(blank=True, null=True)
    celllinegeneticmodupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinegeneticmodupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line genetic mod')
        verbose_name_plural = _(u'Cell line genetic modes')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinegenomeseq(models.Model):
    genomeseqcellline = models.ForeignKey(Cellline, blank=True, null=True)
    celllinegenomeseqlink = models.CharField(_(u'Cell line genome seq link'), max_length=45, blank=True)
    celllinegenomesequpdate = models.DateField(blank=True, null=True)
    celllinegenomesequpdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinegenomesequpdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line genome seqence')
        verbose_name_plural = _(u'Cell line genome seqences')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinegenotypingother(models.Model):
    genometypothercellline = models.ForeignKey(Cellline, blank=True, null=True)
    celllinegenotypingother = models.TextField(_(u'Cell line geno typing other'), null=True, blank=True)
    celllinegenotypingotherupdate = models.DateField(blank=True, null=True)
    celllinegenotypingotherupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinegenotypingotherupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line genotyping other')
        verbose_name_plural = _(u'Cell line genotyping others')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinehlatyping(models.Model):
    hlatypingcellline = models.ForeignKey(Cellline, blank=True, null=True)
    celllinehlaclass = models.IntegerField(_(u'Cell line hla class'), blank=True, null=True)
    celllinehla = models.ForeignKey('Hla', blank=True, null=True)
    celllinehlaallele1 = models.CharField(_(u'Cell line hla all ele1'), max_length=45, blank=True)
    celllinehlaallele2 = models.CharField(_(u'Cell line hla all ele2'), max_length=45, blank=True)
    celllinehlatypingupdate = models.DateField(blank=True, null=True)
    celllinehlatypingupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinehlatypingupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line hla typing')
        verbose_name_plural = _(u'Cell line hla typing')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinekaryotype(models.Model):
    karyotypecellline = models.ForeignKey(Cellline, blank=True, null=True)
    passagenumber = models.CharField(_(u'Passage number'), max_length=5, blank=True)
    karyotype = models.CharField(_(u'Karyotype'), max_length=45, blank=True)
    karyotypemethod = models.ForeignKey('Karyotypemethod', blank=True, null=True)
    celllinekaryotypeupdate = models.DateField(blank=True, null=True)
    celllinekaryotypeupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinekaryotypeupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line karyotype')
        verbose_name_plural = _(u'Cell line karyotypes')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinelab(models.Model):
    labcellline = models.ForeignKey(Cellline, blank=True, null=True)
    cryodate = models.DateField(blank=True, null=True)
    expansioninprogress = models.IntegerField(_(u'Expansion in progress'), blank=True, null=True)
    funder = models.CharField(_(u'Funder'), max_length=45, blank=True)
    reprogrammingmethod1 = models.ForeignKey('Reprogrammingmethod1', blank=True, null=True)
    reprogrammingmethod2 = models.ForeignKey('Reprogrammingmethod2', blank=True, null=True)
    reprogrammingmethod3 = models.ForeignKey('Reprogrammingmethod3', blank=True, null=True)
    clonenumber = models.IntegerField(_(u'Clone number'), blank=True, null=True)
    passagenumber = models.CharField(_(u'Passage number'), max_length=5, blank=True)
    culturesystem = models.ForeignKey('Culturesystem', blank=True, null=True)
    culturesystemcomment = models.CharField(_(u'Culture system comment'), max_length=45, blank=True)
    celllinelabupdate = models.DateField(blank=True, null=True)
    celllinelabupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinelabupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line lab')
        verbose_name_plural = _(u'Cell line labs')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinelegal(models.Model):
    legalcellline = models.ForeignKey(Cellline, blank=True, null=True)
    q1donorconsent = models.IntegerField(_(u'Q1 donor consent'), blank=True, null=True)
    q2donortrace = models.IntegerField(_(u'Q2 donor trace'), blank=True, null=True)
    q3irbapproval = models.IntegerField(_(u'Q3 irb approval'), blank=True, null=True)
    q4approveduse = models.ForeignKey(Approveduse, blank=True, null=True)
    q5informedconsentreference = models.CharField(_(u'Q5 informed consent reference'), max_length=20, blank=True)
    q6restrictions = models.TextField(_(u'Q6 restrictions'), null=True, blank=True)
    q7iprestrictions = models.TextField(_(u'Q7 ip restrictions'), null=True, blank=True)
    q8jurisdiction = models.ForeignKey('Country', blank=True, null=True)
    q9applicablelegislationandregulation = models.TextField(_(u'Q9 applicable legislation and regulation'), null=True, blank=True)
    q10managedaccess = models.TextField(_(u'Q10 managed access'), null=True, blank=True)
    celllinelegalupdate = models.DateField(blank=True, null=True)
    celllinelegalupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinelegalupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line legal')
        verbose_name_plural = _(u'Cell line legal')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinemarker(models.Model):
    markercellline = models.ForeignKey(Cellline, unique=True)
    morphologymethod = models.ForeignKey('Morphologymethod', blank=True, null=True)
    celllinemarker = models.ForeignKey('Marker', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line marker')
        verbose_name_plural = _(u'Cell line markers')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllineorganization(models.Model):
    orgcellline = models.ForeignKey(Cellline, blank=True, null=True)
    organization = models.ForeignKey('Organization', blank=True, null=True)
    celllineorgtype = models.ForeignKey('Celllineorgtype', blank=True, null=True)
    orgstatus = models.IntegerField(_(u'Org status'), blank=True, null=True)
    orgregistrationdate = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line organization')
        verbose_name_plural = _(u'Cell line organizations')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllineorgtype(models.Model):
    celllineorgtype = models.CharField(_(u'Cell line org type'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Cell line org type')
        verbose_name_plural = _(u'Cell line org types')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinepublication(models.Model):
    publicationcellline = models.ForeignKey(Cellline, blank=True, null=True)
    pubmedreference = models.CharField(_(u'Pubmed reference'), max_length=45, blank=True)
    celllinepublicationdoiurl = models.URLField(_(u'Cell line publication doi url'), blank=True, null=True)
    celllinepublisher = models.ForeignKey('Publisher', blank=True, null=True)
    celllinepublicationupdate = models.DateField(blank=True, null=True)
    celllinepublicationupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinepublicationupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line publication')
        verbose_name_plural = _(u'Cell line publications')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinesnp(models.Model):
    snpcellline = models.ForeignKey(Cellline, blank=True, null=True)
    weblink = models.CharField(_(u'Weblink'), max_length=45, blank=True)
    celllinesnpupdate = models.DateField(blank=True, null=True)
    celllinesnpupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinesnpupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line snp')
        verbose_name_plural = _(u'Cell line snps')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinesnpdetails(models.Model):
    celllinesnp = models.ForeignKey(Celllinesnp, blank=True, null=True)
    celllinesnpgene = models.CharField(_(u'Cell line snp gene'), max_length=45, blank=True)
    celllinesnpchromosomalposition = models.CharField(_(u'Cell line snp chromosomal position'), max_length=45, blank=True)
    celllinesnpdetailsupdate = models.DateField(blank=True, null=True)
    celllinesnpdetailsupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinesnpdetailsupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line snp details')
        verbose_name_plural = _(u'Cell line snp details')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinesnprslinks(models.Model):
    celllinesnp = models.ForeignKey(Celllinesnp, blank=True, null=True)
    rsnumber = models.CharField(_(u'Rs number'), max_length=45, blank=True)
    rslink = models.CharField(_(u'Rs link'), max_length=100, blank=True)
    celllinesnprslinksupdate = models.DateField(blank=True, null=True)
    celllinesnprslinksupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinesnprslinksupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line snp Rs links')
        verbose_name_plural = _(u'Cell line snp Rs links')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinestatus(models.Model):
    celllinestatus = models.CharField(_(u'Cell line status'), max_length=20, blank=True)

    class Meta:
        verbose_name = _(u'Cell line status')
        verbose_name_plural = _(u'Cell line statuses')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinestrfingerprinting(models.Model):
    strfpcellline = models.ForeignKey(Cellline, blank=True, null=True)
    locus = models.ForeignKey('Strfplocus', blank=True, null=True)
    allele1 = models.CharField(_(u'All ele1'), max_length=45, blank=True)
    allele2 = models.CharField(_(u'All ele2'), max_length=45, blank=True)
    celllinestrfpupdate = models.DateField(blank=True, null=True)
    celllinestrfpupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinestrfpupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line str finger printing')
        verbose_name_plural = _(u'Cell line str finger printings')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinevalue(models.Model):
    valuecellline = models.ForeignKey(Cellline, blank=True, null=True)
    potentialuse = models.CharField(_(u'Potential use'), max_length=100, blank=True)
    valuetosociety = models.CharField(_(u'Value to society'), max_length=100, blank=True)
    valuetoresearch = models.CharField(_(u'Value to research'), max_length=100, blank=True)
    othervalue = models.CharField(_(u'Other value'), max_length=100, blank=True)
    celllinevalueupdate = models.DateField(blank=True, null=True)
    celllinevalueupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinevalueupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line value')
        verbose_name_plural = _(u'Cell line values')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinevector(models.Model):
    vectorcellline = models.ForeignKey(Cellline, blank=True, null=True)
    vectortype = models.ForeignKey('Vectortype', blank=True, null=True)
    vector = models.ForeignKey('Vector', blank=True, null=True)
    vectorexcisable = models.CharField(_(u'Vector excisable'), max_length=4, blank=True)
    virus = models.ForeignKey('Virus', blank=True, null=True)
    transposon = models.ForeignKey('Transposon', blank=True, null=True)
    celllinevectorupdate = models.DateField(blank=True, null=True)
    celllinevectorupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinevectorupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line vector')
        verbose_name_plural = _(u'Cell line vectors')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinevectorfreereprogramming(models.Model):
    vectorfreecellline = models.ForeignKey(Cellline, blank=True, null=True)
    vectorfreereprogrammingfactor = models.ForeignKey('Vectorfreereprogramfactor', blank=True, null=True)
    celllinevectorfreereprogupate = models.DateField(blank=True, null=True)
    celllinevectorfreereprogupatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinevectorfreereprogupatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line vector free reprogramming')
        verbose_name_plural = _(u'Cell line vector free reprogrammings')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinevectormolecule(models.Model):
    celllinevector = models.ForeignKey(Celllinevector, blank=True, null=True)
    molecule = models.ForeignKey('Molecule', blank=True, null=True)
    celllinevectormoleculeupdate = models.DateField(blank=True, null=True)
    celllinevectormoleculeupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinevectormoleculeupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line vector molecule')
        verbose_name_plural = _(u'Cell line vector molecules')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celltype(models.Model):
    celltype = models.CharField(_(u'Celltypes'), max_length=30, blank=True)

    class Meta:
        verbose_name = _(u'Cell type')
        verbose_name_plural = _(u'Cell types')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Clinicaltreatmentb4Donation(models.Model):
    clininicaltreatmentb4donation = models.CharField(_(u'Clininical treatment b4 donation'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Clininical treatment b4 donation')
        verbose_name_plural = _(u'Clininical treatment b4 donations')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Contact(models.Model):
    contacttype = models.ForeignKey('Contacttype', blank=True, null=True)
    country = models.ForeignKey('Country', db_column='country')
    postcode = models.ForeignKey('Postcode', db_column='postcode')
    statecounty = models.IntegerField(_(u'State county'), blank=True, null=True)
    city = models.CharField(_(u'City'), max_length=45, blank=True)
    street = models.CharField(_(u'Street'), max_length=45, blank=True)
    buildingnumber = models.CharField(_(u'Building number'), max_length=20, blank=True)
    suiteoraptordept = models.CharField(_(u'Suite or apt or dept'), max_length=10, blank=True)
    officephonecountrycode = models.ForeignKey('Phonecountrycode', related_name='contacts_officephonecountrycode', blank=True, null=True)
    officephone = models.CharField(_(u'Office phone'), max_length=20, blank=True)
    faxcountrycode = models.ForeignKey('Phonecountrycode', related_name='contacts_faxcountrycode', blank=True, null=True)
    fax = models.CharField(_(u'Fax'), max_length=20, blank=True)
    mobilecountrycode = models.ForeignKey('Phonecountrycode', related_name='contacts_mobilecountrycode', blank=True, null=True)
    mobilephone = models.CharField(_(u'Mobile phone'), max_length=20, blank=True)
    website = models.CharField(_(u'Website'), max_length=45, blank=True)
    emailaddress = models.CharField(_(u'Email address'), max_length=45, blank=True)
    contactupdate = models.DateField(blank=True, null=True)
    contactupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    contactupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Contact')
        verbose_name_plural = _(u'Contacts')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Contacttype(models.Model):
    contacttype = models.CharField(_(u'Contact type'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Contact type')
        verbose_name_plural = _(u'Contact types')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Country(models.Model):
    country = models.CharField(_(u'Country'), max_length=45, blank=True)
    countrycode = models.CharField(_(u'Country code'), max_length=3)

    class Meta:
        verbose_name = _(u'Country')
        verbose_name_plural = _(u'Countries')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Culturemedium(models.Model):
    culturemediumbase = models.CharField(_(u'Culture medium base'), max_length=45, blank=True)
    proteinsource = models.ForeignKey('Proteinsource', blank=True, null=True)
    serumconcentration = models.IntegerField(_(u'Serum concentration'), blank=True, null=True)

    class Meta:
        verbose_name = _(u'Culture medium')
        verbose_name_plural = _(u'Culture mediums')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Culturesystem(models.Model):
    culturesystem = models.CharField(_(u'Culture system'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Culture system')
        verbose_name_plural = _(u'Culture systems')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Disease(models.Model):
    icdcode = models.CharField(_(u'Icd code'), unique=True, max_length=10, blank=True)
    disease = models.CharField(_(u'Disease'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Disease')
        verbose_name_plural = _(u'Diseases')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Document(models.Model):
    cellline = models.IntegerField(_(u'Cell line'), blank=True, null=True)
    title = models.CharField(_(u'Title'), max_length=45, blank=True)
    abstract = models.TextField(_(u'Abstract'), null=True, blank=True)
    documenttype = models.ForeignKey('Documenttype', blank=True, null=True)
    documentdepositor = models.IntegerField(_(u'Document depositor'), blank=True, null=True)
    authors = models.TextField(_(u'Authors'), null=True, blank=True)
    owner = models.IntegerField(_(u'Owner'), blank=True, null=True)
    version = models.CharField(_(u'Version'), max_length=5, blank=True)
    accesslevel = models.IntegerField(_(u'Access level'), blank=True, null=True)
    documentupdate = models.IntegerField(_(u'Document update'), blank=True, null=True)
    documentupdatetype = models.IntegerField(_(u'Document update type'), blank=True, null=True)
    documentupdatedby = models.IntegerField(_(u'Document updated by'), blank=True, null=True)

    class Meta:
        verbose_name = _(u'Document')
        verbose_name_plural = _(u'Documents')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Documenttype(models.Model):
    documenttype = models.CharField(_(u'Document type'), max_length=30, blank=True)

    class Meta:
        verbose_name = _(u'Document type')
        verbose_name_plural = _(u'Document types')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Donor(models.Model):
    hescregdonorid = models.CharField(_(u'Hescreg donor id'), max_length=3, blank=True)
    age = models.ForeignKey(Binnedage, blank=True, null=True)
    gender = models.ForeignKey('Gender', blank=True, null=True)
    countryoforigin = models.ForeignKey(Country, blank=True, null=True)
    primarydisease = models.ForeignKey(Disease, blank=True, null=True)
    diseaseadditionalinfo = models.CharField(_(u'Disease additional info'), max_length=45, blank=True)
    othercelllinefromdonor = models.ForeignKey(Cellline, related_name='celllines_othercelllinefromdonor', blank=True, null=True)
    parentcellline = models.ForeignKey(Cellline, related_name='celllines_parentcellline', blank=True, null=True)
    providerdonorid = models.CharField(_(u'Provider donor id'), max_length=45, blank=True)
    cellabnormalkaryotype = models.CharField(_(u'Cell abnormal karyotype'), max_length=45, blank=True)
    donorabnormalkaryotype = models.CharField(_(u'Donor abnormal karyotype'), max_length=45, blank=True)
    otherclinicalinformation = models.CharField(_(u'Other clinical information'), max_length=100, blank=True)
    phenotype = models.ForeignKey('Phenotype', blank=True, null=True)
    donorupdate = models.DateField(blank=True, null=True)
    donorupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    donorupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Donor')
        verbose_name_plural = _(u'Donors')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Ebisckeyword(models.Model):
    cellline = models.ForeignKey(Cellline, blank=True, null=True)
    document = models.ForeignKey(Document, blank=True, null=True)
    ebisckeyword = models.ForeignKey('Keyword', blank=True, null=True)
    ebisckeywordupdate = models.DateField(blank=True, null=True)
    ebisckeywordupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    ebisckeywordupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Ebisc keyword')
        verbose_name_plural = _(u'Ebisc keywords')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Enzymatically(models.Model):
    enzymatically = models.CharField(_(u'Enzymatically'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Enzymatically')
        verbose_name_plural = _(u'Enzymatically')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Enzymefree(models.Model):
    enzymefree = models.CharField(_(u'Enzyme free'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Enzyme free')
        verbose_name_plural = _(u'Enzyme free')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Gender(models.Model):
    gender = models.CharField(_(u'Gender'), max_length=10, blank=True)

    class Meta:
        verbose_name = _(u'Gender')
        verbose_name_plural = _(u'Genders')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Germlayer(models.Model):
    germlayer = models.CharField(_(u'Germ layer'), max_length=15, blank=True)

    class Meta:
        verbose_name = _(u'Germ layer')
        verbose_name_plural = _(u'Germ layers')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Hla(models.Model):
    hla = models.CharField(_(u'Hla'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Hla')
        verbose_name_plural = _(u'Hla')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Karyotypemethod(models.Model):
    karyotypemethod = models.CharField(_(u'Karyotype method'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Karyotype method')
        verbose_name_plural = _(u'Karyotype methods')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Keyword(models.Model):
    keyword = models.CharField(_(u'Keyword'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Keyword')
        verbose_name_plural = _(u'Keywords')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Lastupdatetype(models.Model):
    lastupdatetype = models.CharField(_(u'Last update type'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Last update type')
        verbose_name_plural = _(u'Last update types')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Marker(models.Model):
    marker = models.CharField(_(u'Marker'), max_length=20, blank=True)

    class Meta:
        verbose_name = _(u'Marker')
        verbose_name_plural = _(u'Markers')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Molecule(models.Model):
    moleculename = models.CharField(_(u'Molecule name'), max_length=45, blank=True)
    referencesource = models.CharField(_(u'Reference source'), max_length=45, blank=True)
    referencesourceid = models.CharField(_(u'Reference source id'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Molecule')
        verbose_name_plural = _(u'Molecules')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Morphologymethod(models.Model):
    morphologymethod = models.CharField(_(u'Morphology method'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Morphology method')
        verbose_name_plural = _(u'Morphology methods')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Organization(models.Model):
    organizationname = models.CharField(_(u'Organization name'), max_length=45, blank=True)
    organizationshortname = models.CharField(_(u'Organization short name'), unique=True, max_length=6, blank=True)
    organizationcontact = models.ForeignKey(Contact, blank=True, null=True)
    organizationupdate = models.DateField(blank=True, null=True)
    organizationupdatetype = models.ForeignKey(Lastupdatetype, blank=True, null=True)
    organizationupdatedby = models.ForeignKey('Useraccount', related_name='organizations', blank=True, null=True)
    organizationtype = models.ForeignKey('Orgtype', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Organization')
        verbose_name_plural = _(u'Organizations')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Orgtype(models.Model):
    orgtype = models.CharField(_(u'Org type'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Organization type')
        verbose_name_plural = _(u'Organization types')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Passagemethod(models.Model):
    passagemethod = models.CharField(_(u'Passage method'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Passage method')
        verbose_name_plural = _(u'Passage methods')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Person(models.Model):
    organization = models.IntegerField(_(u'Organization'), blank=True, null=True)
    personlastname = models.CharField(_(u'Person last name'), max_length=20, blank=True)
    personfirstname = models.CharField(_(u'Person first name'), max_length=45, blank=True)
    personcontact = models.ForeignKey(Contact, blank=True, null=True)
    personupdate = models.DateField(blank=True, null=True)
    personupdatetype = models.ForeignKey(Lastupdatetype, blank=True, null=True)
    personupdatedby = models.ForeignKey('Useraccount', related_name='people', blank=True, null=True)

    class Meta:
        verbose_name = _(u'Person')
        verbose_name_plural = _(u'Persons')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Phenotype(models.Model):
    phenotype = models.CharField(_(u'Phenotype'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Phenotype')
        verbose_name_plural = _(u'Phenotypes')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Phonecountrycode(models.Model):
    phonecountrycode = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        verbose_name = _(u'Phone country code')
        verbose_name_plural = _(u'Phone country codes')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Postcode(models.Model):
    postcode = models.CharField(_(u'Postcode'), max_length=45, blank=True)
    district = models.CharField(_(u'District'), max_length=20)

    class Meta:
        verbose_name = _(u'Postcode')
        verbose_name_plural = _(u'Postcodes')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Primarycelldevelopmentalstage(models.Model):
    primarycelldevelopmentalstage = models.CharField(_(u'Primary cell developmental stage'), max_length=20, blank=True)

    class Meta:
        verbose_name = _(u'Primary cell developmental stage')
        verbose_name_plural = _(u'Primary cell developmental stages')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Proteinsource(models.Model):
    proteinsource = models.CharField(_(u'Protein source'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Protein source')
        verbose_name_plural = _(u'Protein sources')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Publisher(models.Model):
    publisher = models.CharField(_(u'Publisher'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Publisher')
        verbose_name_plural = _(u'Publishers')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Reprogrammingmethod1(models.Model):
    reprogrammingmethod1 = models.CharField(_(u'Reprogramming method 1'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Reprogramming method 1')
        verbose_name_plural = _(u'Reprogramming methods 1')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Reprogrammingmethod2(models.Model):
    reprogrammingmethod2 = models.CharField(_(u'Reprogramming method 2'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Reprogramming method 2')
        verbose_name_plural = _(u'Reprogramming methods 2')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Reprogrammingmethod3(models.Model):
    reprogrammingmethod3 = models.CharField(_(u'Reprogramming method 3'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Reprogramming method 3')
        verbose_name_plural = _(u'Reprogramming methods 3')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Strfplocus(models.Model):
    strfplocus = models.CharField(_(u'Str fp locus'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Str fp locus')
        verbose_name_plural = _(u'Str fp loci')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Surfacecoating(models.Model):
    surfacecoating = models.CharField(_(u'Surface coating'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Surface coating')
        verbose_name_plural = _(u'Surface coatings')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Tissuesource(models.Model):
    tissuesource = models.CharField(_(u'Tissue source'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Tissue source')
        verbose_name_plural = _(u'Tissue sources')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Transposon(models.Model):
    transposon = models.CharField(_(u'Transposon'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Transposon')
        verbose_name_plural = _(u'Transposons')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Units(models.Model):
    units = models.CharField(_(u'Units'), max_length=10, blank=True)

    class Meta:
        verbose_name = _(u'Units')
        verbose_name_plural = _(u'Units')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Useraccount(models.Model):
    username = models.CharField(_(u'Username'), max_length=45, blank=True)
    useraccounttype = models.ForeignKey('Useraccounttype', blank=True, null=True)
    person = models.ForeignKey(Person, blank=True, null=True)
    organization = models.ForeignKey(Organization, blank=True, null=True)
    accesslevel = models.ForeignKey(Accesslevel, blank=True, null=True)
    useraccountupdate = models.DateField(blank=True, null=True)
    useraccountupdatetype = models.ForeignKey(Lastupdatetype, blank=True, null=True)
    useraccountupdatedby = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        verbose_name = _(u'User account')
        verbose_name_plural = _(u'User accounts')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Useraccounttype(models.Model):
    useraccounttype = models.CharField(_(u'User account type'), max_length=15)

    class Meta:
        verbose_name = _(u'User account type')
        verbose_name_plural = _(u'User account types')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Vector(models.Model):
    vector = models.CharField(_(u'Vector'), max_length=20, blank=True)

    class Meta:
        verbose_name = _(u'Vector')
        verbose_name_plural = _(u'Vectors')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Vectorfreereprogramfactor(models.Model):
    vectorfreereprogramfactor = models.CharField(_(u'Vector free reprogram factor'), max_length=15, blank=True)
    referenceid = models.CharField(_(u'Referenceid'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Vector free reprogram factor')
        verbose_name_plural = _(u'Vector free reprogram factors')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Vectortype(models.Model):
    vectortype = models.CharField(_(u'Vector type'), max_length=15, blank=True)

    class Meta:
        verbose_name = _(u'Vector type')
        verbose_name_plural = _(u'Vector types')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Virus(models.Model):
    virus = models.CharField(_(u'Virus'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Virus')
        verbose_name_plural = _(u'Viruses')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)
