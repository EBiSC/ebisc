from django.conf import settings

def is_live(context):
    return {'IS_LIVE': settings.IS_LIVE}
