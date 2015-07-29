import csv
import sys

from ebisc.celllines.models import Cellline


'''Export temporary CSV for ECACC'''


# -----------------------------------------------------------------------------
#  Run

def run():

    writer = csv.writer(sys.stdout, dialect=csv.excel_tab)

    writer.writerow((
        'biosamples_id',

        'name',
        'alternative_names',

        'depositor',

        'donor_biosamples_id',
        'donor_gender',
        'donor_age',

        'primary_disease_doid',
        'primary_disease_name',
        'primary_disease_synonyms',

        'cell_type',
        'karyotype',

        'reprogramming_method_type',
        'reprogramming_method_vector',
        'reprogramming_method_virus',
        'reprogramming_method_transposon',
        'reprogramming_method_excisable',

        'culture_conditions_culture_medium',
        'culture_conditions_passage_method',
        'culture_conditions_surface_coating',
        'culture_conditions_co2_concentration',
        'culture_conditions_o2_concentration',

        'pubmed_url',
        'pubmed_title',
    ))

    for cl in Cellline.objects.all():

        if hasattr(cl, 'integrating_vector'):
            reprogramming_method = [
                'integrating',
                cl.integrating_vector.vector,
                cl.integrating_vector.virus,
                cl.integrating_vector.transposon,
                cl.integrating_vector.excisable,
            ]
        elif hasattr(cl, 'non_integrating_vector'):
            reprogramming_method = [
                'non-integrating',
                cl.non_integrating_vector.vector,
                None, None, None
            ]
        else:
            reprogramming_method = [None, None, None, None, None]

        writer.writerow(flatten((
            cl.biosamplesid,

            cl.celllinename,
            cl.celllinenamesynonyms,

            cl.generator.organizationname.encode('utf8'),

            cl.donor.biosamplesid,
            cl.donor.gender,
            cl.donor_age,

            cl.celllineprimarydisease.icdcode if cl.celllineprimarydisease else '',
            cl.celllineprimarydisease.disease if cl.celllineprimarydisease else 'CONTROL',
            cl.celllineprimarydisease.synonyms if cl.celllineprimarydisease else '',

            cl.celllinecelltype,
            cl.karyotype if hasattr(cl, 'karyotype') and cl.karyotype else '',

            reprogramming_method,

            cl.celllinecultureconditions.culture_medium,
            cl.celllinecultureconditions.passagemethod,
            cl.celllinecultureconditions.surfacecoating,
            cl.celllinecultureconditions.co2concentration,
            cl.celllinecultureconditions.o2concentration,

            cl.publications.all()[0].reference_url if cl.publications.all().count() else '',
            cl.publications.all()[0].reference_title.encode('utf8') if cl.publications.all().count() else '',
        )))


# -----------------------------------------------------------------------------
#  Utils

def flatten(lis):

    '''Given a list, possibly nested to any level, return it flattened.'''

    new_list = []

    for item in lis:
        if isinstance(item, type([])):
            new_list.extend(flatten(item))
        else:
            new_list.append(item)

    return new_list

# -----------------------------------------------------------------------------
