'''
hPSCreg JSON data API importer.
'''

import re
import functools
import requests

from django.conf import settings

import logging
logger = logging.getLogger('management.commands')

from ebisc.celllines.models import Cellline, Country

from . import parser


# -----------------------------------------------------------------------------
#  Run

def run():

    cellline_ids = request_get(settings.HPSCREG['list_url'])

    if cellline_ids is None:
        return

    # Tests
    # json = request_get('http://test.hescreg.eu/api/export/2')
    # import_cellline(json)

    # for cellline_id in [id for id in cellline_ids if id != 'BCRTi005-A']:
    for cellline_id in [id for id in cellline_ids]:
        if cellline_id == 'BCRTi005-A' or cellline_id == 'BCRTi004-A':
            pass
        else:
            logger.info('Importing data for cell line %s' % cellline_id)
            json = request_get(settings.HPSCREG['cellline_url'] + cellline_id)

            if json is None:
                continue
            elif type(json) is unicode:
                # hPSCreg returns 200 and error message instead of 404 NOT_FOUND
                logger.warn('Invalid cellline data: %s' % json)
            else:
                import_cellline(json)


# -----------------------------------------------------------------------------
# Import cell line

def import_cellline(source):

    valuef = functools.partial(parser.value_of_json, source)

    (generator, owner, organizations) = get_providers(valuef('providers'))

    if valuef('biosamples_id') is None:
        logger.warn('Missing biosamples id for %s' % valuef('name'))
        return

    cell_line, cell_line_created = Cellline.objects.get_or_create(
        biosamples_id=valuef('biosamples_id'),
        defaults={
            'name': valuef('name'),
            'generator': generator,
        })

    if cell_line_created:
        logger.info('Found new cell line %s' % valuef('name'))

    cell_line.validated = valuef('validation_status')
    cell_line.hescreg_id = valuef('id')
    cell_line.name = valuef('name')
    cell_line.alternative_names = ', '.join(valuef('alternate_name')) if valuef('alternate_name') is not None else ''
    cell_line.donor = parser.parse_donor(source)
    cell_line.donor_age = valuef('donor_age', 'age_range')
    cell_line.generator = generator
    cell_line.owner = owner
    cell_line.derivation_country = parser.term_list_value_of_json(source, 'derivation_country', Country)
    cell_line.primary_disease_diagnosis = valuef('disease_flag')
    cell_line.primary_disease = parser.parse_disease(source)
    cell_line.primary_disease_not_normalised = valuef('disease_other')
    cell_line.primary_disease_stage = valuef('disease_stage')
    cell_line.disease_associated_phenotypes = valuef('disease_associated_phenotypes')
    cell_line.affected_status = valuef('disease_affected_flag')
    cell_line.family_history = valuef('family_history')
    cell_line.medical_history = valuef('medical_history')
    cell_line.clinical_information = valuef('clinical_information')

    dirty = [cell_line.is_dirty(check_relationship=True)]

    # # Organizations
    #
    # for organization, organization_role in organizations:
    #
    #     cell_line_organization, created = CelllineOrganization.objects.get_or_create(
    #         cell_line=cell_line,
    #         organization=organization,
    #         cell_line_org_type=organization_role,
    #     )
    #     if created:
    #         logger.info('Added organization %s as %s' % (organization, organization_role))
    #

    # Vector

    if valuef('vector_type') == 'Integrating':
        dirty += [parser.parse_integrating_vector(source, cell_line)]

    if valuef('vector_type') == 'Non-integrating':
        dirty += [parser.parse_non_integrating_vector(source, cell_line)]

    # if valuef('vector_free_types'):
    #     dirty += [parser.parse_vector_free_factors(source, cell_line)]

    dirty += [
        parser.parse_ethics(source, cell_line),
        parser.parse_derivation(source, cell_line),
        parser.parse_culture_conditions(source, cell_line),
        parser.parse_karyotyping(source, cell_line),
        parser.parse_hla_typing(source, cell_line),
        parser.parse_str_fingerprinting(source, cell_line),
        parser.parse_genome_analysis(source, cell_line),
        parser.parse_publications(source, cell_line),
        parser.parse_characterization(source, cell_line),
        parser.parse_characterization_markers(source, cell_line),
        # parser.parse_characterization_pluritest(source, cell_line),
        # parser.parse_characterization_epipluriscore(source, cell_line),
        parser.parse_genetic_modifications(source, cell_line),
        parser.parse_disease_associated_genotype(source, cell_line),
        check_availability_on_ecacc(cell_line),
    ]

    if True in dirty:
        if cell_line_created:
            logger.info('Saving new cell line %s' % cell_line.name)
        else:
            logger.info('Updating cell line %s' % cell_line.name)
        cell_line.save()


# -----------------------------------------------------------------------------
# Get providers

def get_providers(providers):

    generator = None
    owner = None
    organizations = []

    for org in providers:
        organization, role = parser.parse_organization(org)

        if role == 'generator':
            generator = organization
        elif role == 'owner':
            owner = organization
        else:
            organizations.append((organization, role))

    return (generator, owner, organizations)


# -----------------------------------------------------------------------------
# Make an API request and return JSON

def request_get(url):

    r = requests.get(url, auth=(settings.HPSCREG['username'], settings.HPSCREG['password']))

    if r.status_code != requests.codes.ok:
        logger.error('Can\' connect to the hPSGreg API (%s): %s' % (url, r.status_code))
        return None
    else:
        return r.json()


# -----------------------------------------------------------------------------
# Check if the cell line exists on ECACC

def check_availability_on_ecacc(cell_line):

    r = requests.get(cell_line.ecacc_url)

    # Highly suspect!!!
    available = r.status_code == requests.codes.ok and re.search(cell_line.name, r.text) is not None

    if available == cell_line.available_for_sale_at_ecacc:
        return False
    else:
        cell_line.available_for_sale_at_ecacc = available
        return True

# -----------------------------------------------------------------------------
