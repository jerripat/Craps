from tkinter import *


tableColor = '#0c6122'
root = Tk()
root.title("Welcome to True Craps")
root.geometry("400x400")
root.configure(background=tableColor)

onFour = IntVar()
onFive = IntVar()
onSix = IntVar()
onEight = IntVar()
onNine = IntVar()
onTen = IntVar()


lblOne = Label(root, text=' 4     5     6     8     9     10', font=("Arial", 20, "bold"), bg=tableColor, fg='white')
lblOne.place(relx=0.5, rely=0.1, anchor=CENTER)

chkOne = Checkbutton(root, text="4", variable=onFour, onvalue=1, offvalue=0, relief=SUNKEN)
chkOne.place(relx=0.19, rely=0.2, anchor=CENTER)

chkTwo = Checkbutton(root, text="5", variable=onFive, onvalue=1, offvalue=0, relief=SUNKEN)
chkTwo.place(relx=0.3, rely=0.2, anchor=CENTER)

chkThree = Checkbutton(root, text="6", variable=onSix, onvalue=1, offvalue=0,relief=SUNKEN)
chkThree.place(relx=0.42, rely=0.2, anchor=CENTER)

chkFour = Checkbutton(root, text="8", variable=onEight, onvalue=1, offvalue=0,relief=SUNKEN)
chkFour.place(relx=0.55, rely=0.2, anchor=CENTER)

chkFive = Checkbutton(root, text="9", variable=onNine, onvalue=1, offvalue=0,relief=SUNKEN)
chkFive.place(relx=0.67, rely=0.2, anchor=CENTER)

chkSix = Checkbutton(root, text="10", variable=onTen, onvalue=1, offvalue=0,relief=SUNKEN)
chkSix.place(relx=0.82, rely=0.2, anchor=CENTER)




root.mainloop()
