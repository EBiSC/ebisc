# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Accesslevel(models.Model):
    idaccesslevel = models.IntegerField(primary_key=True, editable=False)
    accesslevel = models.CharField(max_length=40, blank=True)

    def __unicode__(self):
        return self.accesslevel

    class Meta:
        managed = False
        db_table = 'accesslevel'


class Aliquotstatus(models.Model):
    idcelllinealiquotstatus = models.IntegerField(primary_key=True, editable=False)
    aliquotstatus = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'aliquotstatus'


class Approveduse(models.Model):
    idapproveduse = models.IntegerField(primary_key=True, editable=False)
    approveduse = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'approveduse'


class Batchstatus(models.Model):
    idbatchstatus = models.IntegerField(primary_key=True, editable=False)
    batchstatus = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'batchstatus'


class Binnedage(models.Model):
    idbinnedage = models.IntegerField(primary_key=True, editable=False)
    binnedage = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return self.binnedage

    class Meta:
        managed = False
        db_table = 'binnedage'


class Cellline(models.Model):
    idcellline = models.IntegerField(primary_key=True, editable=False)
    biosamplesid = models.CharField(unique=True, max_length=24, blank=True)
    celllinedepositor = models.ForeignKey('Depositor', db_column='celllinedepositor', blank=True, null=True)
    celllinename = models.CharField(max_length=30, blank=True)
    celllinecollection = models.IntegerField(blank=True, null=True)
    celllinecelltype = models.ForeignKey('Celltype', db_column='celllinecelltype', blank=True, null=True)
    celllinedepositorsname = models.CharField(max_length=90, blank=True)
    celllinealternatenames = models.CharField(max_length=90, blank=True)
    celllinedepositorsuri = models.CharField(max_length=90, blank=True)
    celllinestatus = models.ForeignKey('Celllinestatus', db_column='celllinestatus', blank=True, null=True)
    celllinedonor = models.ForeignKey('Donor', db_column='celllinedonor', blank=True, null=True)
    celllinetissuesource = models.ForeignKey('Tissuesource', db_column='celllinetissuesource', blank=True, null=True)
    celllinetissuedate = models.IntegerField(blank=True, null=True)
    celllinetissuetreatment = models.ForeignKey('Clinicaltreatmentb4Donation', db_column='celllinetissuetreatment', blank=True, null=True)

    def __unicode__(self):
        return self.celllinename

    class Meta:
        managed = False
        db_table = 'cellline'


class Celllineadditionalinformation(models.Model):
    idcellineadditionalinformation = models.IntegerField(primary_key=True, editable=False)
    cellline = models.ForeignKey(Cellline, db_column='cellline', blank=True, null=True)
    cellinederivationpurpose = models.CharField(max_length=200, blank=True)
    cellinederivedundergmp = models.IntegerField(db_column='cellinederivedunderGMP', blank=True, null=True)  # Field name made lowercase.
    culturemedium = models.IntegerField(blank=True, null=True)
    serumconcentration = models.CharField(max_length=200, blank=True)
    surfacecoatingmatrix = models.IntegerField(blank=True, null=True)
    supplements = models.CharField(max_length=200, blank=True)
    growthfactors = models.CharField(max_length=200, blank=True)
    enzymesused = models.CharField(max_length=200, blank=True)
    o2concentration = models.IntegerField(blank=True, null=True)
    co2concentration = models.IntegerField(blank=True, null=True)
    changingmedia = models.CharField(max_length=200, blank=True)
    feedercells = models.IntegerField(blank=True, null=True)
    seedingdensity = models.CharField(max_length=200, blank=True)
    maxpassageofuse = models.CharField(max_length=90, blank=True)
    feedercellinactivitation = models.CharField(max_length=90, blank=True)
    proteinsused = models.CharField(max_length=90, blank=True)
    materialused = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'celllineadditionalinformation'


class Celllinealiquot(models.Model):
    idcelllinealiquot = models.IntegerField(primary_key=True, editable=False)
    cellline = models.ForeignKey(Cellline, db_column='cellline', blank=True, null=True)
    aliquotstatus = models.ForeignKey(Aliquotstatus, db_column='aliquotstatus', blank=True, null=True)
    aliquotstatusdate = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'celllinealiquot'


class Celllinebatch(models.Model):
    idcelllinebatch = models.IntegerField(primary_key=True, editable=False)
    cellline = models.ForeignKey(Cellline, db_column='cellline', blank=True, null=True)
    batchstatus = models.ForeignKey(Batchstatus, db_column='batchstatus', blank=True, null=True)
    batchstatusdate = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'celllinebatch'


class Celllinecollection(models.Model):
    idcelllinecollection = models.IntegerField(primary_key=True, editable=False)
    celllinecollectiontotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinecollection'


class Celllinederivation(models.Model):
    idderivation = models.IntegerField(primary_key=True, editable=False)
    cellline = models.IntegerField(blank=True, null=True)
    depositoraliquotid = models.CharField(max_length=90, blank=True)
    cellsubcloneid = models.IntegerField(blank=True, null=True)
    derivationdate = models.CharField(max_length=40, blank=True)
    passagenumber = models.CharField(max_length=2, blank=True)
    derivationmethod = models.ForeignKey('Derivationmethod', db_column='derivationmethod', blank=True, null=True)
    transformationtechnique = models.ForeignKey('Transformationtechnique', db_column='transformationtechnique', blank=True, null=True)
    providerqc = models.ForeignKey('Qctest', db_column='providerqc', blank=True, null=True)
    providerqcreport = models.ForeignKey('Document', db_column='providerqcreport', blank=True, null=True)
    cellstrainoforigin = models.CharField(max_length=90, blank=True)
    originaltissuetype = models.ForeignKey('Tissuesource', db_column='originaltissuetype', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinederivation'


class Celllinedisease(models.Model):
    idcelllinedisease = models.IntegerField(primary_key=True)
    cellline = models.ForeignKey(Cellline, db_column='cellline', unique=True, related_name='disease')
    celllinedisease = models.ForeignKey('Disease', db_column='celllinedisease', blank=True, null=True)
    celllinediseasestage = models.ForeignKey('Diseasestage', db_column='celllinediseasestage', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinedisease'


class Celllinefunctionalcharacter(models.Model):
    idcelllinefunctionalcharacter = models.IntegerField(primary_key=True, editable=False)
    cellline = models.ForeignKey(Cellline, db_column='cellline', blank=True, null=True)
    karotypeabnormaldiagnosed = models.IntegerField(blank=True, null=True)
    karotypingavailable = models.IntegerField(blank=True, null=True)
    karotypehipassage = models.IntegerField(blank=True, null=True)
    karotypechange = models.CharField(max_length=90, blank=True)
    geneticmanipulationmutation = models.CharField(max_length=90, blank=True)
    morphologymethod = models.ForeignKey('Morphologymethod', db_column='morphologymethod', blank=True, null=True)
    morphologydocurl = models.CharField(max_length=200, blank=True)
    passageused = models.CharField(max_length=90, blank=True)
    passagemethod = models.IntegerField(blank=True, null=True)
    invitrodiffectoderm = models.IntegerField(blank=True, null=True)
    invitrodiffmesoderm = models.IntegerField(blank=True, null=True)
    invitrodiffendoderm = models.IntegerField(blank=True, null=True)
    invivoteratomaassaygermlayerder = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'celllinefunctionalcharacter'


class Celllinegeneration(models.Model):
    idcelllinegeneration = models.IntegerField(primary_key=True, editable=False)
    cellline = models.ForeignKey(Cellline, db_column='cellline', blank=True, null=True)
    vectortype = models.IntegerField(blank=True, null=True)
    vectorused = models.ForeignKey('Vectorused', db_column='vectorused', blank=True, null=True)
    vector = models.ForeignKey('Vector', db_column='vector', blank=True, null=True)
    cloneselectioncriteria = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'celllinegeneration'


class Celllinegenotype(models.Model):
    idcelllinegenotype = models.IntegerField(primary_key=True, editable=False)
    cellline = models.ForeignKey(Cellline, db_column='cellline', blank=True, null=True)
    genotype = models.ForeignKey('Genotype', db_column='genotype', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinegenotype'


class Celllinelegal(models.Model):
    idcelllinelegal = models.IntegerField(primary_key=True, editable=False)
    cellline = models.IntegerField(blank=True, null=True)
    q1donorconsent = models.IntegerField(blank=True, null=True)
    q2donortrace = models.IntegerField(blank=True, null=True)
    q3irbapproval = models.IntegerField(blank=True, null=True)
    q4approveduse = models.IntegerField(blank=True, null=True)
    q5informedconsent = models.CharField(max_length=200, blank=True)
    q6restrictions = models.CharField(max_length=200, blank=True)
    q7iprestrictions = models.CharField(max_length=200, blank=True)
    q8jurisdiction = models.CharField(max_length=200, blank=True)
    q9applicablelegislationandregulation = models.CharField(max_length=200, blank=True)
    q10managedaccess = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'celllinelegal'


class Celllinemolecularcharacterization(models.Model):
    idmolecularcharacterization = models.IntegerField(primary_key=True, editable=False)
    cellline = models.ForeignKey(Cellline, db_column='cellline', blank=True, null=True)
    retroviralsilencing = models.CharField(max_length=200, blank=True)
    transgeneintegrationlocation = models.CharField(max_length=200, blank=True)
    transgenesilencing = models.CharField(max_length=200, blank=True)
    hlatyping = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'celllinemolecularcharacterization'


class Celllinepluripotentmarkers(models.Model):
    idcelllinepluripotentmarkers = models.IntegerField(primary_key=True, editable=False)
    cellline = models.IntegerField(unique=True)
    celllinepluripotentmarker1 = models.ForeignKey(Cellline, db_column='celllinepluripotentmarker1', blank=True, null=True)
    celllinepluripotentmarker2 = models.ForeignKey('Pluripotentmarker2', db_column='celllinepluripotentmarker2', blank=True, null=True)
    celllinepluripotentmarker3 = models.ForeignKey('Pluripotentmarker3', db_column='celllinepluripotentmarker3', blank=True, null=True)
    celllinepluripotentmarker4 = models.ForeignKey('Pluripotentmarker4', db_column='celllinepluripotentmarker4', blank=True, null=True)
    celllinepluripotentmarker5 = models.ForeignKey('Pluripotentmarker5', db_column='celllinepluripotentmarker5', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinepluripotentmarkers'


class Celllinepublication(models.Model):
    idcelllinepublication = models.IntegerField(primary_key=True, editable=False)
    cellline = models.ForeignKey(Cellline, db_column='cellline', blank=True, null=True)
    celllinepublicationdoiurl = models.CharField(max_length=2000, blank=True)
    celllinepublisher = models.ForeignKey('Publisher', db_column='celllinepublisher', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinepublication'


class Celllinereprogramming(models.Model):
    idcelllinereprogramming = models.IntegerField(primary_key=True, editable=False)
    cellline = models.ForeignKey(Cellline, db_column='cellline', blank=True, null=True)
    epigeneticregulators = models.CharField(max_length=90, blank=True)
    inhibibitors = models.CharField(max_length=90, blank=True)
    smallmolecules = models.CharField(max_length=90, blank=True)
    microrna = models.CharField(max_length=90, blank=True)
    proliferationcellcycleregulators = models.CharField(max_length=90, blank=True)
    others = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'celllinereprogramming'


class Celllinestatus(models.Model):
    idcelllinestatus = models.IntegerField(primary_key=True, editable=False)
    celllinestatus = models.CharField(max_length=40, blank=True)

    def __unicode__(self):
        return self.celllinestatus

    class Meta:
        managed = False
        db_table = 'celllinestatus'


class Celllinevalue(models.Model):
    idcelllinevalue = models.IntegerField(primary_key=True, editable=False)
    celllineid = models.ForeignKey(Cellline, db_column='celllineid', blank=True, null=True)
    potentialuse = models.CharField(max_length=200, blank=True)
    valuetosociety = models.CharField(max_length=200, blank=True)
    valuetoresearch = models.CharField(max_length=200, blank=True)
    othervalue = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'celllinevalue'


class Celltype(models.Model):
    idcelltype = models.IntegerField(primary_key=True, editable=False)
    celltype = models.CharField(max_length=60, blank=True)

    def __unicode__(self):
        return self.celltype

    class Meta:
        managed = False
        db_table = 'celltype'


class City(models.Model):
    idcity = models.IntegerField(primary_key=True, editable=False)
    city = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'city'


class Clinicaltreatmentb4Donation(models.Model):
    idclininicaltreatmentb4donation = models.IntegerField(primary_key=True, editable=False)
    clininicaltreatmentb4donation = models.CharField(max_length=90, blank=True)

    def __unicode__(self):
        return self.clininicaltreatmentb4donation

    class Meta:
        managed = False
        db_table = 'clinicaltreatmentb4donation'


class Contact(models.Model):
    idcontact = models.IntegerField(primary_key=True, editable=False)
    contacttype = models.IntegerField(blank=True, null=True)
    contactcountry = models.IntegerField(blank=True, null=True)
    contactpostcode = models.IntegerField(blank=True, null=True)
    contacttatecounty = models.IntegerField(blank=True, null=True)
    contactcity = models.CharField(max_length=90, blank=True)
    contactaddress1 = models.CharField(max_length=90, blank=True)
    contactaddress2 = models.CharField(max_length=90, blank=True)
    contactphonecountrycode = models.IntegerField(blank=True, null=True)
    contactphone = models.CharField(max_length=40)
    contactwebsite = models.CharField(max_length=90, blank=True)
    contactemailaddress = models.CharField(max_length=90)
    contactfax = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'contact'


class Contacttype(models.Model):
    idcontacttype = models.IntegerField(primary_key=True, editable=False)
    contacttype = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'contacttype'


class Country(models.Model):
    idcountry = models.IntegerField(primary_key=True, editable=False)
    country = models.CharField(max_length=90, blank=True)
    countrycode = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'country'


class Culturemedium(models.Model):
    idculturemedium = models.IntegerField(primary_key=True, editable=False)
    culturemedium = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'culturemedium'


class Depositor(models.Model):
    iddepositor = models.IntegerField(db_column='idDepositor', unique=True, primary_key=True, editable=False)
    organization = models.IntegerField(blank=True, null=True)
    depositorstatus = models.IntegerField(blank=True, null=True)
    depositorregistrationdate = models.CharField(max_length=40)

    def __unicode__(self):
        return u'%s-%s-%s' % (self.organization, self.depositorstatus, self.depositorregistrationdate)

    class Meta:
        managed = False
        db_table = 'depositor'


class Depositorcontacttype(models.Model):
    iddepositorcontacttype = models.IntegerField(primary_key=True, editable=False)
    depositorcontacttype = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'depositorcontacttype'


class Derivationmethod(models.Model):
    idderivationmethod = models.IntegerField(primary_key=True, editable=False)
    derivationmethod = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'derivationmethod'


class Disease(models.Model):
    iddisease = models.IntegerField(primary_key=True, editable=False)
    icdcode = models.CharField(unique=True, max_length=20, blank=True)
    disease = models.CharField(max_length=90, blank=True)

    def __unicode__(self):
        return self.disease

    class Meta:
        ordering = ['disease']
        managed = False
        db_table = 'disease'


class Diseasestage(models.Model):
    iddiseasestage = models.IntegerField(primary_key=True, editable=False)
    disease = models.ForeignKey(Disease, db_column='disease', blank=True, null=True)
    diseasestage = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'diseasestage'


class Document(models.Model):
    iddocument = models.IntegerField(primary_key=True, editable=False)
    cellline = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=90, blank=True)
    abstract = models.CharField(max_length=2000, blank=True)
    documenttype = models.IntegerField(blank=True, null=True)
    documentdepositor = models.IntegerField(blank=True, null=True)
    authors = models.CharField(max_length=2000, blank=True)
    owner = models.IntegerField(blank=True, null=True)
    version = models.CharField(max_length=10, blank=True)
    accesslevel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document'


class Documenttype(models.Model):
    iddocumenttype = models.IntegerField(primary_key=True, editable=False)
    documenttype = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'documenttype'


class Donor(models.Model):
    iddonor = models.IntegerField(primary_key=True, editable=False)
    provider = models.IntegerField(blank=True, null=True)
    age = models.ForeignKey(Binnedage, db_column='age', blank=True, null=True)
    gender = models.ForeignKey('Gender', db_column='gender', blank=True, null=True)
    countryoforigin = models.ForeignKey(Country, db_column='countryoforigin', blank=True, null=True)
    primarydisease = models.ForeignKey(Disease, db_column='primarydisease', blank=True, null=True)
    diseasestage = models.ForeignKey(Diseasestage, db_column='diseasestage', blank=True, null=True)
    phenotype = models.ForeignKey('Phenotype', db_column='phenotype', blank=True, null=True)
    otherclinicalinformation = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return u'%s-%s-%s' % (self.provider, self.age, self.gender)

    class Meta:
        managed = False
        db_table = 'donor'


class Donorsecondarydiseases(models.Model):
    iddonorsecondarydiseases = models.IntegerField(primary_key=True, editable=False)
    donor = models.ForeignKey(Donor, db_column='donor', blank=True, null=True)
    disease = models.ForeignKey(Disease, db_column='disease', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donorsecondarydiseases'


class Ebisckeyword(models.Model):
    idebisckeyword = models.IntegerField(primary_key=True, editable=False)
    cellline = models.ForeignKey(Cellline, db_column='cellline', blank=True, null=True)
    document = models.ForeignKey(Document, db_column='document', blank=True, null=True)
    ebisckeyword = models.ForeignKey('Keyword', db_column='ebisckeyword', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebisckeyword'


class Gender(models.Model):
    idgender = models.IntegerField(db_column='idGender', primary_key=True, editable=False)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=20, blank=True)  # Field name made lowercase.

    def __unicode__(self):
        return self.gender

    class Meta:
        managed = False
        db_table = 'gender'


class Genotype(models.Model):
    idgenotype = models.IntegerField(primary_key=True, editable=False)
    genotype = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'genotype'


class Keyword(models.Model):
    idkeyword = models.IntegerField(primary_key=True, editable=False)
    keyword = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'keyword'


class Morphologymethod(models.Model):
    idmorphologymethod = models.IntegerField(primary_key=True, editable=False)
    morphologymethod = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'morphologymethod'


class Organizations(models.Model):
    idorganization = models.IntegerField(primary_key=True, editable=False)
    organizationname = models.CharField(max_length=90, blank=True)
    organizationshortname = models.CharField(unique=True, max_length=8, blank=True)
    organizationcontact = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organizations'


class Orgcontact(models.Model):
    iddepositorpoc = models.IntegerField(primary_key=True, editable=False)
    depositor = models.IntegerField(blank=True, null=True)
    depositorpocperson = models.IntegerField(blank=True, null=True)
    depositorpoctype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgcontact'


class Passagemethod(models.Model):
    idpassagemethod = models.IntegerField(primary_key=True, editable=False)
    passagemethod = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'passagemethod'


class Persons(models.Model):
    idperson = models.IntegerField(primary_key=True, editable=False)
    organization = models.IntegerField(blank=True, null=True)
    personlastname = models.CharField(max_length=40, blank=True)
    personfirstname = models.CharField(max_length=90, blank=True)
    personcontact = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons'


class Phenotype(models.Model):
    idphenotype = models.IntegerField(primary_key=True, editable=False)
    phenotype = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'phenotype'


class Phonecountrycode(models.Model):
    idphonecountrycode = models.IntegerField(primary_key=True, editable=False)
    phonecountrycode = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phonecountrycode'


class Pluripotentmarker1(models.Model):
    idpluripotentmarker1 = models.IntegerField(primary_key=True, editable=False)
    pluripotentmarker1 = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'pluripotentmarker1'


class Pluripotentmarker2(models.Model):
    idpluripotentmarker2 = models.IntegerField(primary_key=True, editable=False)
    pluripotentmarker2 = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'pluripotentmarker2'


class Pluripotentmarker3(models.Model):
    idpluripotentmarker3 = models.IntegerField(primary_key=True, editable=False)
    pluripotentmarker3 = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'pluripotentmarker3'


class Pluripotentmarker4(models.Model):
    idpluripotentmarker4 = models.IntegerField(primary_key=True, editable=False)
    pluripotentmarker4 = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'pluripotentmarker4'


class Pluripotentmarker5(models.Model):
    idpluripotentmarker5 = models.IntegerField(primary_key=True, editable=False)
    pluripotentmarker5 = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'pluripotentmarker5'


class Postcode(models.Model):
    idpostcode = models.IntegerField(primary_key=True, editable=False)
    postcode = models.CharField(max_length=90, blank=True)
    district = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'postcode'


class Publisher(models.Model):
    idpublisher = models.IntegerField(primary_key=True, editable=False)
    publisher = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'publisher'


class Qctest(models.Model):
    idqctest = models.IntegerField(primary_key=True, editable=False)
    qctest = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'qctest'


class Raceethnicgroup(models.Model):
    idethnicgroup = models.IntegerField(primary_key=True, editable=False)
    ethnicgroup = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'raceethnicgroup'


class Stateprovincecounty(models.Model):
    idstateprovince = models.IntegerField(primary_key=True, editable=False)
    stateprovincecounty = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'stateprovincecounty'


class Surfacecoatingmatrix(models.Model):
    idsurfacecoatingmatrix = models.IntegerField(primary_key=True, editable=False)
    surfacecoatingmatrix = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'surfacecoatingmatrix'


class Tissuesource(models.Model):
    idtissuesource = models.IntegerField(primary_key=True, editable=False)
    tissuesource = models.CharField(max_length=90, blank=True)

    def __unicode__(self):
        return self.tissuesource

    class Meta:
        managed = False
        db_table = 'tissuesource'


class Transformationtechnique(models.Model):
    idtransformationtechnique = models.IntegerField(primary_key=True, editable=False)
    transformationtechnique = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'transformationtechnique'


class Useraccounttype(models.Model):
    iduseraccounttype = models.IntegerField(db_column='idUserAccountType', primary_key=True, editable=False)  # Field name made lowercase.
    useraccounttype = models.CharField(db_column='UserAccountType', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'useraccounttype'


class Vector(models.Model):
    idvector = models.IntegerField(db_column='idVector', primary_key=True, editable=False)  # Field name made lowercase.
    vector = models.CharField(db_column='Vector', max_length=20, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vector'


class Vectortype(models.Model):
    idvectortype = models.IntegerField(primary_key=True, editable=False)
    vectortype = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'vectortype'


class Vectorused(models.Model):
    idvector = models.IntegerField(primary_key=True, editable=False)
    vectorused = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'vectorused'


class Yesno(models.Model):
    idyesno = models.IntegerField(primary_key=True, editable=False)
    yesno = models.CharField(max_length=6, blank=True)

    class Meta:
        managed = False
        db_table = 'yesno'


class Yesno2(models.Model):
    idyesno2 = models.IntegerField(primary_key=True, editable=False)
    yesno2 = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'yesno2'


class Yesno3(models.Model):
    idyesno3 = models.IntegerField(primary_key=True, editable=False)
    yesno3 = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'yesno3'


class Yesno4(models.Model):
    idyesno4 = models.IntegerField(primary_key=True, editable=False)
    yesno4 = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'yesno4'


class Yesno5(models.Model):
    idyesno5 = models.IntegerField(primary_key=True, editable=False)
    yesno5 = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'yesno5'


class Yesno6(models.Model):
    idyesno6 = models.IntegerField(primary_key=True, editable=False)
    yesno6 = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'yesno6'
