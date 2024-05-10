from tkinter import *
import os
import tempfile
from tkinter import scrolledtext as st
root = Tk()
root.geometry('800x550')
def print_bill(doc):
    print_itm=tempfile.mktemp('.doc')
    open(print_itm, 'w').write(doc)
    os.startfile(print_itm, 'print')

#txtA=st.ScrolledText(root,width=50,height=20)
#txtA.place(x=50,y=50)

#prnt_buttn=Button(root,text='print', command = lambda:print_bill(txtA.get('1.0',END)))
prnt_buttn=Button(root,text='print', command = lambda:print_bill("qr_doc.doc"))
prnt_buttn.place(x=200,y=390)
root.mainloop()