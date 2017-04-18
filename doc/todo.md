# TODO

## ECACC exchange

- Start using the ECACC API to check for availability in their catalogue

## LIMS exchange

- Go from pseudo LIMS to LIMS?

## New data from hPSCreg

1) Donor karyotype

  Add files and method (with links and files)
  Move fields from cellline to donor (medical history, clinical info, ...)

2) In the depositor culture conditions section:

  1)  "Has Rock inhibitor (Y27632) been used at passage previously with this cell line?" -> “Yes” or “No” or “Unknown”  (Mandatory question)
  2)  "Has Rock inhibitor (Y27632) been used at cryo previously with this cell line?" -> “Yes” or “No” or “Unknown”  (Mandatory question)
  3)  "Has Rock inhibitor (Y27632) been used at thaw previously with this cell line?" -> “Yes” or “No” or “Unknown”  (Mandatory question)

3) In the reprogramming method section.

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

4) Characterization


## hPSCreg importer

+ Documents
- Check for updates for genes in Reprogramming method and Genotyping data
- Check Disease associated genotype (no data yet)

## Exec dashboard

- Stock information

## Cell line Catalog

- Ontologies
- Search all
- Keywords and filters in urls
- Disease pages
- FAQ
- Videos
- limiting and paging of search results
- cell line name sort descending not working correctly
- number of unique donors in search results e.g. 60 cell lines from 48 donors
- one page per donor, summarizing information and linking to all lines?
