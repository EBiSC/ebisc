# TODO

## Before launch

- [x] implement CLIP upoload
- [x] user management (accounts + open the catalogue)
- [x] change from BioSamples ID to hPSCreg name in the URLs and tables
- [x] implement flag "go live" and status/availability to be set in the IMS (exec dash)
- [x] Set ECACC catalogue numbers for expand to order lines - get all assigned ECACC catalogue numbers from RC
- [x] change ECACC URL
- [x] can_manage_executive_dashboard works only for superusers

Data import and display:
- [x] get feedback on data displayed in the Catalogue
- [ ] import new disease, cell type and characterization data from hPSCreg
- [ ] ordering in the catalogue (initial state) - has to be alphabetical by name

Elastic search:
- [x] remove biosamples id from table
- [x] add donor sex to filters
- [ ] fix filter loading/init on facet additions
- [ ] add search fields
- [ ] reset search input

## LIMS exchange

### Old data from hPSCreg

primary_celltype_purl
integrating_vector_gene_list
non_integrating_vector_gene_list
vector_free_types
feeder_cells_name
culture_conditions_medium_culture_medium_other_supplements
internal_donor_ids
disease_associated_phenotypes
donor_karyotype
virology_screening_flag
certificate_of_analysis_flag

primary_celltype_purl
integrating_vector_gene_list
non_integrating_vector_gene_list
vector_free_types
feeder_cells_name
culture_conditions_medium_culture_medium_protocol_file
internal_donor_ids
disease_associated_phenotypes
donor_karyotype_flag
virology_screening_flag
certificate_of_analysis_flag

### New data from hPSCreg

In the depositor culture conditions section:

  1)  "Has Rock inhibitor (Y27632) been used at passage previously with this cell line?" -> “Yes” or “No” or “Unknown”  (Mandatory question)
  2)  "Has Rock inhibitor (Y27632) been used at cryo previously with this cell line?" -> “Yes” or “No” or “Unknown”  (Mandatory question)
  3)  "Has Rock inhibitor (Y27632) been used at thaw previously with this cell line?" -> “Yes” or “No” or “Unknown”  (Mandatory question)

In the reprogramming method section.

  If the depositor selects non-intergrating vector then ask:
  	4) Is reprogramming vector detectable? -> “Yes” or “No” or “Unknown”  (Mandatory question)
  	if depositor answers “Yes” then ask:
  		5) “Method used?” -> “immune marker staining” or “PCR” or “rtPCR” or “sequencing”  (Mandatory question)
  		5b) “Notes on reprogramming vector detection” -> Free text  (Optional question)
  		5c) “Files and images showing reprogramming vector presence or absence” -> File upload  (Optional question)

  If the depositor selects intergrating vector then ask:
  	6) Have the reprogramming vectors been silenced? -> “Yes” or “No” or “Unknown”  (Mandatory question)
  	if depositor answers “Yes” then ask:
  		7) “Method used?” -> “immune marker staining” or “PCR” or “rtPCR” or “sequencing”  (Mandatory question)
  		7b) “Notes on reprogramming vector silencing” -> Free text  (Optional question)
  		7c) “Files and images showing reprogramming vector expressed or silenced” -> File upload  (Optional question)


## hPSCreg importer

- Characterization
- Documents
- Check for updates for genes in Reprogramming method and Genetic modification
- Check Disease associated genotype (no data yet)

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

- Table:
    - Biosamples ID
    - Name
    - Depositor
    - Disease
    - Cell type
    - Cell line name synonyms
- Filters:
    - Disease
    - Depositor
    - Cell type
    - Tissue source
- For sales link to ECACC? ... It would make more sense if users could "fill" their basket on IMS and then just complete the checkout on ECACC.
- hPSCreg "comparator line"

## EBiSC Knowledge Community

- Assistance and support on differentiation, tests performed etc.?

  Services:
    - Protocols (support material): (uploaded by depositors, approved by execs?)
        - cell line derivation protocol
        - quality control
        - investigations
        - etc
    - Training, support and experts
    - Knowledge forum

- Feedback form 30 days after purchase
- Support - not finalized

## Users

- Could project members have the same passwords?

## Feedback ideas, suggestions, ...

- limiting and paging of search results - currently works for 60, won't scale much higher
- add/remove which result columns displayed?
- not obvious that columns are sortable - display double arrows when unsorted?
- search and facet on executive dashboard
- cell line name sort descending not working correctly
- number of unique donors in search results e.g. 60 cell lines from 48 donors
- only searches information in table, not full record e.g. ATXN3 has no results
- omit types where no value avaliable, and sections where no values avaliable
- links/mouseover to longer descriptions of attributes ??
- hescreg name in title, biosample id in url - should be consistently one or the other
- one page per donor, summarizing information and linking to all lines?
- one page per batch with QC information?

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

+ Set up production server
+ Display all data in the IMS on the EBISC portal
- Change log for production server

1) As an IMS user I want IMS to reflect hPSCreg updates within 24 hours - Done when IMS is pulling hPSCreg data automatically every 24 hours.

2) Ontologies

3) Querying for batch and vial Biosample IDs

+ In ECACC if there is no disease specified, it should display ‘Normal’ not ‘CONTROL’. Fix in IMS export. Maja


User Stories #1469: As an EBiSC Developer I need a plan on how to pull updates from the hPSCreg API
    - Overtime, cell lines which are part of EBiSC may see updates to their information registered in hPSCreg.
    - DC need to plan how they will monitor for updates and update the IMS to reflect the changes.
    - This will be done when the requirements analysis is done, a written plan is in place and the tickets representing the implementation place are in redmine.


### November/December

As an IMS developer I want to document how data updates are recorded in the IMS
    Define how IMS is recording data updates, audit trail, level of granularity.
    The IMS needs to define its update schedule and the granularity at which updates are recorded and what the audit trail is for updates

As an IMS developer I want define sync dates for data exchange between different WP7 components
    Coordinate discussion with members of the dev team to define sync dates for automated data flows between all EBiSC components: hESCreg, IMS, ECACC, LIMS/RC and BioSamples.
    DOD: Document the reached decision and make the final document available on the ARTTIC website.

Get stock and sales info from ECACC (via EBI ftp)

As the IMS I need to track the latest image thumbnail with "some" meta data for morphology

Make the first implementation for ECACC catalog number assignment

Availability (ETA … in 5 months). ECACC needs to pull even if not shipped to them. (flag?) – linked to cell line because some may not even have first batches made.

Allow users to assign embargos/hold untill publication dates for cellular data  Steffi/Maja

Complete single sign on between IMS and Hpscreg Steffi/Maja/Rok

For automation of (i) IMS - HpscReg exchange process and (ii) LIMS - IMS BioSample batch IDs exchange define synch dates. (Define synch dates for non linear data flow processes within IMS/WP7 data flow)

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
