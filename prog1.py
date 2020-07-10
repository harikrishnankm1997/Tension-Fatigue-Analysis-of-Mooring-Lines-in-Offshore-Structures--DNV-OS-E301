'''
Created on Jan 20, 2020

@author: Digin Antony
'''
from tkinter import *
from tkinter import filedialog,messagebox
from tkinter.ttk import Progressbar
#from pip._internal.cli.cmdoptions import progress_bar
'''from mypacage.ExcellEtractor import extractFiles,gcount,curfile,nofile
import mypacage.ExcellEtractor'''
import pandas as pd
import math
import os
import numpy as np
import time
import re
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

global count,curfile,nofile
gcount=0
curfile=''
nofile=0

class main(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.frame= Frame(self)
        self.geometry("350x300")
        self.frame.button=Button(text="Browse",borderwidth=2)
        self.frame.textbox=Entry(borderwidth=2)
        self.frame.textbox.place(height=30,relwidth=.85,relx=0.0,rely=0.01)
        self.frame.button.place(relwidth=.15,relx=0.85,rely=0.01,height=30)
        self.frame.button.bind(sequence='<Button>', func = self.cmdpathbrowse,add=True)
        self.frame.progress_bar=Progressbar(self, orient=HORIZONTAL,length=100,  mode='determinate')
        self.varlblcurfile=StringVar()
        self.varlalprogress=StringVar()
        self.frame.lablel_filelist=Label(textvariable=self.varlblcurfile)
        self.frame.lablel_filelist.place(relheight=0.045,relwidth=0.90,relx=0.0,rely=0.15)
        self.frame.lablel_progress=Label(textvariable=self.varlalprogress)
        self.frame.lablel_progress.place(height=20,relwidth=0.10,relx=0.90,rely=0.20)
        self.frame.progress_bar.place(height=20,relwidth=0.90,relx=0.0,rely=0.20)
        self.frame.butExtract=Button(text="ExtractFile",borderwidth=2)
        self.frame.butExtract.place(relwidth=0.20,relx=0.38,rely=0.35)
        self.frame.butExtract.bind(sequence='<Button>', func = self.fileExtracting,add=True)
        self.minsize(350,300)
        self.title("FileExtractor")
    
    def fileExtracting(self,event):
        self.extractFiles(self.frame.textbox.get())   

    def cmdpathbrowse(self,event):
        folder=filedialog.askdirectory()
        if folder is None:
            return
        self.frame.textbox.delete(0, END)
        self.frame.textbox.insert(0, folder)

    def extractFiles(self,path):
        global gcount,curfile,nofile
        data_lines=dict()
        df_line1=df_line2=df_line3=df_line4=df_line5=df_line6=df_line7=df_line8=df_line9=pd.DataFrame()
        x = os.listdir(path)
        x.sort(key=natural_keys)
        nofile=len(x)
        for i in x:
            gcount=x.index(i)+1
            self.frame.progress_bar['value']=(gcount/nofile)*100
            self.update_idletasks()
            self.varlblcurfile.set(i)
            self.update_idletasks()
            self.varlalprogress.set(str(math.floor(gcount/nofile*100))+"%")
            self.update_idletasks()
            curfile=path+'/'+i
            with open(curfile,"r") as f:
                count=0
                for line in f.readlines():
                    count+=1
                    if line.startswith('Tz_up') or line.startswith('sigma'):
                        if ("Tz_up LF (s)" in line):
                            line=line.lstrip("Tz_up LF (s)")
                            line=line.lstrip()
                            line=line.rstrip('\n')
                            line=line.rstrip()
                            data_lines["Tz_up LF (s)"]=line.split("\t")
                        elif "Tz_up HF (s)" in line:
                            line=line.lstrip("Tz_up HF (s)")
                            line=line.lstrip()
                            line=line.rstrip('\n')
                            line=line.rstrip()
                            data_lines["Tz_up HF (s)"]=line.split("\t")
                        elif "sigma_LF (kN)" in line:
                            line=line.lstrip("sigma_LF (kN)")
                            line=line.lstrip()
                            line=line.rstrip('\n')
                            line=line.rstrip()
                            data_lines["sigma_LF (kN)"]=line.split("\t")
                        elif "sigma_HF (kN)" in line:
                            line=line.lstrip("sigma_HF (kN)")
                            line=line.lstrip()
                            line=line.rstrip('\n')
                            line=line.rstrip()
                            data_lines["sigma_HF (kN)"]=line.split("\t")
                            break
            nd_array=np.array([v for (k,v) in data_lines.items()],dtype=float)
            df=pd.DataFrame.from_dict(data_lines,dtype=float)
            df_line1=df_line1.append(df[:1])
            df_line2=df_line2.append(df[1:2])
            df_line3=df_line3.append(df[2:3])
            df_line4=df_line4.append(df[3:4])
            df_line5=df_line5.append(df[4:5])
            df_line6=df_line6.append(df[5:6])
            df_line7=df_line7.append(df[6:7])
            df_line8=df_line8.append(df[7:8])
            df_line9=df_line9.append(df[8:])
        df_line1.to_csv("line1.csv",index=False)
        df_line2.to_csv("line2.csv",index=False)
        df_line3.to_csv("line3.csv",index=False)
        df_line4.to_csv("line4.csv",index=False)
        df_line5.to_csv("line5.csv",index=False)
        df_line6.to_csv("line6.csv",index=False)
        df_line7.to_csv("line7.csv",index=False)
        df_line8.to_csv("line8.csv",index=False)
        df_line9.to_csv("line9.csv",index=False)
        messagebox.showinfo("FileExtraction", "ExtractionCompleted")
if __name__=='__main__':
    main().mainloop()