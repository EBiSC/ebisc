from django.db import models
from django.utils.translation import ugettext as _


class Accesslevel(models.Model):
    accesslevel = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = _(u'Access level')
        verbose_name_plural = _(u'Access levels')
        ordering = ['accesslevel']

    def __unicode__(self):
        return u'%s' % (self.accesslevel,)


class Aliquotstatus(models.Model):
    aliquotstatus = models.CharField(max_length=20, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Approveduse(models.Model):
    approveduse = models.CharField(max_length=60, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Batchstatus(models.Model):
    batchstatus = models.CharField(max_length=20, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Binnedage(models.Model):
    binnedage = models.CharField(max_length=5, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Cellline(models.Model):
    biosamplesid = models.CharField(unique=True, max_length=12)
    celllinename = models.CharField(unique=True, max_length=15)
    celllinedonor = models.ForeignKey('Donor', blank=True, null=True)
    celllineprimarydisease = models.ForeignKey('Disease', blank=True, null=True)
    celllinediseaseaddinfo = models.CharField(max_length=100, blank=True)
    celllinestatus = models.ForeignKey('Celllinestatus', blank=True, null=True)
    celllinecelltype = models.ForeignKey('Celltype', blank=True, null=True)
    celllinecollection = models.ForeignKey('Celllinecollection', blank=True, null=True)
    celllinetissuesource = models.ForeignKey('Tissuesource', blank=True, null=True)
    celllinetissuetreatment = models.ForeignKey('Clinicaltreatmentb4Donation', blank=True, null=True)
    celllinetissuedate = models.DateField(blank=True, null=True)
    celllinenamesynonyms = models.CharField(max_length=1000, blank=True)
    depositorscelllineuri = models.CharField(max_length=45, blank=True)
    celllinecomments = models.CharField(max_length=1000, blank=True)
    celllineupdate = models.DateField(blank=True, null=True)
    celllineupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllineupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)
    celllineecaccurl = models.CharField(max_length=100, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinealiquot(models.Model):
    aliquotcellline = models.ForeignKey(Cellline, blank=True, null=True)
    aliquotstatus = models.ForeignKey(Aliquotstatus, blank=True, null=True)
    aliquotstatusdate = models.CharField(max_length=20, blank=True)
    aliquotupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllineannotation(models.Model):
    annotationcellline = models.ForeignKey(Cellline, blank=True, null=True)
    celllineannotationsource = models.CharField(max_length=45, blank=True)
    celllineannotationsourceid = models.CharField(max_length=45, blank=True)
    celllineannotationsourceversion = models.CharField(max_length=45, blank=True)
    celllineannotation = models.CharField(max_length=1000, blank=True)
    celllineannotationupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllineannotationupdate = models.DateField(blank=True, null=True)
    celllineannotationupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinebatch(models.Model):
    batchcellline = models.ForeignKey(Cellline, blank=True, null=True)
    batchstatus = models.ForeignKey(Batchstatus, blank=True, null=True)
    batchstatusdate = models.CharField(max_length=20, blank=True)
    batchstatusupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinecharacterization(models.Model):
    characterizationcellline = models.ForeignKey(Cellline, blank=True, null=True)
    certificateofanalysispassage = models.CharField(max_length=5, blank=True)
    hiv1screening = models.IntegerField(blank=True, null=True)
    hiv2screening = models.IntegerField(blank=True, null=True)
    hepititusb = models.IntegerField(blank=True, null=True)
    hepititusc = models.IntegerField(blank=True, null=True)
    mycoplasma = models.IntegerField(blank=True, null=True)
    celllinecharacterizationupdate = models.DateField(blank=True, null=True)
    celllinecharacterizationupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinecharacterizationupdateby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinecollection(models.Model):
    celllinecollectiontotal = models.IntegerField(blank=True, null=True)
    celllinecollectionupdate = models.DateField(blank=True, null=True)
    celllinecollectionupdatetype = models.IntegerField(blank=True, null=True)
    celllinecollectionupdatedby = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinecomments(models.Model):
    commentscellline = models.IntegerField(blank=True, null=True)
    celllinecomments = models.TextField(blank=True)
    celllinecommentsupdated = models.DateField(blank=True, null=True)
    celllinecommentsupdatedtype = models.IntegerField(blank=True, null=True)
    celllinecommentsupdatedby = models.IntegerField(blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinecultureconditions(models.Model):
    cultureconditionscellline = models.ForeignKey(Cellline, blank=True, null=True)
    surfacecoating = models.ForeignKey('Surfacecoating', blank=True, null=True)
    feedercelltype = models.CharField(max_length=45, blank=True)
    feedercellid = models.CharField(max_length=45, blank=True)
    passagemethod = models.ForeignKey('Passagemethod', blank=True, null=True)
    enzymatically = models.ForeignKey('Enzymatically', blank=True, null=True)
    enzymefree = models.ForeignKey('Enzymefree', blank=True, null=True)
    o2concentration = models.IntegerField(blank=True, null=True)
    co2concentration = models.IntegerField(blank=True, null=True)
    culturemedium = models.ForeignKey('Culturemedium', blank=True, null=True)
    celllinecultureconditionsupdate = models.DateField(blank=True, null=True)
    celllinecultureconditionsupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinecultureconditionsupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllineculturesupplements(models.Model):
    celllinecultureconditions = models.ForeignKey(Celllinecultureconditions, blank=True, null=True)
    supplement = models.CharField(max_length=45, blank=True)
    supplementamount = models.CharField(max_length=45, blank=True)
    supplementamountunit = models.ForeignKey('Units', blank=True, null=True)
    celllineculturesupplementsupdated = models.DateField(blank=True, null=True)
    celllineculturesupplementsupdatedtype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllineculturesupplementsupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinederivation(models.Model):
    derivationcellline = models.ForeignKey(Cellline, blank=True, null=True)
    primarycelltypename = models.CharField(max_length=45, blank=True)
    primarycelltypecellfinderid = models.CharField(max_length=45, blank=True)
    primarycelldevelopmentalstage = models.ForeignKey('Primarycelldevelopmentalstage', blank=True, null=True)
    selectioncriteriaforclones = models.CharField(max_length=1000, blank=True)
    xenofreeconditions = models.CharField(max_length=4, blank=True)
    derivedundergmp = models.CharField(max_length=4, blank=True)
    availableasclinicalgrade = models.CharField(max_length=4, blank=True)
    celllinederivationupdated = models.DateField(blank=True, null=True)
    celllinederivationupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinederivationupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinediffpotency(models.Model):
    diffpotencycellline = models.ForeignKey(Cellline, blank=True, null=True)
    passagenumber = models.CharField(max_length=5, blank=True)
    germlayer = models.ForeignKey('Germlayer', blank=True, null=True)
    celllinediffpotencyupdated = models.DateField(blank=True, null=True)
    celllinediffpotencyupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinediffpotencyupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
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
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinediffpotencymolecule(models.Model):
    celllinediffpotencymarker = models.IntegerField(blank=True, null=True)
    diffpotencymolecule = models.ForeignKey('Molecule', blank=True, null=True)
    diffpotencymoleculeupdate = models.DateField(blank=True, null=True)
    diffpotencymoleculeupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    diffpotencymoleculeupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinegenemutations(models.Model):
    genemutationscellline = models.ForeignKey(Cellline, blank=True, null=True)
    weblink = models.CharField(max_length=100, blank=True)
    celllinegenemutationsupdate = models.DateField(blank=True, null=True)
    celllinegenemutationsupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinegenemutationsupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
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
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinegeneticmod(models.Model):
    geneticmodcellline = models.ForeignKey(Cellline, blank=True, null=True)
    celllinegeneticmod = models.CharField(max_length=45, blank=True)
    celllinegeneticmodupdate = models.DateField(blank=True, null=True)
    celllinegeneticmodupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinegeneticmodupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinegenomeseq(models.Model):
    genomeseqcellline = models.ForeignKey(Cellline, blank=True, null=True)
    celllinegenomeseqlink = models.CharField(max_length=45, blank=True)
    celllinegenomesequpdate = models.DateField(blank=True, null=True)
    celllinegenomesequpdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinegenomesequpdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinegenotypingother(models.Model):
    genometypothercellline = models.ForeignKey(Cellline, blank=True, null=True)
    celllinegenotypingother = models.CharField(max_length=1000, blank=True)
    celllinegenotypingotherupdate = models.DateField(blank=True, null=True)
    celllinegenotypingotherupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinegenotypingotherupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinehlatyping(models.Model):
    hlatypingcellline = models.ForeignKey(Cellline, blank=True, null=True)
    celllinehlaclass = models.IntegerField(blank=True, null=True)
    celllinehla = models.ForeignKey('Hla', blank=True, null=True)
    celllinehlaallele1 = models.CharField(max_length=45, blank=True)
    celllinehlaallele2 = models.CharField(max_length=45, blank=True)
    celllinehlatypingupdate = models.DateField(blank=True, null=True)
    celllinehlatypingupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinehlatypingupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinekaryotype(models.Model):
    karyotypecellline = models.ForeignKey(Cellline, blank=True, null=True)
    passagenumber = models.CharField(max_length=5, blank=True)
    karyotype = models.CharField(max_length=45, blank=True)
    karyotypemethod = models.ForeignKey('Karyotypemethod', blank=True, null=True)
    celllinekaryotypeupdate = models.DateField(blank=True, null=True)
    celllinekaryotypeupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinekaryotypeupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinelab(models.Model):
    labcellline = models.ForeignKey(Cellline, blank=True, null=True)
    cryodate = models.DateField(blank=True, null=True)
    expansioninprogress = models.IntegerField(blank=True, null=True)
    funder = models.CharField(max_length=45, blank=True)
    reprogrammingmethod1 = models.ForeignKey('Reprogrammingmethod1', blank=True, null=True)
    reprogrammingmethod2 = models.ForeignKey('Reprogrammingmethod2', blank=True, null=True)
    reprogrammingmethod3 = models.ForeignKey('Reprogrammingmethod3', blank=True, null=True)
    clonenumber = models.IntegerField(blank=True, null=True)
    passagenumber = models.CharField(max_length=5, blank=True)
    culturesystem = models.ForeignKey('Culturesystem', blank=True, null=True)
    culturesystemcomment = models.CharField(max_length=45, blank=True)
    celllinelabupdate = models.DateField(blank=True, null=True)
    celllinelabupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinelabupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinelegal(models.Model):
    legalcellline = models.ForeignKey(Cellline, blank=True, null=True)
    q1donorconsent = models.IntegerField(blank=True, null=True)
    q2donortrace = models.IntegerField(blank=True, null=True)
    q3irbapproval = models.IntegerField(blank=True, null=True)
    q4approveduse = models.ForeignKey(Approveduse, blank=True, null=True)
    q5informedconsentreference = models.CharField(max_length=20, blank=True)
    q6restrictions = models.CharField(max_length=1000, blank=True)
    q7iprestrictions = models.CharField(max_length=1000, blank=True)
    q8jurisdiction = models.ForeignKey('Country', blank=True, null=True)
    q9applicablelegislationandregulation = models.CharField(max_length=1000, blank=True)
    q10managedaccess = models.CharField(max_length=1000, blank=True)
    celllinelegalupdate = models.DateField(blank=True, null=True)
    celllinelegalupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinelegalupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinemarker(models.Model):
    markercellline = models.ForeignKey(Cellline, unique=True)
    morphologymethod = models.ForeignKey('Morphologymethod', blank=True, null=True)
    celllinemarker = models.ForeignKey('Marker', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllineorganization(models.Model):
    idcelllineorganization = models.IntegerField(unique=True)
    orgcellline = models.ForeignKey(Cellline, blank=True, null=True)
    organization = models.ForeignKey('Organization', blank=True, null=True)
    celllineorgtype = models.ForeignKey('Celllineorgtype', blank=True, null=True)
    orgstatus = models.IntegerField(blank=True, null=True)
    orgregistrationdate = models.DateField(blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllineorgtype(models.Model):
    celllineorgtype = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinepublication(models.Model):
    publicationcellline = models.ForeignKey(Cellline, blank=True, null=True)
    pubmedreference = models.CharField(max_length=45, blank=True)
    celllinepublicationdoiurl = models.CharField(max_length=1000, blank=True)
    celllinepublisher = models.ForeignKey('Publisher', blank=True, null=True)
    celllinepublicationupdate = models.DateField(blank=True, null=True)
    celllinepublicationupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinepublicationupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinesnp(models.Model):
    snpcellline = models.ForeignKey(Cellline, blank=True, null=True)
    weblink = models.CharField(max_length=45, blank=True)
    celllinesnpupdate = models.DateField(blank=True, null=True)
    celllinesnpupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinesnpupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinesnpdetails(models.Model):
    celllinesnp = models.ForeignKey(Celllinesnp, blank=True, null=True)
    celllinesnpgene = models.CharField(max_length=45, blank=True)
    celllinesnpchromosomalposition = models.CharField(max_length=45, blank=True)
    celllinesnpdetailsupdate = models.DateField(blank=True, null=True)
    celllinesnpdetailsupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinesnpdetailsupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinesnprslinks(models.Model):
    celllinesnp = models.ForeignKey(Celllinesnp, blank=True, null=True)
    rsnumber = models.CharField(max_length=45, blank=True)
    rslink = models.CharField(max_length=100, blank=True)
    celllinesnprslinksupdate = models.DateField(blank=True, null=True)
    celllinesnprslinksupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinesnprslinksupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinestatus(models.Model):
    celllinestatus = models.CharField(max_length=20, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinestrfingerprinting(models.Model):
    strfpcellline = models.ForeignKey(Cellline, blank=True, null=True)
    locus = models.ForeignKey('Strfplocus', blank=True, null=True)
    allele1 = models.CharField(max_length=45, blank=True)
    allele2 = models.CharField(max_length=45, blank=True)
    celllinestrfpupdate = models.DateField(blank=True, null=True)
    celllinestrfpupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinestrfpupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinevalue(models.Model):
    valuecellline = models.ForeignKey(Cellline, blank=True, null=True)
    potentialuse = models.CharField(max_length=100, blank=True)
    valuetosociety = models.CharField(max_length=100, blank=True)
    valuetoresearch = models.CharField(max_length=100, blank=True)
    othervalue = models.CharField(max_length=100, blank=True)
    celllinevalueupdate = models.DateField(blank=True, null=True)
    celllinevalueupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinevalueupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinevector(models.Model):
    vectorcellline = models.ForeignKey(Cellline, blank=True, null=True)
    vectortype = models.ForeignKey('Vectortype', blank=True, null=True)
    vector = models.ForeignKey('Vector', blank=True, null=True)
    vectorexcisable = models.CharField(max_length=4, blank=True)
    virus = models.ForeignKey('Virus', blank=True, null=True)
    transposon = models.ForeignKey('Transposon', blank=True, null=True)
    celllinevectorupdate = models.DateField(blank=True, null=True)
    celllinevectorupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllinevectorupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
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
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
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
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celltype(models.Model):
    celltype = models.CharField(max_length=30, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Clinicaltreatmentb4Donation(models.Model):
    clininicaltreatmentb4donation = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Contact(models.Model):
    contacttype = models.ForeignKey('Contacttype', blank=True, null=True)
    country = models.ForeignKey('Country', db_column='country')
    postcode = models.ForeignKey('Postcode', db_column='postcode')
    statecounty = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=45, blank=True)
    street = models.CharField(max_length=45, blank=True)
    buildingnumber = models.CharField(max_length=20, blank=True)
    suiteoraptordept = models.CharField(max_length=10, blank=True)
    officephonecountrycode = models.ForeignKey('Phonecountrycode', related_name='contacts_officephonecountrycode', blank=True, null=True)
    officephone = models.CharField(max_length=20, blank=True)
    faxcountrycode = models.ForeignKey('Phonecountrycode', related_name='contacts_faxcountrycode', blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True)
    mobilecountrycode = models.ForeignKey('Phonecountrycode', related_name='contacts_mobilecountrycode', blank=True, null=True)
    mobilephone = models.CharField(max_length=20, blank=True)
    website = models.CharField(max_length=45, blank=True)
    emailaddress = models.CharField(max_length=45, blank=True)
    contactupdate = models.DateField(blank=True, null=True)
    contactupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    contactupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Contacttype(models.Model):
    contacttype = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Country(models.Model):
    country = models.CharField(max_length=45, blank=True)
    countrycode = models.CharField(max_length=3)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Culturemedium(models.Model):
    culturemediumbase = models.CharField(max_length=45, blank=True)
    proteinsource = models.ForeignKey('Proteinsource', blank=True, null=True)
    serumconcentration = models.IntegerField(blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Culturesystem(models.Model):
    culturesystem = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Disease(models.Model):
    icdcode = models.CharField(unique=True, max_length=10, blank=True)
    disease = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Document(models.Model):
    cellline = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=45, blank=True)
    abstract = models.CharField(max_length=1000, blank=True)
    documenttype = models.ForeignKey('Documenttype', blank=True, null=True)
    documentdepositor = models.IntegerField(blank=True, null=True)
    authors = models.CharField(max_length=1000, blank=True)
    owner = models.IntegerField(blank=True, null=True)
    version = models.CharField(max_length=5, blank=True)
    accesslevel = models.IntegerField(blank=True, null=True)
    documentupdate = models.IntegerField(blank=True, null=True)
    documentupdatetype = models.IntegerField(blank=True, null=True)
    documentupdatedby = models.IntegerField(blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Documenttype(models.Model):
    documenttype = models.CharField(max_length=30, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Donor(models.Model):
    hescregdonorid = models.CharField(max_length=3, blank=True)
    age = models.ForeignKey(Binnedage, blank=True, null=True)
    gender = models.ForeignKey('Gender', blank=True, null=True)
    countryoforigin = models.ForeignKey(Country, blank=True, null=True)
    primarydisease = models.ForeignKey(Disease, blank=True, null=True)
    diseaseadditionalinfo = models.CharField(max_length=45, blank=True)
    othercelllinefromdonor = models.ForeignKey(Cellline, related_name='celllines_othercelllinefromdonor', blank=True, null=True)
    parentcellline = models.ForeignKey(Cellline, related_name='celllines_parentcellline', blank=True, null=True)
    providerdonorid = models.CharField(max_length=45, blank=True)
    cellabnormalkaryotype = models.CharField(max_length=45, blank=True)
    donorabnormalkaryotype = models.CharField(max_length=45, blank=True)
    otherclinicalinformation = models.CharField(max_length=100, blank=True)
    phenotype = models.ForeignKey('Phenotype', blank=True, null=True)
    donorupdate = models.DateField(blank=True, null=True)
    donorupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    donorupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
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
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Enzymatically(models.Model):
    enzymatically = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Enzymefree(models.Model):
    enzymefree = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Gender(models.Model):
    gender = models.CharField(max_length=10, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Germlayer(models.Model):
    germlayer = models.CharField(max_length=15, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Hla(models.Model):
    hla = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Karyotypemethod(models.Model):
    karyotypemethod = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Keyword(models.Model):
    keyword = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Lastupdatetype(models.Model):
    lastupdatetype = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Marker(models.Model):
    marker = models.CharField(max_length=20, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Molecule(models.Model):
    moleculename = models.CharField(max_length=45, blank=True)
    referencesource = models.CharField(max_length=45, blank=True)
    referencesourceid = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Morphologymethod(models.Model):
    morphologymethod = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Organization(models.Model):
    organizationname = models.CharField(max_length=45, blank=True)
    organizationshortname = models.CharField(unique=True, max_length=6, blank=True)
    organizationcontact = models.ForeignKey(Contact, blank=True, null=True)
    organizationupdate = models.DateField(blank=True, null=True)
    organizationupdatetype = models.ForeignKey(Lastupdatetype, blank=True, null=True)
    organizationupdatedby = models.ForeignKey('Useraccount', related_name='organizations', blank=True, null=True)
    organizationtype = models.ForeignKey('Orgtype', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Orgtype(models.Model):
    orgtype = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Passagemethod(models.Model):
    passagemethod = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Person(models.Model):
    organization = models.IntegerField(blank=True, null=True)
    personlastname = models.CharField(max_length=20, blank=True)
    personfirstname = models.CharField(max_length=45, blank=True)
    personcontact = models.ForeignKey(Contact, blank=True, null=True)
    personupdate = models.DateField(blank=True, null=True)
    personupdatetype = models.ForeignKey(Lastupdatetype, blank=True, null=True)
    personupdatedby = models.ForeignKey('Useraccount', related_name='people', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Phenotype(models.Model):
    phenotype = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Phonecountrycode(models.Model):
    phonecountrycode = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Postcode(models.Model):
    postcode = models.CharField(max_length=45, blank=True)
    district = models.CharField(max_length=20)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Primarycelldevelopmentalstage(models.Model):
    primarycelldevelopmentalstage = models.CharField(max_length=20, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Proteinsource(models.Model):
    proteinsource = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Publisher(models.Model):
    publisher = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Reprogrammingmethod1(models.Model):
    reprogrammingmethod1 = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Reprogrammingmethod2(models.Model):
    reprogrammingmethod2 = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Reprogrammingmethod3(models.Model):
    reprogrammingmethod3 = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Strfplocus(models.Model):
    strfplocus = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Surfacecoating(models.Model):
    surfacecoating = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Tissuesource(models.Model):
    tissuesource = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Transposon(models.Model):
    transposon = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Units(models.Model):
    units = models.CharField(max_length=10, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Useraccount(models.Model):
    username = models.CharField(max_length=45, blank=True)
    useraccounttype = models.ForeignKey('Useraccounttype', blank=True, null=True)
    person = models.ForeignKey(Person, blank=True, null=True)
    organization = models.ForeignKey(Organization, blank=True, null=True)
    accesslevel = models.ForeignKey(Accesslevel, blank=True, null=True)
    useraccountupdate = models.DateField(blank=True, null=True)
    useraccountupdatetype = models.ForeignKey(Lastupdatetype, blank=True, null=True)
    useraccountupdatedby = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Useraccounttype(models.Model):
    useraccounttype = models.CharField(max_length=15)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Vector(models.Model):
    vector = models.CharField(max_length=20, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Vectorfreereprogramfactor(models.Model):
    vectorfreereprogramfactor = models.CharField(max_length=15, blank=True)
    referenceid = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Vectortype(models.Model):
    vectortype = models.CharField(max_length=15, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Virus(models.Model):
    virus = models.CharField(max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)
