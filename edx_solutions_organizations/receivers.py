"""
Signal handlers supporting various organization use cases
"""
import logging

from django.dispatch import Signal, receiver

from .models import OrganizationUserMapping

user_organization_updated = Signal(providing_args=['user_id', 'organization_id'])

log = logging.getLogger(__name__)


@receiver(user_organization_updated)
def on_user_organization_updated(sender, *args, **kwargs):
    user_id = kwargs.get('user_id')
    organization_id = kwargs.get('organization_id')
    try:
        OrganizationUserMapping.objects.update_or_create(
            user_id=user_id,
            defaults={
                'organization_id': organization_id,
                'is_main_company':True,
            },
        )
    except Exception as exc:
        log.exception(exc)
    else:
        log.info(u'User %s updated with organization id %s.', user_id, organization_id)
