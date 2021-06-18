from os import read
from tkinter import *
from tkinter import filedialog

file = filedialog.askopenfilename(title = "Select a File")

f = open(file, 'r')
for i in f:
	print(i)