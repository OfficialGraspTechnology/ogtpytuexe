#! python3
#@author: Jaedan Willis

from tkinter import filedialog

class File(object):
	def __init__(self,master):
		self.master = master

	def browse(self):
		# this funtion allows you to browse for an .py or .pyw file
		filename = filedialog.askopenfilename(parent=self.master,defaultextension='.py',filetypes=[('Python Files','*.py'),('Python Files','.pyw')])
		return str(filename)