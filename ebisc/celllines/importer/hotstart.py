import os
import json
import functools

import logging
logger = logging.getLogger('management.commands')

from ..models import *


'''
This is HotsStart JSON data importer.
'''


# -----------------------------------------------------------------------------
# Importer

def value_of_json(source, field, cast=None):

    if cast == 'bool':

        if source.get(field, None) == '1':
            return True
        else:
            return False

    else:
        return source.get(field, None)


def inject_valuef(func):
    def wrapper(source, *args):
        args = [functools.partial(value_of_json, source), source] + list(args)
        return func(*args)
    return wrapper


@inject_valuef
def parse_disease(valuef, source):

    if not valuef('disease_flag', 'bool'):
        disease = None
    else:
        disease, created = Disease.objects.get_or_create(
            icdcode=valuef('disease_doid'),
            disease=valuef('disease_doid_name'),
        )

        if created:
            logger.info('Found new disease: %s' % disease)

    return disease


@inject_valuef
def parse_cell_type(valuef, source):

    cell_type, created = Celltype.objects.get_or_create(
        celltype=valuef('primary_celltype_ont_name'),
    )

    if created:
        logger.info('Found new cell type: %s' % cell_type)

    return cell_type


@inject_valuef
def parse_organization(valuef, source):

    # Organization

    organization, created = Organization.objects.get_or_create(
        organizationname=valuef('name')
    )
    if created:
        logger.info('Found new organization: %s' % organization)

    if valuef('role') == 'Generator':

        return (organization, 'generator')

    elif valuef('role') == 'Generator':

        return (organization, 'owner')

    else:

        # Other organization roles

        organization_role, created = Celllineorgtype.objects.get_or_create(
            celllineorgtype=valuef('role')
        )
        if created:
            logger.info('Found new organization type: %s' % organization_role)

        # Cell line organization

        return (organization, organization_role)


def import_data(basedir):

    for f in os.listdir(basedir):

        logger.info('Importing %s' % f)

        with open(os.path.join(basedir, f), 'r') as fi:

            source = json.load(fi)
            valuef = functools.partial(value_of_json, source)

            logger.info('Importing cell line %s' % valuef('name'))

            cell_line = Cellline(
                biosamplesid=valuef('biosample_id'),
                celllinename=valuef('name'),
                celllineprimarydisease=parse_disease(source),
                celllinecelltype=parse_cell_type(source),
                celllinenamesynonyms=', '.join(valuef('alternate_name')),
            )

            organizations = []

            for org in valuef('providers'):
                organization, role = parse_organization(org)

                if role == 'generator':
                    cell_line.generator = organization
                elif role == 'owner':
                    cell_line.owner = organization
                else:
                    organizations.append((organization, role))

            cell_line.save()

            for organization, organization_role in organizations:

                cell_line_organization, created = Celllineorganization.objects.get_or_create(
                    orgcellline=cell_line,
                    organization=organization,
                    celllineorgtype=organization_role,
                )
                if created:
                    logger.info('Added organization %s as %s' % (organization, organization_role))


# -----------------------------------------------------------------------------
# Example JSON

{
    "form_finished_flag": "1",
    "final_name_generated_flag": "1",
    "id": "1088",
    "validation_status": "1",
    "name": "ESi001-A",
    "biosample_id": "SAMEA3302942",
    "alternate_name": [
        "SPO2#1"
    ],
    "type_name": "hiPSC",
    "internal_donor_id": [
        "1088",
        "SP02"
    ],
    "donor_biosample_id": "SAMEA3302933",
    "available_flag": "1",
    "same_donor_cell_line_flag": "0",
    "same_donor_derived_from_flag": "0",
    "registration_reference": "S\u00e1nchez-Dan\u00e9s A et al. Disease-specific phenotypes in dopamine neurons from human iPS-based models of genetic and sporadic Parkinson's disease. EMBO Mol Med. 2012 May;4(5):380-95.",
    "registration_reference_publication_pubmed_id": "22407749",
    "informed_consent_flag": "1",
    "approval_flag": "1",
    "approval_auth_name": "Ethic Committee Center of Regenerative Medicine in Barcelona",
    "vector_type": "integrating",
    "integrating_vector": "virus",
    "integrating_vector_virus_type": "retrovirus",
    "integrating_vector_gene_list": [
        "5460###POU5F1###entrez_id###id_type_gene",
        "9314###KLF4###entrez_id###id_type_gene",
        "6657###SOX2###entrez_id###id_type_gene"
    ],
    "dev_stage_primary_cell": "adult",
    "donor_age": "55-59",
    "gender_primary_cell": "male",
    "disease_flag": "1",
    "disease_doid": "DOID:14330",
    "disease_doid_name": "Parkinson's disease",
    "disease_doid_synonyms": "paralysis agitans EXACT CSP2005:2057-3689,Parkinson disease EXACT ",
    "disease_purl": "http://www.ebi.ac.uk/efo/EFO_0002508",
    "disease_control_cellline_abnormal_karyotype": "0",
    "primary_celltype_ont_id": "CL_0000362",
    "primary_celltype_name": "Epidermal keratinocytes ",
    "primary_celltype_purl": "http://purl.obolibrary.org/obo/CL_0000362",
    "derivation_gmp_ips_flag": "0",
    "available_clinical_grade_ips_flag": "0",
    "derivation_xeno_graft_free_flag": "0",
    "surface_coating": "gelatine",
    "feeder_cells_flag": "1",
    "feeder_cells_name": "Human foreskin fibroblasts",
    "feeder_cells_ont_id": "CELDA_000001419",
    "passage_method": "mechanically",
    "co2_concentration": "5",
    "culture_conditions_medium_culture_medium": "other_medium",
    "culture_conditions_medium_culture_medium_other_base": "KnockOut DMEM",
    "culture_conditions_medium_culture_medium_other_protein_source": "knockout_serum_replacement",
    "culture_conditions_medium_culture_medium_other_concentration": "20",
    "culture_conditions_medium_culture_medium_other_supplements": [
        "Glutamax###2###millimeter",
        "2-mercaptoethanol###50###mikrometer",
        "NEAA###1###percent",
        "bFGF###10###nanogram_millilitre"
    ],
    "undiff_immstain_marker": [
        "alpl###+",
        "nanog###+",
        "pou5f1###+",
        "ssea3###+",
        "ssea4###+",
        "tra160###+",
        "tra181###+",
        "###+###Sox2###entrez_id###id_type_protein"
    ],
    "undiff_immstain_marker_passage_number": "11",
    "virology_screening_flag": "1",
    "virology_screening_mycoplasma_flag": "1",
    "virology_screening_mycoplasma_result": "negative",
    "embryoid_body_differentiation_flag": "1",
    "embryoid_body_passage_number": "13",
    "embryoid_body_endo_flag": "1",
    "embryoid_body_endo_marker_immstain_marker": [
        "###+###AFP###entrez_id###id_type_protein",
        "###+###FoxA2###entrez_id###id_type_protein"
    ],
    "embryoid_body_meso_flag": "1",
    "embryoid_body_meso_marker_immstain_marker": [
        "###+###SMA###entrez_id###id_type_protein"
    ],
    "embryoid_body_ekto_flag": "1",
    "embryoid_body_ekto_marker_immstain_marker": [
        "###+###TUJ1###entrez_id###id_type_protein"
    ],
    "teratoma_formation_differentiation_flag": "1",
    "teratoma_formation_endo_flag": "1",
    "teratoma_formation_endo_marker_immstain_marker": [
        "###+###FoxA2###entrez_id###id_type_protein",
        "###+###AFP###entrez_id###id_type_protein"
    ],
    "teratoma_formation_meso_flag": "1",
    "teratoma_formation_meso_marker_immstain_marker": [
        "###+###CS###entrez_id###id_type_protein",
        "###+###Sox9###entrez_id###id_type_protein"
    ],
    "teratoma_formation_ekto_flag": "1",
    "teratoma_formation_ekto_marker_immstain_marker": [
        "###+###Tuj1###entrez_id###id_type_protein",
        "###+###GFAP###entrez_id###id_type_protein"
    ],
    "karyotyping_flag": "1",
    "karyotyping_karyotype": "46,XY",
    "karyotyping_image_upload_file": "SP02_1_Karyotype.pdf",
    "karyotyping_image_upload_file_enc": "ad5579c4a248a497bc55b7f13e422912.pdf",
    "karyotyping_method": "g_banding",
    "derivation_country": "Spain",
    "providers": [
        {
            "id": "427",
            "name": "Spanish Stem Cell Bank",
            "contact_person_fullname": "",
            "adress": "",
            "role": "Generator"
        }
    ]
}

# -----------------------------------------------------------------------------
