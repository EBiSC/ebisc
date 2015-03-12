# EBiSC

## Development setup

    virtualenv var/virtualenv
    go ebisc
    pip install -r requirements.txt
    createdb ebisc
    cd ebisc/settings/ ; ln -s develop.py __init__.py ; cd -
    ./manage.py migrate
    ./manage.py initcms
    ./manage.py loaddata var/fixtures/auth.json
    npm install
    bower install

In one shell run `./manage.py runserver` and then in the other `gulp watch`.


## ORM

CREATE DATABASE ebisc;
CREATE USER 'joh'@'localhost';
GRANT ALL ON ebisc.* TO 'joh'@'localhost';
mysql ebisc < schema.sql
./manage.py inspectdb --database source > ebisc/celllines/models-inspectd.py


## Questions

- Schema migration: how it is done?
    - Freeze feb 20
    - 4 changes since then
- HotStart data: is it aligned with the model?
    - It is incomplete
    - Has referential problems
    - cellinelab & cellinechecklist added
    - Report: where?
    - ECACC -> FTP, CSV
- Are there any 'unique together' constraints?
- Do we validate URLs -> fields containing url to URLField?
- Do we convert max_length=1000 fields to variable length char field TextField?

- A lot of fields are optional - this does not look right!

- Why is ForeignKey + Unique=True used instead of embedded fields?


## TODO

- [ ] Convert ForeignKey + Unique=True to OneToOne field or use embed (see questions)


## Changes

    Model: Celllinestatus
    Before: celllinestatus = models.CharField(_(u'Cell line status'), max_length=20, blank=True)
    After: celllinestatus = models.CharField(_(u'Cell line status'), max_length=50, blank=True)
    Example: Hot Start cell line (not available)


    Model: Celllinechecklist
    New:
        checklistcellline = models.OneToOneField(Cellline)
        morphologicalassessment = models.BooleanField(_(u'Morphological assessment'), default=False)
        facs = models.BooleanField(_(u'FACS'), default=False)
        ihc = models.BooleanField(_(u'IHC'), default=False)
        pcrforreprofactorremoval = models.BooleanField(_(u'PCR for reprofactor removal'), default=False)
        pcrforpluripotency = models.BooleanField(_(u'PCR for pluripotency'), default=False)
        teratoma = models.BooleanField(_(u'Teratoma'), default=False)
        invitrodifferentiation = models.BooleanField(_(u'Invitro differentiation'), default=False)
        karyotype = models.BooleanField(_(u'Karyo type'), default=False)
        cnvanalysis = models.BooleanField(_(u'CNV analysis'), default=False)
        dnamethylation = models.BooleanField(_(u'DNA methylation'), default=False)
        microbiologyinclmycoplasma = models.BooleanField(_(u'Micro biology inclmycoplasma'), default=False)
        dnagenotyping = models.BooleanField(_(u'DNA genotyping'), default=False)
        hlatyping = models.BooleanField(_(u'HLA typing'), default=False)
        virustesting = models.BooleanField(_(u'Viru stesting'), default=False)
        postthawviability = models.BooleanField(_(u'Post thawviability'), default=False)
        checklistcomments = models.TextField('Checklist comments', null=True, blank=True)

clininicaltreatmentb4donation -> clinicaltreatmentb4donation
