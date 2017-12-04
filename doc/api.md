# The EBiSC IMS API

## Access

The API can be accessed with an username/key pair. These have been generated for each EBiSC component currently using the API (ECACC, EBI, hPSCreg, BioSamples) and were sent out by email. New credentials can be created in the [Django Admin interface](https://cells.ebisc.org/admin/).

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
                        "name": "LB-34-1 P001 vial 0001",
                        "number": "0001"
                    },
                    {
                        "biosamples_id": "SAMEA2590987",
                        "name": "LB-34-1 P001 vial 0002",
                        "number": "0002"
                    },
                    {
                        "biosamples_id": "SAMEA2591011",
                        "name": "LB-34-1 P001 vial 0003",
                        "number": "0003"
                    },
                    {
                        "biosamples_id": "SAMEA2591030",
                        "name": "LB-34-1 P001 vial 0004",
                        "number": "0004"
                    },
                    {
                        "biosamples_id": "SAMEA2590894",
                        "name": "LB-34-1 P001 vial 0005",
                        "number": "0005"
                    },
                    {
                        "biosamples_id": "SAMEA2590889",
                        "name": "LB-34-1 P001 vial 0006",
                        "number": "0006"
                    },
                    {
                        "biosamples_id": "SAMEA2590910",
                        "name": "LB-34-1 P001 vial 0007",
                        "number": "0007"
                    },
                    {
                        "biosamples_id": "SAMEA2590923",
                        "name": "LB-34-1 P001 vial 0008",
                        "number": "0008"
                    },
                    {
                        "biosamples_id": "SAMEA2590940",
                        "name": "LB-34-1 P001 vial 0009",
                        "number": "0009"
                    },
                    {
                        "biosamples_id": "SAMEA2590878",
                        "name": "LB-34-1 P001 vial 0010",
                        "number": "0010"
                    },
                    {
                        "biosamples_id": "SAMEA2590906",
                        "name": "LB-34-1 P001 vial 0011",
                        "number": "0011"
                    },
                    {
                        "biosamples_id": "SAMEA2590915",
                        "name": "LB-34-1 P001 vial 0012",
                        "number": "0012"
                    },
                    {
                        "biosamples_id": "SAMEA2591017",
                        "name": "LB-34-1 P001 vial 0013",
                        "number": "0013"
                    },
                    {
                        "biosamples_id": "SAMEA2591031",
                        "name": "LB-34-1 P001 vial 0014",
                        "number": "0014"
                    },
                    {
                        "biosamples_id": "SAMEA2590960",
                        "name": "LB-34-1 P001 vial 0015",
                        "number": "0015"
                    },
                    {
                        "biosamples_id": "SAMEA2590986",
                        "name": "LB-34-1 P001 vial 0016",
                        "number": "0016"
                    },
                    {
                        "biosamples_id": "SAMEA2590953",
                        "name": "LB-34-1 P001 vial 0017",
                        "number": "0017"
                    },
                    {
                        "biosamples_id": "SAMEA2590942",
                        "name": "LB-34-1 P001 vial 0018",
                        "number": "0018"
                    },
                    {
                        "biosamples_id": "SAMEA2590928",
                        "name": "LB-34-1 P001 vial 0019",
                        "number": "0019"
                    },
                    {
                        "biosamples_id": "SAMEA2590979",
                        "name": "LB-34-1 P001 vial 0020",
                        "number": "0020"
                    },
                    {
                        "biosamples_id": "SAMEA2590992",
                        "name": "LB-34-1 P001 vial 0021",
                        "number": "0021"
                    },
                    {
                        "biosamples_id": "SAMEA2591012",
                        "name": "LB-34-1 P001 vial 0022",
                        "number": "0022"
                    },
                    {
                        "biosamples_id": "SAMEA2591003",
                        "name": "LB-34-1 P001 vial 0023",
                        "number": "0023"
                    },
                    {
                        "biosamples_id": "SAMEA2591018",
                        "name": "LB-34-1 P001 vial 0024",
                        "number": "0024"
                    },
                    {
                        "biosamples_id": "SAMEA2590897",
                        "name": "LB-34-1 P001 vial 0025",
                        "number": "0025"
                    },
                    {
                        "biosamples_id": "SAMEA2590907",
                        "name": "LB-34-1 P001 vial 0026",
                        "number": "0026"
                    },
                    {
                        "biosamples_id": "SAMEA2590924",
                        "name": "LB-34-1 P001 vial 0027",
                        "number": "0027"
                    },
                    {
                        "biosamples_id": "SAMEA2590947",
                        "name": "LB-34-1 P001 vial 0028",
                        "number": "0028"
                    },
                    {
                        "biosamples_id": "SAMEA2590951",
                        "name": "LB-34-1 P001 vial 0029",
                        "number": "0029"
                    },
                    {
                        "biosamples_id": "SAMEA2591028",
                        "name": "LB-34-1 P001 vial 0030",
                        "number": "0030"
                    },
                    {
                        "biosamples_id": "SAMEA2591004",
                        "name": "LB-34-1 P001 vial 0031",
                        "number": "0031"
                    },
                    {
                        "biosamples_id": "SAMEA2590901",
                        "name": "LB-34-1 P001 vial 0032",
                        "number": "0032"
                    },
                    {
                        "biosamples_id": "SAMEA2590881",
                        "name": "LB-34-1 P001 vial 0033",
                        "number": "0033"
                    },
                    {
                        "biosamples_id": "SAMEA2590898",
                        "name": "LB-34-1 P001 vial 0034",
                        "number": "0034"
                    },
                    {
                        "biosamples_id": "SAMEA2590952",
                        "name": "LB-34-1 P001 vial 0035",
                        "number": "0035"
                    },
                    {
                        "biosamples_id": "SAMEA2590931",
                        "name": "LB-34-1 P001 vial 0036",
                        "number": "0036"
                    },
                    {
                        "biosamples_id": "SAMEA2590984",
                        "name": "LB-34-1 P001 vial 0037",
                        "number": "0037"
                    },
                    {
                        "biosamples_id": "SAMEA2590963",
                        "name": "LB-34-1 P001 vial 0038",
                        "number": "0038"
                    },
                    {
                        "biosamples_id": "SAMEA2591024",
                        "name": "LB-34-1 P001 vial 0039",
                        "number": "0039"
                    },
                    {
                        "biosamples_id": "SAMEA2590880",
                        "name": "LB-34-1 P001 vial 0040",
                        "number": "0040"
                    },
                    {
                        "biosamples_id": "SAMEA2590905",
                        "name": "LB-34-1 P001 vial 0041",
                        "number": "0041"
                    },
                    {
                        "biosamples_id": "SAMEA2590935",
                        "name": "LB-34-1 P001 vial 0042",
                        "number": "0042"
                    },
                    {
                        "biosamples_id": "SAMEA2590948",
                        "name": "LB-34-1 P001 vial 0043",
                        "number": "0043"
                    },
                    {
                        "biosamples_id": "SAMEA2590977",
                        "name": "LB-34-1 P001 vial 0044",
                        "number": "0044"
                    },
                    {
                        "biosamples_id": "SAMEA2590962",
                        "name": "LB-34-1 P001 vial 0045",
                        "number": "0045"
                    },
                    {
                        "biosamples_id": "SAMEA2590989",
                        "name": "LB-34-1 P001 vial 0046",
                        "number": "0046"
                    },
                    {
                        "biosamples_id": "SAMEA2591007",
                        "name": "LB-34-1 P001 vial 0047",
                        "number": "0047"
                    },
                    {
                        "biosamples_id": "SAMEA2591027",
                        "name": "LB-34-1 P001 vial 0048",
                        "number": "0048"
                    },
                    {
                        "biosamples_id": "SAMEA2590939",
                        "name": "LB-34-1 P001 vial 0049",
                        "number": "0049"
                    },
                    {
                        "biosamples_id": "SAMEA2590893",
                        "name": "LB-34-1 P001 vial 0050",
                        "number": "0050"
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
        ],
        "diseases": [
        {
            "affected_status": "True",
            "carrier": null,
            "disease_stage": null,
            "free_text_name": null,
            "name": "Parkinson's disease",
            "notes": null,
            "primary_disease": false,
            "purl": "http://www.ebi.ac.uk/efo/EFO_0002508",
            "synonyms": [
                "Parkinson's syndrome",
                "Parkinsons",
                "Primary Parkinsonism",
                "Parkinsons disease",
                "Parkinson disease",
                "Parkinson's disease (disorder)",
                "Parkinson's disease NOS",
                "Parkinson Disease"
            ]
        }
        ],
        "donor": {
            "biosamples_id": "SAMEA2590985",
            "country_of_origin": null,
            "diseases": [
                  {
                  "affected_status": null,
                  "carrier": null,
                  "disease_stage": null,
                  "free_text_name": null,
                  "name": "unipolar depression",
                  "notes": null,
                  "primary_disease": false,
                  "purl": "http://www.ebi.ac.uk/efo/EFO_0003761",
                  "synonyms": [
                      "Melancholia",
                      "Neuroses",
                      "Depressive",
                      "Emotional Depression",
                      "Depressive Disorders",
                      "Major",
                      "MAJOR DEPRESSIVE DIS",
                      "Neurosis",
                      "Depressive"
                  ]
                  },
                  {
                  "affected_status": null,
                  "carrier": null,
                  "disease_stage": null,
                  "free_text_name": null,
                  "name": "anti-social behavior",
                  "notes": null,
                  "primary_disease": false,
                  "purl": "http://www.ebi.ac.uk/efo/EFO_0004890",
                  "synonyms": [
                  ""
                  ]
            }
            ],
            "ethnicity": null,
            "gender": "male",
            "internal_donor_ids": [
                "G1882",
                "RCFB53",
                "G1870",
                "RCFB44"
            ],
            "karyotype": null
        },
        "donor_age": 35-39,
        "ecacc_cat_no": "66540003",
        "flag_go_live": true,
        "genetic_modification_flag": true,
        "genetic_modifications_non_disease": [
          {
            "chromosome_location": "19q13.32",
            "clinvar_id": null,
            "dbsnp_id": null,
            "dbvar_id": null,
            "gene": "ApoE",
            "notes": "ApoE3/E3 isogenic mutant of BIONi010-C (ApoE3/E4)",
            "nucleotide_sequence_hgvs": "NM_001302691: rs429358 (C/C), rs7412 (T/T)",
            "protein_sequence_hgvs": "NP_001289620.1 (ApoE3/E3)",
            "publication_pmid": null,
            "type": "Variant",
            "zygosity_status": "Heterozygous"
          }
        ],
        "name": "UKBi008-A",
        "primary_cell_type": {
            "name": "fibroblast of dermis"
        },
        "primary_disease": {
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


### flag Fields

Fields that end with `_flag` can hold three values:
* `true` or `false` if information for the field is provided by depositors or central facility and marked as being true of false
* `null` if no information is available (this is the case for fields that are not mandatory)

Examples of these types of fields are: `certificate_of_analysis_flag`, `variant_of_interest_flag`, ...

### Availability and Status log

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

### hPSCreg validation

`validation_status` field can hold four possible values:
* Validated, visible
* Validated, not visible
* Unvalidated
* Name registered, no data

### Diseases

Disease information is provided in two places:
* In the `donor` field under `diseases`
* On the top level field under `diseases`

In both cases the field `diseases` holds a list of diseases. The diseases under top level field `diseases` hold data for genetically modified lines if the modifications are associated to a disease. Each disease has information about variants/modifications. There are five different types of Variants/modifications, for each specific fields are exported (see examples below).

To insure backward compatibility two disease related fields will still remain in the export until needed:
* `primary_disease_diagnosed` can have values `0`, `1`. If the value is `0`, there is no disease diagnosed and this disease status should be displayed as `normal`. If the value is `1` the disease has been diagnosed.
* `primary_disease` field: holds data on primary disease if one is specified. If not, the first disease is taken from a combined (donor and cell line) list of diseases.

#### Donor disease test sample

      "donor": {
        "biosamples_id": "SAMEA3105780",
        "diseases": [
          {
            "affected_status": null,
            "carrier": null,
            "disease_stage": null,
            "free_text_name": null,
            "name": "normal",
            "notes": null,
            "primary_disease": false,
            "purl": "http://purl.obolibrary.org/obo/PATO_0000461",
            "synonyms": [
              "Normalities",
              "Health",
              "Normalcy",
              "Normality"
            ],
            "variants": [
              {
                "chromosome_location": "cytoband location: 3p21",
                "clinvar_id": "3455634563456",
                "dbsnp_id": "3456354737",
                "dbvar_id": "35675673567",
                "gene": "psd",
                "notes": "Detailed free text explanation ...",
                "nucleotide_sequence_hgvs": "NM_005228.3:c.2312_2314delinsGCGTGGACAACG",
                "protein_sequence_hgvs": "NP_005219.2:p.(Val689_Glu690delinsGlyValAspAsn)",
                "publication_pmid": "26132555",
                "zygosity_status": "Homozygous"
              }
            ]
            }
        ],
      },

#### Cell line disease test sample (with all five types of possible modifications listed in the field `variants`):

      "diseases": [
        {
          "affected_status": null,
          "carrier": null,
          "disease_stage": null,
          "free_text_name": null,
          "name": "Alzheimers disease",
          "notes": null,
          "primary_disease": false,
          "purl": "http://www.ebi.ac.uk/efo/EFO_0000249",
          "synonyms": [
            "Disease",
            "Alzheimer",
            "Alzheimer Senile Dementia",
            "Dementia in Alzheimer's disease",
            "unspecified (disorder)",
            "Presenile Alzheimer Dementia"
          ],
          "variants": [
            {
              "chromosome_location": "19q13.32",
              "clinvar_id": null,
              "dbsnp_id": null,
              "dbvar_id": null,
              "gene": "ApoE",
              "notes": "ApoE3/E3 isogenic mutant of BIONi010-C (ApoE3/E4)",
              "nucleotide_sequence_hgvs": "NM_001302691: rs429358 (C/C), rs7412 (T/T)",
              "protein_sequence_hgvs": "NP_001289620.1 (ApoE3/E3)",
              "publication_pmid": null,
              "type": "Variant",
              "zygosity_status": "Heterozygous"
            },
            {
              "chromosome_location": null,
              "delivery_method": null,
              "gene": "psd",
              "notes": "Supporting evidence",
              "transposon": null,
              "type": "Transgene expression",
              "virus": null
            },
            {
              "chromosome_location": null,
              "delivery_method": "Viral",
              "gene": "plm",
              "notes": null,
              "transposon": null,
              "type": "Gene knock-out",
              "virus": "Retrovirus"
            },
            {
              "chromosome_location": null,
              "gene": "plm",
              "modification_type": null,
              "notes": null,
              "nucleotide_sequence_hgvs": null,
              "protein_sequence_hgvs": null,
              "type": "Isogenic modification",
              "zygosity_status": null
            },
            {
              "chromosome_location": null,
              "chromosome_location_transgene": "ddd",
              "delivery_method": "TALEN",
              "notes": "Supporting evidence ...",
              "target_gene": "plm",
              "transgene": "psd",
              "transposon": null,
              "type": "Gene knock-in",
              "virus": null
            }
          ]
        }
      ]

#### Genetic modifications not related to diseases test sample (with all five types of possible modifications listed):

Data for genetic modifications that are not related to a disease are exported in the field `genetic_modifications_non_disease` as a list. There are five different types of modifications, for each specific fields are exported (same as for cell line diseases).

      "genetic_modifications_non_disease": [
        {
          "chromosome_location": "19q13.32",
          "clinvar_id": null,
          "dbsnp_id": null,
          "dbvar_id": null,
          "gene": "ApoE",
          "notes": "ApoE3/E3 isogenic mutant of BIONi010-C (ApoE3/E4)",
          "nucleotide_sequence_hgvs": "NM_001302691: rs429358 (C/C), rs7412 (T/T)",
          "protein_sequence_hgvs": "NP_001289620.1 (ApoE3/E3)",
          "publication_pmid": null,
          "type": "Variant",
          "zygosity_status": "Heterozygous"
        },
        {
          "chromosome_location": null,
          "delivery_method": null,
          "gene": "psd",
          "notes": "Supporting evidence",
          "transposon": null,
          "type": "Transgene expression",
          "virus": null
        },
        {
          "chromosome_location": null,
          "delivery_method": "Viral",
          "gene": "plm",
          "notes": null,
          "transposon": null,
          "type": "Gene knock-out",
          "virus": "Retrovirus"
        },
        {
          "chromosome_location": null,
          "gene": "plm",
          "modification_type": null,
          "notes": null,
          "nucleotide_sequence_hgvs": null,
          "protein_sequence_hgvs": null,
          "type": "Isogenic modification",
          "zygosity_status": null
        },
        {
          "chromosome_location": null,
          "chromosome_location_transgene": "ddd",
          "delivery_method": "TALEN",
          "notes": "Supporting evidence ...",
          "target_gene": "plm",
          "transgene": "psd",
          "transposon": null,
          "type": "Gene knock-in",
          "virus": null
        }
      ]

### Reprogramming method

Reprogramming method field has a different structure depending on the `type`. Possible types are:

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

### Genetic modification (Old fields, will be removed)

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
                    "name": "LB-34-1 P001 vial 0001",
                    "number": "0001"
                },
                {
                    "biosamples_id": "SAMEA2590987",
                    "name": "LB-34-1 P001 vial 0002",
                    "number": "0002"
                },
                {
                    "biosamples_id": "SAMEA2591011",
                    "name": "LB-34-1 P001 vial 0003",
                    "number": "0003"
                },
                {
                    "biosamples_id": "SAMEA2591030",
                    "name": "LB-34-1 P001 vial 0004",
                    "number": "0004"
                },
                {
                    "biosamples_id": "SAMEA2590894",
                    "name": "LB-34-1 P001 vial 0005",
                    "number": "0005"
                },
                {
                    "biosamples_id": "SAMEA2590889",
                    "name": "LB-34-1 P001 vial 0006",
                    "number": "0006"
                },
                {
                    "biosamples_id": "SAMEA2590910",
                    "name": "LB-34-1 P001 vial 0007",
                    "number": "0007"
                },
                {
                    "biosamples_id": "SAMEA2590923",
                    "name": "LB-34-1 P001 vial 0008",
                    "number": "0008"
                },
                {
                    "biosamples_id": "SAMEA2590940",
                    "name": "LB-34-1 P001 vial 0009",
                    "number": "0009"
                },
                {
                    "biosamples_id": "SAMEA2590878",
                    "name": "LB-34-1 P001 vial 0010",
                    "number": "0010"
                },
                {
                    "biosamples_id": "SAMEA2590906",
                    "name": "LB-34-1 P001 vial 0011",
                    "number": "0011"
                },
                {
                    "biosamples_id": "SAMEA2590915",
                    "name": "LB-34-1 P001 vial 0012",
                    "number": "0012"
                },
                {
                    "biosamples_id": "SAMEA2591017",
                    "name": "LB-34-1 P001 vial 0013",
                    "number": "0013"
                },
                {
                    "biosamples_id": "SAMEA2591031",
                    "name": "LB-34-1 P001 vial 0014",
                    "number": "0014"
                },
                {
                    "biosamples_id": "SAMEA2590960",
                    "name": "LB-34-1 P001 vial 0015",
                    "number": "0015"
                },
                {
                    "biosamples_id": "SAMEA2590986",
                    "name": "LB-34-1 P001 vial 0016",
                    "number": "0016"
                },
                {
                    "biosamples_id": "SAMEA2590953",
                    "name": "LB-34-1 P001 vial 0017",
                    "number": "0017"
                },
                {
                    "biosamples_id": "SAMEA2590942",
                    "name": "LB-34-1 P001 vial 0018",
                    "number": "0018"
                },
                {
                    "biosamples_id": "SAMEA2590928",
                    "name": "LB-34-1 P001 vial 0019",
                    "number": "0019"
                },
                {
                    "biosamples_id": "SAMEA2590979",
                    "name": "LB-34-1 P001 vial 0020",
                    "number": "0020"
                },
                {
                    "biosamples_id": "SAMEA2590992",
                    "name": "LB-34-1 P001 vial 0021",
                    "number": "0021"
                },
                {
                    "biosamples_id": "SAMEA2591012",
                    "name": "LB-34-1 P001 vial 0022",
                    "number": "0022"
                },
                {
                    "biosamples_id": "SAMEA2591003",
                    "name": "LB-34-1 P001 vial 0023",
                    "number": "0023"
                },
                {
                    "biosamples_id": "SAMEA2591018",
                    "name": "LB-34-1 P001 vial 0024",
                    "number": "0024"
                },
                {
                    "biosamples_id": "SAMEA2590897",
                    "name": "LB-34-1 P001 vial 0025",
                    "number": "0025"
                },
                {
                    "biosamples_id": "SAMEA2590907",
                    "name": "LB-34-1 P001 vial 0026",
                    "number": "0026"
                },
                {
                    "biosamples_id": "SAMEA2590924",
                    "name": "LB-34-1 P001 vial 0027",
                    "number": "0027"
                },
                {
                    "biosamples_id": "SAMEA2590947",
                    "name": "LB-34-1 P001 vial 0028",
                    "number": "0028"
                },
                {
                    "biosamples_id": "SAMEA2590951",
                    "name": "LB-34-1 P001 vial 0029",
                    "number": "0029"
                },
                {
                    "biosamples_id": "SAMEA2591028",
                    "name": "LB-34-1 P001 vial 0030",
                    "number": "0030"
                },
                {
                    "biosamples_id": "SAMEA2591004",
                    "name": "LB-34-1 P001 vial 0031",
                    "number": "0031"
                },
                {
                    "biosamples_id": "SAMEA2590901",
                    "name": "LB-34-1 P001 vial 0032",
                    "number": "0032"
                },
                {
                    "biosamples_id": "SAMEA2590881",
                    "name": "LB-34-1 P001 vial 0033",
                    "number": "0033"
                },
                {
                    "biosamples_id": "SAMEA2590898",
                    "name": "LB-34-1 P001 vial 0034",
                    "number": "0034"
                },
                {
                    "biosamples_id": "SAMEA2590952",
                    "name": "LB-34-1 P001 vial 0035",
                    "number": "0035"
                },
                {
                    "biosamples_id": "SAMEA2590931",
                    "name": "LB-34-1 P001 vial 0036",
                    "number": "0036"
                },
                {
                    "biosamples_id": "SAMEA2590984",
                    "name": "LB-34-1 P001 vial 0037",
                    "number": "0037"
                },
                {
                    "biosamples_id": "SAMEA2590963",
                    "name": "LB-34-1 P001 vial 0038",
                    "number": "0038"
                },
                {
                    "biosamples_id": "SAMEA2591024",
                    "name": "LB-34-1 P001 vial 0039",
                    "number": "0039"
                },
                {
                    "biosamples_id": "SAMEA2590880",
                    "name": "LB-34-1 P001 vial 0040",
                    "number": "0040"
                },
                {
                    "biosamples_id": "SAMEA2590905",
                    "name": "LB-34-1 P001 vial 0041",
                    "number": "0041"
                },
                {
                    "biosamples_id": "SAMEA2590935",
                    "name": "LB-34-1 P001 vial 0042",
                    "number": "0042"
                },
                {
                    "biosamples_id": "SAMEA2590948",
                    "name": "LB-34-1 P001 vial 0043",
                    "number": "0043"
                },
                {
                    "biosamples_id": "SAMEA2590977",
                    "name": "LB-34-1 P001 vial 0044",
                    "number": "0044"
                },
                {
                    "biosamples_id": "SAMEA2590962",
                    "name": "LB-34-1 P001 vial 0045",
                    "number": "0045"
                },
                {
                    "biosamples_id": "SAMEA2590989",
                    "name": "LB-34-1 P001 vial 0046",
                    "number": "0046"
                },
                {
                    "biosamples_id": "SAMEA2591007",
                    "name": "LB-34-1 P001 vial 0047",
                    "number": "0047"
                },
                {
                    "biosamples_id": "SAMEA2591027",
                    "name": "LB-34-1 P001 vial 0048",
                    "number": "0048"
                },
                {
                    "biosamples_id": "SAMEA2590939",
                    "name": "LB-34-1 P001 vial 0049",
                    "number": "0049"
                },
                {
                    "biosamples_id": "SAMEA2590893",
                    "name": "LB-34-1 P001 vial 0050",
                    "number": "0050"
                }
            ],
            "vials_at_roslin": 0,
            "vials_shipped_to_ecacc": 19,
            "vials_shipped_to_fraunhoffer": 5
        }


####Batch types

`batch_type` field can hold one of three possible values:

* Depositor Expansion
* Central Facility Expansion
* Unknown
