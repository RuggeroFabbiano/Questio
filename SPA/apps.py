"""
SPA app. config.
"""

from django.apps import AppConfig

class SPAConfig(AppConfig):
    """
    SPA config. class
    """

    name = 'SPA'
    def ready(self):
        import SPA.signals
