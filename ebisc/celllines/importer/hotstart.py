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
# Convert JSON values to python values

def value_of_json(source, field, cast=None):

    if cast == 'bool':

        if source.get(field, None) == '1':
            return True
        else:
            return False

    elif cast == 'int':

        try:
            return int(source.get(field))
        except KeyError:
            return None
        except:
            logger.warn('Invalid field value for int: %s=%s' % (field, source.get(field)))
            return None

    elif cast == 'gender':

        try:
            return Gender.objects.get(name=source.get(field))
        except KeyError:
            pass
        except Gender.DoesNotExist:
            logger.warn('Invalid donor gender: %s' % source.get(field))

        return None

    elif cast == 'age_range':

        try:
            return AgeRange.objects.get(name=source.get(field))
        except KeyError:
            pass
        except AgeRange.DoesNotExist:
            logger.warn('Invalid age range: %s' % source.get(field))

        return None

    else:
        return source.get(field, None)


def term_list_value_of_json(source, source_field, model, model_field='name'):

    if source_field not in source:
        return None

    return term_list_value(source[source_field], model, model_field)


def term_list_value(value, model, model_field='name'):

    if value is None:
        return None

    kwargs = {}
    kwargs[model_field] = value

    value, created = model.objects.get_or_create(**kwargs)

    return value


# -----------------------------------------------------------------------------
# Specific parsers

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


@inject_valuef
def parse_donor(valuef, source):

    gender = valuef('gender_primary_cell', 'gender')

    try:
        donor = Donor.objects.get(biosamplesid=valuef('donor_biosample_id'))

        if donor.gender != gender:
            logger.warn('Changing donor gender from %s to %s' % (donor.gender, gender))
            donor.gender = gender

    except Donor.DoesNotExist:
        donor = Donor(
            biosamplesid=valuef('donor_biosample_id'),
            gender=gender
        )

    donor.save()

    return donor


@inject_valuef
def parse_legal(valuef, source, cell_line):

    if valuef('informed_consent_flag', 'bool'):

        cell_line_legal = CellLineLegal(
            cell_line=cell_line,
            q1donorconsent=valuef('informed_consent_flag', 'bool'),
        )

        cell_line_legal.save()


@inject_valuef
def parse_integrating_vector(valuef, source, cell_line):

    vector = CellLineIntegratingVector(
        cell_line=cell_line,
        vector=term_list_value_of_json(source, 'integrating_vector', IntegratingVector),
        virus=term_list_value_of_json(source, 'integrating_vector_virus_type', Virus),
        transposon=term_list_value_of_json(source, 'integrating_vector_transposon_type', Transposon),
        excisable=valuef('excisable_vector_flag', 'bool'),
    )

    logger.info('Added integrating vector: %s' % vector)

    vector.save()


@inject_valuef
def parse_non_integrating_vector(valuef, source, cell_line):

    vector = CellLineNonIntegratingVector(
        cell_line=cell_line,
        vector=term_list_value_of_json(source, 'non_integrating_vector', NonIntegratingVector),
    )

    logger.info('Added non-integrating vector: %s' % vector)

    vector.save()


@inject_valuef
def parse_derivation(valuef, source, cell_line):

    cell_line_derivation = Celllinederivation(
        cell_line=cell_line,
        primarycelldevelopmentalstage=term_list_value_of_json(source, 'dev_stage_primary_cell', PrimaryCellDevelopmentalStage),
        primarycelltypename=valuef('primary_celltype_ont_name'),
        selectioncriteriaforclones=valuef('selection_of_clones'),
        xenofreeconditions=valuef('derivation_xeno_graft_free_flag', 'bool'),
        derivedundergmp=valuef('derivation_gmp_ips_flag', 'bool'),
    )

    logger.info('Added cell line derivation: %s' % cell_line_derivation)

    cell_line_derivation.save()


@inject_valuef
def parse_culture_condions(valuef, source, cell_line):

    cell_line_culture_conditions = Celllinecultureconditions(
        cell_line=cell_line,

        surfacecoating=term_list_value_of_json(source, 'surface_coating', SurfaceCoating),

        feedercellid=valuef('feeder_cells_ont_id'),
        feedercelltype=valuef('feeder_cells_name'),

        passagemethod=term_list_value_of_json(source, 'passage_method', PassageMethod),
        enzymatically=term_list_value_of_json(source, 'passage_method_enzymatically', Enzymatically),
        enzymefree=term_list_value_of_json(source, 'passage_method_enzyme_free', EnzymeFree),

        o2concentration=valuef('o2_concentration', 'int'),
        co2concentration=valuef('co2_concentration', 'int'),
    )

    cell_line_culture_conditions.save()

    # Culture medium

    def parse_supplements(cell_line_culture_conditions, supplements):

        if supplements is None:
            return

        else:
            for supplement in supplements:
                (supplement, amount, unit) = supplement.split('###')
                CellLineCultureMediumSupplement(
                    cell_line_culture_conditions=cell_line_culture_conditions,
                    supplement=supplement,
                    amount=amount,
                    unit=term_list_value(unit, Unit),
                ).save()

    if not valuef('culture_conditions_medium_culture_medium') == 'other_medium':
        cell_line_culture_conditions.culture_medium = term_list_value_of_json(source, 'culture_conditions_medium_culture_medium', CultureMedium)

        # Culture medium supplements
        parse_supplements(cell_line_culture_conditions, valuef('culture_conditions_medium_culture_medium_supplements'))

    else:
        CultureMediumOther(
            cell_line_culture_conditions=cell_line_culture_conditions,
            base=valuef('culture_conditions_medium_culture_medium_other_base'),
            protein_source=term_list_value_of_json(source, 'culture_conditions_medium_culture_medium_other_protein_source', ProteinSource),
            serum_concentration=valuef('culture_conditions_medium_culture_medium_other_concentration', 'int'),
        ).save()

        # Culture medium supplements
        parse_supplements(cell_line_culture_conditions, valuef('culture_conditions_medium_culture_medium_other_supplements'))

    # Final save

    cell_line_culture_conditions.save()
    logger.info('Added cell line culture conditions: %s' % cell_line_culture_conditions)


# -----------------------------------------------------------------------------
#  Importer

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
                donor=parse_donor(source),
                donor_age=valuef('donor_age', 'age_range'),
            )

            # Organizations

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

            # Legal
            parse_legal(source, cell_line)

            # Vector

            if valuef('vector_type') == 'integrating':
                parse_integrating_vector(source, cell_line)

            if valuef('vector_type') == 'non_integrating':
                parse_non_integrating_vector(source, cell_line)

            # Derivation
            parse_derivation(source, cell_line)

            # Culture conditions
            parse_culture_condions(source, cell_line)

            # Final save
            cell_line.save()

# -----------------------------------------------------------------------------
