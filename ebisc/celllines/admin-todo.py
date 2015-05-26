class CelllinevectormoleculeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinevectormolecule, CelllinevectormoleculeAdmin)

class CelllinevectorfreereprogrammingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinevectorfreereprogramming, CelllinevectorfreereprogrammingAdmin)


class AccesslevelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Accesslevel, AccesslevelAdmin)

class CelllinealiquotAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinealiquot, CelllinealiquotAdmin)

class CelllineannotationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllineannotation, CelllineannotationAdmin)

class CelllinebatchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celllinebatch, CelllinebatchAdmin)


class UseraccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(Useraccount, UseraccountAdmin)


class UseraccounttypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Useraccounttype, UseraccounttypeAdmin)


class AliquotstatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Aliquotstatus, AliquotstatusAdmin)
