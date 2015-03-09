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
    idaccesslevel = models.IntegerField(primary_key=True)
    accesslevel = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'accesslevel'


class Aliquotstatus(models.Model):
    idcelllinealiquotstatus = models.IntegerField(primary_key=True)
    aliquotstatus = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'aliquotstatus'


class Approveduse(models.Model):
    idapproveduse = models.IntegerField(primary_key=True)
    approveduse = models.CharField(max_length=60, blank=True)

    class Meta:
        managed = False
        db_table = 'approveduse'


class Batchstatus(models.Model):
    idbatchstatus = models.IntegerField(primary_key=True)
    batchstatus = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'batchstatus'


class Binnedage(models.Model):
    idbinnedage = models.IntegerField(primary_key=True)
    binnedage = models.CharField(max_length=5, blank=True)

    class Meta:
        managed = False
        db_table = 'binnedage'


class Cellline(models.Model):
    idcellline = models.IntegerField(primary_key=True)
    biosamplesid = models.CharField(unique=True, max_length=12)
    celllinename = models.CharField(unique=True, max_length=15)
    celllinedonor = models.ForeignKey('Donor', db_column='celllinedonor', blank=True, null=True)
    celllineprimarydisease = models.ForeignKey('Disease', db_column='celllineprimarydisease', blank=True, null=True)
    celllinediseaseaddinfo = models.CharField(max_length=100, blank=True)
    celllinestatus = models.ForeignKey('Celllinestatus', db_column='celllinestatus', blank=True, null=True)
    celllinecelltype = models.ForeignKey('Celltype', db_column='celllinecelltype', blank=True, null=True)
    celllinecollection = models.ForeignKey('Celllinecollection', db_column='celllinecollection', blank=True, null=True)
    celllinetissuesource = models.ForeignKey('Tissuesource', db_column='celllinetissuesource', blank=True, null=True)
    celllinetissuetreatment = models.ForeignKey('Clinicaltreatmentb4Donation', db_column='celllinetissuetreatment', blank=True, null=True)
    celllinetissuedate = models.DateField(blank=True, null=True)
    celllinenamesynonyms = models.CharField(max_length=1000, blank=True)
    depositorscelllineuri = models.CharField(max_length=45, blank=True)
    celllinecomments = models.CharField(max_length=1000, blank=True)
    celllineupdate = models.DateField(blank=True, null=True)
    celllineupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllineupdatetype', blank=True, null=True)
    celllineupdatedby = models.ForeignKey('Useraccount', db_column='celllineupdatedby', blank=True, null=True)
    celllineecaccurl = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'cellline'


class Celllinealiquot(models.Model):
    idcelllinealiquot = models.IntegerField(primary_key=True)
    aliquotcellline = models.ForeignKey(Cellline, db_column='aliquotcellline', blank=True, null=True)
    aliquotstatus = models.ForeignKey(Aliquotstatus, db_column='aliquotstatus', blank=True, null=True)
    aliquotstatusdate = models.CharField(max_length=20, blank=True)
    aliquotupdatedby = models.ForeignKey('Useraccount', db_column='aliquotupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinealiquot'


class Celllineannotation(models.Model):
    idcelllineannotation = models.IntegerField(db_column='idCelllineannotation', primary_key=True)  # Field name made lowercase.
    annotationcellline = models.ForeignKey(Cellline, db_column='annotationcellline', blank=True, null=True)
    celllineannotationsource = models.CharField(max_length=45, blank=True)
    celllineannotationsourceid = models.CharField(max_length=45, blank=True)
    celllineannotationsourceversion = models.CharField(max_length=45, blank=True)
    celllineannotation = models.CharField(max_length=1000, blank=True)
    celllineannotationupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllineannotationupdatetype', blank=True, null=True)
    celllineannotationupdate = models.DateField(blank=True, null=True)
    celllineannotationupdatedby = models.ForeignKey('Useraccount', db_column='celllineannotationupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllineannotation'


class Celllinebatch(models.Model):
    idcelllinebatch = models.IntegerField(primary_key=True)
    batchcellline = models.ForeignKey(Cellline, db_column='batchcellline', blank=True, null=True)
    batchstatus = models.ForeignKey(Batchstatus, db_column='batchstatus', blank=True, null=True)
    batchstatusdate = models.CharField(max_length=20, blank=True)
    batchstatusupdatedby = models.ForeignKey('Useraccount', db_column='batchstatusupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinebatch'


class Celllinecharacterization(models.Model):
    idcelllinecharacterization = models.IntegerField(primary_key=True)
    characterizationcellline = models.ForeignKey(Cellline, db_column='characterizationcellline', blank=True, null=True)
    certificateofanalysispassage = models.CharField(max_length=5, blank=True)
    hiv1screening = models.IntegerField(blank=True, null=True)
    hiv2screening = models.IntegerField(blank=True, null=True)
    hepititusb = models.IntegerField(blank=True, null=True)
    hepititusc = models.IntegerField(blank=True, null=True)
    mycoplasma = models.IntegerField(blank=True, null=True)
    celllinecharacterizationupdate = models.DateField(blank=True, null=True)
    celllinecharacterizationupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinecharacterizationupdatetype', blank=True, null=True)
    celllinecharacterizationupdateby = models.ForeignKey('Useraccount', db_column='celllinecharacterizationupdateby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinecharacterization'


class Celllinecollection(models.Model):
    idcelllinecollection = models.IntegerField(primary_key=True)
    celllinecollectiontotal = models.IntegerField(blank=True, null=True)
    celllinecollectionupdate = models.DateField(blank=True, null=True)
    celllinecollectionupdatetype = models.IntegerField(blank=True, null=True)
    celllinecollectionupdatedby = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'celllinecollection'


class Celllinecomments(models.Model):
    idcelllinecomments = models.IntegerField(primary_key=True)
    commentscellline = models.IntegerField(blank=True, null=True)
    celllinecomments = models.TextField(blank=True)
    celllinecommentsupdated = models.DateField(blank=True, null=True)
    celllinecommentsupdatedtype = models.IntegerField(blank=True, null=True)
    celllinecommentsupdatedby = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinecomments'


class Celllinecultureconditions(models.Model):
    idcellinecultureconditions = models.IntegerField(primary_key=True)
    cultureconditionscellline = models.ForeignKey(Cellline, db_column='cultureconditionscellline', blank=True, null=True)
    surfacecoating = models.ForeignKey('Surfacecoating', db_column='surfacecoating', blank=True, null=True)
    feedercelltype = models.CharField(max_length=45, blank=True)
    feedercellid = models.CharField(max_length=45, blank=True)
    passagemethod = models.ForeignKey('Passagemethod', db_column='passagemethod', blank=True, null=True)
    enzymatically = models.ForeignKey('Enzymatically', db_column='enzymatically', blank=True, null=True)
    enzymefree = models.ForeignKey('Enzymefree', db_column='enzymefree', blank=True, null=True)
    o2concentration = models.IntegerField(blank=True, null=True)
    co2concentration = models.IntegerField(blank=True, null=True)
    culturemedium = models.ForeignKey('Culturemedium', db_column='culturemedium', blank=True, null=True)
    celllinecultureconditionsupdate = models.DateField(blank=True, null=True)
    celllinecultureconditionsupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinecultureconditionsupdatetype', blank=True, null=True)
    celllinecultureconditionsupdatedby = models.ForeignKey('Useraccount', db_column='celllinecultureconditionsupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinecultureconditions'


class Celllineculturesupplements(models.Model):
    idcelllineculturesupplements = models.IntegerField(primary_key=True)
    celllinecultureconditions = models.ForeignKey(Celllinecultureconditions, db_column='celllinecultureconditions', blank=True, null=True)
    supplement = models.CharField(max_length=45, blank=True)
    supplementamount = models.CharField(max_length=45, blank=True)
    supplementamountunit = models.ForeignKey('Units', db_column='supplementamountunit', blank=True, null=True)
    celllineculturesupplementsupdated = models.DateField(blank=True, null=True)
    celllineculturesupplementsupdatedtype = models.ForeignKey('Lastupdatetype', db_column='celllineculturesupplementsupdatedtype', blank=True, null=True)
    celllineculturesupplementsupdatedby = models.ForeignKey('Useraccount', db_column='celllineculturesupplementsupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllineculturesupplements'


class Celllinederivation(models.Model):
    idcelllinederivation = models.IntegerField(primary_key=True)
    derivationcellline = models.ForeignKey(Cellline, db_column='derivationcellline', blank=True, null=True)
    primarycelltypename = models.CharField(max_length=45, blank=True)
    primarycelltypecellfinderid = models.CharField(max_length=45, blank=True)
    primarycelldevelopmentalstage = models.ForeignKey('Primarycelldevelopmentalstage', db_column='primarycelldevelopmentalstage', blank=True, null=True)
    selectioncriteriaforclones = models.CharField(max_length=1000, blank=True)
    xenofreeconditions = models.CharField(max_length=4, blank=True)
    derivedundergmp = models.CharField(max_length=4, blank=True)
    availableasclinicalgrade = models.CharField(max_length=4, blank=True)
    celllinederivationupdated = models.DateField(blank=True, null=True)
    celllinederivationupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinederivationupdatetype', blank=True, null=True)
    celllinederivationupdatedby = models.ForeignKey('Useraccount', db_column='celllinederivationupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinederivation'


class Celllinediffpotency(models.Model):
    idcelllinediffpotency = models.IntegerField(primary_key=True)
    diffpotencycellline = models.ForeignKey(Cellline, db_column='diffpotencycellline', blank=True, null=True)
    passagenumber = models.CharField(max_length=5, blank=True)
    germlayer = models.ForeignKey('Germlayer', db_column='germlayer', blank=True, null=True)
    celllinediffpotencyupdated = models.DateField(blank=True, null=True)
    celllinediffpotencyupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinediffpotencyupdatetype', blank=True, null=True)
    celllinediffpotencyupdatedby = models.ForeignKey('Useraccount', db_column='celllinediffpotencyupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinediffpotency'


class Celllinediffpotencymarker(models.Model):
    idcelllinediffpotencymarker = models.IntegerField(primary_key=True)
    celllinediffpotency = models.ForeignKey(Celllinediffpotency, db_column='celllinediffpotency', blank=True, null=True)
    morphologymethod = models.ForeignKey('Morphologymethod', db_column='morphologymethod', blank=True, null=True)
    celllinediffpotencymarkerupdate = models.DateField(blank=True, null=True)
    celllinediffpotencymarkerupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinediffpotencymarkerupdatetype', blank=True, null=True)
    celllinediffpotencymarkerupdatedby = models.ForeignKey('Useraccount', db_column='celllinediffpotencymarkerupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinediffpotencymarker'


class Celllinediffpotencymolecule(models.Model):
    idcelllinediffpotencymolecule = models.IntegerField(primary_key=True)
    celllinediffpotencymarker = models.IntegerField(blank=True, null=True)
    diffpotencymolecule = models.ForeignKey('Molecule', db_column='diffpotencymolecule', blank=True, null=True)
    diffpotencymoleculeupdate = models.DateField(blank=True, null=True)
    diffpotencymoleculeupdatetype = models.ForeignKey('Lastupdatetype', db_column='diffpotencymoleculeupdatetype', blank=True, null=True)
    diffpotencymoleculeupdatedby = models.ForeignKey('Useraccount', db_column='diffpotencymoleculeupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinediffpotencymolecule'


class Celllinegenemutations(models.Model):
    idcelllinegenemutations = models.IntegerField(primary_key=True)
    genemutationscellline = models.ForeignKey(Cellline, db_column='genemutationscellline', blank=True, null=True)
    weblink = models.CharField(max_length=100, blank=True)
    celllinegenemutationsupdate = models.DateField(blank=True, null=True)
    celllinegenemutationsupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinegenemutationsupdatetype', blank=True, null=True)
    celllinegenemutationsupdatedby = models.ForeignKey('Useraccount', db_column='celllinegenemutationsupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinegenemutations'


class Celllinegenemutationsmolecule(models.Model):
    idcelllinegenemutationsmolecule = models.IntegerField(primary_key=True)
    celllinegenemutations = models.ForeignKey(Celllinegenemutations, db_column='celllinegenemutations', blank=True, null=True)
    genemutationsmolecule = models.ForeignKey('Molecule', db_column='genemutationsmolecule', blank=True, null=True)
    celllinegenemutationsmoleculeupdate = models.DateField(blank=True, null=True)
    celllinegenemutationsmoleculeupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinegenemutationsmoleculeupdatetype', blank=True, null=True)
    celllinegenemutationsmoleculeupdatedby = models.ForeignKey('Useraccount', db_column='celllinegenemutationsmoleculeupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinegenemutationsmolecule'


class Celllinegeneticmod(models.Model):
    idcelllinegeneticmod = models.IntegerField(primary_key=True)
    geneticmodcellline = models.ForeignKey(Cellline, db_column='geneticmodcellline', blank=True, null=True)
    celllinegeneticmod = models.CharField(max_length=45, blank=True)
    celllinegeneticmodupdate = models.DateField(blank=True, null=True)
    celllinegeneticmodupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinegeneticmodupdatetype', blank=True, null=True)
    celllinegeneticmodupdatedby = models.ForeignKey('Useraccount', db_column='celllinegeneticmodupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinegeneticmod'


class Celllinegenomeseq(models.Model):
    idcelllinegenomeseq = models.IntegerField(primary_key=True)
    genomeseqcellline = models.ForeignKey(Cellline, db_column='genomeseqcellline', blank=True, null=True)
    celllinegenomeseqlink = models.CharField(max_length=45, blank=True)
    celllinegenomesequpdate = models.DateField(blank=True, null=True)
    celllinegenomesequpdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinegenomesequpdatetype', blank=True, null=True)
    celllinegenomesequpdatedby = models.ForeignKey('Useraccount', db_column='celllinegenomesequpdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinegenomeseq'


class Celllinegenotypingother(models.Model):
    idcelllinegenotypingother = models.IntegerField(primary_key=True)
    genometypothercellline = models.ForeignKey(Cellline, db_column='genometypothercellline', blank=True, null=True)
    celllinegenotypingother = models.CharField(max_length=1000, blank=True)
    celllinegenotypingotherupdate = models.DateField(blank=True, null=True)
    celllinegenotypingotherupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinegenotypingotherupdatetype', blank=True, null=True)
    celllinegenotypingotherupdatedby = models.ForeignKey('Useraccount', db_column='celllinegenotypingotherupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinegenotypingother'


class Celllinehlatyping(models.Model):
    idcelllinehlatyping = models.IntegerField(primary_key=True)
    hlatypingcellline = models.ForeignKey(Cellline, db_column='hlatypingcellline', blank=True, null=True)
    celllinehlaclass = models.IntegerField(blank=True, null=True)
    celllinehla = models.ForeignKey('Hla', db_column='celllinehla', blank=True, null=True)
    celllinehlaallele1 = models.CharField(max_length=45, blank=True)
    celllinehlaallele2 = models.CharField(max_length=45, blank=True)
    celllinehlatypingupdate = models.DateField(blank=True, null=True)
    celllinehlatypingupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinehlatypingupdatetype', blank=True, null=True)
    celllinehlatypingupdatedby = models.ForeignKey('Useraccount', db_column='celllinehlatypingupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinehlatyping'


class Celllinekaryotype(models.Model):
    idcelllinekaryotype = models.IntegerField(primary_key=True)
    karyotypecellline = models.ForeignKey(Cellline, db_column='karyotypecellline', blank=True, null=True)
    passagenumber = models.CharField(max_length=5, blank=True)
    karyotype = models.CharField(max_length=45, blank=True)
    karyotypemethod = models.ForeignKey('Karyotypemethod', db_column='karyotypemethod', blank=True, null=True)
    celllinekaryotypeupdate = models.DateField(blank=True, null=True)
    celllinekaryotypeupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinekaryotypeupdatetype', blank=True, null=True)
    celllinekaryotypeupdatedby = models.ForeignKey('Useraccount', db_column='celllinekaryotypeupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinekaryotype'


class Celllinelab(models.Model):
    idcelllinelab = models.IntegerField(primary_key=True)
    labcellline = models.ForeignKey(Cellline, db_column='labcellline', blank=True, null=True)
    cryodate = models.DateField(blank=True, null=True)
    expansioninprogress = models.IntegerField(blank=True, null=True)
    funder = models.CharField(max_length=45, blank=True)
    reprogrammingmethod1 = models.ForeignKey('Reprogrammingmethod1', db_column='reprogrammingmethod1', blank=True, null=True)
    reprogrammingmethod2 = models.ForeignKey('Reprogrammingmethod2', db_column='reprogrammingmethod2', blank=True, null=True)
    reprogrammingmethod3 = models.ForeignKey('Reprogrammingmethod3', db_column='reprogrammingmethod3', blank=True, null=True)
    clonenumber = models.IntegerField(blank=True, null=True)
    passagenumber = models.CharField(max_length=5, blank=True)
    culturesystem = models.ForeignKey('Culturesystem', db_column='culturesystem', blank=True, null=True)
    culturesystemcomment = models.CharField(max_length=45, blank=True)
    celllinelabupdate = models.DateField(blank=True, null=True)
    celllinelabupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinelabupdatetype', blank=True, null=True)
    celllinelabupdatedby = models.ForeignKey('Useraccount', db_column='celllinelabupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinelab'


class Celllinelegal(models.Model):
    idcelllinelegal = models.IntegerField(primary_key=True)
    legalcellline = models.ForeignKey(Cellline, db_column='legalcellline', blank=True, null=True)
    q1donorconsent = models.IntegerField(blank=True, null=True)
    q2donortrace = models.IntegerField(blank=True, null=True)
    q3irbapproval = models.IntegerField(blank=True, null=True)
    q4approveduse = models.ForeignKey(Approveduse, db_column='q4approveduse', blank=True, null=True)
    q5informedconsentreference = models.CharField(max_length=20, blank=True)
    q6restrictions = models.CharField(max_length=1000, blank=True)
    q7iprestrictions = models.CharField(max_length=1000, blank=True)
    q8jurisdiction = models.ForeignKey('Country', db_column='q8jurisdiction', blank=True, null=True)
    q9applicablelegislationandregulation = models.CharField(max_length=1000, blank=True)
    q10managedaccess = models.CharField(max_length=1000, blank=True)
    celllinelegalupdate = models.DateField(blank=True, null=True)
    celllinelegalupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinelegalupdatetype', blank=True, null=True)
    celllinelegalupdatedby = models.ForeignKey('Useraccount', db_column='celllinelegalupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinelegal'


class Celllinemarker(models.Model):
    idcelllinemarker = models.IntegerField(primary_key=True)
    markercellline = models.ForeignKey(Cellline, db_column='markercellline', unique=True)
    morphologymethod = models.ForeignKey('Morphologymethod', db_column='morphologymethod', blank=True, null=True)
    celllinemarker = models.ForeignKey('Marker', db_column='celllinemarker', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinemarker'


class Celllineorganization(models.Model):
    idcelllineorganization = models.IntegerField(unique=True)
    orgcellline = models.ForeignKey(Cellline, db_column='orgcellline', blank=True, null=True)
    organization = models.ForeignKey('Organization', db_column='organization', blank=True, null=True)
    celllineorgtype = models.ForeignKey('Celllineorgtype', db_column='celllineorgtype', blank=True, null=True)
    orgstatus = models.IntegerField(blank=True, null=True)
    orgregistrationdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllineorganization'


class Celllineorgtype(models.Model):
    idcelllineorgtype = models.IntegerField(primary_key=True)
    celllineorgtype = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'celllineorgtype'


class Celllinepublication(models.Model):
    idcelllinepublication = models.IntegerField(primary_key=True)
    publicationcellline = models.ForeignKey(Cellline, db_column='publicationcellline', blank=True, null=True)
    pubmedreference = models.CharField(max_length=45, blank=True)
    celllinepublicationdoiurl = models.CharField(max_length=1000, blank=True)
    celllinepublisher = models.ForeignKey('Publisher', db_column='celllinepublisher', blank=True, null=True)
    celllinepublicationupdate = models.DateField(blank=True, null=True)
    celllinepublicationupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinepublicationupdatetype', blank=True, null=True)
    celllinepublicationupdatedby = models.ForeignKey('Useraccount', db_column='celllinepublicationupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinepublication'


class Celllinesnp(models.Model):
    idcelllinesnp = models.IntegerField(primary_key=True)
    snpcellline = models.ForeignKey(Cellline, db_column='snpcellline', blank=True, null=True)
    weblink = models.CharField(max_length=45, blank=True)
    celllinesnpupdate = models.DateField(blank=True, null=True)
    celllinesnpupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinesnpupdatetype', blank=True, null=True)
    celllinesnpupdatedby = models.ForeignKey('Useraccount', db_column='celllinesnpupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinesnp'


class Celllinesnpdetails(models.Model):
    idcelllinesnpdetails = models.IntegerField(primary_key=True)
    celllinesnp = models.ForeignKey(Celllinesnp, db_column='celllinesnp', blank=True, null=True)
    celllinesnpgene = models.CharField(max_length=45, blank=True)
    celllinesnpchromosomalposition = models.CharField(max_length=45, blank=True)
    celllinesnpdetailsupdate = models.DateField(blank=True, null=True)
    celllinesnpdetailsupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinesnpdetailsupdatetype', blank=True, null=True)
    celllinesnpdetailsupdatedby = models.ForeignKey('Useraccount', db_column='celllinesnpdetailsupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinesnpdetails'


class Celllinesnprslinks(models.Model):
    idcelllinesnprslinks = models.IntegerField(primary_key=True)
    celllinesnp = models.ForeignKey(Celllinesnp, db_column='celllinesnp', blank=True, null=True)
    rsnumber = models.CharField(max_length=45, blank=True)
    rslink = models.CharField(max_length=100, blank=True)
    celllinesnprslinksupdate = models.DateField(blank=True, null=True)
    celllinesnprslinksupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinesnprslinksupdatetype', blank=True, null=True)
    celllinesnprslinksupdatedby = models.ForeignKey('Useraccount', db_column='celllinesnprslinksupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinesnprslinks'


class Celllinestatus(models.Model):
    idcelllinestatus = models.IntegerField(primary_key=True)
    celllinestatus = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'celllinestatus'


class Celllinestrfingerprinting(models.Model):
    idcelllinestrfingerprinting = models.IntegerField(primary_key=True)
    strfpcellline = models.ForeignKey(Cellline, db_column='strfpcellline', blank=True, null=True)
    locus = models.ForeignKey('Strfplocus', db_column='locus', blank=True, null=True)
    allele1 = models.CharField(max_length=45, blank=True)
    allele2 = models.CharField(max_length=45, blank=True)
    celllinestrfpupdate = models.DateField(blank=True, null=True)
    celllinestrfpupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinestrfpupdatetype', blank=True, null=True)
    celllinestrfpupdatedby = models.ForeignKey('Useraccount', db_column='celllinestrfpupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinestrfingerprinting'


class Celllinevalue(models.Model):
    idcelllinevalue = models.IntegerField(primary_key=True)
    valuecellline = models.ForeignKey(Cellline, db_column='valuecellline', blank=True, null=True)
    potentialuse = models.CharField(max_length=100, blank=True)
    valuetosociety = models.CharField(max_length=100, blank=True)
    valuetoresearch = models.CharField(max_length=100, blank=True)
    othervalue = models.CharField(max_length=100, blank=True)
    celllinevalueupdate = models.DateField(blank=True, null=True)
    celllinevalueupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinevalueupdatetype', blank=True, null=True)
    celllinevalueupdatedby = models.ForeignKey('Useraccount', db_column='celllinevalueupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinevalue'


class Celllinevector(models.Model):
    idcelllinevector = models.IntegerField(primary_key=True)
    vectorcellline = models.ForeignKey(Cellline, db_column='vectorcellline', blank=True, null=True)
    vectortype = models.ForeignKey('Vectortype', db_column='vectortype', blank=True, null=True)
    vector = models.ForeignKey('Vector', db_column='vector', blank=True, null=True)
    vectorexcisable = models.CharField(max_length=4, blank=True)
    virus = models.ForeignKey('Virus', db_column='virus', blank=True, null=True)
    transposon = models.ForeignKey('Transposon', db_column='transposon', blank=True, null=True)
    celllinevectorupdate = models.DateField(blank=True, null=True)
    celllinevectorupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinevectorupdatetype', blank=True, null=True)
    celllinevectorupdatedby = models.ForeignKey('Useraccount', db_column='celllinevectorupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinevector'


class Celllinevectorfreereprogramming(models.Model):
    idcelllinevectorfreereprogramming = models.IntegerField(primary_key=True)
    vectorfreecellline = models.ForeignKey(Cellline, db_column='vectorfreecellline', blank=True, null=True)
    vectorfreereprogrammingfactor = models.ForeignKey('Vectorfreereprogramfactor', db_column='vectorfreereprogrammingfactor', blank=True, null=True)
    celllinevectorfreereprogupate = models.DateField(blank=True, null=True)
    celllinevectorfreereprogupatetype = models.ForeignKey('Lastupdatetype', db_column='celllinevectorfreereprogupatetype', blank=True, null=True)
    celllinevectorfreereprogupatedby = models.ForeignKey('Useraccount', db_column='celllinevectorfreereprogupatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinevectorfreereprogramming'


class Celllinevectormolecule(models.Model):
    idcelllinevectormolecule = models.IntegerField(primary_key=True)
    celllinevector = models.ForeignKey(Celllinevector, db_column='celllinevector', blank=True, null=True)
    molecule = models.ForeignKey('Molecule', db_column='molecule', blank=True, null=True)
    celllinevectormoleculeupdate = models.DateField(blank=True, null=True)
    celllinevectormoleculeupdatetype = models.ForeignKey('Lastupdatetype', db_column='celllinevectormoleculeupdatetype', blank=True, null=True)
    celllinevectormoleculeupdatedby = models.ForeignKey('Useraccount', db_column='celllinevectormoleculeupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celllinevectormolecule'


class Celltype(models.Model):
    idcelltype = models.IntegerField(primary_key=True)
    celltype = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'celltype'


class Clinicaltreatmentb4Donation(models.Model):
    idclininicaltreatmentb4donation = models.IntegerField(primary_key=True)
    clininicaltreatmentb4donation = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'clinicaltreatmentb4donation'


class Contact(models.Model):
    idcontact = models.IntegerField(primary_key=True)
    contacttype = models.ForeignKey('Contacttype', db_column='contacttype', blank=True, null=True)
    country = models.ForeignKey('Country', db_column='country')
    postcode = models.ForeignKey('Postcode', db_column='postcode')
    statecounty = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=45, blank=True)
    street = models.CharField(max_length=45, blank=True)
    buildingnumber = models.CharField(max_length=20, blank=True)
    suiteoraptordept = models.CharField(max_length=10, blank=True)
    officephonecountrycode = models.ForeignKey('Phonecountrycode', db_column='officephonecountrycode', blank=True, null=True)
    officephone = models.CharField(max_length=20, blank=True)
    faxcountrycode = models.ForeignKey('Phonecountrycode', db_column='faxcountrycode', blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True)
    mobilecountrycode = models.ForeignKey('Phonecountrycode', db_column='mobilecountrycode', blank=True, null=True)
    mobilephone = models.CharField(max_length=20, blank=True)
    website = models.CharField(max_length=45, blank=True)
    emailaddress = models.CharField(max_length=45, blank=True)
    contactupdate = models.DateField(blank=True, null=True)
    contactupdatetype = models.ForeignKey('Lastupdatetype', db_column='contactupdatetype', blank=True, null=True)
    contactupdatedby = models.ForeignKey('Useraccount', db_column='contactupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'


class Contacttype(models.Model):
    idcontacttype = models.IntegerField(primary_key=True)
    contacttype = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'contacttype'


class Country(models.Model):
    idcountry = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=45, blank=True)
    countrycode = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'country'


class Culturemedium(models.Model):
    idculturemedium = models.IntegerField(primary_key=True)
    culturemediumbase = models.CharField(max_length=45, blank=True)
    proteinsource = models.ForeignKey('Proteinsource', db_column='proteinsource', blank=True, null=True)
    serumconcentration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'culturemedium'


class Culturesystem(models.Model):
    idculturesystem = models.IntegerField(primary_key=True)
    culturesystem = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'culturesystem'


class Disease(models.Model):
    iddisease = models.IntegerField(primary_key=True)
    icdcode = models.CharField(unique=True, max_length=10, blank=True)
    disease = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'disease'


class Document(models.Model):
    iddocument = models.IntegerField(primary_key=True)
    cellline = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=45, blank=True)
    abstract = models.CharField(max_length=1000, blank=True)
    documenttype = models.ForeignKey('Documenttype', db_column='documenttype', blank=True, null=True)
    documentdepositor = models.IntegerField(blank=True, null=True)
    authors = models.CharField(max_length=1000, blank=True)
    owner = models.IntegerField(blank=True, null=True)
    version = models.CharField(max_length=5, blank=True)
    accesslevel = models.IntegerField(blank=True, null=True)
    documentupdate = models.IntegerField(blank=True, null=True)
    documentupdatetype = models.IntegerField(blank=True, null=True)
    documentupdatedby = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document'


class Documenttype(models.Model):
    iddocumenttype = models.IntegerField(primary_key=True)
    documenttype = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'documenttype'


class Donor(models.Model):
    iddonor = models.IntegerField(primary_key=True)
    hescregdonorid = models.CharField(max_length=3, blank=True)
    age = models.ForeignKey(Binnedage, db_column='age', blank=True, null=True)
    gender = models.ForeignKey('Gender', db_column='gender', blank=True, null=True)
    countryoforigin = models.ForeignKey(Country, db_column='countryoforigin', blank=True, null=True)
    primarydisease = models.ForeignKey(Disease, db_column='primarydisease', blank=True, null=True)
    diseaseadditionalinfo = models.CharField(max_length=45, blank=True)
    othercelllinefromdonor = models.ForeignKey(Cellline, db_column='othercelllinefromdonor', blank=True, null=True)
    parentcellline = models.ForeignKey(Cellline, db_column='parentcellline', blank=True, null=True)
    providerdonorid = models.CharField(max_length=45, blank=True)
    cellabnormalkaryotype = models.CharField(max_length=45, blank=True)
    donorabnormalkaryotype = models.CharField(max_length=45, blank=True)
    otherclinicalinformation = models.CharField(max_length=100, blank=True)
    phenotype = models.ForeignKey('Phenotype', db_column='phenotype', blank=True, null=True)
    donorupdate = models.DateField(blank=True, null=True)
    donorupdatetype = models.ForeignKey('Lastupdatetype', db_column='donorupdatetype', blank=True, null=True)
    donorupdatedby = models.ForeignKey('Useraccount', db_column='donorupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donor'


class Ebisckeyword(models.Model):
    idebisckeyword = models.IntegerField(primary_key=True)
    cellline = models.ForeignKey(Cellline, db_column='cellline', blank=True, null=True)
    document = models.ForeignKey(Document, db_column='document', blank=True, null=True)
    ebisckeyword = models.ForeignKey('Keyword', db_column='ebisckeyword', blank=True, null=True)
    ebisckeywordupdate = models.DateField(blank=True, null=True)
    ebisckeywordupdatetype = models.ForeignKey('Lastupdatetype', db_column='ebisckeywordupdatetype', blank=True, null=True)
    ebisckeywordupdatedby = models.ForeignKey('Useraccount', db_column='ebisckeywordupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebisckeyword'


class Enzymatically(models.Model):
    idenzymatically = models.IntegerField(primary_key=True)
    enzymatically = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'enzymatically'


class Enzymefree(models.Model):
    idenzymefree = models.IntegerField(primary_key=True)
    enzymefree = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'enzymefree'


class Gender(models.Model):
    idgender = models.IntegerField(db_column='idGender', primary_key=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gender'


class Germlayer(models.Model):
    idgermlayer = models.IntegerField(primary_key=True)
    germlayer = models.CharField(max_length=15, blank=True)

    class Meta:
        managed = False
        db_table = 'germlayer'


class Hla(models.Model):
    idhla = models.IntegerField(primary_key=True)
    hla = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'hla'


class Karyotypemethod(models.Model):
    idkaryotypemethod = models.IntegerField(primary_key=True)
    karyotypemethod = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'karyotypemethod'


class Keyword(models.Model):
    idkeyword = models.IntegerField(primary_key=True)
    keyword = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'keyword'


class Lastupdatetype(models.Model):
    idlastupdatetype = models.IntegerField(primary_key=True)
    lastupdatetype = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'lastupdatetype'


class Marker(models.Model):
    idmarker = models.IntegerField(primary_key=True)
    marker = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'marker'


class Molecule(models.Model):
    idmolecule = models.IntegerField(primary_key=True)
    moleculename = models.CharField(max_length=45, blank=True)
    referencesource = models.CharField(max_length=45, blank=True)
    referencesourceid = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'molecule'


class Morphologymethod(models.Model):
    idmorphologymethod = models.IntegerField(primary_key=True)
    morphologymethod = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'morphologymethod'


class Organization(models.Model):
    idorganization = models.IntegerField(primary_key=True)
    organizationname = models.CharField(max_length=45, blank=True)
    organizationshortname = models.CharField(unique=True, max_length=6, blank=True)
    organizationcontact = models.ForeignKey(Contact, db_column='organizationcontact', blank=True, null=True)
    organizationupdate = models.DateField(blank=True, null=True)
    organizationupdatetype = models.ForeignKey(Lastupdatetype, db_column='organizationupdatetype', blank=True, null=True)
    organizationupdatedby = models.ForeignKey('Useraccount', db_column='organizationupdatedby', blank=True, null=True)
    organizationtype = models.ForeignKey('Orgtype', db_column='organizationtype', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organization'


class Orgtype(models.Model):
    idorgtype = models.IntegerField(primary_key=True)
    orgtype = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'orgtype'


class Passagemethod(models.Model):
    idpassagemethod = models.IntegerField(primary_key=True)
    passagemethod = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'passagemethod'


class Person(models.Model):
    idperson = models.IntegerField(primary_key=True)
    organization = models.IntegerField(blank=True, null=True)
    personlastname = models.CharField(max_length=20, blank=True)
    personfirstname = models.CharField(max_length=45, blank=True)
    personcontact = models.ForeignKey(Contact, db_column='personcontact', blank=True, null=True)
    personupdate = models.DateField(blank=True, null=True)
    personupdatetype = models.ForeignKey(Lastupdatetype, db_column='personupdatetype', blank=True, null=True)
    personupdatedby = models.ForeignKey('Useraccount', db_column='personupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class Phenotype(models.Model):
    idphenotype = models.IntegerField(primary_key=True)
    phenotype = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'phenotype'


class Phonecountrycode(models.Model):
    idphonecountrycode = models.IntegerField(primary_key=True)
    phonecountrycode = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phonecountrycode'


class Postcode(models.Model):
    idpostcode = models.IntegerField(primary_key=True)
    postcode = models.CharField(max_length=45, blank=True)
    district = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'postcode'


class Primarycelldevelopmentalstage(models.Model):
    idprimarycelldevelopmentalstageid = models.IntegerField(primary_key=True)
    primarycelldevelopmentalstage = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'primarycelldevelopmentalstage'


class Proteinsource(models.Model):
    idproteinsource = models.IntegerField(primary_key=True)
    proteinsource = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'proteinsource'


class Publisher(models.Model):
    idpublisher = models.IntegerField(primary_key=True)
    publisher = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'publisher'


class Reprogrammingmethod1(models.Model):
    idprogrammingmethod1 = models.IntegerField(primary_key=True)
    reprogrammingmethod1 = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'reprogrammingmethod1'


class Reprogrammingmethod2(models.Model):
    idprogrammingmethod2 = models.IntegerField(primary_key=True)
    reprogrammingmethod2 = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'reprogrammingmethod2'


class Reprogrammingmethod3(models.Model):
    idprogrammingmethod3 = models.IntegerField(primary_key=True)
    reprogrammingmethod3 = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'reprogrammingmethod3'


class Strfplocus(models.Model):
    idstrfplocus = models.IntegerField(primary_key=True)
    strfplocus = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'strfplocus'


class Surfacecoating(models.Model):
    idsurfacecoating = models.IntegerField(primary_key=True)
    surfacecoating = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'surfacecoating'


class Tissuesource(models.Model):
    idtissuesource = models.IntegerField(primary_key=True)
    tissuesource = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'tissuesource'


class Transposon(models.Model):
    idtransposon = models.IntegerField(primary_key=True)
    transposon = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'transposon'


class Units(models.Model):
    idunits = models.IntegerField(db_column='idUnits', primary_key=True)  # Field name made lowercase.
    units = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'units'


class Useraccount(models.Model):
    iduseraccount = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45, blank=True)
    useraccounttype = models.ForeignKey('Useraccounttype', db_column='useraccounttype', blank=True, null=True)
    person = models.ForeignKey(Person, db_column='person', blank=True, null=True)
    organization = models.ForeignKey(Organization, db_column='organization', blank=True, null=True)
    accesslevel = models.ForeignKey(Accesslevel, db_column='accesslevel', blank=True, null=True)
    useraccountupdate = models.DateField(blank=True, null=True)
    useraccountupdatetype = models.ForeignKey(Lastupdatetype, db_column='useraccountupdatetype', blank=True, null=True)
    useraccountupdatedby = models.ForeignKey('self', db_column='useraccountupdatedby', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'useraccount'


class Useraccounttype(models.Model):
    iduseraccounttype = models.IntegerField(db_column='idUserAccountType', primary_key=True)  # Field name made lowercase.
    useraccounttype = models.CharField(db_column='UserAccountType', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'useraccounttype'


class Vector(models.Model):
    idvector = models.IntegerField(primary_key=True)
    vector = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'vector'


class Vectorfreereprogramfactor(models.Model):
    idvectorfreereprogramfactor = models.IntegerField(primary_key=True)
    vectorfreereprogramfactor = models.CharField(max_length=15, blank=True)
    referenceid = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'vectorfreereprogramfactor'


class Vectortype(models.Model):
    idvectortype = models.IntegerField(primary_key=True)
    vectortype = models.CharField(max_length=15, blank=True)

    class Meta:
        managed = False
        db_table = 'vectortype'


class Virus(models.Model):
    idvirus = models.IntegerField(primary_key=True)
    virus = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'virus'
