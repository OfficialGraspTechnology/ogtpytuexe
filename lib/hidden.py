#! python3
#@author: Jaedan Willis

import os
import shutil
from split import Split
from tkinter import messagebox

class Hidden(object):
	def __init__(self,master,filename):
		self.master = master
		self.filename = filename

	def merge(self):
		# the funtion will run the file in the background
		# with out the user knowing it

		# spliting the filename in 2 to get the loaction and the filename
		head,tail = os.path.split(self.filename)

		# creating command line arguments and past them to the spliting class
		data = 'pyinstaller -w "' + str(self.filename) + '" --distpath "' + str(head) + '/dist' + '" --workpath "' + str(head) + '" --specpath "' + str(head) + '"'
		s = Split(self.master,data)
		s.split()

		# remove the folder and spec file that have the same name after conversion is complete
		try:			
			
			if tail.endswith('.pyw'):				
				filename_folder = head + '/' + tail.replace('.pyw','')
				filename_cache = head + '/__pycache__'
				filename_spec = head + '/' + tail.replace('.pyw','.spec')
				
				if os.path.exists(filename_folder):
					shutil.rmtree(filename_folder)

				if os.path.exists(filename_cache):
					shutil.rmtree(filename_cache)

				if os.path.isfile(filename_spec):
					os.remove(filename_spec)
			else:
				filename_folder = head + '/' + tail.replace('.py','')
				filename_cache = head + '/__pycache__'
				filename_spec = head + '/' + tail.replace('.py','.spec')
				
				if os.path.exists(filename_folder):
					shutil.rmtree(filename_folder)

				if os.path.exists(filename_cache):
					shutil.rmtree(filename_cache)

				if os.path.isfile(filename_spec):
					os.remove(filename_spec)
		
		except Exception as e:
			messagebox.showerror(parent-self.master,title='FileNotFound',message=str(e))