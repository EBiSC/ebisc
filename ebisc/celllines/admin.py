from django.contrib import admin

from .models import *


# -----------------------------------------------------------------------------
# Helpers

class StackedInline(admin.StackedInline):
    extra = 0


class TabularInline(admin.TabularInline):
    extra = 0


class OneToOneStackedInline(admin.StackedInline):
    min_num = 1
    max_num = 1
    extra = 0


# -----------------------------------------------------------------------------
# Dictionaries

class GenderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gender, GenderAdmin)


class AgeRangeAdmin(admin.ModelAdmin):
    pass

admin.site.register(AgeRange, AgeRangeAdmin)


# -----------------------------------------------------------------------------
# Disease

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['xpurl', 'name']

admin.site.register(Disease, DiseaseAdmin)


# -----------------------------------------------------------------------------
# CellLine

class CelllineDiseaseInline(StackedInline):
    model = CelllineDisease


class CelllineCharacterizationInline(OneToOneStackedInline):
    model = CelllineCharacterization


class CelllineCultureConditionsInline(OneToOneStackedInline):
    model = CelllineCultureConditions


class CelllineDerivationInline(OneToOneStackedInline):
    model = CelllineDerivation


class CelllineCharacterizationPluritestInline(OneToOneStackedInline):
    model = CelllineCharacterizationPluritest


class CelllineEthicsInline(OneToOneStackedInline):
    model = CelllineEthics


class CelllineValueInline(OneToOneStackedInline):
    model = CelllineValue


class CelllineIntegratingVectorInline(OneToOneStackedInline):
    model = CelllineIntegratingVector


class CelllineNonIntegratingVectorInline(OneToOneStackedInline):
    model = CelllineNonIntegratingVector


class CelllineStatusInline(TabularInline):
    model = CelllineStatus


class CelllineAdmin(admin.ModelAdmin):
    list_display = ['name', 'biosamples_id', 'alternative_names', 'current_status', 'available_for_sale_at_ecacc']
    inlines = (
        CelllineDiseaseInline,
        CelllineStatusInline,
        CelllineCharacterizationInline,
        CelllineCultureConditionsInline,
        CelllineDerivationInline,
        CelllineCharacterizationPluritestInline,
        CelllineEthicsInline,
        CelllineValueInline,
        CelllineIntegratingVectorInline,
        CelllineNonIntegratingVectorInline,
    )
    list_filter = ['current_status__status', 'available_for_sale_at_ecacc', 'generator__name']
    search_fields = ['name', 'biosamples_id']

admin.site.register(Cellline, CelllineAdmin)


# -----------------------------------------------------------------------------
# Donors

class DonorDiseaseInline(StackedInline):
    model = DonorDisease


class DonorAdmin(admin.ModelAdmin):
    list_display = ['biosamples_id', 'provider_donor_ids', 'gender']
    search_fields = ['biosamples_id', 'provider_donor_ids']
    inlines = (DonorDiseaseInline,)
    list_filter = ['gender', 'country_of_origin', 'ethnicity']

admin.site.register(Donor, DonorAdmin)


# -----------------------------------------------------------------------------
# Batches

class BatchAliquotInline(TabularInline):
    model = CelllineAliquot


class CelllineBatchAdmin(admin.ModelAdmin):

    list_display = ['biosamples_id', 'batch_id', 'batch_type', 'cell_line', 'get_cell_line_name']
    search_fields = ['biosamples_id', 'cell_line__name', 'cell_line__biosamples_id', 'aliquots__biosamples_id']
    inlines = (BatchAliquotInline,)
    list_filter = ['batch_type']

    def get_cell_line_name(self, obj):
        return obj.cell_line.name
    get_cell_line_name.short_description = 'Cell line name'

admin.site.register(CelllineBatch, CelllineBatchAdmin)


# -----------------------------------------------------------------------------
# Clips

class CelllineInformationPackAdmin(admin.ModelAdmin):
    list_display = ['cell_line', 'version', 'created', 'updated']

admin.site.register(CelllineInformationPack, CelllineInformationPackAdmin)
