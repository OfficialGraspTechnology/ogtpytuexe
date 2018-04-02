#! python3
#@author: Jaedan Willis

from cvert import Convert
from tkinter import messagebox

class Split(object):
	def __init__(self,master,data):
		self.master = master
		self.data = data

	def split(self):
		# this function will separate
		# the arguments in to different
		# sections and then past them
		# on to the final stage which
		# is converting to exe
		
		# display a message to let the
		# user no the program will convert
		# in the background and they
		# will be notified when is complete
		messagebox.showinfo(parent=self.master,title='Please Wait',message='Don\'t panic.We will notiy you when your conversion is completed.' )
		
		# verifying the arguments past on
		# from the functions above
		if '-w -F -i' in str(self.data):
			# pasing on the data for conversion in the conversion class
			cvert = Convert(self.master,self.data)
			data = cvert.convert()
			
			# if the retrun value is 0 simples means
			# that the program completed successfully
			# else we raise an conversion error message
			if int(data) == 0:
				messagebox.showinfo(parent=self.master,title='Conversion',message='Conversion complete.')
			else:
				messagebox.showerror(parent=self.master,title='Conversion Error',message='Conversion error.')
		
		elif '-w -F' in str(self.data):
			# pasing on the data for conversion in the conversion class
			cvert = Convert(self.master,self.data)
			data = cvert.convert()
			
			# if the retrun value is 0 simples means
			# that the program completed successfully
			# else we raise an conversion error message
			if int(data) == 0:
				messagebox.showinfo(parent=self.master,title='Conversion',message='Conversion complete.')
			else:
				messagebox.showerror(parent=self.master,title='Conversion Error',message='Conversion error.')
		
		elif '-F -i' in str(self.data):
			# pasing on the data for conversion in the conversion class
			cvert = Convert(self.master,self.data)
			data = cvert.convert()
			
			# if the retrun value is 0 simples means
			# that the program completed successfully
			# else we raise an conversion error message
			if int(data) == 0:
				messagebox.showinfo(parent=self.master,title='Conversion',message='Conversion complete.')
			else:
				messagebox.showerror(parent=self.master,title='Conversion Error',message='Conversion error.')
		
		elif '-w -i' in  str(self.data):
			# pasing on the data for conversion in the conversion class
			cvert = Convert(self.master,self.data)
			data = cvert.convert()
			
			# if the retrun value is 0 simples means
			# that the program completed successfully
			# else we raise an conversion error message
			if int(data) == 0:
				messagebox.showinfo(parent=self.master,title='Conversion',message='Conversion complete.')
			else:
				messagebox.showerror(parent=self.master,title='Conversion Error',message='Conversion error.')
		
		elif '-w' in str(self.data):
			# pasing on the data for conversion in the conversion class
			cvert = Convert(self.master,self.data)
			data = cvert.convert()
			
			# if the retrun value is 0 simples means
			# that the program completed successfully
			# else we raise an conversion error message
			if int(data) == 0:
				messagebox.showinfo(parent=self.master,title='Conversion',message='Conversion complete.')
			else:
				messagebox.showerror(parent=self.master,title='Conversion Error',message='Conversion error.')
		
		elif '-F' in str(self.data):
			# pasing on the data for conversion in the conversion class
			cvert = Convert(self.master,self.data)
			data = cvert.convert()
			
			# if the retrun value is 0 simples means
			# that the program completed successfully
			# else we raise an conversion error message
			if int(data) == 0:
				messagebox.showinfo(parent=self.master,title='Conversion',message='Conversion complete.')
			else:
				messagebox.showerror(parent=self.master,title='Conversion Error',message='Conversion error.')
		
		else:
			pass