from draft_extractor import *
from ExcellEtractor import Csv_Extractror
import numpy as np
import math,time
print("Select Procedure from following\n")
print("""\t1. API RP 2SK\n\t2. DNVGL-OS-E301""")
state=True
while state:
    try:
        inp=int(input("\nYour Selection :"))
        if inp==1 or inp==2:
           state=False
        else:
            raise Exception
    except Exception as e:
        print("wrong input try Again !")
    else:
        if inp ==1:
            print("You Selected - API-RP-2SK")
            PROC="API-RP-2SK"
        elif  inp==2:
            print("You Selected - DNVGL-OS-E301")
            PROC="DNVGL-OS-E301"
print("Select Mooring Segment(MSEG) \n")
print("""\t1. Comon Studlink\n\t2. Common Studless link\n\t3. Baldt and Kenter connection link \n\t4. Six/multi starnd rope\n\t5. Spiral strand rope""")
state=True
while state:
    try:
        inp1=int(input("\nYour Selection :"))
        if inp1 in range(1,6):
            state=False
        else:
            raise Exception
    except Exception as e:
        print("wrong input try Again !")
if inp1==1:
    MSEG = "Common Studlink"
elif inp1==2:
    MSEG = "Common Studless link"
elif inp1==3:
    MSEG = "Baldt and Kenter connection link"
elif inp1==4:
    MSEG = "Six/multi strand rope"
elif inp1==5:
    MSEG = "Spiral strand rope"
NDIA_SOL = float(input("Input nominal dia., mm : "))
RBS = float(input("Input RBS, kN : "))
print(f"Calculations according to {PROC} Procedure.")
print(f"Segment type {MSEG}")
print(f"Nominal Dia at SOL = {NDIA_SOL} mm")
print(f"Reference Breaking Strength EOL ={RBS} KN")
ND=int(input("No of Drafts : "))
path_to_draft="E:\\Projects\\My_project\\files\\draft.txt"
path_to_mooring="E:\\Projects\\My_project\\files\\mooring.txt"
df_draft=draft_extacractor(path_to_draft)
df_mooring=draft_extacractor(path_to_mooring)
DPSUM=df_draft.Percent.sum()
if DPSUM not in np.arange(99.9,100.1):
    print("Sum is not 100 percent")
AZIMj=df_mooring['Azimuth, deg'].max()<=360
NL=int(input("No of Mooring Lines : "))
NS=int(input("Input No. of Sea States : "))
sea_states = pd.read_csv("E:\\Projects\\My_project\\files\\loadcases1.txt",usecols=["#Loadcase","Hs-s","Tp-s","g-s","Dir-s","g-s","Dir-s","Uw","Dir-wi","Uc","Dir-cu","Probability"])
PSUM=sea_states.Probability.sum()
print(PSUM)
if PSUM<0.99: 
    print("Warning : Probability less than 1")
elif PSUM>1.01:
    print("Warning : Probability grater than 1")
PSUM_N=sea_states[sea_states["Dir-s"].between(337.5,360)]["Probability"].sum()+sea_states[sea_states["Dir-s"].between(0,22.5)]["Probability"].sum()
PSUM_NE= sea_states[sea_states["Dir-s"].between(22.5,67.5)]["Probability"].sum()
PSUM_E= sea_states[sea_states["Dir-s"].between(67.5,112.5)]["Probability"].sum()
PSUM_SE= sea_states[sea_states["Dir-s"].between(112.5,157.5)]["Probability"].sum()
PSUM_S= sea_states[sea_states["Dir-s"].between(157.5,202.5)]["Probability"].sum()
PSUM_SW= sea_states[sea_states["Dir-s"].between(202.5,247.5)]["Probability"].sum()
PSUM_W= sea_states[sea_states["Dir-s"].between(247.5,292.5)]["Probability"].sum()
PSUM_NW= sea_states[sea_states["Dir-s"].between(292.5,337.5)]["Probability"].sum()
P=[PSUM_N,PSUM_NE,PSUM_E,PSUM_SE,PSUM_S,PSUM_SW,PSUM_W,PSUM_NW]
P.append(sum(P))
#============ FILE EXTRACTION HERE ======================
df_lines=Csv_Extractror("E:\\Projects\\My_project\\files\\Fatigue-M")
Dss100kj=[];Dcs100kj=[];Ddnb100kj=[]
if PROC=="API-RP-2SK":
     print("Warning :!!")

elif PROC=="DNVGL-OS-E301":  

    if MSEG == "Common Studlink":
        M,K=3.0,1000
    elif MSEG == "Common Studless link": 
        M,K=3.0,316
    elif MSEG == "Baldt and Kenter connection link":
        M,K=3.0,178
for k in range(ND):
    for j in range(NL):
        df_line=df_lines[j]
        Dss100kji=[]
        Dcs100kji=[]
        Ddnb100kji=[]
        for i in range(NS):
            if PROC=="DNVGL-OS-E301":
                if MSEG == "Six/multi strand rope":
                    M=4.09
                    Lmk=df_line["Tmean"].iloc[i]/RBS
                    K=10**(3.20-3.43*Lmk)
                elif MSEG == "Spiral strand rope":
                    M=5.05
                    Lmk=df_line["Tmean"].iloc[i]/RBS
                    K=10**(3.20-3.43*Lmk)
                GF=math.gamma(1+(M/2))
                Rw=(2*df_line["DAF_sigma_wf"].iloc[i]*df_line["sigma_HF (kN)"].iloc[i])/RBS
                Vw=1/df_line["Tz_up HF (s)"].iloc[i]
                nw=Vw*sea_states["Probability"].iloc[i]*3.15576*10**7
                Rl=(2*df_line["sigma_LF (kN)"].iloc[i])/RBS
                Vl=1/df_line["Tz_up LF (s)"].iloc[i]
                nl=Vl*sea_states["Probability"].iloc[i]*3.15576*10**7
                dss=(nw/K)*((math.sqrt(2*Rw))**M)*GF+nl/K*((math.sqrt(2*Rl))**M)*GF#damage in simple summation
                area1 = (math.pi/4) * (NDIA_SOL * NDIA_SOL)#areamulti
                dss1=dss*area1
                Dss100kji.append(dss1)
                Rcs=math.sqrt(Rw**2+Rl**2)
                lambl=Rl**2/(Rl**2+Rw**2)
                lambw=Rw**2/(Rl**2+Rw**2)
                Vc=math.sqrt((lambl*Vl**2)+(lambw*Vw**2))
                nc=Vc*sea_states["Probability"].iloc[i]*3.15576*10**7
                dcs=nc/K*(math.sqrt(2*Rcs)**M)*GF#damage in combined spectrum
                area2 = (math.pi/4) * (NDIA_SOL * NDIA_SOL)#areamulti
                dcs1=dcs*area2
                Dcs100kji.append(dcs1)
                deltaw=0.1
                Ve=math.sqrt((lambl**2*Vl**2)+(lambl*lambw*Vw**2*deltaw))
                p=Ve/Vc*(lambl**((M/2)+2)*(1-math.sqrt(lambw/lambl)+math.sqrt(math.pi*lambl*lambw)*(M*math.gamma((1+M)/2)/math.gamma((2+M)/2)))+Vw/Vc*(lambw**(M/2)))
                dnb=p*dcs#damage in dual narrow band metho
                area3 = (math.pi/4) * (NDIA_SOL * NDIA_SOL)#areamulti
                dnb1=dnb*area3
                Ddnb100kji.append(dnb1)
        Dss100kj.append(sum(Dss100kji))
        Dcs100kj.append(sum(Dcs100kji))
        Ddnb100kj.append(sum(Ddnb100kji))
HDSUM=[Dss100kj,Dcs100kj,Ddnb100kj]
for i in range(len(HDSUM)):
    HDSUM[i]=np.asarray(HDSUM[i])
    HDSUM[i].shape=(9,3)
    anual_damage=np.zeros((NL,ND))
    for k in range(NL):
        for j in range(ND):
            anual_damage[k,j]=HDSUM[i][k,j]*df_draft["Draft,m"].iloc[j]
    columns=[f"percent{i}" for i in range(1,ND)]
    df_anual_damage=pd.DataFrame({f"percent{i}":anual_damage[:,i]for i in range(ND)})
    df_anual_damage["Damage_ss"]=df_anual_damage.sum(axis=1)
    df_anual_damage["fatigue_lif_ss"]=1/df_anual_damage["Damage_ss"]
    print(df_anual_damage,"\n")