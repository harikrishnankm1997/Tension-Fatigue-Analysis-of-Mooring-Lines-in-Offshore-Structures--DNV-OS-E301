import re
import pandas as pd
def draft_extacractor(path):
	df=pd.DataFrame()
	with open(path,"r") as f:
		for line in f:
			if not line.startswith("="):
				if line.startswith("#"):
					columns=line.split("\t")
					columns=[i.strip("\n") for i in columns if not i.strip()==""]
				elif re.match(r'\d',line):
					values=[i.strip("\n") for i in line.split("\t") if i.strip()!=""]
					#data={columns[i]:values[i] for i in range(1,len(columns))}
					df=df.append({columns[i]:values[i] for i in range(1,len(columns))},ignore_index=True)
		df=df.apply(pd.to_numeric, errors='ignore')
		return(df)