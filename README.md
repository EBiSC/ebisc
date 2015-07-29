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

1) As an IMS developer I want to query pseudo LIMS API and begin importing data from the Central facility (interim solution)

Connect to LIMS API.
Import sample batch data from EBI "LIMS" API.

2) As an IMS developer I want to query hPSCreg API and automate import of depositor data into the IMS

Use hPSCreg API for data import.

3) As an IMS developer I want to document authority for each field in the IMS

Collect:
    - info on who holds authority for each field in the IMS
    - API field names for data exchange
    - ...

4) As an IMS developer I want to document how data updates are recorded in the IMS 

Define how IMS is recording data updates, audit trail, level of granularity.


### August/September

I as an IMS developer need to track the number of vials at Core facility and IMBT in order to track stock levels. The IMS needs to track this information.  Ian/maja    

### September

1) As an IMS developer I want to display and export batch data

Display batch data on EBiSC cell line catalogue.
Display batch data on EBiSC executive dashboard.
Export batch data in IMS API.

2) Ontologies

?

3) Querying for batch and vial Biosample IDs


September

WORK ON API !!! (all data, additional endpoints - donor, batch, transaction log)

Complete single sign on between IMS and Hpscreg Steffi/Maja/Rok

Allow users to assign embargos/hold untill publication dates for cellular data  Steffi/Maja 
In ECACC if there is no disease specified, it should display ‘Normal’ not ‘CONTROL’. Fix in IMS export. Maja
IMS to take in LIMs culture conditions and export them to ECACC.    Maja

IMS needs to assemble AUA (MTA) from standard EBiSC template and user specified restrictions in order to provide to ECACC as single per line PDF. ??? (Kevin: not to done automatically)
- AUA (MTA) – get manually input into IMS by someone within EBiSC . EBiSC exec will add 3rd party restrictions to AUA template and upload it to IMS. IMS will send AUA via API to ECACC.

- Availability (ETA … in 5 months). ECACC needs to pull even if not shipped to them. (flag?) – linked to cell line because some may not even have first batches made.


### September, October

IMS needs to pull donor / line updates from hPSCReg?


### October/November

As the IMS I need to track the latest image thumbnail with "some" meta data for morphology


### November

For automation of (i) IMS - HpscReg exchange process and (ii) LIMS - IMS BioSample batch IDs exchange define synch dates. (Define synch dates for non linear data flow processes within IMS/WP7 data flow)


### December

I as an EBiSC catalog user need a walk-through for key tasks.   Maja    December


### 2016

I as an EBiSC catalogue user want to know time to ship for an individual cell line to enable purchase decision making   DC  2016


### Not assigned dates

- Import ECACC data from ftp

- Cell lines related to this line (isogenic,... same donor line ... connect these)
- Gene edited lines (also use disease phenotype even if it has been edited so that the cell line has no more phenotype) Maybe an icon for gene edited lines.

- "These tests have been performed on all our cell lines" - this should be part of every cell line (same for all).
- INFO on the website: our cell lines go through these protocols, QC.

- Protocols for QC - in principle they need to be available to users (as pdfs).
- Culture protocols are being prepared as user manuals. They will be shared with users. Alex sets this as top protocols (cellluler phenotypes and differentation)

- Intent to deposit





