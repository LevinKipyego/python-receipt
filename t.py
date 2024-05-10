import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.geometry('800x500')

def get_data():
    item = lable1_entry.get()
    quantity = lable2_entry.get()
    checkb = check_var.get()
    if checkb == "Accepted":
        #print(f"{item} : {quantity} : {checkb}")
        #print("..........................................")
        messagebox.showinfo('Succes','Your Data have Been Succesfuly Submitted')
    else:
        #print("error")
        messagebox.showwarning('Terms and Conditions',' You Must Agree To The Terms and Conditions ')

lable1 = tk.Label(window,text="Item:",font=('Helvetica',14),fg='blue')
lable1.grid()

lable1_entry = tk.Entry(window,fg='green')
lable1_entry.grid(row=0,column=1,padx=5,pady=10)

lable2 = tk.Label(window,text="quantity",font=20,fg='blue')
lable2.grid()

lable2_entry = tk.Entry(window)
lable2_entry.grid(row=1,column=1,padx=5,pady=10)

#CHECK Box#
check_var = tk.StringVar(value="not accepted")
check = tk.Checkbutton(window,variable=check_var,onvalue="Accepted",offvalue="Not Accepted")
check.grid(row=2,column=1)
check_entry = tk.Label(window,text="accept Terms")
check_entry.grid(row=2,column=2)

b = tk.Button(window, text="submit", bg='lightgreen',command=get_data)
b.grid(row=2,column=0,padx=5,pady=10)



window.mainloop()