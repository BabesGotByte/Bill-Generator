from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import time

win1 = Tk()

w=Scale(win1, from_=0, to=5, orient=VERTICAL)
w.grid(row=2,column=2)

#=================================List1 functions=================================
def open1():
    open2=filedialog.askopenfile()
    open3=open2.name
    open4=open(open3)
    label4 = Label(text=open4.read())
    label4.grid(row=0)
def save1():
    save2 = messagebox.askyesno(title="Save file",message="Do you want to save the file")
def delete1():
    messagebox.askyesno(title="Delete file",message="Are you sure to delete the file")
def quit1():
    quit2 = messagebox.askyesno(title="Quit",message="Do you want to quit")
    if quit2 == 1:
        win1.destroy()
#==================================Button functions================================
def button1a():
    entry1a=float(entryv1.get())
    entry2a=float(entryv2.get())
    entry3a=float(entryv3.get())
    entry4a=float(entryv4.get())
    entry5a=float(entryv5.get())

    entry1b=entry1a*10
    entry2b=entry2a*20
    entry3b=entry3a*30
    entry4b=entry4a*40
    entry5b=entry5a*50

    meal_cost=entry1b + entry2b + entry3b + entry4b + entry5b
    gst_tax=meal_cost*0.05
    ser_tax=meal_cost*2.5
    tip=100
    total=meal_cost +gst_tax +ser_tax+tip
    entryv6.set(meal_cost)
    entryv7.set(gst_tax)
    entryv8.set(ser_tax)
    entryv9.set(tip)
    entryv10.set(total)

def button2a():
    entryv1.set(0)
    entryv2.set(0)
    entryv3.set(0)
    entryv4.set(0)
    entryv5.set(0)
    entryv6.set("")
    entryv7.set("")
    entryv8.set("")
    entryv9.set("")
    entryv10.set("")

def button3a():
        win1.destroy()
#=================================Radio button functions==========================    
def radio1():
    a=v.get()
    if(a==1):
        Label(text="You choose CASH mode",font=('arial',15)).grid(row=0)
    elif(a==2):
        Label(text="You choose DEBIT CARD mode",font=('arial',15)).grid(row=0)
    elif(a==3):
        Label(text="You choose ONLINE PAYMENT mode",font=('arial',15)).grid(row=0)
    elif(a==4):
        Label(text="You choose PAYTM mode",font=('arial',15)).grid(row=0)
    elif(a==5):
        Label(text="You choose TEZ mode",font=('arial',15)).grid(row=0)
#==================================Heading=========================================
label1 = Label(text="XYZ Hotel",fg="black",font=('arial',40,'bold'))
label1.grid(row=0,column=5)
label2 = Label(text="Thanks for visiting",fg="black",font=('arial',25,'bold'))
label2.grid(row=1,column=5)
#==================================Time============================================
time1 = time.asctime(time.localtime(time.time()))
label3 = Label(text=time1,font=('arial',20,'bold'))
label3.grid(row=2,column=5)
#================================Radio button======================================
v=IntVar()
v.set(1)
Label(win1,text="Choose your payment mode",anchor=W).grid(row=3)
Radiobutton(win1,text="Cash",padx=25,indicatoron=0,width=15,variable=v,value=1,command=radio1).grid(row=4)
Radiobutton(win1,text="Debit card",padx=25,indicatoron=0,width=15,variable=v,value=2,command=radio1).grid(row=5)
Radiobutton(win1,text="Online banking",padx=25,indicatoron=0,width=15,variable=v,value=3,command=radio1).grid(row=6)
Radiobutton(win1,text="Paytm",padx=25,indicatoron=0,width=15,variable=v,value=4,command=radio1).grid(row=7)
Radiobutton(win1,text="Tez",padx=25,indicatoron=0,width=15,variable=v,value=5,command=radio1).grid(row=8)


win1.title("Restaraunt Bill")
win1.geometry("5000x5000+0+0")
#==================================Menubar=========================================
menulist1 = Menu()

list1 = Menu()
list1.add_command(label="New File")
list1.add_command(label="Open",command=open1)
list1.add_command(label="Print")
list1.add_command(label="Save",command=save1)
list1.add_command(label="Delete",command=delete1)
list1.add_command(label="Quit",command=quit1)

list2 = Menu()
list2.add_command(label="Contact details")
list2.add_command(label="Staff")

list3 = Menu()
list3.add_command(label="Dishes")
list3.add_command(label="Price list")
list3.add_command(label="Crocery list")

menulist1.add_cascade(label="File",menu=list1)
menulist1.add_cascade(label="About us",menu=list2)
menulist1.add_cascade(label="Hotel Menu",menu=list3)
#=================================Entry list 1======================================

label6=Label(font=('arial',16,'bold'),text="Burger").grid(row=10,column=2)
label7=Label(font=('arial',16,'bold'),text="Pizza").grid(row=11,column=2)
label8=Label(font=('arial',16,'bold'),text="Chicken").grid(row=12,column=2)
label9=Label(font=('arial',16,'bold'),text="Ice cream").grid(row=13,column=2)
label10=Label(font=('arial',16,'bold'),text="Cold drink").grid(row=14,column=2)

entryv1=StringVar()
entryv2=StringVar()
entryv3=StringVar()
entryv4=StringVar()
entryv5=StringVar()
entryv1.set(0)
entryv2.set(0)
entryv3.set(0)
entryv4.set(0)
entryv5.set(0)
entry1 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv1,width=20).grid(row=10,column=3)
entry2 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv2,width=20).grid(row=11,column=3)
entry3 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv3,width=20).grid(row=12,column=3)
entry4 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv4,width=20).grid(row=13,column=3)
entry5 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv5,width=20).grid(row=14,column=3)

#=================================Entry list 2==========================================
label11=Label(font=('arial',16,'bold'),text="Meal cost",anchor=W).grid(row=10,column=5)
label12=Label(font=('arial',16,'bold'),text="GST",anchor=W).grid(row=11,column=5)
label13=Label(font=('arial',16,'bold'),text="Service tax",anchor=W).grid(row=12,column=5)
label14=Label(font=('arial',16,'bold'),text="Tip",anchor=W).grid(row=13,column=5)
label15=Label(font=('arial',16,'bold'),text="Total price",anchor=W).grid(row=14,column=5)
label16=Label(font=('arial',16,'bold'),text="COSTUMER NAME",anchor=W).grid(row=16,column=1)


entryv6=StringVar()
entryv7=StringVar()
entryv8=StringVar()
entryv9=StringVar()
entryv10=StringVar()
entryv11=StringVar()
entry6 =Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv6,width=20).grid(row=10,column=6)
entry7 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv7,width=20).grid(row=11,column=6)
entry8 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv8,width=20).grid(row=12,column=6)
entry9 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv9,width=20).grid(row=13,column=6)
entry10 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv10,width=20).grid(row=14,column=6)
entry11 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv11,width=20).grid(row=16,column=2)
#=================================Buttons===============================================
button1 = Button(font=('arial',16,'bold'),text="Total",bd=6,width=15,command=button1a).grid(row=15,column=3)
button2 = Button(font=('arial',16,'bold'),text="Reset",bd=6,width=15,command=button2a).grid(row=15,column=5)
button3 = Button(font=('arial',16,'bold'),text="Quit",bd=6,width=15,command=button3a).grid(row=15,column=6)



win1.config(menu=menulist1)
win1.mainloop()


















