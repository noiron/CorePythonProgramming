# !/usr/bin/env python

from functools import partial as pto 
from Tkinter import Tk, Button, X
from tkMessageBox import showinfo, showwarning, showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
	'do not enter': CRIT,
	'railroad crossing': WARN,
	'55\nspeed limit': REGU,
	'wrong way': CRIT,
	'meging traffic': WARN,
	'one way': REGU,
}

critCB = lambda: showerror('Error', 'Error Button Pressed!')
warnCB = lambda: showwarning('Warning', 'Warning Button Pressed')
infoCB = 