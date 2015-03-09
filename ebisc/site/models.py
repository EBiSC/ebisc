# -*- coding: utf-8 -*-

from cms.schema import Schema, Document, ListField, DictField, CharField, TextField, HtmlField


# -----------------------------------------------------------------------------
# Default

class Default(Document):

    title = DictField(Schema.build(
        title=CharField(u'Naslov', attrs={'size': 80, 'class': 'uploadIt'}),
        subtitle=CharField(u'Podnaslov', attrs={'size': 80}),
    ), verbose_name=u'Naslov')

    content = HtmlField(u'Content', display_label=False)

    class Meta:
        default = True
        template = 'site/default.html'
        verbose_name = 'Default'


class Grid(Default):

    SPAN_TYPES = [('col-%d' % i, 'Col %d' % i) for i in range(1, 13)]
    OFFSET_TYPES = [('', 'No offset')] + [('offset-%d' % i, 'Offset %d' % i) for i in range(1, 12)]

    content = ListField(DictField(Schema.build(
        rows=ListField(DictField(Schema.build(
            columns=ListField(DictField(Schema.build(
                span=CharField(u'Širina', options=SPAN_TYPES),
                offset=CharField(u'Odmik', options=OFFSET_TYPES),
                content=HtmlField(u'Vsebina', display_label=False)
            )), verbose_name=u'Kolone')
        )), verbose_name=u'Vrstice')
    )), verbose_name=u'Sklopi')

    class Meta:
        template = 'site/grid.html'
        verbose_name = 'Grid'

# -----------------------------------------------------------------------------
