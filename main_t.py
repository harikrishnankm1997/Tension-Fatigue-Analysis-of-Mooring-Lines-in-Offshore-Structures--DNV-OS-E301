import tkinter as tk
from tkinter import *
from tkinter import ttk,Button
import tkinter.filedialog as filedialog

class main(tk.Frame):
    def __init__(self,master):
        self.master=master
       
        super().__init__(master)
        dnv_page=Frame(self)
        Label(dnv_page,text="Select the Mooring segment (MSG)",justify=CENTER).grid(row=0,column=0)
        self.comb_Mooring=ttk.Combobox(dnv_page,
            values=["Common Studlink","Common Studless link","Balt and Kennar Connection link","Six/multi standard rope","Spiral Strand rope"]
        )
        self.comb_Mooring.grid(row=0,column=1)
        Label(dnv_page,text="Nominal dia, mm",justify=CENTER).grid(row=1,column=0)
        self.nominalDia=Entry(dnv_page)
        self.nominalDia.grid(row=1,column=1)
        Label(dnv_page,text="RBS").grid(row=2,column=0)
        self.erbs=Entry(dnv_page)
        self.erbs.grid(row=2,column=1)
        Label(dnv_page,text="No. of Drafts").grid(row=3,column=0)
        self.endrafts=Entry(dnv_page)
        self.endrafts.grid(row=3,column=1)
        Label(dnv_page,text="No. of sea states").grid(row=4,column=0)
        self.enstate=Entry(dnv_page)
        self.enstate.grid(row=4,column=1)
        Label(dnv_page,text="No. of Mooring LiNE ").grid(row=5,column=0)
        self.enline=Entry(dnv_page)
        self.enline.grid(row=5,column=1)
        Label(dnv_page, text="loc of fatigue data:").grid(row=6,column=0)
        self.enline=Entry(dnv_page)
        self.enline.grid(row=6,column=1)
        Button(dnv_page,text='Browse').grid(row=6,column=2)
        self.enline=Entry(dnv_page)

        Label(dnv_page, text="loc of loadcast file data:").grid(row=7,column=0)
        self.enline=Entry(dnv_page)
        self.enline.grid(row=7,column=1)
        Button(dnv_page,text='Browse').grid(row=7,column=2)
        self.enline=Entry(dnv_page)

        Label(dnv_page, text="loc of draft file:").grid(row=8,column=0)
        self.enline=Entry(dnv_page)
        self.enline.grid(row=8,column=1)
        Button(dnv_page,text='Browse').grid(row=8,column=2)
        self.enline=Entry(dnv_page)

        Label(dnv_page, text="loc of mooring line file data:").grid(row=9,column=0)
        self.enline=Entry(dnv_page)
        self.enline.grid(row=9,column=1)
        Button(dnv_page,text='Browse').grid(row=9,column=2)
        self.enline=Entry(dnv_page)








        Button(dnv_page, text='Begin!').grid(row=10,column=0)
        self.enline=Entry(dnv_page)
        
        dnv_page.pack(expand=True,fill=BOTH,side=TOP)
        self.pack(expand=True,fill=BOTH)
    def do_bindings(self):
        self.comb_Mooring.bind("<<ComboboxSelected>>", self.selectedMsg)
    def selectedMsg(self):
        self.MSG=self.comb_Mooring.get()
if __name__ == "__main__":
    root=Tk()
    a=main(root)
    root.configure(bg= "#17202a",width=800,height=500)
    a.mainloop()