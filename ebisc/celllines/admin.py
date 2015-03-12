from django.contrib import admin

from .models import *


class AccesslevelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Accesslevel, AccesslevelAdmin)


class AliquotstatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Aliquotstatus, AliquotstatusAdmin)


class ApproveduseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Approveduse, ApproveduseAdmin)


class BatchstatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Batchstatus, BatchstatusAdmin)


class BinnedageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Binnedage, BinnedageAdmin)


class CelllinecharacterizationInline(admin.StackedInline):
    model = Celllinecharacterization
    min_num = 1
    max_num = 1
    extra = 0
    inline_classes = ('grp-collapse grp-open',)


class CelllinechecklistInline(admin.StackedInline):
    model = Celllinechecklist
    min_num = 1
    max_num = 1
    extra = 0
    inline_classes = ('grp-collapse grp-open',)


class CelllinecultureconditionsInline(admin.StackedInline):
    model = Celllinecultureconditions
    min_num = 1
    max_num = 1
    extra = 0
    inline_classes = ('grp-collapse grp-open',)


class CelllinederivationInline(admin.StackedInline):
    model = Celllinederivation
    min_num = 1
    max_num = 1
    extra = 0
    inline_classes = ('grp-collapse grp-open',)


class CelllinelabInline(admin.StackedInline):
    model = Celllinelab
    min_num = 1
    max_num = 1
    extra = 0
    inline_classes = ('grp-collapse grp-open',)


class CelllinelegalInline(admin.StackedInline):
    model = Celllinelegal
    min_num = 1
    max_num = 1
    extra = 0
    inline_classes = ('grp-collapse grp-open',)


class CelllinevalueInline(admin.StackedInline):
    model = Celllinevalue
    min_num = 1
    max_num = 1
    extra = 0
    inline_classes = ('grp-collapse grp-open',)


class CelllineAdmin(admin.ModelAdmin):

    list_display = ['biosamplesid', 'celllinename', 'celllinedonor', 'celllineprimarydisease', 'celllinestatus', 'celllinecelltype', 'celllinecollection', 'celllinetissuesource', 'celllinetissuetreatment', 'celllinetissuedate', 'celllinenamesynonyms', 'celllineupdate', 'celllineupdatetype', 'celllineupdatedby', 'celllineecaccurl']
    inlines = (CelllinecharacterizationInline, CelllinechecklistInline, CelllinecultureconditionsInline, CelllinederivationInline, CelllinelabInline, CelllinelegalInline, CelllinevalueInline)

    list_filter = ('celllinestatus', 'celllineprimarydisease', 'celllinetissuesource', 'celllinecelltype')

admin.site.register(Cellline, CelllineAdmin)


class CelllinealiquotAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinealiquot, CelllinealiquotAdmin)


class CelllineannotationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllineannotation, CelllineannotationAdmin)


class CelllinebatchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinebatch, CelllinebatchAdmin)


class CelllinecollectionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinecollection, CelllinecollectionAdmin)


class CelllinecommentsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinecomments, CelllinecommentsAdmin)


class CelllineculturesupplementsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllineculturesupplements, CelllineculturesupplementsAdmin)


class CelllinediffpotencyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinediffpotency, CelllinediffpotencyAdmin)


class CelllinediffpotencymarkerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinediffpotencymarker, CelllinediffpotencymarkerAdmin)


class CelllinediffpotencymoleculeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinediffpotencymolecule, CelllinediffpotencymoleculeAdmin)


class CelllinegenemutationsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinegenemutations, CelllinegenemutationsAdmin)


class CelllinegenemutationsmoleculeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinegenemutationsmolecule, CelllinegenemutationsmoleculeAdmin)


class CelllinegeneticmodAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinegeneticmod, CelllinegeneticmodAdmin)


class CelllinegenomeseqAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinegenomeseq, CelllinegenomeseqAdmin)


class CelllinegenotypingotherAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinegenotypingother, CelllinegenotypingotherAdmin)


class CelllinehlatypingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinehlatyping, CelllinehlatypingAdmin)


class CelllinekaryotypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinekaryotype, CelllinekaryotypeAdmin)


class CelllinemarkerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinemarker, CelllinemarkerAdmin)


class CelllineorganizationAdmin(admin.ModelAdmin):

    list_display = ['orgcellline', 'organization', 'celllineorgtype', 'orgstatus', 'orgregistrationdate']

admin.site.register(Celllineorganization, CelllineorganizationAdmin)


class CelllineorgtypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllineorgtype, CelllineorgtypeAdmin)


class CelllinepublicationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinepublication, CelllinepublicationAdmin)


class CelllinesnpAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinesnp, CelllinesnpAdmin)


class CelllinesnpdetailsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinesnpdetails, CelllinesnpdetailsAdmin)


class CelllinesnprslinksAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinesnprslinks, CelllinesnprslinksAdmin)


class CelllinestatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinestatus, CelllinestatusAdmin)


class CelllinestrfingerprintingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinestrfingerprinting, CelllinestrfingerprintingAdmin)


class CelllinevectorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinevector, CelllinevectorAdmin)


class CelllinevectorfreereprogrammingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinevectorfreereprogramming, CelllinevectorfreereprogrammingAdmin)


class CelllinevectormoleculeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinevectormolecule, CelllinevectormoleculeAdmin)


class CelltypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celltype, CelltypeAdmin)


class Clinicaltreatmentb4donationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Clinicaltreatmentb4donation, Clinicaltreatmentb4donationAdmin)


class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)


class ContacttypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contacttype, ContacttypeAdmin)


class CountryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country, CountryAdmin)


class CulturemediumAdmin(admin.ModelAdmin):
    pass

admin.site.register(Culturemedium, CulturemediumAdmin)


class CulturesystemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Culturesystem, CulturesystemAdmin)


class DiseaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Disease, DiseaseAdmin)


class DocumentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Document, DocumentAdmin)


class DocumenttypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Documenttype, DocumenttypeAdmin)


class DonorAdmin(admin.ModelAdmin):

    list_display = ['hescregdonorid', 'age', 'gender', 'countryoforigin', 'primarydisease', 'diseaseadditionalinfo', 'providerdonorid']
    list_display_links = ['hescregdonorid']
    list_filter = ['age', 'gender', 'countryoforigin']

admin.site.register(Donor, DonorAdmin)


class EbisckeywordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ebisckeyword, EbisckeywordAdmin)


class EnzymaticallyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Enzymatically, EnzymaticallyAdmin)


class EnzymefreeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Enzymefree, EnzymefreeAdmin)


class GenderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gender, GenderAdmin)


class GermlayerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Germlayer, GermlayerAdmin)


class HlaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hla, HlaAdmin)


class KaryotypemethodAdmin(admin.ModelAdmin):
    pass

admin.site.register(Karyotypemethod, KaryotypemethodAdmin)


class KeywordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Keyword, KeywordAdmin)


class LastupdatetypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lastupdatetype, LastupdatetypeAdmin)


class MarkerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Marker, MarkerAdmin)


class MoleculeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Molecule, MoleculeAdmin)


class MorphologymethodAdmin(admin.ModelAdmin):
    pass

admin.site.register(Morphologymethod, MorphologymethodAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Organization, OrganizationAdmin)


class OrgtypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Orgtype, OrgtypeAdmin)


class PassagemethodAdmin(admin.ModelAdmin):
    pass

admin.site.register(Passagemethod, PassagemethodAdmin)


class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)


class PhenotypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Phenotype, PhenotypeAdmin)


class PhonecountrycodeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Phonecountrycode, PhonecountrycodeAdmin)


class PostcodeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Postcode, PostcodeAdmin)


class PrimarycelldevelopmentalstageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Primarycelldevelopmentalstage, PrimarycelldevelopmentalstageAdmin)


class ProteinsourceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Proteinsource, ProteinsourceAdmin)


class PublisherAdmin(admin.ModelAdmin):
    pass

admin.site.register(Publisher, PublisherAdmin)


class Reprogrammingmethod1Admin(admin.ModelAdmin):
    pass

admin.site.register(Reprogrammingmethod1, Reprogrammingmethod1Admin)


class Reprogrammingmethod2Admin(admin.ModelAdmin):
    pass

admin.site.register(Reprogrammingmethod2, Reprogrammingmethod2Admin)


class Reprogrammingmethod3Admin(admin.ModelAdmin):
    pass

admin.site.register(Reprogrammingmethod3, Reprogrammingmethod3Admin)


class StrfplocusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Strfplocus, StrfplocusAdmin)


class SurfacecoatingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Surfacecoating, SurfacecoatingAdmin)


class TissuesourceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tissuesource, TissuesourceAdmin)


class TransposonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Transposon, TransposonAdmin)


class UnitsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Units, UnitsAdmin)


class UseraccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(Useraccount, UseraccountAdmin)


class UseraccounttypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Useraccounttype, UseraccounttypeAdmin)


class VectorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vector, VectorAdmin)


class VectorfreereprogramfactorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vectorfreereprogramfactor, VectorfreereprogramfactorAdmin)


class VectortypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vectortype, VectortypeAdmin)


class VirusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Virus, VirusAdmin)
