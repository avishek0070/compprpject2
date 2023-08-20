# from tkinter import *
# root=Tk()
# i=14
# def A():
#     global i,l1
#     if(i>150):
#         # global l1
#         i=14
#     else:
#         i=i+14
#         l1=Label(root,text="KICKFLIX",font=("Courier",i),bg="red")
#         l1.place(x=210,y=25)
#     root.after(1000,A)
# A()
# i=1
# k="MOVIES"
# def bcs():
#     global i,l1,k
#     if(i>64):
#         i=16
#         l1=Label(root,text="MoViEs",font=("Courier",i),bg="red").place(x=200,y=410)
#         k="MoViEs"
        
#     else:
#         i=i+15
#         l1=Label(root,text=k,font=("Courier",i),bg="red").place(x=200,y=410)
#     root.after(500,bcs)   
# bcs()
# root.mainloop()
from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.title("KICKFLIX")
root.geometry("750x500")
# bg=PhotoImage(file=r"C:\Users\agarw\OneDrive\Desktop\logo2.png")
# bg=bg.subsample(1,1)
# label1=Label(root,image=bg)
# label1.place(x=100,y=20)
# l1=Label(root,text="   ",padx=50,font=("Courier",14)).grid(row=0,column=0)
l1=Label(root,text=" WELCOME TO ",padx=50,font=("Courier",24),bg="red").place(x=45,y=0)
# l2=Label(root,text=" KICKFLIX ! ",font=("Courier",14),bg="red")
# l2.place(x=210,y=25)
i=0
def kick():
    global i,l1
    if(i>64):
        i=14
        # l1.destroy()
    else:
        i=i+14
        # l1=Label(root,text=" WELCOME TO ",padx=50,font=("Courier",i),bg="red").place(x=45,y=0)
        l1=Label(root,text="KICKFL!X",font=("Courier",i),bg="red")
        l1.place(x=150,y=115)
    root.after(500,kick)
kick()
photo = PhotoImage(file = r"C:\Users\agarw\OneDrive\Desktop\computer project\movies_down_bot.png")
photoimage = photo.subsample(5, 5)
# i=Image.open(r"C:\Users\agarw\OneDrive\Desktop\logo2.png")
# resize=i.resize((450,350))
# img=ImageTk.PhotoImage(resize)
# # b2=Button(root,text="",image=img).place(x=275,y=130)
# label1=Label(root,image=img)
# label1.place(x=100,y=20)
def A():
    rt.destroy()
    global r
    r=Tk()
    r.geometry("800x900")
    # r.title("A")
    # image2 = Image.open(r"C:\Users\agarw\OneDrive\Desktop\computer project\7a44528278ebb8a89e7f9923a4e52dcbe723600ff1179f9cd9a6284c73fa376e._UY500_UX667_RI_V_TTW_.png")
    # resize_image2 = image2.resize((175,140))
    # img2 = ImageTk.PhotoImage(resize_image2)
    # b6=Button(r,text="",image=img2,command=lambda:A()).place(x=0,y=0)
    # l5=Label(r,text="--->",font=("Courier",14),bg="blue").place(x=185,y=60)
#     l6=Label(r,text="""In June 2012, A huge, dead, unmanned ship-"Sea Bird", on its way to a shipyard, broke its ties and ran ashore Juhu beach. Prithvi, a shipping officer recovering from psychotic depression due to the loss of his family, is in charge of getting Sea B.
# IMDb --- 5.4/10
# """,font=("Courier",14)).place(x=250,y=20)
    global our_images,count
    count=-1
    img1=Image.open(r"C:\Users\agarw\OneDrive\Desktop\compprpject2\7a44528278ebb8a89e7f9923a4e52dcbe723600ff1179f9cd9a6284c73fa376e._UY500_UX667_RI_V_TTW_.png")
    resize1=img1.resize((850,520))
    img1=ImageTk.PhotoImage(resize1)
    img2=Image.open(r"C:\Users\agarw\OneDrive\Desktop\compprpject2\_1fb98ba8-4657-11ea-b9ea-c2a424b98379.png")
    resize2=img2.resize((850,520))
    img2=ImageTk.PhotoImage(resize2)
    img3=Image.open(r"C:\Users\agarw\OneDrive\Desktop\compprpject2\120220054144-5e43eb804cb99vicky-bhumi-channa-ve-resized.png")
    resize3=img3.resize((850,520))
    img3=ImageTk.PhotoImage(resize3)
    our_images=[img1,img2,img3]
    # create canvas
    my_canvas=Canvas(r,width=1000,height=200)
    my_canvas.pack(fill=BOTH,expand=True)
    my_canvas.create_image(0,0,image=our_images[0],anchor=NW)
    def next():
        global count,our_images
        if(count==2):
            my_canvas.create_image(0,0,image=our_images[0],anchor=NW)
            count=0
        else:
            my_canvas.create_image(0,0,image=our_images[count+1],anchor=NW)
            count+=1
        root.after(2000,next)
    next()
    r.mainloop()
    return
def B():
    rt.destroy()
    global r
    r=Tk()
    r.geometry("800x900")
    global our_images,count
    count=-1
    img1=Image.open(r"C:\Users\agarw\Downloads\1587622960134288-0.png")
    resize1=img1.resize((850,520))
    img1=ImageTk.PhotoImage(resize1)
    img2=Image.open(r"C:\Users\agarw\OneDrive\Desktop\compprpject2\_1fb98ba8-4657-11ea-b9ea-c2a424b98379.png")
    resize2=img2.resize((850,520))
    img2=ImageTk.PhotoImage(resize2)
    img3=Image.open(r"C:\Users\agarw\OneDrive\Desktop\compprpject2\120220054144-5e43eb804cb99vicky-bhumi-channa-ve-resized.png")
    resize3=img3.resize((850,520))
    img3=ImageTk.PhotoImage(resize3)
    our_images=[img1,img2,img3]
    # create canvas
    my_canvas=Canvas(r,width=1000,height=200)
    my_canvas.pack(fill=BOTH,expand=True)
    my_canvas.create_image(0,0,image=our_images[0],anchor=NW)
    def next():
        global count,our_images
        if(count==2):
            my_canvas.create_image(0,0,image=our_images[0],anchor=NW)
            count=0
        else:
            my_canvas.create_image(0,0,image=our_images[count+1],anchor=NW)
            count+=1
        root.after(2000,next)
    next()
    r.mainloop()
    return
def horror():
    rot.destroy()
    global rt
    rt=Tk()
    rt.title("HORROR")
    rt.geometry("500x520")
    image2 = Image.open(r"C:\Users\agarw\OneDrive\Desktop\computer project\7a44528278ebb8a89e7f9923a4e52dcbe723600ff1179f9cd9a6284c73fa376e._UY500_UX667_RI_V_TTW_.png")
    resize_image2 = image2.resize((135,100))
    img2 = ImageTk.PhotoImage(resize_image2)
    b6=Button(rt,text="",image=img2,command=lambda:A()).place(x=0,y=0)
    l5=Label(rt,text="BHOOT PART 1",font=("Courier",14),bg="red").place(x=0,y=110)
    image23 = Image.open(r"C:\Users\agarw\Downloads\1587622960134288-0.png")
    resize_image23 = image23.resize((135,105))
    img23 = ImageTk.PhotoImage(resize_image23)
    b6=Button(rt,text="",image=img23,command=lambda:B()).place(x=200,y=0)
    l5=Label(rt,text="PARI",font=("Courier",14),bg="red").place(x=240,y=110)
    rt.mainloop()
    return
def AAA():
    rot.destroy()
    return
def comedy():
    rot.destroy()
    return
def crime():
    rot.destroy()
    return
def Movie():
    root.destroy()
    global rot,b1,l1
    rot=Tk()
    rot.title("GENRE")
    rot.geometry("750x500")
    photo=PhotoImage(file=r"C:\Users\agarw\OneDrive\Desktop\computer project\watercolor-halloween-background_52683-43698.png")
    photo=photo.subsample(4,4)
    b1=Button(rot,text="",image=photo,command=lambda:horror()).place(x=0,y=0)
    l1=Label(rot,text="HORROR",font=("Courier",14),bg="red").place(x=39,y=110)
    # photo2=PhotoImage(file=r"C:\Users\agarw\OneDrive\Desktop\computer project\download.png")
    # resize_image = photo2.resize((20,10))
    # # photo=photo2.subsample(2,2)
    # b1=Button(rot,text="",image=photo2,padx=200,pady=100).place(x=280,y=0)
    # l1=Label(rot,text="AAA",font=("Courier",14),bg="red").place(x=310,y=110)
    image = Image.open(r"C:\Users\agarw\OneDrive\Desktop\computer project\download.png")
    resize_image = image.resize((155,100))
    img = ImageTk.PhotoImage(resize_image)
    # label1 = Label(image=img)
    # label1.image = img
    # label1.pack()
    b1=Button(rot,text="",image=img,command=lambda:AAA()).place(x=225,y=0)
    l1=Label(rot,text="ACTION AND ADVENTURE",font=("Courier",14),bg="red").place(x=179,y=110)
    image2 = Image.open(r"C:\Users\agarw\Downloads\sodapdf-converted (1).png")
    resize_image2 = image2.resize((125,100))
    img2 = ImageTk.PhotoImage(resize_image2)
    b1=Button(rot,text="",image=img2,command=lambda:comedy()).place(x=445,y=0)
    l1=Label(rot,text="COMEDY",font=("Courier",14),bg="red").place(x=479,y=110)
    b1=Button(rot,text="",image=img).place(x=225,y=0)
    # l1=Label(rot,text="ACTION AND ADVENTURE",font=("Courier",14),bg="red").place(x=179,y=110)
    image3 = Image.open(r"C:\Users\agarw\OneDrive\Desktop\computer project\Crime_film_clapperboard.svg.png")
    resize_image3 = image3.resize((125,120))
    img3 = ImageTk.PhotoImage(resize_image3)
    b1=Button(rot,text="",image=img3).place(x=5,y=150)
    l1=Label(rot,text="CRIME",font=("Courier",14),bg="red").place(x=35,y=275)
    rot.mainloop()
b1=Button(root,text="",image=photoimage,command=lambda:Movie()).place(x=200,y=350)
l1=Label(root,text="MOVIES",font=("Courier",14),bg="red").place(x=200,y=410)
photo = PhotoImage(file =r"C:\Users\agarw\OneDrive\Desktop\computer project\preview_21707_1540639785.png")
photoimage2 = photo.subsample(4, 4)
b1=Button(root,text="",image=photoimage2).place(x=450,y=350)
l1=Label(root,text="SERIES",font=("Courier",14),bg="red").place(x=450,y=410)
root.mainloop()