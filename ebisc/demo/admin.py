from django.contrib import admin

from models import Accesslevel, Aliquotstatus, Approveduse, Batchstatus, Binnedage, Cellline, Celllineadditionalinformation, Celllinealiquot, Celllinebatch, Celllinecollection, Celllinederivation, Celllinedisease, Celllinefunctionalcharacter, Celllinegeneration, Celllinegenotype, Celllinelegal, Celllinemolecularcharacterization, Celllinepluripotentmarkers, Celllinepublication, Celllinereprogramming, Celllinestatus, Celllinevalue, Celltype, City, Clinicaltreatmentb4Donation, Contact, Contacttype, Country, Culturemedium, Depositor, Depositorcontacttype, Derivationmethod, Disease, Diseasestage, Document, Documenttype, Donor, Donorsecondarydiseases, Ebisckeyword, Gender, Genotype, Keyword, Morphologymethod, Organizations, Orgcontact, Passagemethod, Persons, Phenotype, Phonecountrycode, Pluripotentmarker1, Pluripotentmarker2, Pluripotentmarker3, Pluripotentmarker4, Pluripotentmarker5, Postcode, Publisher, Qctest, Raceethnicgroup, Stateprovincecounty, Surfacecoatingmatrix, Tissuesource, Transformationtechnique, Useraccounttype, Vector, Vectortype, Vectorused, Yesno, Yesno2, Yesno3, Yesno4, Yesno5, Yesno6


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


class CelllineAdmin(admin.ModelAdmin):
    list_display = ('biosamplesid', 'celllinedepositor', 'celllinename', 'celllinecollection', 'celllinecelltype', 'celllinedepositorsname', 'celllinestatus', 'celllinedonor', 'celllinetissuesource')
    list_filter = ('celllinestatus',)

admin.site.register(Cellline, CelllineAdmin)


class CelllineadditionalinformationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllineadditionalinformation, CelllineadditionalinformationAdmin)


class CelllinealiquotAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinealiquot, CelllinealiquotAdmin)


class CelllinebatchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinebatch, CelllinebatchAdmin)


class CelllinecollectionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinecollection, CelllinecollectionAdmin)


class CelllinederivationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinederivation, CelllinederivationAdmin)


class CelllinediseaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinedisease, CelllinediseaseAdmin)


class CelllinefunctionalcharacterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinefunctionalcharacter, CelllinefunctionalcharacterAdmin)


class CelllinegenerationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinegeneration, CelllinegenerationAdmin)


class CelllinegenotypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinegenotype, CelllinegenotypeAdmin)


class CelllinelegalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinelegal, CelllinelegalAdmin)


class CelllinemolecularcharacterizationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinemolecularcharacterization, CelllinemolecularcharacterizationAdmin)


class CelllinepluripotentmarkersAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinepluripotentmarkers, CelllinepluripotentmarkersAdmin)


class CelllinepublicationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinepublication, CelllinepublicationAdmin)


class CelllinereprogrammingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinereprogramming, CelllinereprogrammingAdmin)


class CelllinestatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinestatus, CelllinestatusAdmin)


class CelllinevalueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinevalue, CelllinevalueAdmin)


class CelltypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celltype, CelltypeAdmin)


class CityAdmin(admin.ModelAdmin):
    pass

admin.site.register(City, CityAdmin)


class Clinicaltreatmentb4DonationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Clinicaltreatmentb4Donation, Clinicaltreatmentb4DonationAdmin)


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


class DepositorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Depositor, DepositorAdmin)


class DepositorcontacttypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Depositorcontacttype, DepositorcontacttypeAdmin)


class DerivationmethodAdmin(admin.ModelAdmin):
    pass

admin.site.register(Derivationmethod, DerivationmethodAdmin)


class DiseaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Disease, DiseaseAdmin)


class DiseasestageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Diseasestage, DiseasestageAdmin)


class DocumentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Document, DocumentAdmin)


class DocumenttypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Documenttype, DocumenttypeAdmin)


class DonorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Donor, DonorAdmin)


class DonorsecondarydiseasesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Donorsecondarydiseases, DonorsecondarydiseasesAdmin)


class EbisckeywordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ebisckeyword, EbisckeywordAdmin)


class GenderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gender, GenderAdmin)


class GenotypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genotype, GenotypeAdmin)


class KeywordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Keyword, KeywordAdmin)


class MorphologymethodAdmin(admin.ModelAdmin):
    pass

admin.site.register(Morphologymethod, MorphologymethodAdmin)


class OrganizationsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Organizations, OrganizationsAdmin)


class OrgcontactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Orgcontact, OrgcontactAdmin)


class PassagemethodAdmin(admin.ModelAdmin):
    pass

admin.site.register(Passagemethod, PassagemethodAdmin)


class PersonsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Persons, PersonsAdmin)


class PhenotypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Phenotype, PhenotypeAdmin)


class PhonecountrycodeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Phonecountrycode, PhonecountrycodeAdmin)


class Pluripotentmarker1Admin(admin.ModelAdmin):
    pass

admin.site.register(Pluripotentmarker1, Pluripotentmarker1Admin)


class Pluripotentmarker2Admin(admin.ModelAdmin):
    pass

admin.site.register(Pluripotentmarker2, Pluripotentmarker2Admin)


class Pluripotentmarker3Admin(admin.ModelAdmin):
    pass

admin.site.register(Pluripotentmarker3, Pluripotentmarker3Admin)


class Pluripotentmarker4Admin(admin.ModelAdmin):
    pass

admin.site.register(Pluripotentmarker4, Pluripotentmarker4Admin)


class Pluripotentmarker5Admin(admin.ModelAdmin):
    pass

admin.site.register(Pluripotentmarker5, Pluripotentmarker5Admin)


class PostcodeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Postcode, PostcodeAdmin)


class PublisherAdmin(admin.ModelAdmin):
    pass

admin.site.register(Publisher, PublisherAdmin)


class QctestAdmin(admin.ModelAdmin):
    pass

admin.site.register(Qctest, QctestAdmin)


class RaceethnicgroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(Raceethnicgroup, RaceethnicgroupAdmin)


class StateprovincecountyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Stateprovincecounty, StateprovincecountyAdmin)


class SurfacecoatingmatrixAdmin(admin.ModelAdmin):
    pass

admin.site.register(Surfacecoatingmatrix, SurfacecoatingmatrixAdmin)


class TissuesourceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tissuesource, TissuesourceAdmin)


class TransformationtechniqueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Transformationtechnique, TransformationtechniqueAdmin)


class UseraccounttypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Useraccounttype, UseraccounttypeAdmin)


class VectorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vector, VectorAdmin)


class VectortypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vectortype, VectortypeAdmin)


class VectorusedAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vectorused, VectorusedAdmin)


class YesnoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Yesno, YesnoAdmin)


class Yesno2Admin(admin.ModelAdmin):
    pass

admin.site.register(Yesno2, Yesno2Admin)


class Yesno3Admin(admin.ModelAdmin):
    pass

admin.site.register(Yesno3, Yesno3Admin)


class Yesno4Admin(admin.ModelAdmin):
    pass

admin.site.register(Yesno4, Yesno4Admin)


class Yesno5Admin(admin.ModelAdmin):
    pass

admin.site.register(Yesno5, Yesno5Admin)


class Yesno6Admin(admin.ModelAdmin):
    pass

admin.site.register(Yesno6, Yesno6Admin)
