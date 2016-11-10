import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
'''
Signals, virtual methods, default handlers
'''

win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)
#win.show_all()
Gtk.main()
