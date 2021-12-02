"""
app configuration
"""
from django.apps import AppConfig


class SolutionsAppOrganizationsConfig(AppConfig):
    """
    Application configuration class.
    It overrides `ready` method to register signals.
    """
    name = 'edx_solutions_organizations'
    verbose_name = 'Solutions apps organizations'

    def ready(self):

        # import signal handlers
        import edx_solutions_organizations.receivers  # pylint: disable=unused-import

