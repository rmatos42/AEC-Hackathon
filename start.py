import Tkinter
from Tkinter import *
import subprocess
import sys
import os
top = Tkinter.Tk()

#def startIt():
#	root = Tk()

def myHandler():
	os.system('python rammonitor.py acad.exe')
	exit

B = Tkinter.Button(top, text="Track Autocad" , font="Helvetica 12", command=myHandler)
B.pack()
top.mainloop()
	
