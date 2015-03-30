# -*- coding: utf-8 -*-

import os

import django.shortcuts
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.core.urlresolvers import reverse


# -----------------------------------------------------------------------------
# Menu

class Menu(object):

    @staticmethod
    def active(item, path):
        path = '/' + path
        return path.startswith(unicode(item))

    def __init__(self, items, path):
        self.menu = ({'path': item[0], 'title': item[1], 'active': Menu.active(item[0], path)} for item in items)

    def __iter__(self):
        return self.menu


# -----------------------------------------------------------------------------
# Document

def get_menu(path):

    MENU = (
        (reverse('search:search'), 'Cell Line Catalogue'),
        (reverse('executive:dashboard'), 'Executive Dashboard'),
        (reverse('site:document', args=['about/']), 'About EBiSC'),
    )

    return Menu(MENU, path)


def document(request, path):

    path = 'site/' + path
    return render(request, os.path.join(path.encode('ascii', 'ignore'), 'index.html'))


def render(request, path, context={}):

    menu = get_menu(path)

    context.update({
        'path': path,
        'menu': menu,
    })

    try:
        return django.shortcuts.render(request, path, context)
    except TemplateDoesNotExist:
        raise Http404


# -----------------------------------------------------------------------------
