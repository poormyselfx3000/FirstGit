from tkinter import *
from tkinter import messagebox
import datetime


root = Tk()
root.title("app tinh nam sinh")
root.minsize(100, 100)  
root.geometry("300x300+50+50")
root.configure(background="pink")

def tinhtoan():
    th_gian_hien_tai = (datetime.datetime.now())
    so_tuoi = nhap_so_tuoi.get()

    if so_tuoi.isdigit():     

        nam_sinh = th_gian_hien_tai.year - int(so_tuoi)
        print('vay nam sinh cua ban la: ',nam_sinh)
        messagebox.showinfo("có phải năm sinh của bạn là",nam_sinh)
    
    else :
        messagebox.showerror("!!!","bạn đã nhấm nhầm hay nhập số âm rồi. Xin kiểm tra lại")



cauhoi = Label(root, text="hãy nhập tuổi của bạn. Chúng tôi sẽ tính năm sinh",bg = "pink")
cauhoi.pack()

nhap_so_tuoi = Entry(root,width=4) 
nhap_so_tuoi.pack()

cauhoi = Label(root, text="",bg = "pink")
cauhoi.pack()

nut1 = Button(root, text="nhấn vào đây để tính năm sinh",bg = "lightblue",command = tinhtoan)
nut1.pack()

dapan = Label(root, text="============================================",bg = "black")
dapan.pack()
root.mainloop()


