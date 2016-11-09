import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

'''
- Diferent constructors with GObject
- Icon browser
- Symbolic vs non symbolic
- Css
- Style providers
'''

theme= """
image {animation: spin 1s linear infinite;}

@keyframes spin {
  from {color:red;}
  to { -gtk-icon-transform: rotate(1turn); color: green;}
}
"""

class GridWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="Theme")

        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button.new_from_icon_name("folder-music-symbolic", Gtk.IconSize.DND)
        button2 = Gtk.Button.new_from_icon_name("folder-music-symbolic", Gtk.IconSize.DND)
        button3 = Gtk.Button.new_from_icon_name("folder-music-symbolic", Gtk.IconSize.DND)
        button4 = Gtk.Button.new_from_icon_name("folder-music-symbolic", Gtk.IconSize.DND)
        button5 = Gtk.Button.new_from_icon_name("folder-music-symbolic", Gtk.IconSize.DND)
        button6 = Gtk.Button.new_from_icon_name("folder-music-symbolic", Gtk.IconSize.DND)
        button6.set_hexpand(True)

        grid.add(button1)
        grid.attach(button2, 1, 0, 2, 1)
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)

        styleContext = self.get_style_context()
        cssProvider = Gtk.CssProvider()
        # Encoding is necesary because the parameter is a C string, array of bytes,
        # not Unicode
        cssProvider.load_from_data(str.encode(theme))
        styleContext.add_provider_for_screen(Gdk.Display.get_default().get_default_screen(),
                                             cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
