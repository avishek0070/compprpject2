from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("300x300")
def bmix():
    ht=float(height.get())
    wt=float(weight.get())
    print(ht)
    print(wt)
    ht=ht/100
    bmi=float(wt / (ht*ht))
    bmi=round(bmi,1)
    conclusion=""
    if bmi<15.5: 
        conclusion="Under Weight" 
    elif bmi>18.4 and bmi<=24.9: 
        conclusion="Normal" 
    elif bmi>24.9 and bmi<=29.9:
        conclusion="Over Weight"
    else:
        conclusion="Obesity"
    output= "BMI = "+str(bmi)+"\n" +conclusion
    l=Label(text=output).place(x=150,y=220)
    # print(output)
    # return
Label(root, text="BMI", font=('Helvetica 17 bold')).place(x=100,y=20)
heightText=Label(root,text="Height (in CM)").place(x=10,y=50)
height=Entry(root)
height.place(x=10,y=80)
weightText=Label(root,text="Weight (in KG)").place(x=10,y=120)
weight=Entry(root)
weight.place(x=10,y=180)
bt=Button(root,text="Calculate BMI",command = bmix).place(x=180,y=175)
root.mainloop()