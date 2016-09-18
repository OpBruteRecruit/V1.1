from Tkinter import *

root = Tk()
root.title("opbruterecruit BETA (V=1.1)")
app = Frame(root)
app.grid



LINK = "www.github.com"
DEFAULT = "python "
NEW = "cd ~"
print"[-] Do not close this terminal, or the programm will crash"

label1 = Label(root,text = "welcome to #opbruterecruit")
label1.grid(row = 1, column = 1, sticky = W)

empty1 = Label(root,text = " ")
empty1.grid(row = 2, column = 1, sticky = W)

label2= Label(root,text = "FOR UPDATES COPY & PASTE TO NEW TERMINAL: ")
label2.grid(row = 3, column = 1, sticky = W)

output1 = Text(root,width = 47, height = 1,wrap = NONE)
output1.grid(row = 4, column = 0, columnspan = 15, sticky = W)
output1.insert(0.0,LINK)

empty2 = Label(root,text = " ")
empty2.grid(row = 5, column = 1, sticky = W)

label3 = Label(root,text = "before every new app command copy & paste:")
label3.grid(row = 6, column = 1, sticky = W)

output2 = Text(root,width = 47, height = 1,wrap = NONE)
output2.grid(row = 7, column = 0, columnspan = 15, sticky = W)
output2.insert(0.0,NEW)

empty2 = Label(root,text = " ")
empty2.grid(row = 8, column = 1, sticky = W)

label3 = Label(root,text = "copy & paste to new terminal")
label3.grid(row = 9, column = 1, sticky = W)

output3 = Text(root,width = 47, height = 1,wrap = NONE)
output3.grid(row = 10, column = 0, columnspan = 15, sticky = W)

empty3 = Label(root,text = " ")
empty3.grid(row = 11, column = 1, sticky = W)


def EXIT():
 print"[-] killing main proccess"
 print"[-] quiting main programm"
 quit()


quitbutton = Button(root, text = "EXIT",command=EXIT)
quitbutton.grid(row =  12,column = 1)


def CAT():
 print"[-] Generating cat.py route"
 print"[-] NOTE: all files must be in  right directory"
 print"[-] for more help go to HELP -> APPS"
 ROUTEcat = (DEFAULT) + "/root/OpBruteRecruit/cat.py"
 output3.delete(0.0,END)
 output3.insert(0.0,ROUTEcat)

def CRUNCHnonselectivenongeneratic():
 print"[-] Generating crunchnonselnongen.py route"
 print"[-] NOTE: all files must be in  right directory"
 print"[-] for more help go to HELP -> APPS"
 ROUTEcrunchnonselectivenongeneratic = (DEFAULT) + "/root/OpBruteRecruit/crunchnonselectivenongeneratic.py"
 output3.delete(0.0,END)
 output3.insert(0.0,ROUTEcrunchnonselectivenongeneratic)


def CRUNCHnonselectivegeneratic():
 print"[-] Generating crunchnonselgen.py route"
 print"[-] NOTE: all files must be in  right directory"
 print"[-] for more help go to HELP -> APPS"
 ROUTEcrunchnonselectivegeneratic = (DEFAULT) + "/root/OpBruteRecruit/crunchnonselectivegeneratic.py"
 output3.delete(0.0,END)
 output3.insert(0.0,ROUTEcrunchnonselectivegeneratic)


'''
helpmenu commands
'''

def HELPterminal():
 roothelpterminal = Tk()
 roothelpterminal.title("HELP/terminal")
 apphelpterminal = Frame(roothelpterminal)
 apphelpterminal.grid

 print"[-] starting HELP/terminal"

 labelhelpterminal1 = Label(roothelpterminal,text = "for new terminal press:\n \nRIGHT mouse -> Open Terminal")
 labelhelpterminal1.grid(row = 1, column = 1, sticky = W)
 
 apphelpterminal.mainloop()
 
def HELPcopypaste():
 roothelpcopypaste = Tk()
 roothelpcopypaste.title("HELP/Copy & Paste")

 apphelpcopypaste = Frame(roothelpcopypaste)
 apphelpcopypaste.grid

 print"[-] starting HELP/copy&paste"

 labelhelpcopypaste1 = Label(roothelpcopypaste,text = "to copy & paste go's a bit difrent than usual\nto copy you have to make the whole line light grey and then use:\n \n CNTRL + C\n \n to paste you have to press:\n \n RIGHT MOUSE -> PASTE\n \n Note: this is ONLY the way for the #opbruterecruit programs")
 labelhelpcopypaste1.grid(row = 1, column = 1, sticky = W)
 
 roothelpcopypaste.mainloop()  
 
 



mainmenu = Menu(root)
root.config(menu=mainmenu)

submenu = Menu(mainmenu)
helpmenu = Menu(mainmenu)

mainmenu.add_cascade(label="apps",menu = submenu)
mainmenu.add_cascade(label="help",menu = helpmenu)

submenu.add_command(label = "cat (create files)",command=CAT)

submenu.add_separator()

submenu.add_command(label = "Crunch(non sel. non gen.)",command=CRUNCHnonselectivenongeneratic)
submenu.add_command(label = "Crunch(non sel. gen.)",command=CRUNCHnonselectivegeneratic)

helpmenu.add_command(label = "terminal",command=HELPterminal)
helpmenu.add_command(label = "Copy & Paste",command=HELPcopypaste)





root.mainloop()
