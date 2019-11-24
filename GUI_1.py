from tkinter import *
root = Tk()
root.title("Check")#ชื่อtitle
root.geometry("500x500+0+0")

heading = Label(root, text="WELLCOME",font=("arial", 40, "bold")).pack()
label1 = Label(root, text="Enter your name(eng): ", font =("arial",10,"bold")).place(x=10, y=200)

name = StringVar()
entry_box = Entry(root, textvariable=name, width = 25, bg = "lightgreen").place(x=280, y=200)#ช่องเติมชื่อ

def do_it():
    list_person = {"A":"1500","B":"2000","C":"2500"}
    print(list_person[str(name.get())])
work = Button(root, text="Check", width=20,height=5, bg="lightblue", command=do_it).place(x=250, y=300)
root.mainloop()
