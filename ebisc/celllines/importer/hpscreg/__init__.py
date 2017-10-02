'''
hPSCreg JSON data API importer.
'''

import re
import os
import functools
import requests

from django.conf import settings

import logging
logger = logging.getLogger('management.commands')

from ebisc.celllines.models import Cellline, CelllineStatus, Country

from . import parser
from . import parser_characterisation
from . import parser_genotyping
from . import parser_derivation


# -----------------------------------------------------------------------------
#  Run

def run(cellline=None, local=False):

    if local:
        if os.getenv("TOMCAT_URL"):
            server = os.getenv("TOMCAT_URL")
        else:
            logging.info(u'no local tomcat_url given')
            local = False

    if local:
        logger.info(u'using ' + server + settings.HPSCREG['local_list_url'])
        cellline_ids = request_get(server + settings.HPSCREG['local_list_url'])
    else:
        cellline_ids = request_get(settings.HPSCREG['list_url'])

    if cellline_ids is None:
        return

    # Tests
    # json = request_get('http://test.hescreg.eu/api/export_readable/EDi001-A-1')
    # import_cellline(json)

    for cellline_id in [id for id in cellline_ids]:
        if cellline is not None and cellline_id != cellline:
            continue
        elif cellline_id == 'BCRTi005-A' or cellline_id == 'BCRTi004-A':
            continue
        else:
            logger.info('Importing data for cell line %s' % cellline_id)
            if local:
                json = request_get(server + settings.HPSCREG['local_cellline_url'] + cellline_id)
            else:
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

        # ECACC catalogue number assignment for new cell lines
        ecacc_cat_number = str(int(cell_line.id) + 66540000 - 100)
        if ecacc_cat_number <= '66999999':
            cell_line.ecacc_id = ecacc_cat_number
            cell_line.save()
        else:
            logger.warn('Ran out of ECACC catalogue numbers for cell line %s' % valuef('name'))

        # Set status to not available for new lines
        status = CelllineStatus(cell_line=cell_line, status='not_available', comment='Initial value at first import')
        status.save()

        logger.info('Found new cell line %s' % valuef('name'))

    cell_line.validated = valuef('validation_status')
    cell_line.hescreg_id = valuef('id')
    cell_line.name = valuef('name')
    cell_line.alternative_names = ', '.join(valuef('alternate_name')) if valuef('alternate_name') is not None else ''
    cell_line.donor = parser.parse_donor(valuef('donor')) if valuef('donor') is not None else None
    cell_line.donor_age = valuef('donor_age', 'age_range')
    cell_line.generator = generator
    cell_line.owner = owner
    cell_line.derivation_country = parser.term_list_value_of_json(source, 'derivation_country', Country)
    cell_line.has_diseases = valuef('disease_flag', 'nullbool')
    cell_line.disease_associated_phenotypes = valuef('disease_associated_phenotypes')
    cell_line.non_disease_associated_phenotypes = valuef('donor_phenotypes')
    cell_line.has_genetic_modification = valuef('genetic_modification_flag', 'nullbool')
    cell_line.derived_from = parser.parse_derived_from(source)
    cell_line.public_notes = valuef('public_notes')

    dirty = [cell_line.is_dirty(check_relationship=True)]

    dirty += [
        parser.parse_cell_line_diseases(source, cell_line),
        parser.parse_genetic_modifications_non_disease(source, cell_line),
        parser_derivation.parse_reprogramming_vector(source, cell_line),
        parser_derivation.parse_derivation(source, cell_line),
        parser_derivation.parse_vector_free_reprogramming_factors(source, cell_line),
        parser.parse_culture_conditions(source, cell_line),
        parser.parse_publications(source, cell_line),
        parser_genotyping.parse_karyotyping(source, cell_line),
        parser_genotyping.parse_hla_typing(source, cell_line),
        parser_genotyping.parse_str_fingerprinting(source, cell_line),
        parser_genotyping.parse_genome_analysis(source, cell_line),
        parser_characterisation.parse_characterization(source, cell_line),
        parser_characterisation.parse_characterization_marker_expression(source, cell_line),
        parser_characterisation.parse_characterization_pluritest(source, cell_line),
        parser_characterisation.parse_characterization_epipluriscore(source, cell_line),
        parser_characterisation.parse_characterization_undiff_morphology(source, cell_line),
        parser_characterisation.parse_characterization_hpscscorecard(source, cell_line),
        parser_characterisation.parse_characterization_rna_sequencing(source, cell_line),
        parser_characterisation.parse_characterization_gene_expression_array(source, cell_line),
        parser_characterisation.parse_characterization_differentiation_potency(source, cell_line),
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

    # Change ECACC availability status only if line is available (temporary fix to prevent the Catalogue from being empty in case of ECACC unavailability)

    if available is False:
        return False
    else:
        if available == cell_line.available_for_sale_at_ecacc:
            return False
        else:
            cell_line.available_for_sale_at_ecacc = available
            return True

# -----------------------------------------------------------------------------
