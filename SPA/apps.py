from django.apps import AppConfig

class SPAConfig(AppConfig):
    name = 'SPA'
    def ready(self):
        import SPA.signals
