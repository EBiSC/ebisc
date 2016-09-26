# -*- coding: utf-8 -*-

import django.shortcuts
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from ebisc.cms.models import Page
from ebisc.celllines.models import Cellline


# -----------------------------------------------------------------------------
# Menu

class Menu(object):

    @staticmethod
    def active(item, path):
        if item == '/':
            return path == item
        else:
            return path.startswith(unicode(item))

    def __init__(self, items, path):
        self.menu = ({'path': item[0], 'title': item[1], 'active': Menu.active(item[0], path)} for item in items)

    def __iter__(self):
        return self.menu


# -----------------------------------------------------------------------------
# Catalog (cellines are served under pages)

def search(request):
    return render(request, 'catalog/search.html', {})


# -----------------------------------------------------------------------------
# Pages

def get_menu(request):

    path = request.path

    MENU = [
        (reverse('site:search'), 'Cell Line Catalogue'),
        ('/customer-information/', 'For customers'),
        ('/depositors/', 'For depositors'),
    ]

    if request.user.has_perm('auth.can_view_executive_dashboard'):
        MENU = MENU + [(reverse('executive:dashboard'), 'Executive Dashboard')]

    return Menu(MENU, path)


def page(request, path):

    try:
        name = path.rstrip('/')
        cellline = Cellline.objects.get(name=name, available_for_sale_at_ecacc=True)

        same_donor_lines = Cellline.objects.filter(donor=cellline.donor, available_for_sale_at_ecacc=True).exclude(name=cellline.name).order_by('name')

        if cellline.derived_from:
            same_donor_lines = Cellline.objects.filter(donor=cellline.donor, available_for_sale_at_ecacc=True).exclude(name=cellline.name).exclude(name=cellline.derived_from.name).exclude(name__regex='(-\d+)$').order_by('name')

        return render(request, 'catalog/cellline.html', {
            'cellline': cellline,
            'same_donor_lines': same_donor_lines,
        })
    except Cellline.DoesNotExist:
        pass

    return render(request, 'page.html', {
        'page': get_object_or_404(Page, path='/' + path, published=True)
    })


def render(request, path, context={}):

    menu = get_menu(request)

    context.update({
        'path': path,
        'menu': menu,
    })

    try:
        return django.shortcuts.render(request, path, context)
    except TemplateDoesNotExist:
        raise Http404


# -----------------------------------------------------------------------------
