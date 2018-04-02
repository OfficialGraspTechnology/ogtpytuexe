#! python3
#@author: Jaedan Willis

from tkinter import filedialog

class Icon(object):
	def __init__(self,master):
		self.master = master

	def browse(self):
		# this funtion allows you to browse for an icon
		icon = filedialog.askopenfilename(parent=self.master,defaultextension='.ico',filetypes=[('Icon','*.ico')])
		return str(icon)