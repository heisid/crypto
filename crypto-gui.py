#!/usr/bin/env python3
# GUI for this toy
# Sid

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import tools
import affine

class MainWindow(Gtk.Window):
   def __init__(self):
      Gtk.Window.__init__(self, title="CrypToy")

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()