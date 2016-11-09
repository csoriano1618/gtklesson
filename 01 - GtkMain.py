import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

'''
Mainloop, single-thread, looking at gtk+ code
'''

print ("Start")

Gtk.main()

print ("Finish")
