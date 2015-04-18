class Celllinevectormolecule(models.Model):
    celllinevector = models.ForeignKey('Celllinevector', verbose_name=_(u'Cell line vector'), blank=True, null=True)
    molecule = models.ForeignKey('Molecule', verbose_name=_(u'Molecule'), blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line vector molecule')
        verbose_name_plural = _(u'Cell line vector molecules')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinevectorfreereprogramming(models.Model):
    vectorfreecellline = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), blank=True, null=True)
    vectorfreereprogrammingfactor = models.ForeignKey('Vectorfreereprogramfactor', verbose_name=_(u'Vector free reprogram factor'), blank=True, null=True)

    class Meta:
        verbose_name = _(u'Cell line vector free reprogramming')
        verbose_name_plural = _(u'Cell line vector free reprogrammings')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)
