#!python3

import os
import sys
import subprocess
from tkinter import messagebox

class RegCheck(object):
	def __init__(self,master):
		self.master = master

		sub = subprocess.Popen('reg query "HKEY_CURRENT_USER\Software\PyTuExe" /v "Verify"',shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
		subdata = sub.stdout.read() + sub.stderr.read()
		if 'The system was unable to find the specified registry key or value' in str(subdata):
			self.important_note()
		else:
			pass

	def important_note(self):
		# message to the user for the requirements
		choice = messagebox.askyesno(parent=self.master,title='Requirements',message='Note: This program wont run if you dont\nhave pyinstaller installed.The version of python\nthat is recommended is python3x. If\nyou already have python3x installed and want\nto install pyinstaller click the yes button else click no.')
		if choice:
			choice = messagebox.askyesno(parent=self.master,title='Requirements',message='Note: This program will install the newest version\nof pyinstaller in your (C:\Python(version)\Lib\site-packages)\ndirectory where python should be installed.If the path is\nnot found you will receive an (Path Not Found Error).\nShould i continue?.')
			if choice:
				messagebox.showinfo(parent=self.master,title='Please Wait',message='Don\'t panic.We will notiy you when your installation is completed.' )
				sub = subprocess.call(['pip','install','pyinstaller'])
				if int(sub) == 0:
					os.system('reg add "HKEY_CURRENT_USER\Software\PyTuExe" /v "Verify" /t REG_DWORD /d 1 /f')
					messagebox.showinfo(parent=self.master,title='Installed',message='PyInstaller sucessfully installed')
				else:
					messagebox.showerror(parent=self.master,title='Path Not Found',message='C:\Python3.5.3 not found.Please reinstall python3.5.3 in your (C) directory.')
					sys.exit(1)
			else:
				sys.exit(1)
		else:
			os.system('reg add "HKEY_CURRENT_USER\Software\PyTuExe" /v "Verify" /t REG_DWORD /d 1 /f')
