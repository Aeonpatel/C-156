from tkinter import*
root=Tk()

from PIL import ImageTk, Image

root.title("Endless Dice Game")
root.geometry("600x600")

root.configure(background="orange")

img=ImageTk.PhotoImage(Image.open(""))

player1 = Label(root,text="Player 1",bg="royal blue" ,fg="white" )
player1.place(relx="0.1",rely="0.5")

player2 = Label(root,text="Player 2" , bg="royal blue" , fg="white")
player2.place(relx="0.9",rely="0.5")

player1_score = Label(root,text="0",bg="orange",fg="white")
player1_score.place(relx="0.1",rely="0.6")

player2_score = Label(root,text="0",bg="orange",fg="white")
player2_score.place(relx="0.9",rely="0.6")


root.mainloop()