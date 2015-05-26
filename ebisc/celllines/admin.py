from django.contrib import admin

from .models import *


class GenderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gender, GenderAdmin)


class AgeRangeAdmin(admin.ModelAdmin):
    pass

admin.site.register(AgeRange, AgeRangeAdmin)


class ApprovedUseAdmin(admin.ModelAdmin):
    pass

admin.site.register(ApprovedUse, ApprovedUseAdmin)


class BatchstatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Batchstatus, BatchstatusAdmin)


class CellLineCharacterizationInline(admin.StackedInline):
    model = CellLineCharacterization
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


class CellLineLegalInline(admin.StackedInline):
    model = CellLineLegal
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


class CellLineIntegratingVectorInline(admin.StackedInline):
    model = CellLineIntegratingVector
    min_num = 1
    max_num = 1
    extra = 0
    inline_classes = ('grp-collapse grp-open',)


class CellLineNonIntegratingVectorInline(admin.StackedInline):
    model = CellLineNonIntegratingVector
    min_num = 1
    max_num = 1
    extra = 0
    inline_classes = ('grp-collapse grp-open',)


class CelllineAdmin(admin.ModelAdmin):

    list_display = ['biosamplesid', 'celllinename', 'donor', 'celllineprimarydisease', 'celllinestatus', 'celllinecelltype', 'celllinecollection', 'celllinetissuesource', 'celllinetissuetreatment', 'celllinetissuedate', 'celllinenamesynonyms', 'celllineecaccurl']
    inlines = (
        CellLineCharacterizationInline,
        CelllinechecklistInline,
        CelllinecultureconditionsInline,
        CelllinederivationInline,
        CelllinelabInline,
        CellLineLegalInline,
        CelllinevalueInline,
        CellLineIntegratingVectorInline,
        CellLineNonIntegratingVectorInline,
    )

    list_filter = ('celllinestatus', 'celllineprimarydisease', 'celllinetissuesource', 'celllinecelltype')

admin.site.register(Cellline, CelllineAdmin)


class CelllinecollectionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinecollection, CelllinecollectionAdmin)


class CelllinecommentsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinecomments, CelllinecommentsAdmin)


class CellLineCultureMediumSupplementAdmin(admin.ModelAdmin):
    pass

admin.site.register(CellLineCultureMediumSupplement, CellLineCultureMediumSupplementAdmin)


class CelllinegenemutationsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinegenemutations, CelllinegenemutationsAdmin)


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


class CellLineKaryotypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(CellLineKaryotype, CellLineKaryotypeAdmin)


class CelllineorganizationAdmin(admin.ModelAdmin):

    list_display = ['orgcellline', 'organization', 'celllineorgtype', 'orgstatus', 'orgregistrationdate']

admin.site.register(Celllineorganization, CelllineorganizationAdmin)


class CelllineorgtypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllineorgtype, CelllineorgtypeAdmin)


class CellLinePublicationAdmin(admin.ModelAdmin):
    list_display = ['cell_line', 'reference_type', 'reference_title', 'reference_url']
    list_display_links = ['cell_line']
    list_filter = ['reference_type']

admin.site.register(CellLinePublication, CellLinePublicationAdmin)


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


class CultureMediumAdmin(admin.ModelAdmin):
    pass

admin.site.register(CultureMedium, CultureMediumAdmin)


class CultureMediumOtherAdmin(admin.ModelAdmin):
    pass

admin.site.register(CultureMediumOther, CultureMediumOtherAdmin)


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

    list_display = ['biosamplesid', 'gender', 'countryoforigin', 'primarydisease', 'diseaseadditionalinfo', 'providerdonorid']
    list_display_links = ['biosamplesid']
    list_filter = ['gender', 'countryoforigin']

admin.site.register(Donor, DonorAdmin)


class EbisckeywordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ebisckeyword, EbisckeywordAdmin)


class EnzymaticallyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Enzymatically, EnzymaticallyAdmin)


class EnzymeFreeAdmin(admin.ModelAdmin):
    pass

admin.site.register(EnzymeFree, EnzymeFreeAdmin)


class GermlayerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Germlayer, GermlayerAdmin)


class HlaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hla, HlaAdmin)


class KaryotypeMethodAdmin(admin.ModelAdmin):
    pass

admin.site.register(KaryotypeMethod, KaryotypeMethodAdmin)


class KeywordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Keyword, KeywordAdmin)


class MoleculeReferenceInline(admin.StackedInline):
    model = MoleculeReference
    extra = 0


class MoleculeAdmin(admin.ModelAdmin):
    list_display = ['name', 'kind']
    list_filter = ['kind']
    inlines = [MoleculeReferenceInline]

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


class PassageMethodAdmin(admin.ModelAdmin):
    pass

admin.site.register(PassageMethod, PassageMethodAdmin)


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


class PrimaryCellDevelopmentalStageAdmin(admin.ModelAdmin):
    pass

admin.site.register(PrimaryCellDevelopmentalStage, PrimaryCellDevelopmentalStageAdmin)


class ProteinSourceAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProteinSource, ProteinSourceAdmin)


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


class SurfaceCoatingAdmin(admin.ModelAdmin):
    pass

admin.site.register(SurfaceCoating, SurfaceCoatingAdmin)


class TissuesourceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tissuesource, TissuesourceAdmin)


class UnitAdmin(admin.ModelAdmin):
    pass

admin.site.register(Unit, UnitAdmin)


class VectorfreereprogramfactorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vectorfreereprogramfactor, VectorfreereprogramfactorAdmin)


# -----------------------------------------------------------------------------
# Cell line vector

class NonIntegratingVectorAdmin(admin.ModelAdmin):
    pass

admin.site.register(NonIntegratingVector, NonIntegratingVectorAdmin)


class IntegratingVectorAdmin(admin.ModelAdmin):
    pass

admin.site.register(IntegratingVector, IntegratingVectorAdmin)


class VirusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Virus, VirusAdmin)


class TransposonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Transposon, TransposonAdmin)

# -----------------------------------------------------------------------------
