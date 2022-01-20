from tkinter import *
from tkinter import ttk
klik=0
def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
def klikker2(event):
    global klik
    if klik>0:
        klik-=1
    else:
        klik=0
    lbl.configure(text=klik)
def text_to_lbl(event):
    text=ent.get()
    lbl.configure(text=text)
    ent.delete(0,END)
def valik():
    val=str(var.get())+", " #value 1,2 või 3
    ent.insert(END,val)

def uus_aken(ind:int):
    uusaken=Toplevel()
    tabs=ttk.Notebook(uusaken)
    texts=["snake1.gif","1.gif","2.gif","3.gif","4.gif","5.gif","6.gif","7.gif","8.gif","9.gif"]
    textn=["snake1.gif","1.gif","2.gif","3.gif","4.gif","5.gif","6.gif","7.gif","8.gif","9.gif"]
    tab=[]
    cann=[]
    for i in range(len(texts)):
        tab.append("tab"+str(i))
        tab[i]=Frame(tabs)
        tabs.add(tab[i],text=texts[i])#,image=img1)
        textn[i]=PhotoImage(file=texts[i]).subsample(1)
        cann.append("cann"+str(i))
        cann[i]=Canvas(tab[i],height=200,width=300,bg="red")
        cann[i].create_image(0,0,image=textn[i], anchor=NW)
        cann[i].pack()

    tabs.grid(row=0,column=0)
    tabs.select(ind)
    uusaken.mainloop()



aken=Tk() #Akna loomine
aken.title("Akna nimetus") #Akna pealkiri
aken.geometry("600x400") #Akna suurus
menu=Menu(aken)
aken.config(menu=menu)
m1=Menu(menu)
menu.add_cascade(label="Tabs",menu=m1)
m1.add_command(label="Tab1",accelerator="Command+A", command=lambda:uus_aken(0))
m1.add_command(label="Tab2",command=lambda:uus_aken(1))
m1.add_command(label="Tab3",command=lambda:uus_aken(2))
m1.add_command(label="Tab4",command=lambda:uus_aken(3))
m1.add_command(label="Tab5",command=lambda:uus_aken(4))
m1.add_separator()



btn=Button(aken,text="Vajuta siia",font="Arial 20",fg="green",bg="lightblue", width=20, height=3,relief=SUNKEN)#GROOVE, RAISED Loome nupp
btn2=Button(aken,text="Veel aken",font="Arial 20",fg="green",bg="lightblue",command=lambda:uus_aken(0))         
lbl=Label(aken,text="...") #Pealkiri
ent=Entry(aken,fg="blue",width=20,font="Arial 20",justify=CENTER) #Rida teksti sisestamiseks. tekxt on keskel
var=IntVar() #StringVar()
#var.set(3) valib kolmas button
r1=Radiobutton(aken,text="Esimene",variable=var,value=1,command=valik)
r2=Radiobutton(aken,text="Teine",variable=var,value=2,command=valik)
r3=Radiobutton(aken,text="Kolmas",variable=var,value=3,command=valik)

btn.bind("<Button-1>",klikker)#LKM 
btn.bind("<Button-3>",klikker2)#PKM
ent.bind("<Return>",text_to_lbl)#Enter
lbl.pack()
btn.pack()
ent.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
btn2.pack(side=RIGHT)
aken.mainloop() 
