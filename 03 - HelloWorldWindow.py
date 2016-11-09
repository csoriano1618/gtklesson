import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

'''
- Python inheritance
- GObject properties and python optional parameters
- Containers, Gtk.Window is a Gtk.Bin
- Our own event handler
'''

class MyWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="Hello World")

        button = Gtk.Button(label="Click Here")
        button.connect("clicked", self._on_button_clicked)
        self.add(button)

    def _on_button_clicked(self, widget):
        print("Hello World")

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
