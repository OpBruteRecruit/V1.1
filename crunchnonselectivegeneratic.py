#import data (Tkinter)
from Tkinter import *
#main
root = Tk()
#gui configration (weith, hight, title, enz)
app = Frame(root)
app.grid()
root.title("wordlist line gen. non selective non generatic ")
root.geometry("320x260")


#firts label
label1 = Label(root, text="minimal lengt passwords")
label1.grid(row = 0, column =0)


#input %s
svalue = StringVar() 
w = Entry(root,textvariable=svalue)
w.grid(row = 1, column = 0)

#second label
label2 = Label(root, text="maximal lengt passwords")
label2.grid(row = 2, column = 0)

#input %r
rvalue = StringVar() 
v = Entry(root,textvariable=rvalue)
v.grid(row = 3, column = 0)

#tirth label
label3 = Label(root, text="all carracters that wil be generated")
label3.grid(row = 4, column = 0)

#input %sr
srvalue = StringVar() 
x = Entry(root,textvariable=srvalue)
x.grid(row = 5, column = 0)

#fifth label
label5 = Label(root, text="  copy line below (FULL LINE) to other terminal ")
label5.grid(row = 8, column = 0)

#sixth label
label6 = Label(root, text = "  use control+c to copy & right klik, paste, to paste")
label6.grid(row = 9, column = 0)
#output
Text = Text(root,width = 25, height = 1, wrap = NONE)
Text.grid(row = 10, column = 0, columnspan = 2)




def hardprintfirst():
	#all inputs to variables
	input1 = "crunch %s "   %svalue.get()
	input2 = "%s"   %rvalue.get()
	input3 = "%s"   %srvalue.get()

	#all preconfiguered carracters
	OUTPUT = (input1) + (input2) + " " +(input3)
	Text.delete(0.0,END)
	Text.insert(0.0,OUTPUT)

#button
try:
 img1 = PhotoImage(file="/pic/anonops.png")
 img1COMPRSD = img1.subsample(21,21)
 hardprintbutton2 = Button(root,text="generate wordlist line",command=hardprintfirst)
 hardprintbutton2.grid()
 hardprintbutton2.config(image=bulletimgCOMPRSD,compound=RIGHT)
except:
 hardprintbutton2 = Button(root,text="generate wordlist line",command=hardprintfirst)
 hardprintbutton2.grid()








root.mainloop()
