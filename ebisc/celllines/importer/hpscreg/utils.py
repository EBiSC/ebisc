import re


def format_integrity_error(e):
    '''Format Django DB integrity error'''
    return re.split(r'\n', e.message)[0]
