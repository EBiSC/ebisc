# ECACC Usage of the EBiSC IMS API

The EBiSC IMS API currently has 2 endpoints:

1. List of all cell lines in the IMS: https://ebisc.douglasconnect.com/api/v0/cell-lines/?format=json 
2. Individual cell line records that can be accessed via their BioSamples ID: https://ebisc.douglasconnect.com/api/v0/cell-lines/{BIOSAMPLES_ID}?format=json 

To access the API you must have a valid session (log in at https://ebisc.douglasconnect.com/).

BioSamples IDs of the 7 cell lines that will be imported into the ECACC catalogue are:

    SAMEA2614016  ==  UKBi001-A
    SAMEA2590957  ==  UKBi002-A
    SAMEA2614075  ==  UKBi003-A
    SAMEA2590936  ==  UKBi006-A
    SAMEA2590882  ==  UKBi008-A
    SAMEA2629464  ==  UKKi007-A
    SAMEA4583816  ==  UKKi009-A

Cell line records currently hold data required for data exchange between the IMS and ECACC.

## JSON record structure

    {
        "biosamples_id": "SAMEA4583816",  
        "resource_uri": "/api/v0/cell-lines/SAMEA4583816",
        "name": "UKKi009-A",
        "alternate_names": [
            "NP0012-8"
        ],
        "depositor": {
            "name": "Klinikum der Universität zu Köln"
        },
        "donor": {
           "biosamples_id": "SAMEA4584076",
            "gender": "female"
        },
        "donor_age": "35-39",
        "primary_disease": {
            "doid": "DOID:10273",
            "name": "heart conduction disease",
            "synonyms": [
                "heart rhythm disease"
            ]
        },
        "cell_type": "fibroblast of dermis",
        "culture_conditions": {
            "co2_concentration": 5,
            "culture_medium": "e8",
            "o2_concentration": 20,
            "passage_method": "enzyme_free",
            "surface_coating": "vitronectin"
        },
        "reprogramming_method": {
            "type": "integrating vector",
            "data": {
                "excisable": true,
                "transposon": "sleeping_beauty",
                "vector": "transposon"
            }
        },
        "cellline_karyotype": {
            "karyotype": "46XX",
            "passage_number": 30
        }
    }


The reprogramming method has a different structure depending on the `type`. Possible types are:

* `integrating vector`
* `non-integrating vector`
* `vector-free`

`data` structures depending on the type of the reprogramming methods are:

* for `integrating vector` and `transposon`:

        "data": {
            "excisable": true,
            "transposon": "sleeping_beauty",
            "vector": "transposon"
        } 

* for `integrating vector` and `virus`:

        "data": {
            "excisable": false,
            "virus": "retrovirus",
            "vector": "virus"
        }

* for `non-integrating vector`:

        "data": {
            "vector": "sendai_virus"
        }

* `vector-free` is currently not implemented and will be added in a future release.


