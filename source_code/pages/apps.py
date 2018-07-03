from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'pages'
    verbose_name = 'Pages'

    def ready(self):
    	from . import signals