import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

'''
- Glade
- GtkBuilder, from file or data
'''

class GridWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="Grid Example")

        self.set_default_size(600, 400)

        builder = Gtk.Builder()
        builder.add_from_file("./grid.ui")
        grid = builder.get_object("OurGrid")
        self.add(grid)

win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
