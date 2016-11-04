# The EBiSC IMS API

## Access

The API can be accessed with an username/key pair. These have been generated for each EBiSC component currently using the API (ECACC, EBI, hPSCreg, BioSamples) and were sent out by email. New credentials will be generated as needed.

The username/key can be specified either in HTTP Request Header or as GET parameters.

**HTTP Request Header**

URL: `https://cells.ebisc.org/api/v0/cell-lines`
Header: `"Authorization: ApiKey USERNAME:KEY"`

**GET Params**

`https://cells.ebisc.org/api/v0/cell-lines?username=USERNAME&api_key=KEY`

## Data and endpoints

Cell line records currently hold data required for three data exchanges:

* IMS/ECACC (cell line data and documents needed for the ECACC catalogue)
* IMS/LIMS (IMS data that will be imported into LIMS)
* IMS/EBI (data tracking)

Additional fields and endpoints may be created for future exchanges.

### Endpoints

1. List of all cell lines in the IMS: `https://cells.ebisc.org/api/v0/cell-lines`
2. Individual cell line records that can be accessed via their BioSamples ID: `https://cells.ebisc.org/api/v0/cell-lines/{BIOSAMPLES_ID}`
3. List of all batches in the IMS: `https://cells.ebisc.org/api/v0/batches`
4. Individual batch records that can be accessed via their BioSamples ID: `https://cells.ebisc.org/api/v0/batches/{BIOSAMPLES_ID}`

### Sample cell line JSON record structure

    {
        "alternative_names": [
            "LB-34-1",
            "iLB-MJD4-34m-r1"
        ],
        "availability": "Stocked by ECACC",
        "batches": [
            {
                "batch_id": "P001",
                "batch_type": "Depositor Expansion",
                "biosamples_id": "SAMEG301734",
                "certificate_of_analysis": {
                    "file": "/media/celllines/2015/09/21/25276167-dcc5-4a4c-9652-ed10eb9ed28c/UKBi008-A.P001.CoA.pdf",
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
                "vials": [
                    {
                        "biosamples_id": "SAMEA2590959",
                        "name": "LB-34-1 vial 01",
                        "number": "01"
                    },
                    {
                        "biosamples_id": "SAMEA2590987",
                        "name": "LB-34-1 vial 02",
                        "number": "02"
                    },
                    {
                        "biosamples_id": "SAMEA2591011",
                        "name": "LB-34-1 vial 03",
                        "number": "03"
                    },
                    {
                        "biosamples_id": "SAMEA2591030",
                        "name": "LB-34-1 vial 04",
                        "number": "04"
                    },
                    {
                        "biosamples_id": "SAMEA2590894",
                        "name": "LB-34-1 vial 05",
                        "number": "05"
                    },
                    {
                        "biosamples_id": "SAMEA2590889",
                        "name": "LB-34-1 vial 06",
                        "number": "06"
                    },
                    {
                        "biosamples_id": "SAMEA2590910",
                        "name": "LB-34-1 vial 07",
                        "number": "07"
                    },
                    {
                        "biosamples_id": "SAMEA2590923",
                        "name": "LB-34-1 vial 08",
                        "number": "08"
                    },
                    {
                        "biosamples_id": "SAMEA2590940",
                        "name": "LB-34-1 vial 09",
                        "number": "09"
                    },
                    {
                        "biosamples_id": "SAMEA2590878",
                        "name": "LB-34-1 vial 10",
                        "number": "10"
                    },
                    {
                        "biosamples_id": "SAMEA2590906",
                        "name": "LB-34-1 vial 11",
                        "number": "11"
                    },
                    {
                        "biosamples_id": "SAMEA2590915",
                        "name": "LB-34-1 vial 12",
                        "number": "12"
                    },
                    {
                        "biosamples_id": "SAMEA2591017",
                        "name": "LB-34-1 vial 13",
                        "number": "13"
                    },
                    {
                        "biosamples_id": "SAMEA2591031",
                        "name": "LB-34-1 vial 14",
                        "number": "14"
                    },
                    {
                        "biosamples_id": "SAMEA2590960",
                        "name": "LB-34-1 vial 15",
                        "number": "15"
                    },
                    {
                        "biosamples_id": "SAMEA2590986",
                        "name": "LB-34-1 vial 16",
                        "number": "16"
                    },
                    {
                        "biosamples_id": "SAMEA2590953",
                        "name": "LB-34-1 vial 17",
                        "number": "17"
                    },
                    {
                        "biosamples_id": "SAMEA2590942",
                        "name": "LB-34-1 vial 18",
                        "number": "18"
                    },
                    {
                        "biosamples_id": "SAMEA2590928",
                        "name": "LB-34-1 vial 19",
                        "number": "19"
                    },
                    {
                        "biosamples_id": "SAMEA2590979",
                        "name": "LB-34-1 vial 20",
                        "number": "20"
                    },
                    {
                        "biosamples_id": "SAMEA2590992",
                        "name": "LB-34-1 vial 21",
                        "number": "21"
                    },
                    {
                        "biosamples_id": "SAMEA2591012",
                        "name": "LB-34-1 vial 22",
                        "number": "22"
                    },
                    {
                        "biosamples_id": "SAMEA2591003",
                        "name": "LB-34-1 vial 23",
                        "number": "23"
                    },
                    {
                        "biosamples_id": "SAMEA2591018",
                        "name": "LB-34-1 vial 24",
                        "number": "24"
                    },
                    {
                        "biosamples_id": "SAMEA2590897",
                        "name": "LB-34-1 vial 25",
                        "number": "25"
                    },
                    {
                        "biosamples_id": "SAMEA2590907",
                        "name": "LB-34-1 vial 26",
                        "number": "26"
                    },
                    {
                        "biosamples_id": "SAMEA2590924",
                        "name": "LB-34-1 vial 27",
                        "number": "27"
                    },
                    {
                        "biosamples_id": "SAMEA2590947",
                        "name": "LB-34-1 vial 28",
                        "number": "28"
                    },
                    {
                        "biosamples_id": "SAMEA2590951",
                        "name": "LB-34-1 vial 29",
                        "number": "29"
                    },
                    {
                        "biosamples_id": "SAMEA2591028",
                        "name": "LB-34-1 vial 30",
                        "number": "30"
                    },
                    {
                        "biosamples_id": "SAMEA2591004",
                        "name": "LB-34-1 vial 31",
                        "number": "31"
                    },
                    {
                        "biosamples_id": "SAMEA2590901",
                        "name": "LB-34-1 vial 32",
                        "number": "32"
                    },
                    {
                        "biosamples_id": "SAMEA2590881",
                        "name": "LB-34-1 vial 33",
                        "number": "33"
                    },
                    {
                        "biosamples_id": "SAMEA2590898",
                        "name": "LB-34-1 vial 34",
                        "number": "34"
                    },
                    {
                        "biosamples_id": "SAMEA2590952",
                        "name": "LB-34-1 vial 35",
                        "number": "35"
                    },
                    {
                        "biosamples_id": "SAMEA2590931",
                        "name": "LB-34-1 vial 36",
                        "number": "36"
                    },
                    {
                        "biosamples_id": "SAMEA2590984",
                        "name": "LB-34-1 vial 37",
                        "number": "37"
                    },
                    {
                        "biosamples_id": "SAMEA2590963",
                        "name": "LB-34-1 vial 38",
                        "number": "38"
                    },
                    {
                        "biosamples_id": "SAMEA2591024",
                        "name": "LB-34-1 vial 39",
                        "number": "39"
                    },
                    {
                        "biosamples_id": "SAMEA2590880",
                        "name": "LB-34-1 vial 40",
                        "number": "40"
                    },
                    {
                        "biosamples_id": "SAMEA2590905",
                        "name": "LB-34-1 vial 41",
                        "number": "41"
                    },
                    {
                        "biosamples_id": "SAMEA2590935",
                        "name": "LB-34-1 vial 42",
                        "number": "42"
                    },
                    {
                        "biosamples_id": "SAMEA2590948",
                        "name": "LB-34-1 vial 43",
                        "number": "43"
                    },
                    {
                        "biosamples_id": "SAMEA2590977",
                        "name": "LB-34-1 vial 44",
                        "number": "44"
                    },
                    {
                        "biosamples_id": "SAMEA2590962",
                        "name": "LB-34-1 vial 45",
                        "number": "45"
                    },
                    {
                        "biosamples_id": "SAMEA2590989",
                        "name": "LB-34-1 vial 46",
                        "number": "46"
                    },
                    {
                        "biosamples_id": "SAMEA2591007",
                        "name": "LB-34-1 vial 47",
                        "number": "47"
                    },
                    {
                        "biosamples_id": "SAMEA2591027",
                        "name": "LB-34-1 vial 48",
                        "number": "48"
                    },
                    {
                        "biosamples_id": "SAMEA2590939",
                        "name": "LB-34-1 vial 49",
                        "number": "49"
                    },
                    {
                        "biosamples_id": "SAMEA2590893",
                        "name": "LB-34-1 vial 50",
                        "number": "50"
                    }
                ],
                "vials_at_roslin": 0,
                "vials_shipped_to_ecacc": 19,
                "vials_shipped_to_fraunhoffer": 5
            }
        ],
        "biosamples_id": "SAMEA2590882",
        "cell_line_information_packs": [
            {
                "clip_file": "/media/celllines/2015/12/27/1abeb45f-0d61-47bc-a78f-eaeeff2cb799/UKBi008-A.CLIP.v1.pdf",
                "md5": "5c49eec2c58e768de88553e085eed576",
                "updated": "2015-12-27T10:45:52.574218",
                "version": "v1"
            }
        ],
        "cellline_certificate_of_analysis": {
            "certificate_of_analysis_flag": true
        },
        "cellline_disease_associated_genotype": {
            "carries_disease_phenotype_associated_variants_flag": false,
            "variant_of_interest_flag": null
        },
        "cellline_karyotype": {
            "karyotype": "46XX",
            "passage_number": 30
        },
        "characterization_pluritest": {
            "novelty_score": "1.399",
            "pluripotency_score": "42.031",
            "pluritest_flag": true
        },
        "depositor": {
            "name": "Universitatsklinikum Bonn"
        },
        "depositor_cellline_culture_conditions": {
            "co2_concentration": 5,
            "culture_history": null,
            "culture_medium": null,
            "culture_medium_other": {
                "base": "KnockOut DMEM",
                "protein_source": "knockout_serum_replacement",
                "serum_concentration": 20
            },
            "culture_medium_supplements": [
                {
                    "amount": "50",
                    "supplement": "2-mercaptoethanol",
                    "unit": "mikrometer"
                },
                {
                    "amount": "2",
                    "supplement": "Glutamax",
                    "unit": "millimeter"
                },
                {
                    "amount": "1",
                    "supplement": "NEAA",
                    "unit": "percent"
                },
                {
                    "amount": "10",
                    "supplement": "bFGF",
                    "unit": "nanogram_millilitre"
                }
            ],
            "enzymatically": null,
            "enzyme_free": null,
            "feeder_cell_id": "CELDA_000001419",
            "feeder_cell_type": "Human foreskin fibroblasts",
            "number_of_vials_banked": "20",
            "o2_concentration": 21,
            "other_culture_environment": null,
            "passage_history": null,
            "passage_method": "mechanically",
            "passage_number_banked": "10",
            "rock_inhibitor_used_at_cryo": "Unknown",
            "rock_inhibitor_used_at_passage": "Unknown",
            "rock_inhibitor_used_at_thaw": "Unknown",
            "surface_coating": "gelatine"
        },
        "disease_associated_phenotypes": [
            "Prolonged QT interval on ECG"
        ],
        "non_disease_associated_phenotypes": [
            "Cardiac arrhythmia at exercise; normal ECG at rest"
        ]
        "donor": {
            "biosamples_id": "SAMEA2590985",
            "gender": "male",
            "internal_donor_ids": [
                "NP0014/YO90096"
            ],
            "karyotype": null
        },
        "donor_age": 35-39,
        "ecacc_cat_no": "66540003",
        "flag_go_live": true,
        "genetic_modification": {
            "genetic_modification_flag": true,
            "types": [
                "gen_mod_gene_knock_out"
            ]
        },
        "genetic_modification_gene_knock_in": null,
        "genetic_modification_gene_knock_out": {
            "delivery_method": "viral",
            "target_genes": [
                "FANCD2"
            ]
        },
        "genetic_modification_isogenic": null,
        "genetic_modification_transgene_expression": null,
        "name": "UKBi008-A",
        "primary_cell_type": {
            "name": "fibroblast of dermis"
        },
        "primary_disease": {
            "doid": "DOID:1440",
            "name": "Machado-Joseph disease",
            "purl": "http://purl.obolibrary.org/obo/DOID_1440",
            "synonyms": [
                "Azorean disease (disorder)",
                "MJD",
                "spinocerebellar ataxia type 3"
            ]
        },
        "primary_disease_diagnosed": "1",
        "publications": [
            {
                "pub": "PubMed",
                "pub_id": "22113611",
                "pub_title": "Koch P et al. Excitation-induced ataxin-3 aggregation in neurons from patients with Machado-Joseph disease. Nature. 2011 Nov 23;480(7378):543-6.",
                "pub_url": "http://www.ncbi.nlm.nih.gov/pubmed/22113611"
            }
        ],
        "reprogramming_method": {
            "data": {
                "absence_reprogramming_vectors": false,
                "excisable": false,
                "integrating_vector_gene_list": [
                    "KLF4",
                    "MYC",
                    "POU5F1",
                    "SOX2"
                ],
                "integrating_vector_methods": null,
                "integrating_vector_silenced": "unknown",
                "integrating_vector_silencing_notes": null,
                "vector": "Virus",
                "virus": "Retrovirus"
            },
            "type": "integrating vector"
        },
        "reprogramming_method_vector_free_types": [
            "vector_free_types_none"
        ],
        "resource_uri": "/api/v0/cell-lines/SAMEA2590882",
        "status_log": [
            {
                "comment": "",
                "status": "Stocked by ECACC",
                "updated": "2016-10-20T11:51:00.016090"
            }
        ],
        "validation_status": "Validated, visible",
        "virology_screening": {
            "hepatitis_b": "Negative",
            "hepatitis_c": "Negative",
            "hiv1": "Negative",
            "hiv2": null,
            "mycoplasma": "Negative",
            "virology_screening_flag": true
        }
    }


#### flag Fields

Fields that end with `_flag` can hold three values:
* `true` or `false` if information for the field is provided by depositors or central facility and marked as being true of false
* `null` if no information is available (this is the case for fields that are not mandatory)

Examples of these types of fields are: `certificate_of_analysis_flag`, `variant_of_interest_flag`, ...

#### Availability and Status log

Availability field can hold 6 possible values:
* Not available
* Stocked by ECACC
* Expand to order
* Restricted distribution
* Recalled
* Withdrawn

If availability is set to `Not available` the value of `flag_go_live` is `false`. Otherwise `flag_go_live` is `true`.

The history of status changes is logged in the field `status_log`. Each change is documented with:
* the new status,
* when the change was made and
* an accompanying comment by the person who made the change.

#### hPSCreg validation

`validation_status` field can hold four possible values:
* Validated, visible
* Validated, not visible
* Unvalidated
* Name registered, no data

#### Primary disease

Primary disease data is provided in two fields:
* `primary_disease_diagnosed` can have values `0`, `1` or `carrier`. If the value is `0`, there is no disease diagnosed and this disease status should be displayed as `normal`. If the value is `1` or `carrier` the disease has been diagnosed or the donor is a carrier.
* `primary_disease` fields cover two different cases:
  * If the value of `primary_disease_diagnosed` is `1` or `carrier`, the `primary_disease` fields hold information about the diagnosed disease.
  * If the value of `primary_disease_diagnosed` is `0`, the `primary_disease` field `name` holds the value `Normal`.

Note: Some fields in `primary_disease` will change with the implementation of ontologies.

#### Reprogramming method

The reprogramming method has a different structure depending on the `type`. Possible types are:

* `integrating vector`
* `non-integrating vector`

`data` structures depending on the type of the reprogramming methods are:

* for `integrating vector` and `transposon`:

        "data": {
            "absence_reprogramming_vectors": false,
            "excisable": true,
            "integrating_vector_gene_list": [
                "KLF4",
                "MYC",
                "POU5F1",
                "SOX2"
            ],
            "integrating_vector_methods": null,
            "integrating_vector_silenced": "unknown",
            "integrating_vector_silencing_notes": null,
            "transposon": "Sleeping beauty",
            "vector": "Transposon"
        }

* for `integrating vector` and `virus`:

        "data": {
            "absence_reprogramming_vectors": false,
            "excisable": false,
            "integrating_vector_gene_list": [
                "KLF4",
                "MYC",
                "POU5F1",
                "SOX2"
            ],
            "integrating_vector_methods": null,
            "integrating_vector_silenced": "unknown",
            "integrating_vector_silencing_notes": null,
            "vector": "Virus",
            "virus": "Retrovirus"
        }

* for `non-integrating vector`:

        "data": {
            "non_integrating_vector_detectable": "unknown",
            "non_integrating_vector_detection_notes": null,
            "non_integrating_vector_gene_list": [
                "KLF4",
                "L-Myc",
                "POU5F1",
                "SOX2",
                "sh-p53"
            ],
            "non_integrating_vector_methods": null,
            "vector": "Episomal"
        }

#### Genetic modification

Data for genetic modification is stored in 5 fields. The field `genetic_modification` holds the information if the line has been modified and what types of modification were used.
The four fields described below contain the details of the modification.

* `genetic_modification_transgene_expression`

        "genetic_modification_transgene_expression": {
              "delivery_method": null,
              "genes": []
        },

* `genetic_modification_gene_knock_in`

        "genetic_modification_gene_knock_in": {
              "delivery_method": "viral",
              "target_genes": [],
              "transgenes": []
        },

* `genetic_modification_gene_knock_out`

        "genetic_modification_gene_knock_out": {
              "delivery_method": "viral",
              "target_genes": [
                  "FANCD2"
              ]
        },

* `genetic_modification_isogenic`

        "genetic_modification_isogenic": {
              "change_type": "repaired",
              "modified_sequence": "some text",
              "target_locus": []
        },


### Sample Batch JSON record structure

        {
            "batch_id": "P001",
            "batch_type": "Depositor Expansion",
            "biosamples_id": "SAMEG301734",
            "certificate_of_analysis": {
                "file": "/media/celllines/2016/02/04/d26fe5d9-6e4c-498c-b01c-d2894f8cfe45/UKBi008-A.P001.CoA.v3.pdf",
                "md5": "7dba4abad952d3937ad7da650c14b4e1"
            },
            "culture_conditions": {
                "co2_concentration": "5%",
                "culture_medium": "mTeSR",
                "matrix": "Matrigel / Geltrex",
                "o2_concentration": "21%",
                "passage_method": "EDTA",
                "temperature": "37C"
            },
            "images": [
                {
                    "image_file": "/media/celllines/2016/03/18/e87e0c09-7fd4-4dd7-b961-3ac0ea31180b/UKBi008-A-bca3142a6f58178cf9ea_a6NRl8T.jpg",
                    "image_md5": "17fedc0a2e8d58c6db3f96a8e6e21791",
                    "magnification": "10x",
                    "time_point": "48 hours post-passage"
                },
                {
                    "image_file": "/media/celllines/2016/03/18/f22de418-fb71-40c3-88b5-84c8b9c5bd53/UKBi008-A-c4e6593e8824b1d46c0c_snsU5sL.jpg",
                    "image_md5": "87a520c2a822ab95acc32de5e803ec64",
                    "magnification": "4x",
                    "time_point": "Confluence"
                },
                {
                    "image_file": "/media/celllines/2016/03/18/853f4b45-4e1e-46c7-aafa-ae71c24227b4/UKBi008-A-153d715c9ab88521b57c_dMkRjdb.jpg",
                    "image_md5": "5f9b9b0818456ffec90e8911d9405ae3",
                    "magnification": "4x",
                    "time_point": "48 hours post-passage"
                },
                {
                    "image_file": "/media/celllines/2016/03/18/2403dbb6-fb8a-451c-ada7-535dce529635/UKBi008-A-9fd1759b08258af02a56_xkggClb.jpg",
                    "image_md5": "f955efc0e5f37878bf1f8feca7e258fe",
                    "magnification": "10x",
                    "time_point": "Confluence"
                }
            ],
            "resource_uri": "/api/v0/batches/SAMEG301734",
            "vials": [
                {
                    "biosamples_id": "SAMEA2590959",
                    "name": "LB-34-1 vial 01",
                    "number": "01"
                },
                {
                    "biosamples_id": "SAMEA2590987",
                    "name": "LB-34-1 vial 02",
                    "number": "02"
                },
                {
                    "biosamples_id": "SAMEA2591011",
                    "name": "LB-34-1 vial 03",
                    "number": "03"
                },
                {
                    "biosamples_id": "SAMEA2591030",
                    "name": "LB-34-1 vial 04",
                    "number": "04"
                },
                {
                    "biosamples_id": "SAMEA2590894",
                    "name": "LB-34-1 vial 05",
                    "number": "05"
                },
                {
                    "biosamples_id": "SAMEA2590889",
                    "name": "LB-34-1 vial 06",
                    "number": "06"
                },
                {
                    "biosamples_id": "SAMEA2590910",
                    "name": "LB-34-1 vial 07",
                    "number": "07"
                },
                {
                    "biosamples_id": "SAMEA2590923",
                    "name": "LB-34-1 vial 08",
                    "number": "08"
                },
                {
                    "biosamples_id": "SAMEA2590940",
                    "name": "LB-34-1 vial 09",
                    "number": "09"
                },
                {
                    "biosamples_id": "SAMEA2590878",
                    "name": "LB-34-1 vial 10",
                    "number": "10"
                },
                {
                    "biosamples_id": "SAMEA2590906",
                    "name": "LB-34-1 vial 11",
                    "number": "11"
                },
                {
                    "biosamples_id": "SAMEA2590915",
                    "name": "LB-34-1 vial 12",
                    "number": "12"
                },
                {
                    "biosamples_id": "SAMEA2591017",
                    "name": "LB-34-1 vial 13",
                    "number": "13"
                },
                {
                    "biosamples_id": "SAMEA2591031",
                    "name": "LB-34-1 vial 14",
                    "number": "14"
                },
                {
                    "biosamples_id": "SAMEA2590960",
                    "name": "LB-34-1 vial 15",
                    "number": "15"
                },
                {
                    "biosamples_id": "SAMEA2590986",
                    "name": "LB-34-1 vial 16",
                    "number": "16"
                },
                {
                    "biosamples_id": "SAMEA2590953",
                    "name": "LB-34-1 vial 17",
                    "number": "17"
                },
                {
                    "biosamples_id": "SAMEA2590942",
                    "name": "LB-34-1 vial 18",
                    "number": "18"
                },
                {
                    "biosamples_id": "SAMEA2590928",
                    "name": "LB-34-1 vial 19",
                    "number": "19"
                },
                {
                    "biosamples_id": "SAMEA2590979",
                    "name": "LB-34-1 vial 20",
                    "number": "20"
                },
                {
                    "biosamples_id": "SAMEA2590992",
                    "name": "LB-34-1 vial 21",
                    "number": "21"
                },
                {
                    "biosamples_id": "SAMEA2591012",
                    "name": "LB-34-1 vial 22",
                    "number": "22"
                },
                {
                    "biosamples_id": "SAMEA2591003",
                    "name": "LB-34-1 vial 23",
                    "number": "23"
                },
                {
                    "biosamples_id": "SAMEA2591018",
                    "name": "LB-34-1 vial 24",
                    "number": "24"
                },
                {
                    "biosamples_id": "SAMEA2590897",
                    "name": "LB-34-1 vial 25",
                    "number": "25"
                },
                {
                    "biosamples_id": "SAMEA2590907",
                    "name": "LB-34-1 vial 26",
                    "number": "26"
                },
                {
                    "biosamples_id": "SAMEA2590924",
                    "name": "LB-34-1 vial 27",
                    "number": "27"
                },
                {
                    "biosamples_id": "SAMEA2590947",
                    "name": "LB-34-1 vial 28",
                    "number": "28"
                },
                {
                    "biosamples_id": "SAMEA2590951",
                    "name": "LB-34-1 vial 29",
                    "number": "29"
                },
                {
                    "biosamples_id": "SAMEA2591028",
                    "name": "LB-34-1 vial 30",
                    "number": "30"
                },
                {
                    "biosamples_id": "SAMEA2591004",
                    "name": "LB-34-1 vial 31",
                    "number": "31"
                },
                {
                    "biosamples_id": "SAMEA2590901",
                    "name": "LB-34-1 vial 32",
                    "number": "32"
                },
                {
                    "biosamples_id": "SAMEA2590881",
                    "name": "LB-34-1 vial 33",
                    "number": "33"
                },
                {
                    "biosamples_id": "SAMEA2590898",
                    "name": "LB-34-1 vial 34",
                    "number": "34"
                },
                {
                    "biosamples_id": "SAMEA2590952",
                    "name": "LB-34-1 vial 35",
                    "number": "35"
                },
                {
                    "biosamples_id": "SAMEA2590931",
                    "name": "LB-34-1 vial 36",
                    "number": "36"
                },
                {
                    "biosamples_id": "SAMEA2590984",
                    "name": "LB-34-1 vial 37",
                    "number": "37"
                },
                {
                    "biosamples_id": "SAMEA2590963",
                    "name": "LB-34-1 vial 38",
                    "number": "38"
                },
                {
                    "biosamples_id": "SAMEA2591024",
                    "name": "LB-34-1 vial 39",
                    "number": "39"
                },
                {
                    "biosamples_id": "SAMEA2590880",
                    "name": "LB-34-1 vial 40",
                    "number": "40"
                },
                {
                    "biosamples_id": "SAMEA2590905",
                    "name": "LB-34-1 vial 41",
                    "number": "41"
                },
                {
                    "biosamples_id": "SAMEA2590935",
                    "name": "LB-34-1 vial 42",
                    "number": "42"
                },
                {
                    "biosamples_id": "SAMEA2590948",
                    "name": "LB-34-1 vial 43",
                    "number": "43"
                },
                {
                    "biosamples_id": "SAMEA2590977",
                    "name": "LB-34-1 vial 44",
                    "number": "44"
                },
                {
                    "biosamples_id": "SAMEA2590962",
                    "name": "LB-34-1 vial 45",
                    "number": "45"
                },
                {
                    "biosamples_id": "SAMEA2590989",
                    "name": "LB-34-1 vial 46",
                    "number": "46"
                },
                {
                    "biosamples_id": "SAMEA2591007",
                    "name": "LB-34-1 vial 47",
                    "number": "47"
                },
                {
                    "biosamples_id": "SAMEA2591027",
                    "name": "LB-34-1 vial 48",
                    "number": "48"
                },
                {
                    "biosamples_id": "SAMEA2590939",
                    "name": "LB-34-1 vial 49",
                    "number": "49"
                },
                {
                    "biosamples_id": "SAMEA2590893",
                    "name": "LB-34-1 vial 50",
                    "number": "50"
                }
            ],
            "vials_at_roslin": 0,
            "vials_shipped_to_ecacc": 19,
            "vials_shipped_to_fraunhoffer": 5
        }


#### Batch types

`batch_type` field can hold one of three possible values:
* Depositor Expansion
* Central Facility Expansion
* Unknown
