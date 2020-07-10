import pandas as pd
my_csv = pd.read_csv("D:\S6 MCA\loadcases1.txt",usecols=["#Loadcase","Hs-s","Tp-s","g-s","Dir-s","g-s","Dir-s","Uw","Dir-wi","Uc","Dir-cu","Probability"])
my_csv.to_csv("sea_states.csv")