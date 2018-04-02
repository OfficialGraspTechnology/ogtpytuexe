#! python3
#@author: Jaedan Willis

import subprocess
from tkinter import messagebox

class Convert(object):
	def __init__(self,master,data):
		self.master = master
		self.data = data
	
	def convert(self):
		# this function converts all the differnt data past to it
		# in to an executable file.We will show an erro message
		# if the conversion failed
		try:
			sub = subprocess.call(self.data)
			return sub
		except ValueError as e:
			messagebox.showerror(parent=self.master,title='Value Error',message=str(e))
		except FileNotFoundError as e:
			messagebox.showerror(parent=self.master,title='FileNotFound Error',message=str(e) + ' (pyinstaller).\nPlease make sure that you have python 3x and pyinstaller installed.')