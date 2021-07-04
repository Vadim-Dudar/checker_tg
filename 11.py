from os import read
from tkinter import *
from tkinter import filedialog



root = Tk()
root.geometry('300x300')

entry = Entry()
entry.place(relx=.3, rely=.3)

def main():
	print(str(entry.get()))

button = Button(command=main)
button.place(rely=.6, relx=.3)

root.mainloop()