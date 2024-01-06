from tkinter import *
from tkinter import messagebox

root = Tk()
root.minsize(width=500, height=500)
root.title("Calculator")
e1 = Entry(root ,bd = 8 ,width = 21)
e1.place(x = 100,y = 100)
def e():
	 e1.delete(0, last = len(e1.get()))
def i0():
	e1.insert(INSERT,"0")
def i1():
	e1.insert(INSERT, "1")
def i2():
	e1.insert(INSERT, "2")
def i3():
	e1.insert(INSERT, "3")
def i4():
	e1.insert(INSERT, "4")
def i5():
	e1.insert(INSERT, "5")
def i6():
	e1.insert(INSERT, "6")
def i7():
	e1.insert(INSERT, "7")
def i8():
	e1.insert(INSERT, "8")
def i9():
	e1.insert(INSERT, "9")
def i11():
	e1.insert(INSERT, "/")
def i12():
	e1.insert(INSERT, "+")
def i13():
	e1.insert(INSERT, "*")
def i14():
	e1.insert(INSERT, "-")
def i15():
	try:
		a = str(eval(e1.get()))
		e1.delete(0,last = len(e1.get()))
		e1.insert(INSERT, a)
	except:
		msg = messagebox.showinfo("error","enter correct operation")
def i17():
	e1.insert(INSERT,".")
b0 = Button(root,text = "0", command= i0).place(x = 200, y = 425)
b1 = Button(root, text = "C", command = e).place(x= 100, y= 165)
b2 = Button(root , text = "1", command = i1).place(x= 100, y = 230)
b3 = Button(root , text = "4", command = i4).place(x = 100, y = 295)
b4 = Button(root , text = "7", command = i7).place(x = 100, y = 360)
b5 = Button(root , text = "2", command = i2).place(x= 200, y= 230)
b6 = Button(root , text = "5", command = i5).place(x = 200, y = 295)
b7 = Button(root , text = "8", command = i8).place(x = 200, y = 360)
b8 = Button(root , text = "3", command = i3).place(x = 300,y = 230)
b9 = Button(root , text = "6", command = i6).place(x = 300, y = 295)
b10 = Button(root , text = "9", command = i9).place(x = 300, y = 360)
b11= Button(root , text = "÷", command = i11).place(x = 400, y = 165)
b12 = Button(root , text = "+", command = i12).place(x = 400, y = 230)
b13 = Button(root , text = "*", command = i13).place( x = 400, y = 295)
b14 = Button(root , text = "-", width = 1, command = i14).place(x = 400, y = 360)
b15 = Button(root , text = "=", command = i15).place(x= 400, y = 425)
b17 = Button(root ,text = ".", width = 1 , command = i17).place(x = 100, y = 425)



root.mainloop()
