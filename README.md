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

## Search

- Dump ORM data to ElasticSearch
- Load data via ajax
- Display data
- Write update function
- Write searching / filtering widgets
- Connect widgets with update function

## Exec dashboard

- EBiSC Board Members (set user accounts)
- Order first by most recent 
- Print version Cell line data
- Grouping of data (Dana)
- Sales information (future goal - need to get QTY info from LIMS and sales data from ECACC)
- Option: Should there be a way for EBM to add notes to the Cell Line regarding Accept/Reject?
- Filters:
    - Accepted/Rejected/Pending (maybe proposed is a better word)
    - Depositor
    - Any other attribute? (Disease, Cell type, Tissue source)
    - Cell line status: available/not available
- Search: inlcudes all atributes

## Depositor dashboard

- Cell line registration? Together will all documentation (MDA, shipping documents, labels for vials)
- Change contact/account info
- See deposited cell lines and their status

## Cell line Catalog

- User is customer
- Table:
    - Biosamples ID
    - Name
    - Depositor
    - Disease
    - Cell type
    - Cell line name synonims
- Filters:
    - Disease
    - Depositor
    - Cell type
    - Tissue source
    ------------------------------------
    - Protocol?
    - Mutant gene? (mutagene - not defined terms)
    - Growth mode?
    - Culture medium (we have, but empty for now) / culture system
    - Available formats? (ECACC)
- For sales link to ECACC? ... It would make more sense if users could "fill" their basket on IMS and then just complete the checkout on ECACC. 

## EBiSC Knowledge Community

- User is customer
- List of diseases? (page 97) -> then you get a list of celllines for that disease?? (... page 99) - primerjave med cell lini
- Assistance and support on differentiation, tests performed etc.?

  Services: 
    - Protocols (support material): (uploaded by depositors, approved by execs?)
        - cell line derivation protocol
        - quality control
        - investigations
        - etc
    - Training, support and experts
    - Knowledge forum

- Objective of the IMS: "To capture and make available all iPSC-associated protocols (generation, characterisation, expansion, differentiation, reporter enhancement) based on standardised approach to metadata and vocabulary (e.g., with ISA-TAB www.isa-tools.org as used by ToxBank (Kohonen et al 2013), Harvard Stem Cell Discovery Engine)."

- Tasks: "procurement of cell lines (interaction with WP2.1 on T2.1.2); protocols and clinical data (interaction with WP2.1 on T2.1.1); data associated with emerging technologies including SOPs for donor cell receipt, reprogramming and iPSC production (WP2.1 and WP3); ethical, legal and IP guidance (WP4.1); training needs (WP4.2) and QC requirements (WP5)."

- Feedback form 30 days after purchase
- Support - not finalized

## Users

- Could project members have the same passwords?

## Data model

Add? (hESCreg has this, if we want it, we have to ask for it, they will put it in the API):
    - Family history
    - Patient history
    - amino acid / or DNA level change (requirement by Alex, the data is captured by hESCreg)
    - anything else ...

## Feedback ideas, suggestions, ...

- "Coord Blood (CD133+ cells)" should be "Cord Blood (CD133+ cells)"
- limiting and paging of search results - currently works for 60, won't scale much higher
- add/remove which result columns displayed?
- not obvious that columns are sortable - display double arrows when unsorted?
- search and facet on executive dashboard
- remove facet when zero hits due to search term?
- cell line name sort descending not working correctly
- some weirdness in ascending e.g. BIONi010-C then BIONi013-A then BIONi010-B
- number of unique donors in search results e.g. 60 cell lines from 48 donors
- only searches information in table, not full record e.g. ATXN3 has no results
- omit types where no value avaliable, and sections where no values avaliable
- links/mouseover to longer descriptions of attributes ??
- hescreg name in title, biosample id in url - should be consistently one or the other
- one page per donor, summarizing information and linking to all lines
- one page per batch with QC information
- some character handling errors? unicode long-dashes? "HUB-SMN02-1" vs "HUB?SMN04-2"
- UKKi0011-A should be UKKi011-A i.e. always 3 digits not always 2 zeros?

Grouping of cell line info (not to be done yet, wait for hESCreg??):
    - Just to follow up the ‘mutagene’ point. As Laura says it is currently under a heading of ‘Labs’. I’m not sure where those headings are coming from, but at least for the mutagene field that does not seem to be correct. For now I would move it up to the ‘General Information’ section. (Also ‘reprogramming method 1-3’ should surely go under ‘Derivation’). And ‘Funder’ would seem to be more at home with the ‘Depositor’ section.


## Questions Barry/Dana

- Do we need to develop cell line registration in the IMS? And as a consequence the depositor registration.
- Are all hot start cell lines banked and available for purchase?
- Which are the milestones for the executive dashboard that we will want to show as status on the dashboard? 
    - is registered
    - MDA ?
    - pending/accepted/rejected for deposit,
    - tracked by LIMS
    - LIMS sent labels to cell line suppliers
    - LIMS received cells

    - QC cell lines (one test/attribute per qc test)
    - LIMS has sent cell line inventory / batch data to IMS
    - LIMS has sent QC data to IMS
    - LIMS has sent Certificate of Analysis (CoA) to IMS
    - ECACC has cells
    - ECACC has CoA / data
    - IBMT mirror bank has cells


    - QC
    - passed QC, can be banked
    - LIMS data sent to depositor
    - Cell lines banked and
    - available in public catalogue

    - registration / MDA
    - pending/accepted/rejected for deposit,
    - shipping instructions, labels, ... sent to depositor
    - cell line received 
    - cell line banked and available in public catalogue

- Cell line batch/Aliquot?? Are children of cell line, have their own biosamplesIDs and have different status then cell line.

## LIMS fields

- Clone ID

- Tests are batch specific

- QC is batch specific, and this doesn’t need to be shown in IMS, LIMS generates the cert. of analysis
- QC tests and results for IMS, Cert. of analysis for ECACC (goes to IMS but then should be passed on to ECACC)

- Determine image storage needs and data model (currently images stored as a document) - type (format), annotation of image and/or region of interest etc

- Protocols (available in SOP format)? Kevin said would provide human readable format - there is a video for ToxBank protocol management

- Passage Number (measured from Reprogramming)

## Biosamples IDs

- IMS needs to get them for batches and vials (once LIMS has done the work)

## hESCreg fields

- Donor
- Cell type (necessary) - Derivation
- Anatomical location - Derivation
- Disease Carrier (affected/unaffected/carrier)
- Donor Phenotype (multiple, entered when there is no disease)
- Disease Phenotype (related to the donor?)
- Disease associated genotypes -> change to ‘Phenotype Associated Variant’
- Donor Karyotype, there might be also a Cell Line karyotype
- Family history
- Medical history available
- Other clinical info
- Ethnicity
- Country of origin

## Sprints

### August 


1) As an IMS developer I want to start using hPSCreg API for importing depositor data into the IMS

Update the importer to include all data exported from hPSCreg (except Characterization section).

Query hPSCreg API for data import.

2) As an IMS developer I want to document authority for each field in the IMS

Collect:
    - info on who holds authority for each field in the IMS
    - json names used in data exchange
    - ...

3) Set up production server

------------------------------

3) As an IMS developer I want to query pseudo LIMS API and begin importing data from the Central facility (interim solution)

Connect to LIMS API.
Import sample batch data from EBI "LIMS" API.

4) As an IMS developer I want to document how data updates are recorded in the IMS 

Define how IMS is recording data updates, audit trail, level of granularity.
The IMS needs to define its update schedule and the granularity at which updates are recorded and what the audit trail is for updates

5) As an IMS developer I want define sync dates for data exchange between different WP7 components

Coordinate discussion with members of the dev team to define sync dates for automated data flows between all EBiSC components: hESCreg, IMS, ECACC, LIMS/RC and BioSamples.

DOD: Document the reached decision and make the final document available on the ARTTIC website.

### August/September

I as an IMS developer need to track the number of vials at Core facility and IMBT in order to track stock levels. 
The IMS needs to track this information.  Ian/maja    

### September

1) As an IMS developer I want to display and export batch data

Display batch data on EBiSC cell line catalogue.
Display batch data on EBiSC executive dashboard.
Export batch data in IMS API.

2) Ontologies

?

3) Querying for batch and vial Biosample IDs

4) Change log for production server

September

WORK ON API !!! (all data, additional endpoints - donor, batch, transaction log)

Complete single sign on between IMS and Hpscreg Steffi/Maja/Rok

Allow users to assign embargos/hold untill publication dates for cellular data  Steffi/Maja 
In ECACC if there is no disease specified, it should display ‘Normal’ not ‘CONTROL’. Fix in IMS export. Maja
IMS to take in LIMs culture conditions and export them to ECACC.    Maja

IMS needs to assemble AUA (MTA) from standard EBiSC template and user specified restrictions in order to provide to ECACC as single per line PDF. ??? (Kevin: not to done automatically)
- AUA (MTA) – get manually input into IMS by someone within EBiSC . EBiSC exec will add 3rd party restrictions to AUA template and upload it to IMS. IMS will send AUA via API to ECACC.

- Availability (ETA … in 5 months). ECACC needs to pull even if not shipped to them. (flag?) – linked to cell line because some may not even have first batches made.


Feature #1430: Defining requirements for reporting stock info back to IMS
    As an ECACC IT manager I would like to know from the EBISC team what stock information IMS would like back from us. The technical restriction is - we cant have any inbound call to our Oracle database (aka FARM)
    Possible solution 
    Can IMS provide us with a host FTPS server login credentials, we can then write the file there from Oracle. Preferable format for the file can be XML, txt (pipe separated) or csv


### September, October

IMS needs to pull donor / line updates from hPSCReg?


### October/November

As the IMS I need to track the latest image thumbnail with "some" meta data for morphology

Make the first implementation for ECACC catalog number assignment

### November

For automation of (i) IMS - HpscReg exchange process and (ii) LIMS - IMS BioSample batch IDs exchange define synch dates. (Define synch dates for non linear data flow processes within IMS/WP7 data flow)

User Stories #1469: As an EBiSC Developer I need a plan on how to pull updates from the hPSCreg API
    - Overtime, cell lines which are part of EBiSC may see updates to their information registered in hPSCreg.
    - DC need to plan how they will monitor for updates and update the IMS to reflect the changes.
    - This will be done when the requirements analysis is done, a written plan is in place and the tickets representing the implementation place are in redmine.


### December

I as an EBiSC catalog user need a walk-through for key tasks.   Maja    December


### 2016

I as an EBiSC catalogue user want to know time to ship for an individual cell line to enable purchase decision making   DC  2016


### Not assigned dates

- As a EBiSC developer I need to plan how to alllow cell line depositors to specify state hold dates on data release
    Many archives/databases including hPSCreg allow users to specify hold dates for data release.
    We need to figure out where it is appropriate in the EBiSC system for hold dates to be specified and how to ensure the difference services know about them and respect them
    This will be done when we have plan for allowing hold data specification which has been approved on a Tuesday WP7 call.

- Import ECACC data from ftp

- Cell lines related to this line (isogenic,... same donor line ... connect these)
- Gene edited lines (also use disease phenotype even if it has been edited so that the cell line has no more phenotype) Maybe an icon for gene edited lines.

- "These tests have been performed on all our cell lines" - this should be part of every cell line (same for all).
- INFO on the website: our cell lines go through these protocols, QC.

- Protocols for QC - in principle they need to be available to users (as pdfs).
- Culture protocols are being prepared as user manuals. They will be shared with users. Alex sets this as top protocols (cellluler phenotypes and differentation)

- Intent to deposit





## Data model cleanup

### Cellline

celllineaccepted
accepted

celllinename
name

celllinenamesynonyms
alternative_names

biosamplesid
biosamples_id

hescregid
hescreg_id

ecaccid
ecacc_id

celllineprimarydisease
primary_disease

celllinediseaseaddinfo
primary_disease_stage
- need to add primary_disease_phenotypes

celllinestatus
status

celllinecelltype
- removed, using Derivation -> primary cell type

celllinecollection
- removed for now. collections were meant to be used for common MDAs and AUAs - will implement in september

celllinetissuesource
- moved to Derivation: tissue_procurement_location

celllinetissuedate
- moved to Derivation: tissue_collection_date

celllinetissuetreatment
- removed. will be probably added later if donor medical/clinical info becomes available

depositorscelllineuri
- removed

comments
- removed

### Donor

countryoforigin
country_of_origin

primarydisease
diseaseadditionalinfo
- removed (goes to cell line)
othercelllinefromdonor
parentcellline
cellabnormalkaryotype
donorabnormalkaryotype
otherclinicalinformation
- removed (hSECreg does not collect this anymore)

<!--     primarydisease = models.ForeignKey('Disease', verbose_name=_(u'Disease'), null=True, blank=True)
    diseaseadditionalinfo = models.CharField(_(u'Disease additional info'), max_length=45, blank=True)
    othercelllinefromdonor = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), related_name='celllines_othercelllinefromdonor', null=True, blank=True)
    parentcellline = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), related_name='celllines_parentcellline', null=True, blank=True)
    cellabnormalkaryotype = models.CharField(_(u'Cell abnormal karyotype'), max_length=45, blank=True)
    donorabnormalkaryotype = models.CharField(_(u'Donor abnormal karyotype'), max_length=45, blank=True)
    otherclinicalinformation = models.CharField(_(u'Other clinical information'), max_length=100, blank=True)
 -->

### Cellline Culture Conditions

surfacecoating
surface_coating

feedercelltype
feeder_cell_type

feedercellid
feeder_cell_id

passagemethod
passage_method

### Batch Culture Conditions

passagemethod
passage_method

enzymefree
enzyme_free

o2concentration
o2_concentration

co2concentration
co2_concentration

other_culture_environment
- added

passage_number_banked
- added

number_of_vials_banked
- added

Add this when completed

Passage history (back to reprogramming)
Culture History (methods used) 

### Cellline Derivation

primarycelltypename
primarycelltypecellfinderid
- moved to foreignkey CellType (id still needs to be done). This will be done with ontologies in some future ...
- need to fix importer to import this correctly (via parse_cell_type)!!!!

primarycelldevelopmentalstage
primary_cell_developmental_stage

reprogramming_passage_number
passage_number_reprogrammed
- added

selectioncriteriaforclones
selection_criteria_for_clones

xenofreeconditions
xeno_free_conditions

derivedundergmp
derived_under_gmp

vectorfreereprogramfactor
vector_free_reprogramming_factor

referenceid
reference_id

### Cellline Organization

orgcellline
cell_line

celllineorgtype
cell_line_org_type

orgstatus
- removed
    <!-- orgstatus = models.IntegerField(_(u'Organization status'), null=True, blank=True) -->

orgregistrationdate
- removed
    <!-- orgregistrationdate = models.DateField(null=True, blank=True) -->


organizationname
name

organizationshortname
short_name

organizationcontact
contact

organizationtype
org_type

celllineorgtype
cell_line_org_type

orgtype
org_type

contacttype
contact_type

statecounty
state_county

buildingnumber
building_number

suiteoraptordept
suite_or_apt_or_dept

officephonecountrycode
office_phone_country_code

officephone
office_phone

faxcountrycode
fax_country_code

mobilecountrycode
mobile_country_code

mobilephone
mobile_phone

emailaddress
email_address

personlastname
last_name

personfirstname
first_name

personcontact
contact

### Document

cellline
cell_line

documenttype
document_type

documentdepositor
depositor

accesslevel
access_level

### Cell line value

valuecellline
cell_line

potentialuse
potential_use

valuetosociety
value_to_society

valuetoresearch
value_to_research

othervalue
other_value



---------------------

Celltype
CellType

Celllinestatus
CelllineStatus

Celllinecollection
- removed for now. collections were meant to be used for common MDAs and AUAs - will implement in september (maybe differently)

<!-- class Celllinecollection(models.Model):
    celllinecollectiontotal = models.IntegerField(_(u'Cell line collection total'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line collection')
        verbose_name_plural = _(u'Cell line collections')
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.celllinecollectiontotal,)
 -->

Tissuesource
TissueLocation

Clinicaltreatmentb4donation
- removed, will be probably added later if donor medical/clinical info becomes available

Celllinecomments
- removed

CellLineCharacterization
CelllineCharacterization

Celllinechecklist
- removed

<!-- class Celllinechecklist(models.Model):
    checklistcellline = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'))
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
    virustesting = models.BooleanField(_(u'Virus testing'), default=False)
    postthawviability = models.BooleanField(_(u'Post thawviability'), default=False)
    checklistcomments = models.TextField('Checklist comments', null=True, blank=True)

    class Meta:
        verbose_name = _(u'Cell line checklist')
        verbose_name_plural = _(u'Cell line checklists')
        ordering = ['checklistcellline']

    def __unicode__(self):
        return u'%s' % (self.checklistcellline,)
 -->


Celllinecultureconditions
CelllineCultureConditions

CellLineCultureMediumSupplement
CelllineCultureMediumSupplement

Celllinederivation
CelllineDerivation

CellLineNonIntegratingVector
CelllineNonIntegratingVector

CellLineIntegratingVector
CelllineIntegratingVector

Vectorfreereprogramfactor
VectorFreeReprogrammingFactor

CellLineVectorFreeReprogrammingFactors
CelllineVectorFreeReprogrammingFactors

Celllinelab
- removed

<!-- class Celllinelab(models.Model):
    labcellline = models.OneToOneField(Cellline, verbose_name=_(u'Cell line'), null=True, blank=True)
    cryodate = models.DateField(null=True, blank=True)
    expansioninprogress = models.IntegerField(_(u'Expansion in progress'), null=True, blank=True)
    funder = models.CharField(_(u'Funder'), max_length=45, blank=True)
    mutagene = models.CharField(_(u'Mutagene'), max_length=100, blank=True)
    clonenumber = models.IntegerField(_(u'Clone number'), null=True, blank=True)
    passagenumber = models.CharField(_(u'Passage number'), max_length=5, blank=True)
    culturesystem = models.ForeignKey('Culturesystem', verbose_name=_(u'Culture system'), null=True, blank=True)
    culturesystemcomment = models.CharField(_(u'Culture system comment'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Cell line lab')
        verbose_name_plural = _(u'Cell line labs')
        ordering = []

    def __unicode__(self):
        return u'%s' % (self.id,)


 -->

Culturesystem
- removed

<!-- class Culturesystem(models.Model):
    culturesystem = models.CharField(_(u'Culture system'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Culture system')
        verbose_name_plural = _(u'Culture systems')
        ordering = ['culturesystem']

    def __unicode__(self):
        return u'%s' % (self.culturesystem,)
 -->



CellLineLegal
CelllineEthics

Celllineorganization
CelllineOrganization

Celllineorgtype
CelllineOrgType

Orgtype
OrgType

Contacttype
ContactType

Phonecountrycode
PhoneCountryCode

Documenttype
DocumentType


Publisher
- removed

<!-- class Publisher(models.Model):
    publisher = models.CharField(_(u'Publisher'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Publisher')
        verbose_name_plural = _(u'Publishers')
        ordering = ['publisher']

    def __unicode__(self):
        return u'%s' % (self.publisher,)

 -->

 Celllinevalue
 CelllineValue


EBiSC Keyword and Keyword
- removed

<!-- class Ebisckeyword(models.Model):

    cellline = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), null=True, blank=True)
    document = models.ForeignKey('Document', verbose_name=_(u'Document'), null=True, blank=True)
    ebisckeyword = models.ForeignKey('Keyword', verbose_name=_(u'Keyword'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Ebisc keyword')
        verbose_name_plural = _(u'Ebisc keywords')
        ordering = ['cellline', 'document', 'ebisckeyword']

    def __unicode__(self):
        return u'%s - %s - %s' % (self.cellline, self.document, self.ebisckeyword)


class Keyword(models.Model):

    keyword = models.CharField(_(u'Keyword'), max_length=45, blank=True)

    class Meta:
        verbose_name = _(u'Keyword')
        verbose_name_plural = _(u'Keywords')
        ordering = ['keyword']

    def __unicode__(self):
        return u'%s' % (self.keyword,)



 -->
