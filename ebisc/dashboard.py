from django.utils.translation import ugettext_lazy as _

from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):

    def init_with_context(self, context):

        # User & groups
        self.children.append(modules.ModelList(
            _('Administration'),
            column=1,
            collapsible=False,
            models=('django.contrib.*',),
        ))

        self.children.append(modules.Group(
            _('EBiSC'),
            column=1,
            collapsible=False,
            children=[
                modules.ModelList(
                    _('One'),
                    collapsible=True,
                    column=1,
                    css_classes=('collapse closed',),
                    models=('ebisc.celllines.models.Accesslevel',),
                ),
            ]
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Links'),
            column=2,
            collapsible=False,
            children=[
                {
                    'title': _('EBiSC Home'),
                    'url': 'http://www.ebisc.org/',
                    'external': True,
                },
                {
                    'title': _('hESCreg'),
                    'url': 'http://www.hescreg.eu/',
                    'external': True,
                },
            ]
        ))

'''
Accesslevel
Aliquotstatus
Approveduse
Batchstatus
Binnedage
Cellline
Celllinealiquot
Celllineannotation
Celllinebatch
Celllinecharacterization
Celllinechecklist
Celllinecollection
Celllinecomments
Celllinecultureconditions
Celllineculturesupplements
Celllinederivation
Celllinediffpotency
Celllinediffpotencymarker
Celllinediffpotencymolecule
Celllinegenemutations
Celllinegenemutationsmolecule
Celllinegeneticmod
Celllinegenomeseq
Celllinegenotypingother
Celllinehlatyping
Celllinekaryotype
Celllinelab
Celllinelegal
Celllinemarker
Celllineorganization
Celllineorgtype
Celllinepublication
Celllinesnp
Celllinesnpdetails
Celllinesnprslinks
Celllinestatus
Celllinestrfingerprinting
Celllinevalue
Celllinevector
Celllinevectorfreereprogramming
Celllinevectormolecule
Celltype
Clinicaltreatmentb4donation
Contact
Contacttype
Country
Culturemedium
Culturesystem
Disease
Document
Documenttype
Donor
Ebisckeyword
Enzymatically
Enzymefree
Gender
Germlayer
Hla
Karyotypemethod
Keyword
Lastupdatetype
Marker
Molecule
Morphologymethod
Organization
Orgtype
Passagemethod
Person
Phenotype
Phonecountrycode
Postcode
Primarycelldevelopmentalstage
Proteinsource
Publisher
Reprogrammingmethod1
Reprogrammingmethod2
Reprogrammingmethod3
Strfplocus
Surfacecoating
Tissuesource
Transposon
Units
Useraccount
Useraccounttype
Vector
Vectorfreereprogramfactor
Vectortype
Virus
'''
