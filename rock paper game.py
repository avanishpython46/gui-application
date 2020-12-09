from tkinter import *
import random
lst = ["Rock","Paper","Scissors"]
computer = random.choice(lst)
computer_points= 0
human_points= 0 
root= Tk()
user = StringVar()
root.geometry('500x500')
root.title('Rock Paper Scissor Game')
user1 = 'Human chose :'
def Rock():
    user.set(lst[0])
def paper():
    user.set(lst[1])
def scissor():
    user.set(lst[2])
def Submit():
    global human_points
    global computer_points
    if user.get()==lst[0] and computer==lst[1]:
        print("computer won ! ")
        computer_points+=1
    if user.get()==lst[1] and computer==lst[0]:
        print("Human won ! ")
        human_points+=1
    if user.get()==lst[0] and computer==lst[-1]:
        print("Human won !")
        human_points+=1
    if user.get()==lst[-1] and computer==lst[0]:
        print("Computer won !")
        computer_points+=1
    if user.get()==lst[1] and computer==lst[-1]:
        print("Computer won !")
        computer_points+=1
    if user.get()==lst[-1] and computer==lst[1]:
        print("Human won !")
        human_points+=1
    if user.get()==lst[0] and computer==lst[0]:
        print("Tie !")
    if user.get()==lst[1] and computer==lst[1]:
        print("Tie !")
    if user.get()==lst[2] and computer==lst[2]:
        print("Tie !")
    labe = Label(frame,text="Computer chose : ",bg="yellow")
    labe.place(x=0,y=15.5)
    labe_entry = Entry(frame,textvariable=computer)
    labe_entry.place(x=97.5,y=15.9)
    labe_entry.delete('0',END)
    labe_entry.insert(0,computer)
    newlab= Label(frame,text="Human Points : ",bg="yellow")
    newlab.place(y=52.9)
    newlab_entry = Entry(frame,textvariable=human_points)
    newlab_entry.place(x=88,y=51.5)
    newlab_entry.delete("0",END)
    newlab_entry.insert(0,human_points)
    newlab1 = Label(frame,text="Computer Points : ",bg="yellow")
    newlab1.place(y=82.9)
    newlab1_entry = Entry(frame,textvariable=computer_points)
    newlab1_entry.place(x=102.2,y=82.9)
    newlab1_entry.delete("0",END)
    newlab1_entry.insert(0,computer_points)
    if human_points==5:
        l = Label(frame,text="Human won the tournament.",bg="yellow",font=("helvetica",18,'bold'))
        l.place(y=110)
    if computer_points==5:
        l = Label(frame,text="Computer won the tournament .",bg="yellow",font=('Helvetica', 18, 'bold'))
        l.place(y=110)

        
button = Button(root,text="Rock",height=2,width=10,bg="light blue",command=Rock)
button.pack()
button3 = Button(root,text="Submit",height=2,width=10,bg="purple",command=Submit)
button3.pack()
button1 = Button(root,text="Paper",height=2,width=10,bg="Pink",command=paper)
button1.pack()
button2 = Button(root,text="Scissor",height=2,width=10,bg="light green",command=scissor).pack()
frame = LabelFrame(root,height=400,width=400,bg="yellow",text=user1)
frame.pack(side="left")
label_entry = Entry(frame,textvariable=user)
label_entry.place(x=88,y=-15.9)
root.mainloop()
