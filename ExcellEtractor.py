import numpy as np
import pandas as pd
import os
import re
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def Csv_Extractror(path=None,no_lines=9):
    data_lines=dict()
    #df_line1=df_line2=df_line3=df_line4=df_line5=df_line6=df_line7=df_line8=df_line9=pd.DataFrame()
    df_lines=list()
    for i in range(no_lines):
        df_lines.append(pd.DataFrame())
    files = os.listdir(path)
    files.sort(key=natural_keys)
    for i in files:
        with open(path+"\\"+i,"r") as f:
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
        for i in range(len(df_lines)):
            df_lines[i]=df_lines[i].append(df[i:i+1])
    k=1
    for i in df_lines:
        val=np.empty(len(i))
        val.fill(0.0000)
        i.insert(loc=4,column='Tmean', value=val)
        val.fill(1.00)
        i.insert(loc=5,column="DAF_sigma_wf",value=val)
        #i.to_csv(f"line{k}.csv",index=False)
        k+=1
    return df_lines
if __name__ == '__main__':
    Csv_Extractror()