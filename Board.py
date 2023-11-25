from tkinter import *
import Place

pl = Place.PlaceBet()

tableColor = "#0c6122"
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

bet5 = IntVar()
bet10 = IntVar()
bet25 = IntVar()
bet50 = IntVar()
bet100 = IntVar()


def getBet():  # sourcery skip: for-append-to-extend, list-comprehension
    bet = [int(bet5.get()), int(bet10.get()),int(bet10.get()),int(bet25.get()),int(bet50.get()),int(bet100.get())]
    theBet = [] 
    for b in bet:
        if b > 0:
            theBet.append(b)
            
        for x in theBet:
            print(x)
    return theBet


Bet = getBet()  
for x in Bet:
    print(x)

def getPlace():  # sourcery skip: for-append-to-extend, list-comprehension
    place = [int(onFour.get()),int(onFive.get()) ,int(onSix.get()),int( onEight.get()),int(onNine.get()),int(onTen.get())]

    newPlace = []
    
    for x in place:
        if x > 0:
            newPlace.append(x)             
    
def testFunction():
    global Bet
    
    for x in Bet:
        print(x)
        
        
def submit():
    pass


lblOne = Label(root, text=" 4     5     6     8     9     10", font=("Arial", 20, "bold"), bg=tableColor, fg="white",)
lblOne.place(relx=0.5, rely=0.1, anchor=CENTER)

lblBet = Label(root, text="Bet", font=("Arial", 12, "bold"), bg=tableColor, fg="red")
lblBet.place(relx=0.03, rely=0.3, anchor="w")

chkOne = Checkbutton(root, text="4", variable=onFour, onvalue=4, offvalue=0, relief=SUNKEN)
chkOne.place(relx=0.19, rely=0.2, anchor=CENTER)

entOne = Entry(root, width=4)
entOne.place(relx=0.19, rely=0.3, anchor=CENTER)

chkTwo = Checkbutton(root, text="5", variable=onFive, onvalue=5, offvalue=0, relief=SUNKEN)
chkTwo.place(relx=0.3, rely=0.2, anchor=CENTER)

entTwo = Entry(root, width=4)
entTwo.place(relx=0.31, rely=0.3, anchor=CENTER)

chkThree = Checkbutton(root, text="6", variable=onSix, onvalue=6, offvalue=0, relief=SUNKEN)
chkThree.place(relx=0.42, rely=0.2, anchor=CENTER)

entThree = Entry(root, width=4)
entThree.place(relx=0.43, rely=0.3, anchor=CENTER)

chkFour = Checkbutton(root, text="8", variable=onEight, onvalue=8, offvalue=0, relief=SUNKEN)
chkFour.place(relx=0.55, rely=0.2, anchor=CENTER)

entFour = Entry(root, width=4)
entFour.place(relx=0.56, rely=0.3, anchor=CENTER)

chkFive = Checkbutton(root, text="9", variable=onNine, onvalue=9, offvalue=0, relief=SUNKEN)
chkFive.place(relx=0.67, rely=0.2, anchor=CENTER)

entFive = Entry(root, width=4)
entFive.place(relx=0.68, rely=0.3, anchor=CENTER)

chkSix = Checkbutton(root, text="10", variable=onTen, onvalue=10, offvalue=0, relief=SUNKEN)
chkSix.place(relx=0.82, rely=0.2, anchor=CENTER)

entSix = Entry(root, width=4)
entSix.place(relx=0.82, rely=0.3, anchor=CENTER)


lblDollar = Label(root, text="$",font=("Arial", 14, "bold" ),bg=tableColor, fg="yellow",)
lblDollar.place(relx=0.2, rely=0.83, anchor="se")

radioOne = Radiobutton(root, text="5", variable=bet5, value=5)
radioOne.place(relx=0.3, rely=0.8, anchor=CENTER)

radioTwo = Radiobutton(root, text="10", variable=bet10, value=10)
radioTwo.place(relx=0.41, rely=0.8, anchor=CENTER)

radioThree = Radiobutton(root, text="25", variable=bet25, value=25)
radioThree.place(relx=0.53, rely=0.8, anchor=CENTER)

radioFour = Radiobutton(root, text="50", variable=bet50, value=50)
radioFour.place(relx=0.65, rely=0.8, anchor=CENTER)

radioFive = Radiobutton(root, text="100", variable=bet100, value=100)
radioFive.place(relx=0.78, rely=0.8, anchor=CENTER)

btnSubmit = Button(
    root,
    text="Roll",
    font=("Arial", 10, "bold"),
    bg=tableColor,
    fg="white",
    command=getPlace,
)
btnSubmit.place(relx=0.5, rely=0.5, anchor="s")

btnTest = Button(root, text="Test",font=("Arial", 10, "bold"),bg=tableColor,fg="white", command=getBet)
btnTest.place(relx=0.5, rely=0.7, anchor="s")

root.mainloop()
