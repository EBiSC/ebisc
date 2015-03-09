# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from cms.models import Node, Document


# -----------------------------------------------------------------------------
# Document

def document_of_path(path):

    node = get_object_or_404(Node, path=path)
    document = get_object_or_404(Document, node=node, active=True)

    return document


def document(request, path):

    return render_document(request, document_of_path(path))


# -----------------------------------------------------------------------------
# Default document template renderer

def render_document(request, document, context={}):

    context.update(document=document)

    if 'render_%s' % document.template in globals():
        return globals()['render_%s' % document.template](request, document, context)
    else:
        return render(request, document.template_filename, context)


# -----------------------------------------------------------------------------
# Preview

def preview(request, document):
    return render_document(request, document)


# -----------------------------------------------------------------------------
# Error pages

def error404(request):
    document = document_of_path(request.LANGUAGE_CODE + '/')
    document.phony = True

    return render(request, 'errors/404.html', {'document': document})


def error500(request):
    document = document_of_path(request.LANGUAGE_CODE + '/')
    document.phony = True

    return render(request, 'errors/500.html', {'document': document})


# -----------------------------------------------------------------------------
# Home

def render_Home(request, document, context):

    context.update({})

    return render(request, document.template_filename, context)

# -----------------------------------------------------------------------------
