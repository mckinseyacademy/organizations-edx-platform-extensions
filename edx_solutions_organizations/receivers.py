"""
Signal handlers supporting various organization use cases
"""
import logging

from django.dispatch import Signal, receiver

from .models import OrganizationUsersAttributes
from .utils import generate_key_for_main_user

user_organization_updated = Signal(providing_args=['user_id', 'organization_id'])

log = logging.getLogger(__name__)


@receiver(user_organization_updated)
def on_user_organization_updated(sender, *args, **kwargs):
    user_id = kwargs.get('user_id')
    organization_id = kwargs.get('organization_id')
    key = generate_key_for_main_user(user_id)
    try:
        OrganizationUsersAttributes.objects.update_or_create(
            user_id=user_id,
            key=key,
            defaults={
                'organization_id': organization_id,
                'is_main_company':True,
            },
        )
    except Exception as exc:
        log.exception(exc)
    else:
        log.info(u'User %s updated with organization id %s.', user_id, organization_id)
