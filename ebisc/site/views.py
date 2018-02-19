# -*- coding: utf-8 -*-

import django.shortcuts
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from ebisc.cms.models import Page, Faq, FaqCategory
from ebisc.celllines.models import Cellline, CelllineCharacterizationMarkerExpression


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
# FAQ

def faq(request, category):

    try:
        category = FaqCategory.objects.get(slug=category)

        return render(request, 'faq/index.html', {
            'category_name': category.name,
            'faqs': Faq.objects.filter(published=True, category=category)
        })

    except FaqCategory.DoesNotExist:
        raise Http404


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
        cellline = Cellline.objects.get(name=name, available_for_sale_at_ecacc=True, current_status__status__in=['at_ecacc', 'expand_to_order', 'restricted_distribution'])

        # Subclones from this line
        subclones = []
        if cellline.derived_cell_lines.all():
            subclones = [subclone for subclone in cellline.derived_cell_lines.all() if subclone.available_for_sale_at_ecacc]

        # All subclones from the line this line was derived from
        available_subclones_from_parent = []
        if cellline.derived_from and cellline.derived_from.derived_cell_lines.all():
            available_subclones_from_parent = [subclone for subclone in cellline.derived_from.derived_cell_lines.all() if subclone.available_for_sale_at_ecacc]

        # Lines from the same donor, subclones excluded
        same_donor_lines = Cellline.objects.filter(donor=cellline.donor, available_for_sale_at_ecacc=True).exclude(name=cellline.name).exclude(name__regex='(-\d+)$').order_by('name')

        if cellline.derived_from:
            same_donor_lines = same_donor_lines.exclude(name=cellline.derived_from.name)

        # Relatives
        relatives = [related_donor for related_donor in cellline.donor.relatives.all()]

        # Characterization data - undifferentiated marker expression
        import collections

        undiff_marker_expression = collections.OrderedDict()

        marker_expression_query = CelllineCharacterizationMarkerExpression.objects.filter(cell_line=cellline).order_by('marker')

        marker_expression_methods = ['Immunostaining', 'RT-PCR', 'FACS', 'Enzymatic Assay', 'Expression Profiles']

        for marker_exp in sorted(set([m for m in marker_expression_query])):
            undiff_marker_expression[marker_exp] = collections.OrderedDict()
            for method in marker_expression_methods:
                undiff_marker_expression[marker_exp][method] = []

        for marker_expression in marker_expression_query:
            for method in marker_expression.marker_expression_method.all():
                undiff_marker_expression[marker_expression][method.name].append(method)

        return render(request, 'catalog/cellline.html', {
            'cellline': cellline,
            'same_donor_lines': same_donor_lines,
            'subclones': subclones,
            'available_subclones_from_parent': available_subclones_from_parent,
            'relatives': relatives,
            'undiff_marker_expression': undiff_marker_expression,
            'marker_expression_methods': marker_expression_methods,
        })
    except Cellline.DoesNotExist:
        try:
            # try to get unavailable (but known) cell line
            cellline = Cellline.objects.get(name=name)
            cellline.available_for_sale = False
            return render(request, 'catalog/cellline.html', {
                'cellline': cellline,
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
