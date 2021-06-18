from sys import path_importer_cache
from config import api_id, api_hash, number
from telegram.client import Telegram
from tkinter import *
from tkinter import filedialog


class Check:

    def __init__(self):

        self.tg = Telegram(
            api_id=api_id,
            api_hash=api_hash,
            phone=number,
            database_encryption_key='changeme1234',
        )
        self.tg.login()

    def pick(self, num):

        r = self.tg.call_method('importContacts', {'contacts': [{'phone_number': num}]})
        r.wait()
        user_id = r.update['user_ids']

        if user_id[0] == 0:
            print('This contact is NOT using Telegram.')
        else:
            print(f'¡This contact({user_id[0]}) uses Telegram!')


class Window:

    def __init__(self):
        root = Tk()
        root.geometry('800x300')
        root.resizable(False, False)
        root.title('Checker')
        # root.iconbitmap('icon.ico')

        l1 = Label(text='Numbers', font=7)
        l1.place(relx=0.2, rely=0.01)
        lbox1 = Listbox(selectmode=EXTENDED, font=7)
        lbox1.place(relx=0, rely=0.09, relwidth=0.5, relheight=0.6)
        e1 = Entry()
        e1.place(relx=0, rely=.73, relwidth=.5, relheight=.1)
        b1 = Button(text='Add')
        b1.place(relx=.0, rely=.85, relwidth=.23, relheight=.1)
        b12 = Button(text='Check')
        b12.place(relx=.25, rely=.85, relwidth=.25, relheight=.1)
        b2 = Button(text='Add file', command=self.file)
        b2.place(relx=.75, rely=.5, relwidth=.25, relheight=.1)

        l2 = Label(text='', font=10)
        l2.place()

        root.mainloop()
    
    def file(self):
        filename = filedialog.askopenfilename(initialdir = '/')


window = Window()