import os
import csv
import datetime

import django.db.models.fields

import logging
logger = logging.getLogger('management.commands')

from ..models import *


'''
This is HotsStart data importer.

Importer is implemented via schema definition which maps CSV files to models.
'''

# -----------------------------------------------------------------------------
# File schema definition

FILES = [
    {
        'filename': 'approveduse.csv',
        'model': Approveduse,
        'fields': {'id': 0, 'approveduse': 1}
    },
    {
        'filename': 'disease.csv',
        'model': Disease,
        'fields': {'id': 0, 'disease': 1}
    },
    {
        'filename': 'binnedage.csv',
        'model': Binnedage,
        'fields': {'id': 0, 'binnedage': 1}
    },
    {
        'filename': 'celllinecollection.csv',
        'model': Celllinecollection,
        'fields': {
            'id': 0,
            'celllinecollectiontotal': 1,
            'celllinecollectionupdate': 2,
            'celllinecollectionupdatetype': 3,
            'celllinecollectionupdatedby': 4,
        }
    },
    {
        'filename': 'celllinestatus.csv',
        'model': Celllinestatus,
        'fields': {'id': 0, 'celllinestatus': 1}
    },
    {
        'filename': 'celltype.csv',
        'model': Celltype,
        'fields': {'id': 0, 'celltype': 1}
    },
    {
        'filename': 'country.csv',
        'model': Country,
        'fields': {'id': 0, 'country': 1}
    },
    {
        'filename': 'culturesystem.csv',
        'model': Culturesystem,
        'fields': {'id': 0, 'culturesystem': 1}
    },
    {
        'filename': 'gender.csv',
        'model': Gender,
        'fields': {'id': 0, 'gender': 1}
    },
    {
        'filename': 'organization.csv',
        'model': Organization,
        'fields': {'id': 0, 'organizationshortname': 1}
    },
    {
        'filename': 'phenotype.csv',
        'model': Phenotype,
        'fields': {'id': 0, 'phenotype': 1}
    },
    {
        'filename': 'phonecountrycode.csv',
        'model': Phonecountrycode,
        'fields': {'id': 0, 'phonecountrycode': 1}
    },
    {
        'filename': 'reprogrammingmethod1.csv',
        'model': Reprogrammingmethod1,
        'fields': {'id': 0, 'reprogrammingmethod1': 1}
    },
    {
        'filename': 'reprogrammingmethod2.csv',
        'model': Reprogrammingmethod2,
        'fields': {'id': 0, 'reprogrammingmethod2': 1}
    },
    {
        'filename': 'reprogrammingmethod3.csv',
        'model': Reprogrammingmethod3,
        'fields': {'id': 0, 'reprogrammingmethod3': 1}
    },
    {
        'filename': 'tissuesource.csv',
        'model': Tissuesource,
        'fields': {'id': 0, 'tissuesource': 1}
    },
    {
        'filename': 'clinicaltreatmentb4donation.csv',
        'model': Clinicaltreatmentb4donation,
        'fields': {'id': 0, 'clinicaltreatmentb4donation': 1}
    },
    {
        'filename': 'lastupdatetype.csv',
        'model': Lastupdatetype,
        'fields': {'id': 0, 'lastupdatetype': 1}
    },
    {
        'filename': 'useraccount.csv',
        'model': Useraccount,
        'fields': {
            'id': 0,
            'username': 1,
            'useraccounttype': 2,
            'person': 3,
            'organization': 4,
            'accesslevel': 5,
            'useraccountupdate': 6,
            'useraccountupdatetype': 7,
            'useraccountupdatedby': 8,
        }
    },
    {
        'filename': 'postcode.csv',
        'model': Postcode,
        'fields': {'id': 0, 'postcode': 1, 'district': 2}
    },
    {
        'filename': 'contacttype.csv',
        'model': Contacttype,
        'fields': {'id': 0, 'contacttype': 1}
    },
    {
        'filename': 'orgtype.csv',
        'model': Orgtype,
        'fields': {'id': 0, 'orgtype': 1}
    },
    {
        'filename': 'celllineorgtype.csv',
        'model': Celllineorgtype,
        'fields': {'id': 0, 'celllineorgtype': 1}
    },

    # --- Related models ---

    {
        'filename': 'contact.csv',
        'model': Contact,
        'fields': {
            'id': 0,
            'contacttype': {'model': Contacttype, 'id': 1},
            'country': {'model': Country, 'id': 2},
            'postcode': {'model': Postcode, 'id': 3},
            'statecounty': 4,
            'city': 5,
            'street': 6,
            'buildingnumber': 7,
            'suiteoraptordept': 8,
            'officephonecountrycode': {'model': Phonecountrycode, 'id': 9},
            'officephone': 10,
            'faxcountrycode': {'model': Phonecountrycode, 'id': 11},
            'fax': 12,
            'mobilecountrycode': {'model': Phonecountrycode, 'id': 13},
            'mobilephone': 14,
            'website': 15,
            'emailaddress': 16,
            'contactupdate': 17,
            'contactupdatetype': {'model': Lastupdatetype, 'id': 18},
            'contactupdatedby': {'model': Useraccount, 'id': 19},
        }
    },
    {
        'filename': 'organization.csv',
        'model': Organization,
        'fields': {
            'id': 0,
            'organizationname': 1,
            'organizationshortname': 2,
            'organizationcontact': {'model': Contact, 'id': 3},
            'organizationupdate': 4,
            'organizationupdatetype': {'model': Lastupdatetype, 'id': 5},
            'organizationupdatedby': {'model': Useraccount, 'id': 6},
            'organizationtype': {'model': Orgtype, 'id': 7},
        }
    },
    {
        'filename': 'donor.csv',
        'model': Donor,
        'fields': {'id': 0, 'hescregdonorid': 1, 'gender': {'model': Gender, 'id': 3}, 'providerdonorid': 7}
    },
    {
        'filename': 'cellline.csv',
        'model': Cellline,
        'fields': {
            'id': 0,
            'biosamplesid': 1,
            'celllinename': 2,
            'celllinedonor': {'model': Donor, 'id': 3},

            'celllineprimarydisease': {'model': Disease, 'id': 4},
            'celllinediseaseaddinfo': 5,
            'celllinestatus': {'model': Celllinestatus, 'id': 6},
            'celllinecelltype': {'model': Celltype, 'id': 7},
            'celllinecollection': {'model': Celllinecollection, 'id': 8},
            'celllinetissuesource': {'model': Tissuesource, 'id': 9},
            'celllinetissuetreatment': {'model': Clinicaltreatmentb4donation, 'id': 10},
            # 'celllinetissuedate': 11,
            'celllinenamesynonyms': 12,
            # 'depositorscelllineuri': 13,
            # 'celllinecomments': 14,
            'celllineupdate': 15,
            'celllineupdatetype': {'model': Lastupdatetype, 'id': 16},
            'celllineupdatedby': {'model': Useraccount, 'id': 17},
            # 'celllineecaccur': 18,
        }
    },
    {
        'filename': 'celllinechecklist.csv',
        'model': Celllinechecklist,
        'fields': {
            'id': 0,
            'checklistcellline': {'model': Cellline, 'id': 1},
            'morphologicalassessment': 2,
            'facs': 3,
            'ihc': 4,
            'pcrforreprofactorremoval': 5,
            'pcrforpluripotency': 6,
            'teratoma': 7,
            'invitrodifferentiation': 8,
            'karyotype': 9,
            'cnvanalysis': 10,
            'dnamethylation': 11,
            'microbiologyinclmycoplasma': 12,
            'dnagenotyping': 13,
            'hlatyping': 14,
            'virustesting': 15,
            'postthawviability': 16,
            'checklistcomments': 17,
        }
    },
    {
        'filename': 'celllinelab.csv',
        'model': Celllinelab,
        'fields': {
            'id': 0,
            'labcellline': {'model': Cellline, 'id': 1},
            'cryodate': 2,
            'expansioninprogress': 3,
            'funder': 4,
            'mutagene': 5,
            'reprogrammingmethod1': {'model': Reprogrammingmethod1, 'id': 6},
            'reprogrammingmethod2': {'model': Reprogrammingmethod2, 'id': 7},
            'reprogrammingmethod3': {'model': Reprogrammingmethod3, 'id': 8},
            'clonenumber': 9,
            'passagenumber': 10,
            'culturesystem': {'model': Culturesystem, 'id': 11},
            'culturesystemcomment': 12,
            'celllinelabupdate': 13,
            'celllinelabupdatetype': {'model': Lastupdatetype, 'id': 14},
            'celllinelabupdatedby': {'model': Useraccount, 'id': 15},
        }
    },
    {
        'filename': 'celllineorganization.csv',
        'model': Celllineorganization,
        'fields': {
            'id': 0,
            'orgcellline': {'model': Cellline, 'id': 1},
            'organization': {'model': Organization, 'id': 2},
            'celllineorgtype': {'model': Celllineorgtype, 'id': 3},
            'orgstatus': 4,
            'orgregistrationdate': 5,
        }
    },
]


# -----------------------------------------------------------------------------
# Importer


def value_of_csv(value):
    if value == 'NULL':
        return None
    return value


def import_hotstart(basedir):

    for f in FILES:
        logger.info('Importing %s' % f['filename'])

        f['model'].objects.all().delete()

        with open(os.path.join(basedir, f['filename']), 'r') as fi:

            reader = csv.reader(fi)
            next(reader, None)

            for line in reader:
                logger.debug('  Data: %s' % line)

                kwargs = {}
                for key, index in f['fields'].items():

                    if isinstance(index, dict):
                        # foreign key index value
                        value = value_of_csv(line[index['id']])
                        if value is not None:
                            value = value_of_csv(index['model'].objects.get(id=value))

                    else:
                        # atomic index value
                        value = value_of_csv(line[index])

                        # inspect the Django model and convert the value to special fields

                        if isinstance(f['model']._meta.get_field_by_name(key)[0], django.db.models.fields.IntegerField):
                            if value is not None:
                                value = int(value)

                        if isinstance(f['model']._meta.get_field_by_name(key)[0], django.db.models.fields.DateField):
                            if value == '':
                                value = None
                            elif value is not None:
                                parts = [int(x) for x in value.split('-')]
                                value = datetime.date(*parts)

                        if isinstance(f['model']._meta.get_field_by_name(key)[0], django.db.models.fields.BooleanField):
                            if value is not None:
                                value = int(value) == 1 and True or False
                            else:
                                value = False

                    kwargs[key] = value

                logger.debug('  Args: %s' % kwargs)

                obj = f['model'](**kwargs)
                try:
                    obj.save()
                    logger.info('  Object: %s' % obj)
                except Exception, e:
                    logger.error('  %s' % str(e).replace('\n', ' '))

# -----------------------------------------------------------------------------
