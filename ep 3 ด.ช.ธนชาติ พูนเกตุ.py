from tkinter import *
from tkinter import ttk #them of tk

GUI = Tk() #นี้คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดโปรแกรม

B1=ttk.Button(GUI,text='กรุณาเลือกน้ำผลไม้')
B1.pack(ipadx=20,ipady=20)


FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=745,y=100)
B2=ttk.Button(FB1,text='น้ำแอปเปิล')
B2.pack(ipadx=20,ipady=20)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=745,y=200)
B3=ttk.Button(FB2,text='น้ำส้ม')
B3.pack(ipadx=20,ipady=20)

FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=745,y=300)
B4=ttk.Button(FB3,text='น้ำมะพร้าว')
B4.pack(ipadx=20,ipady=20)

FB4 = Frame(GUI) #คล้ายกระดาน
FB4.place(x=745,y=400)
B5=ttk.Button(FB4,text='น้ำองุ่น')
B5.pack(ipadx=20,ipady=20)

FB5 = Frame(GUI) #คล้ายกระดาน
FB5.place(x=745,y=500)
B6=ttk.Button(FB5,text='น้ำกล้วย')
B6.pack(ipadx=20,ipady=20)

GUI.mainloop()
