from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

a = Tk()
a.title("Game")
a.minsize(height = 400, width = 400)


img_stone = ImageTk.PhotoImage(Image.open("resizedstone.png"))
img_paper = ImageTk.PhotoImage(Image.open("resizedpaper.jpg"))
img_scissor = ImageTk.PhotoImage(Image.open("resizedscissor.jpg"))
img = ImageTk.PhotoImage(Image.open("resizedrps.png"))
l1 = Label(a , text = "WELCOME TO\nRock, Paper,Scissor", relief = RAISED, font = ("Sans-serif",20), fg = "red", bg = "light green", bd = 10)
l1.pack()
l4 = Label(a, image = img)
l4.pack()
def comp():
	global ab
	lis =["stone", "paper" , "scissor"]
	import random
	ab = random.choice(lis)
	
def start():
	l1.destroy()
	b1.destroy()
	l4.destroy()
	l2 = Label(a,text = "Pick your choice", relief = SUNKEN, font = ("Ariel Font",15), bg = "orange",fg = "blue", bd = 10)
	l2.grid(row = 0, column = 2)
	l3 = Label(a,text = "————>")
	l3.grid(row = 2, column = 3)

	def stone():
		comp()
		l5 = Label(a,text = "Opponent is:", relief = RIDGE, fg = "blue", font = ("Ariel Font",15))
		l5.grid(row = 1, column = 4)
		if ab == "stone":
			l3 = Label(a , image = img_stone)
			l3.grid(row = 2 , column = 4)
			msg = messagebox.showinfo("Opponent is stone","it's a tie")
			l3.destroy()
		elif ab == "paper":
			l3 = Label(a , image = img_paper)
			l3.grid(row = 2 , column = 4)
			msg = messagebox.showinfo("Opponent is paper","you loose")
			l3.destroy()
		elif ab == "scissor":
			l3 = Label(a , image = img_scissor)
			l3.grid(row = 2 , column = 4)
			msg = messagebox.showinfo("Opponent is scissor","you win")
			l3.destroy()
	b2 = Button(a , image = img_stone , command = stone)
	b2.grid(row = 1 , column = 2)
	def paper():
		comp()
		l5 = Label(a,text = "Opponent is:", relief = RIDGE, fg = "blue", font = ("Ariel Font",15))
		l5.grid(row = 1, column = 4)
		if ab == "stone":
			l3 = Label(a , image = img_stone)
			l3.grid(row = 2 , column = 4)
			msg = messagebox.showinfo("Opponent is stone","you win")
			l3.destroy()
		elif ab == "paper":
			l3 = Label(a , image = img_paper)
			l3.grid(row = 2 , column = 4)
			msg = messagebox.showinfo("Opponent is paper","it's a tie")
			l3.destroy()
		elif ab == "scissor":
			l3 = Label(a , image = img_scissor)
			l3.grid(row = 2 , column = 4)
			msg = messagebox.showinfo("Opponent is scissor","you loose")
			l3.destroy()
	b3 = Button(a, image = img_paper, command = paper)
	b3.grid(row = 2, column = 2)
	def scissor():
		comp()
		l5 = Label(a,text = "Opponent is:", relief = RIDGE, fg = "blue", font = ("Ariel Font",15))
		l5.grid(row = 1, column = 4)
		if ab == "stone":
			l3 = Label(a , image = img_stone)
			l3.grid(row = 2 , column = 4)
			msg = messagebox.showinfo("Opponent is stone","you loose")
			l3.destroy()
		elif ab == "paper":
			l3 = Label(a , image = img_paper)
			l3.grid(row = 2 , column = 4)
			msg = messagebox.showinfo("Opponent is paper","you win")
			l3.destroy()
		elif ab == "scissor":
			l3 = Label(a , image = img_scissor)
			l3.grid(row = 2 , column = 4)
			msg = messagebox.showinfo("Opponent is scissor","it's a tie")
			l3.destroy()
	b4 = Button(a ,image = img_scissor, command = scissor)
	b4.grid(row = 3 ,column = 2)
b1 = Button( a ,text = "Start", command = start, relief = RAISED, bd = 15, fg = "blue", bg = "yellow", font = ("Ariel Font", 15))
b1.pack()


a.mainloop()