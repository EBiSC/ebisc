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



class Useraccount(models.Model):
    username = models.CharField(_(u'Username'), max_length=45, blank=True)
    useraccounttype = models.ForeignKey('Useraccounttype', verbose_name=_(u'User account type'), null=True, blank=True)
    person = models.ForeignKey('Person', verbose_name=_(u'Person'), null=True, blank=True)
    organization = models.ForeignKey('Organization', verbose_name=_(u'Organization'), null=True, blank=True)
    accesslevel = models.ForeignKey('Accesslevel', verbose_name=_(u'Access level'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'User account')
        verbose_name_plural = _(u'User accounts')
        ordering = ['username']

    def __unicode__(self):
        return u'%s' % (self.username,)


class Useraccounttype(models.Model):
    useraccounttype = models.CharField(_(u'User account type'), max_length=15)

    class Meta:
        verbose_name = _(u'User account type')
        verbose_name_plural = _(u'User account types')
        ordering = ['useraccounttype']

    def __unicode__(self):
        return u'%s' % (self.useraccounttype,)



class Accesslevel(models.Model):
    accesslevel = models.CharField(_(u'Access level'), max_length=20, blank=True)

    class Meta:
        verbose_name = _(u'Access level')
        verbose_name_plural = _(u'Access levels')
        ordering = ['accesslevel']

    def __unicode__(self):
        return u'%s' % (self.accesslevel,)


class Celllinealiquot(models.Model):
    aliquotcellline = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), null=True, blank=True)
    aliquotstatus = models.ForeignKey('Aliquotstatus', verbose_name=_(u'Aliquot status'), null=True, blank=True)
    aliquotstatusdate = models.CharField(_(u'Aliquot status date'), max_length=20, blank=True)
    aliquotupdatedby = models.ForeignKey('Useraccount', verbose_name=_(u'User account'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line aliquot')
        verbose_name_plural = _(u'Cell line aliquotes')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllineannotation(models.Model):
    annotationcellline = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), null=True, blank=True)
    celllineannotationsource = models.CharField(_(u'Cell line annotation source'), max_length=45, blank=True)
    celllineannotationsourceid = models.CharField(_(u'Cell line annotation source id'), max_length=45, blank=True)
    celllineannotationsourceversion = models.CharField(_(u'Cell line annotation source version'), max_length=45, blank=True)
    celllineannotation = models.TextField(_(u'Cell line annotation'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line annotation')
        verbose_name_plural = _(u'Cell line annotations')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


class Celllinebatch(models.Model):
    batchcellline = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), null=True, blank=True)
    batchstatus = models.ForeignKey('Batchstatus', verbose_name=_(u'Batch status'), null=True, blank=True)
    batchstatusdate = models.CharField(_(u'Batch status date'), max_length=20, blank=True)
    batchstatusupdatedby = models.ForeignKey('Useraccount', verbose_name=_(u'User account'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line batch')
        verbose_name_plural = _(u'Cell line batches')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)



class Aliquotstatus(models.Model):
    aliquotstatus = models.CharField(_(u'Aliquot status'), max_length=20, blank=True)

    class Meta:
        verbose_name = _(u'Aliquot status')
        verbose_name_plural = _(u'Aliquot statuses')
        ordering = ['aliquotstatus']

    def __unicode__(self):
        return u'%s' % (self.aliquotstatus,)


class Celllinegenemutationsmolecule(models.Model):
    celllinegenemutations = models.ForeignKey('Celllinegenemutations', verbose_name=_(u'Cell line gene mutations'), null=True, blank=True)
    genemutationsmolecule = models.ForeignKey('Molecule', verbose_name=_(u'Molecule'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line gene mutations molecule')
        verbose_name_plural = _(u'Cell line gene mutations molecules')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)
