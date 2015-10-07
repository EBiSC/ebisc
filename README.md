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


## Search

- Dump ORM data to ElasticSearch
- Load data via ajax
- Display data
- Write update function
- Write searching / filtering widgets
- Connect widgets with update function

## Exec dashboard

- Data display: depositor data, batch QC data, document management
- EBiSC Board Members (set user accounts)
- Order first by most recent
- Print version Cell line data
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
- List of diseases? (page 97) -> then you get a list of celllines for that disease?? (... page 99) - cell line comparisons
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

## Questions Barry/Dana

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

### Users

Cell line depositor -- is someone who is coming to the service to provide EBiSC with iPSCs. 
Catalogue user -- is someone coming to the EBiSC website to search for cell lines ultimately with the intention to buy them 
ECACC user -- someone who is interacting with ECACC rather than EBiSC directly
Core facility user -- representing people like Rachel from Roslin cells who need to interact with the IMS
WP7 member -- representing Helen/Andreas/Alex and other stake holders within the work package 
Board member -- representing Aidan/Tim and would be used if we need to meet EBiSC business needs such as reporting

### October

As a WP7 member I want to view data stored in the IMS

- Set up production server
- Display all data in the IMS on the EBISC portal
- Change log for production server

1) As an IMS user I want IMS to reflect hPSCreg updates within 24 hours - Done when IMS is pulling hPSCreg data automatically every 24 hours.

2) Ontologies

3) Querying for batch and vial Biosample IDs

- In ECACC if there is no disease specified, it should display ‘Normal’ not ‘CONTROL’. Fix in IMS export. Maja



### October/November

As an IMS developer I want to document how data updates are recorded in the IMS
    Define how IMS is recording data updates, audit trail, level of granularity.
    The IMS needs to define its update schedule and the granularity at which updates are recorded and what the audit trail is for updates

As an IMS developer I want define sync dates for data exchange between different WP7 components
    Coordinate discussion with members of the dev team to define sync dates for automated data flows between all EBiSC components: hESCreg, IMS, ECACC, LIMS/RC and BioSamples.
    DOD: Document the reached decision and make the final document available on the ARTTIC website.

Get stock and sales info from ECACC (via EBI ftp)

Complete single sign on between IMS and Hpscreg Steffi/Maja/Rok

As the IMS I need to track the latest image thumbnail with "some" meta data for morphology

Make the first implementation for ECACC catalog number assignment

Allow users to assign embargos/hold untill publication dates for cellular data  Steffi/Maja

Availability (ETA … in 5 months). ECACC needs to pull even if not shipped to them. (flag?) – linked to cell line because some may not even have first batches made.

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

- As a EBiSC customer I want to see documents about receipt of cell lines
    There will be a set of documents applicable to all cell lines. The documents will describe what to do when the customer receives a cell line, e.g. how to culture them.
    Done when IMS can display these documents to customers.

- "These tests have been performed on all our cell lines" - this should be part of every cell line (same for all).
- INFO on the website: our cell lines go through these protocols, QC.

- Protocols for QC - in principle they need to be available to users (as pdfs).
- Culture protocols are being prepared as user manuals. They will be shared with users. Alex sets this as top protocols (cellluler phenotypes and differentation)

- Intent to deposit


