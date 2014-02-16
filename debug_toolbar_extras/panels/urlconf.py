from django.conf import settings
from django.utils.importlib import import_module
from django.utils.translation import ugettext_lazy as _

from debug_toolbar.panels import DebugPanel



class URLconfDebugPanel(DebugPanel):
    """
    A panel that lists all url mappings for this request.
    """
    name = 'URLconf'
    template = 'debug_toolbar/panels/urlconf.html'
    has_content = True

    def nav_title(self):
        return _('URL Mappings')

    def title(self):
        return _('URL Mappings')

    def url(self):
        return ''

    def process_response(self, request, response):
        debug = {}

        urlconf = import_module(settings.ROOT_URLCONF)

        self.record_stats({
            'urlconf': urlconf.__name__,
            'urlpatterns': urlconf.urlpatterns,
            'debug': debug,
        })
