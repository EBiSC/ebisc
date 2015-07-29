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


class ApprovedUseAdmin(admin.ModelAdmin):
    pass

admin.site.register(ApprovedUse, ApprovedUseAdmin)


# -----------------------------------------------------------------------------
# CellLine

class CellLineCharacterizationInline(OneToOneStackedInline):
    model = CellLineCharacterization


class CelllinechecklistInline(OneToOneStackedInline):
    model = Celllinechecklist


class CelllinecultureconditionsInline(OneToOneStackedInline):
    model = Celllinecultureconditions


class CelllinederivationInline(OneToOneStackedInline):
    model = Celllinederivation


class CelllinelabInline(OneToOneStackedInline):
    model = Celllinelab


class CellLineLegalInline(OneToOneStackedInline):
    model = CellLineLegal


class CelllinevalueInline(OneToOneStackedInline):
    model = Celllinevalue


class CellLineIntegratingVectorInline(OneToOneStackedInline):
    model = CellLineIntegratingVector


class CellLineNonIntegratingVectorInline(OneToOneStackedInline):
    model = CellLineNonIntegratingVector


class CelllineAdmin(admin.ModelAdmin):

    list_display = ['biosamplesid', 'celllinename', 'celllinestatus', 'celllinenamesynonyms']
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

    list_filter = ('celllinestatus',)

admin.site.register(Cellline, CelllineAdmin)


# -----------------------------------------------------------------------------
# Batches

class BatchAliquotInline(TabularInline):
    model = CelllineAliquot


class CelllineBatchAdmin(admin.ModelAdmin):

    list_display = ['biosamplesid', 'batch_id', 'cell_line']
    inlines = (BatchAliquotInline,)

    # list_filter = ('celllinestatus',)

admin.site.register(CelllineBatch, CelllineBatchAdmin)


# -----------------------------------------------------------------------------
