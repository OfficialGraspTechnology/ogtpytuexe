#! python3
#@author: Jaedan Willis

import os
import sys
import shutil
import argparse
import subprocess
from tkinter import *
from file import File
from icon import Icon
from ain1 import Ain1
from merge import Merge
from tkinter import ttk
from hidden import Hidden
from inicon import Inicon
from inmerge import Inmerge
from regcheck import RegCheck
from tkinter import filedialog
from tkinter import messagebox
from mergeicon import MergeIcon

class Layout(object):
	""""this class will convert/compile
	any .py/.pyw script to an executable
	and also allows the user to select three(3)
	different options"""

	def __init__(self, master):
		# initalize function
		self.master = master
		self.master.update_idletasks()
		width = 362
		height =260
		x = (self.master.winfo_screenwidth() // 2) - (width // 2)
		y = (self.master.winfo_screenheight() // 2) - (height // 2)
		self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
		self.master.deiconify()
		self.master.resizable(False,False)
		self.master.iconbitmap('assets\\icon\\HPControl.ico')
		self.master.title('OGT PyTuExe (v1.1.0)')

		# claasing a class to check to see if the user already see the important message,if not go to the important_note function
		RegCheck(self.master)

		#styling the gui
		self.red_black = '#321d1d'
		self.tint_red = '#ff3232'
		self.master.configure(background=self.red_black)
		self.style = ttk.Style()
		self.style.configure('TFrame',background=self.red_black)
		self.style.configure('TButton',background=self.red_black)
		self.style.configure('Convert.TButton',foreground=self.tint_red)
		self.style.configure('Browse.TButton',foreground=self.tint_red)
		self.style.configure('TLabel',foreground='white',background=self.red_black,font=('Arial',11,'italic'))
		self.style.configure('TCheckbutton',background=self.red_black,foreground='white')
		self.style.configure('Header.TLabel',foreground=self.tint_red,font=('san-serif',40,'bold','italic'))

		# header frame
		self.header_frame = ttk.Frame(self.master)
		self.header_frame.pack(fill=X,padx=2,pady=2)
		self.header_frame.config(padding=((1,0)),relief=RAISED)

		# header lable
		self.header_label = ttk.Label(self.header_frame,text='OGT PyTuExe',style='Header.TLabel')
		self.header_label.grid(row=0,column=0,pady=5,sticky='sw')

		# pytoexe frame
		self.pytoexe_frame = ttk.Frame(self.master)
		self.pytoexe_frame.pack(fill=X,padx=2)
		#self.pytoexe_frame.config(relief=GROOVE)

		# getfilename settings
		self.pytoexe_lable = ttk.Label(self.pytoexe_frame,text='Filename:')
		self.pytoexe_lable.grid(row=0,column=0,pady=5,padx=5,stick='w')

		self.entry_var = StringVar()
		self.pytoexe_list_entry = Entry(self.pytoexe_frame,width=30,textvariable=self.entry_var)
		self.pytoexe_list_entry.grid(row=1,column=1,sticky='sw',pady=5)
		self.pytoexe_list_entry.insert(0,"Your Script Goes Here")

		# browse button
		self.file_browse_button = ttk.Button(self.pytoexe_frame,text='Browse',command=self.file_browse,style='Browse.TButton')
		self.file_browse_button.grid(row=1,column=2,padx=5)

		# icon settings
		self.icon_lable = ttk.Label(self.pytoexe_frame,text='Icon File:')
		self.icon_lable.grid(row=3,column=0,sticky='w',pady=5,padx=5)

		self.icon = StringVar()
		self.icon_entry = ttk.Entry(self.pytoexe_frame,width=30,textvariable=self.icon)
		self.icon_entry.grid(row=4,column=1,sticky='sw',pady=5)
		self.icon_entry.insert(0,"Your Icon Goes Here")

		self.icon_browse_button = ttk.Button(self.pytoexe_frame,text='Browse',command=self.icon_browse,style='Browse.TButton')
		self.icon_browse_button.grid(row=4,column=2,padx=5)

		# invisable checkbox
		self.invisbale_button = IntVar()
		self.invisible_checkbox = ttk.Checkbutton(self.pytoexe_frame,text='Invisable',variable=self.invisbale_button)
		self.invisible_checkbox.grid(row=6,column=0,padx=5)

		# merge checkbox
		self.merge_button = IntVar()
		self.merge_checkbox = ttk.Checkbutton(self.pytoexe_frame,text='Merge',variable=self.merge_button)
		self.merge_checkbox.grid(row=6,column=1)
		self.merge_button.set(1)

		# con checkbox
		self.icon_button = IntVar()
		self.icon_checkbox = ttk.Checkbutton(self.pytoexe_frame,text='Icon',variable=self.icon_button)
		self.icon_checkbox.grid(row=6,column=2)

		# convert button
		self.convert_button = ttk.Button(self.pytoexe_frame,text='CONVERT',command=self.verify_fileds,style='Convert.TButton')
		self.convert_button.grid(row=7,column=1,pady=5)

	def file_browse(self):
		# this funtion allows you to browse for an .py or .pyw file
		file = File.browse(self.master)
		self.pytoexe_list_entry.delete(0,'end')
		self.pytoexe_list_entry.insert(0,file)


	def icon_browse(self):
		icon = Icon.browse(self.master)
		self.icon_entry.delete(0,'end')
		self.icon_entry.insert(0,icon)

	def verify_fileds(self):
		# this funtion will check to
		# see if the fields or check
		# or not if not raise an erro message

		invisbale_button = self.invisbale_button.get()
		merge_button = self.merge_button.get()
		icon_button = self.icon_button.get()
		filename = self.entry_var.get()
		icon = self.icon.get()
		if filename.endswith(('.py','.pyw')):
			if invisbale_button == True and merge_button == True and icon_button == True:
				if icon.endswith('.ico'):
					# Calling the ain1 class
					a1 = Ain1(self.master,filename,icon)
					a1.merge()
				else:
					messagebox.showerror(parent=self.master,title='Icon Error',message="Icon file should end with a (.ico) extension")
			elif invisbale_button == 1 and merge_button == 1:
				# callign the inmerge class
				inmerge = Inmerge(self.master,filename)
				inmerge.merge()
			elif invisbale_button == True and icon_button == True:
				if icon.endswith('.ico'):
					#calling the inicon class
					inicon = Inicon(self.master,filename,icon)
					inicon.merge()
				else:
					messagebox.showerror(parent=self.master,title='Icon Error',message="Icon file should end with a (.ico) extension")
			elif merge_button == True and icon_button ==  True:
				if icon.endswith('.ico'):
					#calling the mergeicon class
					mergeicon = MergeIcon(self.master,filename,icon)
					mergeicon.merge()
				else:
					messagebox.showerror(parent=self.master,title='Icon Error',message="Icon file should end with a (.ico) extension")
			elif invisbale_button == True:
				#calling the hidden class
				hidden = Hidden(self.master,filename)
				hidden.merge()
			elif merge_button == True:
				#calling the merge class
				merge = Merge(self.master,filename)
				merge.merge()
			elif icon_button == True:
				messagebox.showerror(parent=self.master,title='Icon Error',message="Icon cannot be merged alone")
			else:
				messagebox.showerror(parent=self.master,title='Invalid Error',message="Please atleast select merge")
		else:
			messagebox.showerror(parent=self.master,title='Filename Error',message="File shoud end with a (.py or .pyw) extention.")

# main part of the program
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-bs','--bootstate',help='Start the program if started from another file')
	args = parser.parse_args()
	if args.bootstate == "8WFEHBN9EFM0EJF!M?SWE0NMSVO*9WEHFWEF9EWMF*0E#WSJD0FEWF0VSD9EWFMWEDMV-EWIFVSFEW-F9UEWVMWE-FWE":
		gui = Tk()
		pytoexe = Layout(gui)
		gui.mainloop()
	else:
		os._exit(1)
if __name__ == '__main__':
	main()
