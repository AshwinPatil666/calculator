from tkinter import*
windo=Tk()
windo.geometry("500x500")
windo.title("Calculator")
e=Entry(windo,width=56,borderwidth=5)
e.place(x=0,y=0)
def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))


#Buttons


b=Button(windo,text="1",width=12,command=lambda:click(1))
b.place(x=10,y=60)

b=Button(windo,text="2",width=12,command=lambda:click(2))
b.place(x=80,y=60)

b=Button(windo,text="3",width=12,command=lambda:click(3))
b.place(x=170,y=60)

b=Button(windo,text="4",width=12,command=lambda:click(4))
b.place(x=10,y=120)

b=Button(windo,text="5",width=12,command=lambda:click(5))
b.place(x=80,y=120)

b=Button(windo,text="6",width=12,command=lambda:click(6))
b.place(x=170,y=120)

b=Button(windo,text="7",width=12,command=lambda:click(7))
b.place(x=10,y=180)

b=Button(windo,text="8",width=12,command=lambda:click(8))
b.place(x=80,y=180)

b=Button(windo,text="9",width=12,command=lambda:click(9))
b.place(x=170,y=180)
def div():
    n1=e.get()
    global math 
    math= "Division"  
    global i
    i= int(n1)
    e.delete(0,END)

b=Button(windo,text="/",width=12,command=div)
b.place(x=10,y=240)

b=Button(windo,text="0",width=12,command=lambda:click(0))
b.place(x=80,y=240)
def add():
    n1=e.get()
    global math
    math="Addition"
    global i
    i= int(n1)
    e.delete(0,END)
b=Button(windo,text="+",width=12,command=add)
b.place(x=170,y=240)
def sub():
    n1=e.get()
    global math
    math="Substraction"
    global i
    i= int(n1)
    e.delete(0,END)
b=Button(windo,text="-",width=12,command=sub)
b.place(x=10,y=300)
def multi():
    n1=e.get()
    global math
    math="Multiply"
    global i
    i= int(n1)
    e.delete(0,END)

b=Button(windo,text="*",width=12,command=multi)
b.place(x=80,y=300)

def equal():
    n2 = e.get()
    e.delete(0,END)
    if math =="Addition":
        e.insert(0,i+int(n2))
    elif math=="Substraction":
        e.insert(0,i-int(n2))
    elif math=="Division":
        e.insert(0,i/int(n2))
    elif math=="Multiply":
        e.insert(0,i*int(n2))



b=Button(windo,text="=",width=12,command=equal)
b.place(x=170,y=300)
def clear():
    e.delete(0,END)


b=Button(windo,text="Clear",width=12,command=clear)
b.place(x=10,y=360)

b=Button(windo,text="_",width=12,command=lambda:click(" "))
b.place(x=80,y=360)
windo.mainloop()
