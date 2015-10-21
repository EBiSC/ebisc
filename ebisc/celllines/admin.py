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
# Directories

class GenderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gender, GenderAdmin)


class AgeRangeAdmin(admin.ModelAdmin):
    pass

admin.site.register(AgeRange, AgeRangeAdmin)


# -----------------------------------------------------------------------------
# CellLine

class CelllineCharacterizationInline(OneToOneStackedInline):
    model = CelllineCharacterization


class CelllineCultureConditionsInline(OneToOneStackedInline):
    model = CelllineCultureConditions


class CelllineDerivationInline(OneToOneStackedInline):
    model = CelllineDerivation


class CelllineEthicsInline(OneToOneStackedInline):
    model = CelllineEthics


class CelllineValueInline(OneToOneStackedInline):
    model = CelllineValue


class CelllineIntegratingVectorInline(OneToOneStackedInline):
    model = CelllineIntegratingVector


class CelllineNonIntegratingVectorInline(OneToOneStackedInline):
    model = CelllineNonIntegratingVector


class CelllineAdmin(admin.ModelAdmin):

    list_display = ['biosamples_id', 'name', 'status', 'alternative_names']
    inlines = (
        CelllineCharacterizationInline,
        CelllineCultureConditionsInline,
        CelllineDerivationInline,
        CelllineEthicsInline,
        CelllineValueInline,
        CelllineIntegratingVectorInline,
        CelllineNonIntegratingVectorInline,
    )

    list_filter = ('status',)

admin.site.register(Cellline, CelllineAdmin)


# -----------------------------------------------------------------------------
# Batches

class BatchAliquotInline(TabularInline):
    model = CelllineAliquot


class CelllineBatchAdmin(admin.ModelAdmin):

    list_display = ['biosamples_id', 'batch_id', 'cell_line']
    inlines = (BatchAliquotInline,)

admin.site.register(CelllineBatch, CelllineBatchAdmin)


# -----------------------------------------------------------------------------
