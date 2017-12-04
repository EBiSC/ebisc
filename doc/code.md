# The EBiSC IMS code

This document gives and overview of the files where main pieces of code that drive the EBiSC IMS are located.

EBiSC IMS is just one of the components in the EBiSC data system. You can refer to file [EBiSC Data Overview](https://cells.ebisc.org/static/documents/201709-EBiSC_Data_Overview.xlsx) to see where EBiSC cell line data originates and how it moves through different system components.

## Models

Definitions of all cell line models are located here:

    /ebisc/celllines/models.py

This file contains the essential fields and behaviours of the stored data in the EBiSC IMS.

Code in the file:

    /ebisc/celllines/admin.py

defines the automatic Django admin interface for managing some cell line data. Since most of the data is imported into IMS from different sources and gets updated once a day, this interface is set up to only manage certain fields (eg. cell line, donor BioSample IDs) in case of errors or inconsistencies between the EBiSC components.

## Importers

### hPSCreg

Importers for cell line data provided by depositors at [hPSCreg](https://hpscreg.eu/):

    /ebisc/celllines/importer/hpscreg/


### ElasticSearch

    /ebisc/celllines/importer/toelastic.py

Imports data to ElasticSearch.

* Which cell line data gets imported is defined in: `/ebisc/celllines/models.py` in method `to_elastic()`.
* ElasticSearch settings are defined in `/ebisc/celllines/elastic` and `/assets/scripts/search/`

### Batch BioSample IDs

Script for importing batch and vial BioSample IDs from .csv BioSample exports:

    /ebisc/celllines/importer/batches.py

 This only needs to be used in case of backfilling already created ID accessions. New batches should be created via EBiSC Executive Dashboard.

## Cell line catalogue

Templates for cell line catalogue pages are located in the folder:

    /ebisc/site/templates/catalog/

View that defines the display logic of an individual cell line page is defined in function `page()` in file `/ebisc/site/views.py`.

## Executive dashboard

The business logic of the Dashboard (eg. creating BioSample ID accessions for batches and vials, batch data uploads) is defined in:

    /ebisc/executive/views.py

Dashboard specific templates are stored in folder:

    /ebisc/executive/templates/executive/

## EBiSC API

Tastypie API framework for Django is used to create the EBiSC API. Settings and definitions are stored here:

    /ebisc/api/

Detailed API documentation is located [here](../api.md).


## Supporting content pages (pages for customers, depositors and FAQ pages)

Pages for customers and depositors are managed via a simple CMS that uses the default Django admin interface. The CMS can be used to edit existing content, create new pages and upload documents. HTML and Markdown markup language are  used for formatting the content. Source code for the CMS is located here:

    /ebisc/cms/

FAQ management is written in a separate app:

        /ebisc/site/faq/

The CMS UI is located here: [https://cells.ebisc.org/admin/cms/](https://cells.ebisc.org/admin/cms/). You need administrator credentials to access these pages.


## Frontend: CSS and JS

CSS and JS source code is stored here:

    /assets/

## User guides and documentation

User documentation for the Executive Dashboard is located here:

    /ebisc/static/documents/

The latest version can also be viewed and downloaded by clicking on the blue `Help` link located on the bottom right side of all pages in the Dashboard.

EBiSC Catalogue user guide is uploaded via the CMS and can be found there.
