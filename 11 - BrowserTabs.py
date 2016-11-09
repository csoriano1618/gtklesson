import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk
from gi.repository import WebKit2

'''
- Notebook
- Widget ownership
- Custom signals (not explained here) vs public API
'''

HOME_PAGE = "http://www.duckduckgo.com"

class BrowserTab(Gtk.Box):

    def __init__(self, browser):
        super().__init__(Gtk.Orientation.VERTICAL, 0)

        self._parent = browser
        self._webview = WebKit2.WebView()
        self._webview.load_uri(HOME_PAGE)
        # "notify::" signals names are emitted for every change in a property.
        # This is based on GObject
        self._webview.connect("notify::uri", self._webview_on_uri_changed)
        self._webview.connect("notify::title", self._webview_on_title_changed)
        self.add(self._webview)

        self.show_all()

    def _webview_on_uri_changed(self, signalSender, propertyValue):
        # property value using gi data structures
        self._parent.tab_on_uri_changed(self, self._webview.get_uri())

    def _webview_on_title_changed(self, signalSender, propertyValue):
        # property value using gi data structures
        self._parent.tab_on_title_changed(self, self._webview.get_title())

    def load_uri(self, uri):
        self._webview.load_uri(uri)

    def get_uri(self):
        return self._webview.get_uri()

    def go_back(self):
        self._webview.go_back()

    def go_forward(self):
        self._webview.go_forward()


class BrowserWindow(Gtk.ApplicationWindow):

    def __init__(self):
        super().__init__()
        self.set_size_request(750, 600)
        titlebar = Gtk.HeaderBar()
        titlebar.set_show_close_button(True)
        self.set_titlebar(titlebar)

        backbutton = Gtk.Button.new_from_icon_name("go-previous-symbolic",
                                                   Gtk.IconSize.MENU)
        backbutton.connect("clicked", lambda x: self._get_current_tab().go_back())
        forwardbutton = Gtk.Button.new_from_icon_name("go-next-symbolic",
                                                      Gtk.IconSize.MENU)
        forwardbutton.connect("clicked", lambda x: self._get_current_tab().go_forward())
        buttonbox = Gtk.Box(Gtk.Orientation.HORIZONTAL, 0)
        buttonbox.add(backbutton)
        buttonbox.add(forwardbutton)
        titlebar.pack_start(buttonbox)
        buttonbox.get_style_context().add_class("linked")

        newtabbutton = Gtk.Button.new_from_icon_name("tab-new-symbolic",
                                                     Gtk.IconSize.MENU)
        newtabbutton.connect("clicked", lambda x: self._create_tab())
        titlebar.pack_end(newtabbutton)

        self._urientry = Gtk.Entry()
        self._urientry.set_size_request(300, -1)
        self._urientry.set_text(HOME_PAGE)
        self._urientry.connect("activate", self._urientry_on_activated)
        titlebar.set_custom_title(self._urientry)

        self.set_titlebar(titlebar)

        self._notebook = Gtk.Notebook()
        # self._notebook.connect("switch-page", self._notebook_on_switch_page)
        self.add(self._notebook)
        self._create_tab()

        self.show_all()

    def _urientry_on_activated(self, entry):
        uri = self._urientry.get_text()
        currenttab = self._notebook.get_nth_page(self._notebook.get_current_page())
        currenttab.load_uri(uri)

    # We could define GObject signals instead of public API.
    def tab_on_title_changed(self, tab, title):
        titlewidget = Gtk.Label(title)
        titlewidget.set_hexpand(True)
        self._notebook.set_tab_label(tab, titlewidget)

    def tab_on_uri_changed(self, tab, uri):
        if self._get_current_tab() == tab:
            self._urientry.set_text(uri)

    def _create_tab(self):
        # It's not just text because we would want to add markup too
        tab = BrowserTab(self)
        titlewidget = Gtk.Label("Loading…")
        titlewidget.set_hexpand(True)
        self._notebook.append_page(tab, titlewidget)
        self._notebook.set_current_page(self._notebook.get_n_pages() - 1)

    def _get_current_tab(self):
        return self._notebook.get_nth_page(self._notebook.get_current_page())

    def _notebook_on_switch_page(self, notebook, current_page, index):
        self._urientry.set_text(current_page.get_uri())

class Browser(Gtk.Application):

    def __init__(self):
        super().__init__()
        self._browserwindow = BrowserWindow()
        self._browserwindow.connect("delete-event", Gtk.main_quit)

app = Browser()

Gtk.main()
