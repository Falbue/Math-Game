from tkinter import *

def changeBut(event, but):
	but.grid_forget()

root = Tk()

for i in range(10):
	for j in range(10):
		but = Button(root, borderwidth = 2)
		but["text"] = str(i) + "_" + str(j)
		but.bind("<Button-1>", lambda event, but=but: changeBut(event,but))
		but.grid(row = i, column = j)

root.mainloop()