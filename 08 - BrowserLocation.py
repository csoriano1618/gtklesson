import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk
from gi.repository import WebKit2

'''
- Gtk.Entry
- notify::
'''

HOME_PAGE = "http://www.duckduckgo.com"

class BrowserWindow(Gtk.ApplicationWindow):

    def __init__(self):
        super().__init__()
        self.set_size_request(750, 600)
        titlebar = Gtk.HeaderBar()
        titlebar.set_show_close_button(True)

        self._urientry = Gtk.Entry()
        self._urientry.set_size_request(300, -1)
        self._urientry.set_text(HOME_PAGE)
        self._urientry.connect("activate", self._urientry_on_activated)
        titlebar.set_custom_title(self._urientry)

        self.set_titlebar(titlebar)
        self._webview = WebKit2.WebView()
        self._webview.load_uri(HOME_PAGE)
        # "notify::" signals names are emitted for every change in a property.
        # This is based on GObject

        self._webview.connect("notify::uri", self._webview_on_uri_changed)
        self.add(self._webview)

        self.show_all()

    def _urientry_on_activated(self, entry):
        uri = self._urientry.get_text()
        self._webview.load_uri(uri)

    def _webview_on_uri_changed(self, signalSender, propertyValue):
        # property value using gi data structures
        self._urientry.set_text(self._webview.get_uri())

class Browser(Gtk.Application):

    def __init__(self):
        super().__init__()
        self._browserwindow = BrowserWindow()
        self._browserwindow.connect("delete-event", Gtk.main_quit)

app = Browser()

Gtk.main()
