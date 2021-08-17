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
        result = ''

        r = self.tg.call_method('importContacts', {'contacts': [{'phone_number': num}]})
        r.wait()
        user_id = r.update['user_ids']

        if user_id[0] == 0:
            print(f'This contact ({num})is NOT using Telegram.')
            result = None
        else:
            print(f'¡This contact({num}) uses Telegram!')
            result = num

        return


class Window:

    def __init__(self):
        root = Tk()
        root.geometry('800x300')
        root.resizable(False, False)
        root.title('Checker')
        self.path = ''
        self.nums = []
        # root.iconbitmap('icon.ico')

        l1 = Label(text='Numbers', font=7)
        l1.place(relx=0.2, rely=0.01)
        self.entry1 = Entry()
        self.entry1.place(relx=0, rely=.73, relwidth=.5, relheight=.1)
        self.lbox1 = Listbox(selectmode=EXTENDED, font=7)
        self.lbox1.place(relx=0, rely=0.09, relwidth=0.5, relheight=0.6)
        b1 = Button(text='Add', command=self.add_num)
        b1.place(relx=.0, rely=.85, relwidth=.23, relheight=.1)
        b12 = Button(text='Check', command=self.check)
        b12.place(relx=.25, rely=.85, relwidth=.25, relheight=.1)
        b2 = Button(text='Add file', command=self.file)
        b2.place(relx=.75, rely=.5, relwidth=.25, relheight=.1)
        b3 = Button()
        b3.place()

        l2 = Label(text='', font=10)
        l2.place()

        root.mainloop()
    
    def file(self):
        self.path = filedialog.askopenfilename(initialdir = '/')
        
        i = Check()
        for b in open(self.path):
            i.pick(b)

    def add_num(self):
        num = self.entry1.get()
        self.lbox1.insert(END, str(num))
        self.entry1.delete(0, END)
        self.nums.append(str(num))

    def check(self):
        self.lbox1.delete(END)
        self.entry1.delete(0, END)

        i = Check()
        for b in self.nums:
            i.pick(b)

        self.nums.clear()

    def save(self, extension):
        pass


window = Window()