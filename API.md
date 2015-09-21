# The EBiSC IMS API

## Access

The API can be accessed with an username/key pair. These have been generated for each EBiSC component currently using the API (ECACC, EBI, hPSCreg) and were sent out by email. New credentials will be generated as needed.

The username/key can be specified either in HTTP Request Header or as GET parameters.

**HTTP Request Header**

URL: `https://ebisc.douglasconnect.com/api/v0/cell-lines`
Header: `"Authorization: ApiKey USERNAME:KEY"`

**GET Params**

`https://ebisc.douglasconnect.com/api/v0/cell-lines?username=USERNAME&api_key=KEY`

## Data and endpoints

Cell line records currently hold data required for two data exchanges:

* IMS/ECACC (cell line data and documents needed for the ECACC catalogue)
* IMS/EBI (data tracking)

Additional fields and endpoints may be created for future exchanges.

### Endpoints 

1. List of all cell lines in the IMS: `https://ebisc.douglasconnect.com/api/v0/cell-lines`
2. Individual cell line records that can be accessed via their BioSamples ID: `https://ebisc.douglasconnect.com/api/v0/cell-lines/{BIOSAMPLES_ID}`
3. List of all batches in the IMS: `https://ebisc.douglasconnect.com/api/v0/batches`
4. Individual batch records that can be accessed via their BioSamples ID: `https://ebisc.douglasconnect.com/api/v0/batches/{BIOSAMPLES_ID}`


### Sample cell line JSON record structure

    {
        "alternative_names": [
            "LB-34-1",
            "iLB-MJD4-34m-r1"
        ],
        "batches": [
            {
                "batch_id": "P001",
                "biosamples_id": "SAMEG301734",
                "certificate_of_analysis": {
                    "file": "celllines/2015/09/21/25276167-dcc5-4a4c-9652-ed10eb9ed28c/UKBi008-A.P001.CoA.pdf",
                    "md5": "05c14fc167c0a946665670846f485492"
                },
                "culture_conditions": {
                    "co2_concentration": "5%",
                    "culture_medium": "mTeSTR",
                    "matrix": "Matrigel / Geltrex",
                    "o2_concentration": "21%",
                    "passage_method": "EDTA",
                    "temperature": "37C"
                },
                "images": [
                    {
                        "image_file": "/media/celllines/2015/09/21/2985c88c-f9b3-4ca3-8de6-6f038ec93e23/20141005%20UKBi008-A%20x4%2048hrs%20po_PJB78pd.jpg",
                        "image_md5": "5f9b9b0818456ffec90e8911d9405ae3",
                        "magnification": "4x",
                        "time_point": "48 hours post-passage"
                    },
                    {
                        "image_file": "/media/celllines/2015/09/21/e4b83bff-b8a7-4cdd-bd37-105672c1c269/20141005%20UKBi008-A%20x10%2048hrs%20p_kcBevWY.jpg",
                        "image_md5": "17fedc0a2e8d58c6db3f96a8e6e21791",
                        "magnification": "10x",
                        "time_point": "48 hours post-passage"
                    },
                    {
                        "image_file": "/media/celllines/2015/09/21/405f74fe-36af-46b4-b3d7-0b3ffbfef006/20141007%20UKBi-008A%20P3%20x4%20Confluence.jpg",
                        "image_md5": "87a520c2a822ab95acc32de5e803ec64",
                        "magnification": "4x",
                        "time_point": "Confluence"
                    },
                    {
                        "image_file": "/media/celllines/2015/09/21/b3b0adb2-deee-4cfa-b27f-292c98b3b86f/20141007%20UKBi-008A%20P3%20x10%20Confluence.jpg",
                        "image_md5": "f955efc0e5f37878bf1f8feca7e258fe",
                        "magnification": "10x",
                        "time_point": "Confluence"
                    }
                ],
                "resource_uri": "/api/v0/batches/SAMEG301734",
                "vials_at_roslin": 0,
                "vials_shipped_to_ecacc": 19,
                "vials_shipped_to_fraunhoffer": 5
            }
        ],
        "biosamples_id": "SAMEA2590882",
        "cellline_karyotype": {
            "karyotype": "46XX",
            "passage_number": 30
        },
        "depositor": {
            "name": "Universitatsklinikum Bonn"
        },
        "donor": {
            "biosamples_id": "SAMEA2590985",
            "gender": "male"
        },
        "donor_age": 35-39,
        "ecacc_cat_no": "66540003",
        "name": "UKBi008-A",
        "primary_cell_type": {
            "name": "Dermal Fibroblasts"
        },
        "primary_disease": {
            "doid": "DOID:1440",
            "name": "Machado-Joseph disease",
            "synonyms": [
                "Azorean disease (disorder)",
                "MJD",
                "spinocerebellar ataxia type 3"
            ]
        },
        "reprogramming_method": {
            "data": {
                "absence_reprogramming_vectors": false,
                "excisable": false,
                "vector": "virus",
                "virus": "retrovirus"
            },
            "type": "integrating vector"
        },
        "resource_uri": "/api/v0/cell-lines/SAMEA2590882"
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


### Sample Batch JSON record structure

    {
        "batch_id": "P001",
        "biosamples_id": "SAMEG301734",
        "certificate_of_analysis": {
            "file": "celllines/2015/09/21/25276167-dcc5-4a4c-9652-ed10eb9ed28c/UKBi008-A.P001.CoA.pdf",
            "md5": "05c14fc167c0a946665670846f485492"
        },
        "culture_conditions": {
            "co2_concentration": "5%",
            "culture_medium": "mTeSTR",
            "matrix": "Matrigel / Geltrex",
            "o2_concentration": "21%",
            "passage_method": "EDTA",
            "temperature": "37C"
        },
        "images": [
            {
                "image_file": "/media/celllines/2015/09/21/2985c88c-f9b3-4ca3-8de6-6f038ec93e23/20141005%20UKBi008-A%20x4%2048hrs%20po_PJB78pd.jpg",
                "image_md5": "5f9b9b0818456ffec90e8911d9405ae3",
                "magnification": "4x",
                "time_point": "48 hours post-passage"
            },
            {
                "image_file": "/media/celllines/2015/09/21/e4b83bff-b8a7-4cdd-bd37-105672c1c269/20141005%20UKBi008-A%20x10%2048hrs%20p_kcBevWY.jpg",
                "image_md5": "17fedc0a2e8d58c6db3f96a8e6e21791",
                "magnification": "10x",
                "time_point": "48 hours post-passage"
            },
            {
                "image_file": "/media/celllines/2015/09/21/405f74fe-36af-46b4-b3d7-0b3ffbfef006/20141007%20UKBi-008A%20P3%20x4%20Confluence.jpg",
                "image_md5": "87a520c2a822ab95acc32de5e803ec64",
                "magnification": "4x",
                "time_point": "Confluence"
            },
            {
                "image_file": "/media/celllines/2015/09/21/b3b0adb2-deee-4cfa-b27f-292c98b3b86f/20141007%20UKBi-008A%20P3%20x10%20Confluence.jpg",
                "image_md5": "f955efc0e5f37878bf1f8feca7e258fe",
                "magnification": "10x",
                "time_point": "Confluence"
            }
        ],
        "resource_uri": "/api/v0/batches/SAMEG301734",
        "vials_at_roslin": 0,
        "vials_shipped_to_ecacc": 19,
        "vials_shipped_to_fraunhoffer": 5
    }


