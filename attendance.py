from tkinter import *
root=Tk()
root.title("calculator")
root.geometry("900x900")
def final():
    t=str(e1.get())
    print(t)
    return
l1=Label(root,text="SUBJECT ").place(x=100,y=55)
e1=Entry(root)
e1.place(x=180,y=55)
l2=Label(root,text="NUMBER OF CLASSES ATTENDEND").place(x=100,y=105)
e2=Entry(root)
e2.place(x=295,y=105)
l3=Label(root,text="NUMBER OF CLASSES").place(x=100,y=145)
e3=Entry(root)
e3.place(x=290,y=145)
B1=Button(root,text="ENTER",command=final).place(x=290,y=195)
root.mainloop()
# from tkinter import *
# root()