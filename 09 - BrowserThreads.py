import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk
from gi.repository import WebKit2

import os
import time
import threading

'''
- Async vs sync, and the importance of having the two
- Python threads
- Python callbacks on the main thread, not explained here, look at python Queue,
  just NEVER CALL UI OPERATINS FROM A THREAD THAT IS NOT THE MAIN ONE
'''

HOME_PAGE = "http://www.duckduckgo.com"
DOWNLOADS_FOLDER = "/home/csoriano/"

class BrowserWindow(Gtk.ApplicationWindow):

    def __init__(self):
        super().__init__()
        self.set_size_request(750, 600)
        titlebar = Gtk.HeaderBar()
        titlebar.set_show_close_button(True)
        self.urientry = Gtk.Entry()
        self.urientry.set_size_request(300, -1)
        self.urientry.set_text(HOME_PAGE)
        self.urientry.connect("activate", self._urientry_on_activated)
        titlebar.set_custom_title(self.urientry)

        self.set_titlebar(titlebar)
        self._webview = WebKit2.WebView()
        self._webview.load_uri(HOME_PAGE)
        # "notify::" signals names are emitted for every change in a property.
        # This is based on GObject
        self._webview.connect("notify::uri", self._webview_on_uri_changed)
        self.add(self._webview)

        self.show_all()

    def _urientry_on_activated(self, entry):
        self._check_dowloads_folder()
        uri = self.urientry.get_text()
        self.webview.load_uri(uri)

    def _webview_on_uri_changed(self, signalSender, propertyValue):
        # property value using gi data structures
        self.urientry.set_text(self._webview.get_uri())

    def _check_dowloads_folder (self):
        self._walk_system_async(DOWNLOADS_FOLDER)

    def _walk_system_sync(self, uri):
        for dirName, subdirList, fileList in os.walk(uri):
            print('Found directory: %s' % dirName)
            # Simulate being a little slower, my SSD is too fast! #firstworldproblems
            time.sleep(0.1)
            for filename in fileList:
                print('\t%s' % filename)

    def _walk_system_async(self, uri):
       t = threading.Thread(target=self._walk_system_sync, args=[uri])
       t.daemon = True
       t.start()

class Browser(Gtk.Application):

    def __init__(self):
        super().__init__()
        self._browserwindow = BrowserWindow()
        self._browserwindow.connect("delete-event", Gtk.main_quit)

app = Browser()

Gtk.main()
