import django.contrib.auth.models


class AccessPermission(django.contrib.auth.models.Permission):

    class Meta:
        proxy = True
        verbose_name = u'Access permission'
        verbose_name_plural = u'Access permissions'
