from tkinter import *
from tkinter import messagebox
import pyttsx3

engine = pyttsx3.init()
b = Tk()
b.title("LOGIN")
engine.say('Hello sir, Please log in')
engine.runAndWait()
l1 = Label(b, text="Email I-D").grid(row=0, column=0)
e1 = Entry(b).grid(row=0, column=1)
l2 = Label(b, text="Password").grid(row=1, column=0)
e2 = Entry(b, show="*").grid(row=1, column=1)


def submit():
    b.destroy()
    engine.say('You are successfully logged in.')
    engine.runAndWait()


Button(b, text="SUBMIT", command=submit).grid(row=2, column=1)
b.mainloop()

a = Tk()
a.title("HOTEL MENU")
l1 = Label(a, text="Name").grid(row=0, column=0)
e1 = Entry(a).grid(row=0, column=1)
l2 = Label(a, text="Phone No").grid(row=1, column=0)
e2 = Entry(a).grid(row=1, column=1)
t = Label(a, text="\n DAL")
t.grid(row=2, column=0)
t = Label(a, text="\n RICE ")
t.grid(row=3, column=0)
t = Label(a, text="\n ROTI")
t.grid(row=4, column=0)
t = Label(a, text="\n SABJI")
t.grid(row=5, column=0)
t = Label(a, text="\n Rs.80/-")
t.grid(row=2, column=1)
t = Label(a, text="\n Rs.50/- ")
t.grid(row=3, column=1)
t = Label(a, text="\n Rs.7/- ")
t.grid(row=4, column=1)
t = Label(a, text="\n Rs.70/- ")
t.grid(row=5, column=1)
t = Label(a, text="\n LIST OF ITEMS")
t.grid(row=6, column=0)
t = Label(a, text="\n PRICE IN RS. ")
t.grid(row=6, column=1)
t = Label(a, text="\n TOTAL ")
t.grid(row=6, column=2)


def dal1x():
    pr = "dal x1"
    rs = 80
    L1.insert(END, rs)
    L.insert(END, pr)
    list1.append(rs)
    engine.say('Selected 1 Dal')
    engine.runAndWait()


b1 = Button(a, text="x1", command=dal1x).grid(row=2, column=3)


def dal2x():
    pr = "dal x2"
    rs = 160
    L1.insert(END, rs)
    L.insert(END, pr)
    list1.append(rs)
    engine.say('Selected 2 Dals')
    engine.runAndWait()

b2 = Button(a, text="x2", command=dal2x).grid(row=2, column=4)


def dal3x():
    pr = "dal x3"
    rs = 240
    L1.insert(END, rs)
    L.insert(END, pr)
    list1.append(rs)
    engine.say('Selected 3 Dals')
    engine.runAndWait()

b3 = Button(a, text="x3", command=dal3x).grid(row=2, column=5)


def rice1x():
    pr = "rice x1"
    rs = 50
    L1.insert(END, rs)
    L.insert(END, pr)
    list1.append(rs)
    engine.say('Selected 1 Rice')
    engine.runAndWait()

b4 = Button(a, text="x1", command=rice1x).grid(row=3, column=3)


def rice2x():
    pr = "rice x2"
    rs = 100
    L1.insert(END, rs)
    L.insert(END, pr)
    list1.append(rs)
    engine.say('Selected 2 Rice')
    engine.runAndWait()

b5 = Button(a, text="x2", command=rice2x).grid(row=3, column=4)


def rice3x():
    pr = "rice x3"
    rs = 150
    L1.insert(END, rs)
    L.insert(END, pr)
    list1.append(rs)
    engine.say('Selected 3 Rice')
    engine.runAndWait()

b6 = Button(a, text="x3", command=rice3x).grid(row=3, column=5)


def roti1x():
    pr = "roti x1"
    rs = 7
    L1.insert(END, rs)
    L.insert(END, pr)
    list1.append(rs)
    engine.say('Selected 1 Roti')
    engine.runAndWait()

b7 = Button(a, text="x1", command=roti1x).grid(row=4, column=3)


def roti2x():
    pr = "roti x2"
    rs = 14
    L1.insert(END, rs)
    L.insert(END, pr)
    list1.append(rs)
    engine.say('Selected 2 Rotis')
    engine.runAndWait()

b8 = Button(a, text="x2", command=roti2x).grid(row=4, column=4)


def roti3x():
    pr = "roti x3"
    rs = 21
    L1.insert(END, rs)
    L.insert(END, pr)
    list1.append(rs)
    engine.say('Selected 3 Rotis')
    engine.runAndWait()

b9 = Button(a, text="x3", command=roti3x).grid(row=4, column=5)


def sabji1x():
    pr = "sabji x1"
    rs = 70
    L1.insert(END, rs)
    L.insert(END, pr)
    list1.append(rs)
    engine.say('Selected 1 Sabji')
    engine.runAndWait()

b10 = Button(a, text="x1", command=sabji1x).grid(row=5, column=3)


def sabji2x():
    pr = "sabji x2"
    rs = 140
    L1.insert(END, rs)
    L.insert(END, pr)
    list1.append(rs)
    engine.say('Selected 2 Sabjis')
    engine.runAndWait()

b11 = Button(a, text="x2", command=sabji2x).grid(row=5, column=4)


def sabji3x():
    pr = "sabji x3"
    rs = 210
    L1.insert(END, rs)
    L.insert(END, pr)
    list1.append(rs)
    engine.say('Selected 3 Sabjis')
    engine.runAndWait()

b12 = Button(a, text="x3", command=sabji3x).grid(row=5, column=5)
list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def sum1():
    sum1 = sum(list1)
    L2.insert(END, sum1)
    engine.say('Your total amount is')
    engine.say(sum1)
    engine.runAndWait()

b13 = Button(a, text="SUM", command=sum1).grid(row=7, column=3)


def bill():
    engine.say('Are you sure you want to exit?')
    engine.runAndWait()
    msg = messagebox.askquestion("Confirm", "Are you sure you want to exit?")
    if msg == 'no':
        engine.say('Selected No')
        engine.say('Process terminated')
        engine.runAndWait()
        top = Tk()
        # Label(top,text="THANK YOU FOR VISITING SEE YOU SOON!!").grid(row=0,column=0,rowspan=2,columnspan=3)
        # B=Button(top,text="GO BACK",command=t).grid(row=2,column=1)
        top.destroy()
        top.mainloop()

    else:
        a.destroy()
        engine.say('Application closed')
        engine.runAndWait()


b14 = Button(a, text="EXIT", command=bill).grid(row=8, column=3)

L = Listbox(a)
L.grid(row=7, column=0)
L1 = Listbox(a)
L1.grid(row=7, column=1)
L2 = Listbox(a)
L2.grid(row=7, column=2)
a.mainloop()
