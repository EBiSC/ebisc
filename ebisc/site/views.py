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
    ]

    if request.user.has_perm('auth.can_view_executive_dashboard'):
        MENU = MENU + [(reverse('executive:dashboard'), 'Executive Dashboard')]

    return Menu(MENU, path)


def page(request, path):

    try:
        name = path.rstrip('/')
        return render(request, 'catalog/cellline.html', {
            'cellline': Cellline.objects.get(name=name, available_for_sale_at_ecacc=True)
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
