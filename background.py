from tkinter import *
from PIL import Image,ImageTk
# from Tkconstants import *
root=Tk()
root.title("BACKGROUND CHANGE")
root.geometry("850x720")
global our_images
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
my_canvas=Canvas(root,width=1000,height=200)
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
root.mainloop()