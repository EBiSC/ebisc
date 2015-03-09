from django.db import models
from django.utils.translation import ugettext as _


class Accesslevel(models.Model):
    accesslevel = models.CharField(_(u'Accesslevel'), max_length=20, blank=True)

    class Meta:
        verbose_name = _(u'Access level')
        verbose_name_plural = _(u'Access levels')
        ordering = ['accesslevel']

    def __unicode__(self):
        return u'%s' % (self.accesslevel,)


class Aliquotstatus(models.Model):
    aliquotstatus = models.CharField(_(u'Aliquotstatus'), max_length=20, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Approveduse(models.Model):
    approveduse = models.CharField(_(u'Approveduse'), max_length=60, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Batchstatus(models.Model):
    batchstatus = models.CharField(_(u'Batchstatus'), max_length=20, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Binnedage(models.Model):
    binnedage = models.CharField(_(u'Binnedage'), max_length=5, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Cellline(models.Model):
    biosamplesid = models.CharField(_(u'Biosamplesid'), unique=True, max_length=12)
    celllinename = models.CharField(_(u'Celllinename'), unique=True, max_length=15)
    celllinedonor = models.ForeignKey('Donor', blank=True, null=True)
    celllineprimarydisease = models.ForeignKey('Disease', blank=True, null=True)
    celllinediseaseaddinfo = models.CharField(_(u'Celllinediseaseaddinfo'), max_length=100, blank=True)
    celllinestatus = models.ForeignKey('Celllinestatus', blank=True, null=True)
    celllinecelltype = models.ForeignKey('Celltype', blank=True, null=True)
    celllinecollection = models.ForeignKey('Celllinecollection', blank=True, null=True)
    celllinetissuesource = models.ForeignKey('Tissuesource', blank=True, null=True)
    celllinetissuetreatment = models.ForeignKey('Clinicaltreatmentb4Donation', blank=True, null=True)
    celllinetissuedate = models.DateField(blank=True, null=True)
    celllinenamesynonyms = models.CharField(_(u'Celllinenamesynonyms'), max_length=1000, blank=True)
    depositorscelllineuri = models.CharField(_(u'Depositorscelllineuri'), max_length=45, blank=True)
    celllinecomments = models.CharField(_(u'Celllinecomments'), max_length=1000, blank=True)
    celllineupdate = models.DateField(blank=True, null=True)
    celllineupdatetype = models.ForeignKey('Lastupdatetype', blank=True, null=True)
    celllineupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)
    celllineecaccurl = models.CharField(_(u'Celllineecaccurl'), max_length=100, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinealiquot(models.Model):
    aliquotcellline = models.ForeignKey(Cellline, blank=True, null=True)
    aliquotstatus = models.ForeignKey(Aliquotstatus, blank=True, null=True)
    aliquotstatusdate = models.CharField(_(u'Aliquotstatusdate'), max_length=20, blank=True)
    aliquotupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllineannotation(models.Model):
    annotationcellline = models.ForeignKey(Cellline, blank=True, null=True)
    celllineannotationsource = models.CharField(_(u'Celllineannotationsource'), max_length=45, blank=True)
    celllineannotationsourceid = models.CharField(_(u'Celllineannotationsourceid'), max_length=45, blank=True)
    celllineannotationsourceversion = models.CharField(_(u'Celllineannotationsourceversion'), max_length=45, blank=True)
    celllineannotation = models.CharField(_(u'Celllineannotation'), max_length=1000, blank=True)
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
    batchstatusdate = models.CharField(_(u'Batchstatusdate'), max_length=20, blank=True)
    batchstatusupdatedby = models.ForeignKey('Useraccount', blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinecharacterization(models.Model):
    characterizationcellline = models.ForeignKey(Cellline, blank=True, null=True)
    certificateofanalysispassage = models.CharField(_(u'Certificateofanalysispassage'), max_length=5, blank=True)
    hiv1screening = models.IntegerField(_(u'Hiv1screening'), blank=True, null=True)
    hiv2screening = models.IntegerField(_(u'Hiv2screening'), blank=True, null=True)
    hepititusb = models.IntegerField(_(u'Hepititusb'), blank=True, null=True)
    hepititusc = models.IntegerField(_(u'Hepititusc'), blank=True, null=True)
    mycoplasma = models.IntegerField(_(u'Mycoplasma'), blank=True, null=True)
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
    celllinecollectiontotal = models.IntegerField(_(u'Celllinecollectiontotal'), blank=True, null=True)
    celllinecollectionupdate = models.DateField(blank=True, null=True)
    celllinecollectionupdatetype = models.IntegerField(_(u'Celllinecollectionupdatetype'), blank=True, null=True)
    celllinecollectionupdatedby = models.CharField(_(u'Celllinecollectionupdatedby'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinecomments(models.Model):
    commentscellline = models.IntegerField(_(u'Commentscellline'), blank=True, null=True)
    celllinecomments = models.TextField(blank=True)
    celllinecommentsupdated = models.DateField(blank=True, null=True)
    celllinecommentsupdatedtype = models.IntegerField(_(u'Celllinecommentsupdatedtype'), blank=True, null=True)
    celllinecommentsupdatedby = models.IntegerField(_(u'Celllinecommentsupdatedby'), blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinecultureconditions(models.Model):
    cultureconditionscellline = models.ForeignKey(Cellline, blank=True, null=True)
    surfacecoating = models.ForeignKey('Surfacecoating', blank=True, null=True)
    feedercelltype = models.CharField(_(u'Feedercelltype'), max_length=45, blank=True)
    feedercellid = models.CharField(_(u'Feedercellid'), max_length=45, blank=True)
    passagemethod = models.ForeignKey('Passagemethod', blank=True, null=True)
    enzymatically = models.ForeignKey('Enzymatically', blank=True, null=True)
    enzymefree = models.ForeignKey('Enzymefree', blank=True, null=True)
    o2concentration = models.IntegerField(_(u'O2concentration'), blank=True, null=True)
    co2concentration = models.IntegerField(_(u'Co2concentration'), blank=True, null=True)
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
    supplement = models.CharField(_(u'Supplement'), max_length=45, blank=True)
    supplementamount = models.CharField(_(u'Supplementamount'), max_length=45, blank=True)
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
    primarycelltypename = models.CharField(_(u'Primarycelltypename'), max_length=45, blank=True)
    primarycelltypecellfinderid = models.CharField(_(u'Primarycelltypecellfinderid'), max_length=45, blank=True)
    primarycelldevelopmentalstage = models.ForeignKey('Primarycelldevelopmentalstage', blank=True, null=True)
    selectioncriteriaforclones = models.CharField(_(u'Selectioncriteriaforclones'), max_length=1000, blank=True)
    xenofreeconditions = models.CharField(_(u'Xenofreeconditions'), max_length=4, blank=True)
    derivedundergmp = models.CharField(_(u'Derivedundergmp'), max_length=4, blank=True)
    availableasclinicalgrade = models.CharField(_(u'Availableasclinicalgrade'), max_length=4, blank=True)
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
    passagenumber = models.CharField(_(u'Passagenumber'), max_length=5, blank=True)
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
    celllinediffpotencymarker = models.IntegerField(_(u'Celllinediffpotencymarker'), blank=True, null=True)
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
    weblink = models.CharField(_(u'Weblink'), max_length=100, blank=True)
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
    celllinegeneticmod = models.CharField(_(u'Celllinegeneticmod'), max_length=45, blank=True)
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
    celllinegenomeseqlink = models.CharField(_(u'Celllinegenomeseqlink'), max_length=45, blank=True)
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
    celllinegenotypingother = models.CharField(_(u'Celllinegenotypingother'), max_length=1000, blank=True)
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
    celllinehlaclass = models.IntegerField(_(u'Celllinehlaclass'), blank=True, null=True)
    celllinehla = models.ForeignKey('Hla', blank=True, null=True)
    celllinehlaallele1 = models.CharField(_(u'Celllinehlaallele1'), max_length=45, blank=True)
    celllinehlaallele2 = models.CharField(_(u'Celllinehlaallele2'), max_length=45, blank=True)
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
    passagenumber = models.CharField(_(u'Passagenumber'), max_length=5, blank=True)
    karyotype = models.CharField(_(u'Karyotype'), max_length=45, blank=True)
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
    expansioninprogress = models.IntegerField(_(u'Expansioninprogress'), blank=True, null=True)
    funder = models.CharField(_(u'Funder'), max_length=45, blank=True)
    reprogrammingmethod1 = models.ForeignKey('Reprogrammingmethod1', blank=True, null=True)
    reprogrammingmethod2 = models.ForeignKey('Reprogrammingmethod2', blank=True, null=True)
    reprogrammingmethod3 = models.ForeignKey('Reprogrammingmethod3', blank=True, null=True)
    clonenumber = models.IntegerField(_(u'Clonenumber'), blank=True, null=True)
    passagenumber = models.CharField(_(u'Passagenumber'), max_length=5, blank=True)
    culturesystem = models.ForeignKey('Culturesystem', blank=True, null=True)
    culturesystemcomment = models.CharField(_(u'Culturesystemcomment'), max_length=45, blank=True)
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
    q1donorconsent = models.IntegerField(_(u'Q1donorconsent'), blank=True, null=True)
    q2donortrace = models.IntegerField(_(u'Q2donortrace'), blank=True, null=True)
    q3irbapproval = models.IntegerField(_(u'Q3irbapproval'), blank=True, null=True)
    q4approveduse = models.ForeignKey(Approveduse, blank=True, null=True)
    q5informedconsentreference = models.CharField(_(u'Q5informedconsentreference'), max_length=20, blank=True)
    q6restrictions = models.CharField(_(u'Q6restrictions'), max_length=1000, blank=True)
    q7iprestrictions = models.CharField(_(u'Q7iprestrictions'), max_length=1000, blank=True)
    q8jurisdiction = models.ForeignKey('Country', blank=True, null=True)
    q9applicablelegislationandregulation = models.CharField(_(u'Q9applicablelegislationandregulation'), max_length=1000, blank=True)
    q10managedaccess = models.CharField(_(u'Q10managedaccess'), max_length=1000, blank=True)
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
    orgcellline = models.ForeignKey(Cellline, blank=True, null=True)
    organization = models.ForeignKey('Organization', blank=True, null=True)
    celllineorgtype = models.ForeignKey('Celllineorgtype', blank=True, null=True)
    orgstatus = models.IntegerField(_(u'Orgstatus'), blank=True, null=True)
    orgregistrationdate = models.DateField(blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllineorgtype(models.Model):
    celllineorgtype = models.CharField(_(u'Celllineorgtype'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinepublication(models.Model):
    publicationcellline = models.ForeignKey(Cellline, blank=True, null=True)
    pubmedreference = models.CharField(_(u'Pubmedreference'), max_length=45, blank=True)
    celllinepublicationdoiurl = models.CharField(_(u'Celllinepublicationdoiurl'), max_length=1000, blank=True)
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
    weblink = models.CharField(_(u'Weblink'), max_length=45, blank=True)
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
    celllinesnpgene = models.CharField(_(u'Celllinesnpgene'), max_length=45, blank=True)
    celllinesnpchromosomalposition = models.CharField(_(u'Celllinesnpchromosomalposition'), max_length=45, blank=True)
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
    rsnumber = models.CharField(_(u'Rsnumber'), max_length=45, blank=True)
    rslink = models.CharField(_(u'Rslink'), max_length=100, blank=True)
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
    celllinestatus = models.CharField(_(u'Celllinestatus'), max_length=20, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinestrfingerprinting(models.Model):
    strfpcellline = models.ForeignKey(Cellline, blank=True, null=True)
    locus = models.ForeignKey('Strfplocus', blank=True, null=True)
    allele1 = models.CharField(_(u'Allele1'), max_length=45, blank=True)
    allele2 = models.CharField(_(u'Allele2'), max_length=45, blank=True)
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
    potentialuse = models.CharField(_(u'Potentialuse'), max_length=100, blank=True)
    valuetosociety = models.CharField(_(u'Valuetosociety'), max_length=100, blank=True)
    valuetoresearch = models.CharField(_(u'Valuetoresearch'), max_length=100, blank=True)
    othervalue = models.CharField(_(u'Othervalue'), max_length=100, blank=True)
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
    vectorexcisable = models.CharField(_(u'Vectorexcisable'), max_length=4, blank=True)
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
    celltype = models.CharField(_(u'Celltype'), max_length=30, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Clinicaltreatmentb4Donation(models.Model):
    clininicaltreatmentb4donation = models.CharField(_(u'Clininicaltreatmentb4donation'), max_length=45, blank=True)

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
    statecounty = models.IntegerField(_(u'Statecounty'), blank=True, null=True)
    city = models.CharField(_(u'City'), max_length=45, blank=True)
    street = models.CharField(_(u'Street'), max_length=45, blank=True)
    buildingnumber = models.CharField(_(u'Buildingnumber'), max_length=20, blank=True)
    suiteoraptordept = models.CharField(_(u'Suiteoraptordept'), max_length=10, blank=True)
    officephonecountrycode = models.ForeignKey('Phonecountrycode', related_name='contacts_officephonecountrycode', blank=True, null=True)
    officephone = models.CharField(_(u'Officephone'), max_length=20, blank=True)
    faxcountrycode = models.ForeignKey('Phonecountrycode', related_name='contacts_faxcountrycode', blank=True, null=True)
    fax = models.CharField(_(u'Fax'), max_length=20, blank=True)
    mobilecountrycode = models.ForeignKey('Phonecountrycode', related_name='contacts_mobilecountrycode', blank=True, null=True)
    mobilephone = models.CharField(_(u'Mobilephone'), max_length=20, blank=True)
    website = models.CharField(_(u'Website'), max_length=45, blank=True)
    emailaddress = models.CharField(_(u'Emailaddress'), max_length=45, blank=True)
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
    contacttype = models.CharField(_(u'Contacttype'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Country(models.Model):
    country = models.CharField(_(u'Country'), max_length=45, blank=True)
    countrycode = models.CharField(_(u'Countrycode'), max_length=3)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Culturemedium(models.Model):
    culturemediumbase = models.CharField(_(u'Culturemediumbase'), max_length=45, blank=True)
    proteinsource = models.ForeignKey('Proteinsource', blank=True, null=True)
    serumconcentration = models.IntegerField(_(u'Serumconcentration'), blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Culturesystem(models.Model):
    culturesystem = models.CharField(_(u'Culturesystem'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Disease(models.Model):
    icdcode = models.CharField(_(u'Icdcode'), unique=True, max_length=10, blank=True)
    disease = models.CharField(_(u'Disease'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Document(models.Model):
    cellline = models.IntegerField(_(u'Cellline'), blank=True, null=True)
    title = models.CharField(_(u'Title'), max_length=45, blank=True)
    abstract = models.CharField(_(u'Abstract'), max_length=1000, blank=True)
    documenttype = models.ForeignKey('Documenttype', blank=True, null=True)
    documentdepositor = models.IntegerField(_(u'Documentdepositor'), blank=True, null=True)
    authors = models.CharField(_(u'Authors'), max_length=1000, blank=True)
    owner = models.IntegerField(_(u'Owner'), blank=True, null=True)
    version = models.CharField(_(u'Version'), max_length=5, blank=True)
    accesslevel = models.IntegerField(_(u'Accesslevel'), blank=True, null=True)
    documentupdate = models.IntegerField(_(u'Documentupdate'), blank=True, null=True)
    documentupdatetype = models.IntegerField(_(u'Documentupdatetype'), blank=True, null=True)
    documentupdatedby = models.IntegerField(_(u'Documentupdatedby'), blank=True, null=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Documenttype(models.Model):
    documenttype = models.CharField(_(u'Documenttype'), max_length=30, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Donor(models.Model):
    hescregdonorid = models.CharField(_(u'Hescregdonorid'), max_length=3, blank=True)
    age = models.ForeignKey(Binnedage, blank=True, null=True)
    gender = models.ForeignKey('Gender', blank=True, null=True)
    countryoforigin = models.ForeignKey(Country, blank=True, null=True)
    primarydisease = models.ForeignKey(Disease, blank=True, null=True)
    diseaseadditionalinfo = models.CharField(_(u'Diseaseadditionalinfo'), max_length=45, blank=True)
    othercelllinefromdonor = models.ForeignKey(Cellline, related_name='celllines_othercelllinefromdonor', blank=True, null=True)
    parentcellline = models.ForeignKey(Cellline, related_name='celllines_parentcellline', blank=True, null=True)
    providerdonorid = models.CharField(_(u'Providerdonorid'), max_length=45, blank=True)
    cellabnormalkaryotype = models.CharField(_(u'Cellabnormalkaryotype'), max_length=45, blank=True)
    donorabnormalkaryotype = models.CharField(_(u'Donorabnormalkaryotype'), max_length=45, blank=True)
    otherclinicalinformation = models.CharField(_(u'Otherclinicalinformation'), max_length=100, blank=True)
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
    enzymatically = models.CharField(_(u'Enzymatically'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Enzymefree(models.Model):
    enzymefree = models.CharField(_(u'Enzymefree'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Gender(models.Model):
    gender = models.CharField(_(u'Gender'), max_length=10, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Germlayer(models.Model):
    germlayer = models.CharField(_(u'Germlayer'), max_length=15, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Hla(models.Model):
    hla = models.CharField(_(u'Hla'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Karyotypemethod(models.Model):
    karyotypemethod = models.CharField(_(u'Karyotypemethod'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Keyword(models.Model):
    keyword = models.CharField(_(u'Keyword'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Lastupdatetype(models.Model):
    lastupdatetype = models.CharField(_(u'Lastupdatetype'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Marker(models.Model):
    marker = models.CharField(_(u'Marker'), max_length=20, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Molecule(models.Model):
    moleculename = models.CharField(_(u'Moleculename'), max_length=45, blank=True)
    referencesource = models.CharField(_(u'Referencesource'), max_length=45, blank=True)
    referencesourceid = models.CharField(_(u'Referencesourceid'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Morphologymethod(models.Model):
    morphologymethod = models.CharField(_(u'Morphologymethod'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Organization(models.Model):
    organizationname = models.CharField(_(u'Organizationname'), max_length=45, blank=True)
    organizationshortname = models.CharField(_(u'Organizationshortname'), unique=True, max_length=6, blank=True)
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
    orgtype = models.CharField(_(u'Orgtype'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Passagemethod(models.Model):
    passagemethod = models.CharField(_(u'Passagemethod'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Person(models.Model):
    organization = models.IntegerField(_(u'Organization'), blank=True, null=True)
    personlastname = models.CharField(_(u'Personlastname'), max_length=20, blank=True)
    personfirstname = models.CharField(_(u'Personfirstname'), max_length=45, blank=True)
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
    phenotype = models.CharField(_(u'Phenotype'), max_length=45, blank=True)

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
    postcode = models.CharField(_(u'Postcode'), max_length=45, blank=True)
    district = models.CharField(_(u'District'), max_length=20)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Primarycelldevelopmentalstage(models.Model):
    primarycelldevelopmentalstage = models.CharField(_(u'Primarycelldevelopmentalstage'), max_length=20, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Proteinsource(models.Model):
    proteinsource = models.CharField(_(u'Proteinsource'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Publisher(models.Model):
    publisher = models.CharField(_(u'Publisher'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Reprogrammingmethod1(models.Model):
    reprogrammingmethod1 = models.CharField(_(u'Reprogrammingmethod1'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Reprogrammingmethod2(models.Model):
    reprogrammingmethod2 = models.CharField(_(u'Reprogrammingmethod2'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Reprogrammingmethod3(models.Model):
    reprogrammingmethod3 = models.CharField(_(u'Reprogrammingmethod3'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Strfplocus(models.Model):
    strfplocus = models.CharField(_(u'Strfplocus'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Surfacecoating(models.Model):
    surfacecoating = models.CharField(_(u'Surfacecoating'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Tissuesource(models.Model):
    tissuesource = models.CharField(_(u'Tissuesource'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Transposon(models.Model):
    transposon = models.CharField(_(u'Transposon'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Units(models.Model):
    units = models.CharField(_(u'Units'), max_length=10, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
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
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Useraccounttype(models.Model):
    useraccounttype = models.CharField(_(u'Useraccounttype'), max_length=15)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Vector(models.Model):
    vector = models.CharField(_(u'Vector'), max_length=20, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Vectorfreereprogramfactor(models.Model):
    vectorfreereprogramfactor = models.CharField(_(u'Vectorfreereprogramfactor'), max_length=15, blank=True)
    referenceid = models.CharField(_(u'Referenceid'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Vectortype(models.Model):
    vectortype = models.CharField(_(u'Vectortype'), max_length=15, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Virus(models.Model):
    virus = models.CharField(_(u'Virus'), max_length=45, blank=True)

    class Meta:
        # verbose_name = _(u'')
        # verbose_name_plural = _(u'')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)
