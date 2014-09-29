from django.contrib import admin

from models import Accesslevel, Aliquotstatus, Approveduse, Batchstatus, Binnedage, Cellline, Celllineadditionalinformation, Celllinealiquot, Celllinebatch, Celllinecollection, Celllinederivation, Celllinedisease, Celllinefunctionalcharacter, Celllinegeneration, Celllinegenotype, Celllinelegal, Celllinemolecularcharacterization, Celllinepluripotentmarkers, Celllinepublication, Celllinereprogramming, Celllinestatus, Celllinevalue, Celltype, City, Clinicaltreatmentb4Donation, Contact, Contacttype, Country, Culturemedium, Depositor, Depositorcontacttype, Derivationmethod, Disease, Diseasestage, Document, Documenttype, Donor, Donorsecondarydiseases, Ebisckeyword, Gender, Genotype, Keyword, Morphologymethod, Organizations, Orgcontact, Passagemethod, Persons, Phenotype, Phonecountrycode, Pluripotentmarker1, Pluripotentmarker2, Pluripotentmarker3, Pluripotentmarker4, Pluripotentmarker5, Postcode, Publisher, Qctest, Raceethnicgroup, Stateprovincecounty, Surfacecoatingmatrix, Tissuesource, Transformationtechnique, Useraccounttype, Vector, Vectortype, Vectorused, Yesno, Yesno2, Yesno3, Yesno4, Yesno5, Yesno6


class AccesslevelAdmin(admin.ModelAdmin):
    pass


class AliquotstatusAdmin(admin.ModelAdmin):
    pass


class ApproveduseAdmin(admin.ModelAdmin):
    pass


class BatchstatusAdmin(admin.ModelAdmin):
    pass


class BinnedageAdmin(admin.ModelAdmin):
    pass


class CelllineDeseaseInline(admin.TabularInline):
    model = Celllinedisease


class CelllineAdmin(admin.ModelAdmin):
    list_display = ('biosamplesid', 'disease_name', 'celllinename', 'celllinecelltype', 'celllinedepositorsname', 'celllinestatus', 'celllinedonor')
    list_filter = ('celllinestatus', 'disease__celllinedisease')
    search_fields = ('celllinename', 'disease__celllinedisease__disease')
    inlines = [CelllineDeseaseInline]

    def disease_name(self, obj):
        return ', '.join([x.celllinedisease.disease for x in obj.disease.all()])


class CelllineadditionalinformationAdmin(admin.ModelAdmin):
    pass


class CelllinealiquotAdmin(admin.ModelAdmin):
    pass


class CelllinebatchAdmin(admin.ModelAdmin):
    pass


class CelllinecollectionAdmin(admin.ModelAdmin):
    pass


class CelllinederivationAdmin(admin.ModelAdmin):
    pass


class CelllinediseaseAdmin(admin.ModelAdmin):
    list_display = ('cellline', 'celllinedisease')


class CelllinefunctionalcharacterAdmin(admin.ModelAdmin):
    pass


class CelllinegenerationAdmin(admin.ModelAdmin):
    pass


class CelllinegenotypeAdmin(admin.ModelAdmin):
    pass


class CelllinelegalAdmin(admin.ModelAdmin):
    pass


class CelllinemolecularcharacterizationAdmin(admin.ModelAdmin):
    pass


class CelllinepluripotentmarkersAdmin(admin.ModelAdmin):
    pass


class CelllinepublicationAdmin(admin.ModelAdmin):
    pass


class CelllinereprogrammingAdmin(admin.ModelAdmin):
    pass


class CelllinestatusAdmin(admin.ModelAdmin):
    pass


class CelllinevalueAdmin(admin.ModelAdmin):
    pass


class CelltypeAdmin(admin.ModelAdmin):
    pass


class CityAdmin(admin.ModelAdmin):
    pass


class Clinicaltreatmentb4DonationAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    pass


class ContacttypeAdmin(admin.ModelAdmin):
    pass


class CountryAdmin(admin.ModelAdmin):
    pass


class CulturemediumAdmin(admin.ModelAdmin):
    pass


class DepositorAdmin(admin.ModelAdmin):
    pass


class DepositorcontacttypeAdmin(admin.ModelAdmin):
    pass


class DerivationmethodAdmin(admin.ModelAdmin):
    pass


class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('disease',)


class DiseasestageAdmin(admin.ModelAdmin):
    pass


class DocumentAdmin(admin.ModelAdmin):
    pass


class DocumenttypeAdmin(admin.ModelAdmin):
    pass


class DonorAdmin(admin.ModelAdmin):
    pass


class DonorsecondarydiseasesAdmin(admin.ModelAdmin):
    pass


class EbisckeywordAdmin(admin.ModelAdmin):
    pass


class GenderAdmin(admin.ModelAdmin):
    pass


class GenotypeAdmin(admin.ModelAdmin):
    pass


class KeywordAdmin(admin.ModelAdmin):
    pass


class MorphologymethodAdmin(admin.ModelAdmin):
    pass


class OrganizationsAdmin(admin.ModelAdmin):
    pass


class OrgcontactAdmin(admin.ModelAdmin):
    pass


class PassagemethodAdmin(admin.ModelAdmin):
    pass


class PersonsAdmin(admin.ModelAdmin):
    pass


class PhenotypeAdmin(admin.ModelAdmin):
    pass


class PhonecountrycodeAdmin(admin.ModelAdmin):
    pass


class Pluripotentmarker1Admin(admin.ModelAdmin):
    pass


class Pluripotentmarker2Admin(admin.ModelAdmin):
    pass


class Pluripotentmarker3Admin(admin.ModelAdmin):
    pass


class Pluripotentmarker4Admin(admin.ModelAdmin):
    pass


class Pluripotentmarker5Admin(admin.ModelAdmin):
    pass


class PostcodeAdmin(admin.ModelAdmin):
    pass


class PublisherAdmin(admin.ModelAdmin):
    pass


class QctestAdmin(admin.ModelAdmin):
    pass


class RaceethnicgroupAdmin(admin.ModelAdmin):
    pass


class StateprovincecountyAdmin(admin.ModelAdmin):
    pass


class SurfacecoatingmatrixAdmin(admin.ModelAdmin):
    pass


class TissuesourceAdmin(admin.ModelAdmin):
    pass


class TransformationtechniqueAdmin(admin.ModelAdmin):
    pass


class UseraccounttypeAdmin(admin.ModelAdmin):
    pass


class VectorAdmin(admin.ModelAdmin):
    pass


class VectortypeAdmin(admin.ModelAdmin):
    pass


class VectorusedAdmin(admin.ModelAdmin):
    pass


class YesnoAdmin(admin.ModelAdmin):
    pass


class Yesno2Admin(admin.ModelAdmin):
    pass


class Yesno3Admin(admin.ModelAdmin):
    pass


class Yesno4Admin(admin.ModelAdmin):
    pass


class Yesno5Admin(admin.ModelAdmin):
    pass


class Yesno6Admin(admin.ModelAdmin):
    pass


admin.site.register(Accesslevel, AccesslevelAdmin)
admin.site.register(Aliquotstatus, AliquotstatusAdmin)
admin.site.register(Approveduse, ApproveduseAdmin)
admin.site.register(Batchstatus, BatchstatusAdmin)
admin.site.register(Binnedage, BinnedageAdmin)
admin.site.register(Cellline, CelllineAdmin)
# admin.site.register(Celllineadditionalinformation, CelllineadditionalinformationAdmin)
# admin.site.register(Celllinealiquot, CelllinealiquotAdmin)
# admin.site.register(Celllinebatch, CelllinebatchAdmin)
# admin.site.register(Celllinecollection, CelllinecollectionAdmin)
# admin.site.register(Celllinederivation, CelllinederivationAdmin)
# admin.site.register(Celllinedisease, CelllinediseaseAdmin)
# admin.site.register(Celllinefunctionalcharacter, CelllinefunctionalcharacterAdmin)
# admin.site.register(Celllinegeneration, CelllinegenerationAdmin)
# admin.site.register(Celllinegenotype, CelllinegenotypeAdmin)
# admin.site.register(Celllinelegal, CelllinelegalAdmin)
# admin.site.register(Celllinemolecularcharacterization, CelllinemolecularcharacterizationAdmin)
# admin.site.register(Celllinepluripotentmarkers, CelllinepluripotentmarkersAdmin)
# admin.site.register(Celllinepublication, CelllinepublicationAdmin)
# admin.site.register(Celllinereprogramming, CelllinereprogrammingAdmin)
# admin.site.register(Celllinestatus, CelllinestatusAdmin)
# admin.site.register(Celllinevalue, CelllinevalueAdmin)
admin.site.register(Celltype, CelltypeAdmin)
# admin.site.register(City, CityAdmin)
# admin.site.register(Clinicaltreatmentb4Donation, Clinicaltreatmentb4DonationAdmin)
admin.site.register(Contact, ContactAdmin)
# admin.site.register(Contacttype, ContacttypeAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Culturemedium, CulturemediumAdmin)
admin.site.register(Depositor, DepositorAdmin)
# admin.site.register(Depositorcontacttype, DepositorcontacttypeAdmin)
admin.site.register(Derivationmethod, DerivationmethodAdmin)
admin.site.register(Disease, DiseaseAdmin)
# admin.site.register(Diseasestage, DiseasestageAdmin)
admin.site.register(Document, DocumentAdmin)
# admin.site.register(Documenttype, DocumenttypeAdmin)
admin.site.register(Donor, DonorAdmin)
# admin.site.register(Donorsecondarydiseases, DonorsecondarydiseasesAdmin)
admin.site.register(Ebisckeyword, EbisckeywordAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Genotype, GenotypeAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Morphologymethod, MorphologymethodAdmin)
admin.site.register(Organizations, OrganizationsAdmin)
# admin.site.register(Orgcontact, OrgcontactAdmin)
# admin.site.register(Passagemethod, PassagemethodAdmin)
admin.site.register(Persons, PersonsAdmin)
admin.site.register(Phenotype, PhenotypeAdmin)
admin.site.register(Phonecountrycode, PhonecountrycodeAdmin)
# admin.site.register(Pluripotentmarker1, Pluripotentmarker1Admin)
# admin.site.register(Pluripotentmarker2, Pluripotentmarker2Admin)
# admin.site.register(Pluripotentmarker3, Pluripotentmarker3Admin)
# admin.site.register(Pluripotentmarker4, Pluripotentmarker4Admin)
# admin.site.register(Pluripotentmarker5, Pluripotentmarker5Admin)
admin.site.register(Postcode, PostcodeAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Qctest, QctestAdmin)
admin.site.register(Raceethnicgroup, RaceethnicgroupAdmin)
admin.site.register(Stateprovincecounty, StateprovincecountyAdmin)
admin.site.register(Surfacecoatingmatrix, SurfacecoatingmatrixAdmin)
admin.site.register(Tissuesource, TissuesourceAdmin)
admin.site.register(Transformationtechnique, TransformationtechniqueAdmin)
admin.site.register(Useraccounttype, UseraccounttypeAdmin)
admin.site.register(Vector, VectorAdmin)
admin.site.register(Vectortype, VectortypeAdmin)
admin.site.register(Vectorused, VectorusedAdmin)
# admin.site.register(Yesno, YesnoAdmin)
# admin.site.register(Yesno2, Yesno2Admin)
# admin.site.register(Yesno3, Yesno3Admin)
# admin.site.register(Yesno4, Yesno4Admin)
# admin.site.register(Yesno5, Yesno5Admin)
# admin.site.register(Yesno6, Yesno6Admin)
