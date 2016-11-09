import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk
from gi.repository import WebKit2

'''
- Gtk.Application
- Header bar, Client Side Decorations vs Server Side Decorations
- WebKit and WebKitView as gtk+ interface
'''

HOME_PAGE = "http://www.duckduckgo.com"

class BrowserWindow(Gtk.ApplicationWindow):

    def __init__(self):
        super().__init__()
        self.set_size_request(750, 600)
        titlebar = Gtk.HeaderBar()
        #titlebar.set_show_close_button(True)

        self.set_titlebar(titlebar)
        self._webview = WebKit2.WebView()
        #self._webview.load_uri(HOME_PAGE)
        self.add(self._webview)

        self.show_all()

class Browser(Gtk.Application):

    def __init__(self):
        super().__init__()
        self._browserwindow = BrowserWindow()
        self._browserwindow.connect("delete-event", Gtk.main_quit)

app = Browser()

Gtk.main()
