import pandas as pd
import numpy as np

data=pd.read_csv('test.csv')

data.set_index('Id', inplace=True)

#MSSUBClass
def MSSUB1(MS):
    if MS==20:
        return 1
    else:
        return 0
def MSSUB2(MS):
    if MS==30:
        return 1
    else:
        return 0
def MSSUB3(MS):
    if MS==40:
        return 1
    else:
        return 0
def MSSUB4(MS):
    if MS==45:
        return 1
    else:
        return 0
def MSSUB5(MS):
    if MS==50:
        return 1
    else:
        return 0
def MSSUB6(MS):
    if MS==60:
        return 1
    else:
        return 0
def MSSUB7(MS):
    if MS==70:
        return 1
    else:
        return 0
def MSSUB8(MS):
    if MS==75:
        return 1
    else:
        return 0
def MSSUB9(MS):
    if MS==80:
        return 1
    else:
        return 0
def MSSUB10(MS):
    if MS==85:
        return 1
    else:
        return 0
def MSSUB11(MS):
    if MS==90:
        return 1
    else:
        return 0
def MSSUB12(MS):
    if MS==120:
        return 1
    else:
        return 0
def MSSUB13(MS):
    if MS==150:
        return 1
    else:
        return 0
def MSSUB14(MS):
    if MS==160:
        return 1
    else:
        return 0
def MSSUB15(MS):
    if MS==180:
        return 1
    else:
        return 0
def MSSUB16(MS):
    if MS==190:
        return 1
    else:
        return 0

data['MSSUB1']=data['MSSubClass'].apply(MSSUB1)
data['MSSUB2']=data['MSSubClass'].apply(MSSUB2)
data['MSSUB3']=data['MSSubClass'].apply(MSSUB3)
data['MSSUB4']=data['MSSubClass'].apply(MSSUB4)
data['MSSUB5']=data['MSSubClass'].apply(MSSUB5)
data['MSSUB6']=data['MSSubClass'].apply(MSSUB6)
data['MSSUB7']=data['MSSubClass'].apply(MSSUB7)
data['MSSUB8']=data['MSSubClass'].apply(MSSUB8)
data['MSSUB9']=data['MSSubClass'].apply(MSSUB9)
data['MSSUB10']=data['MSSubClass'].apply(MSSUB10)
data['MSSUB11']=data['MSSubClass'].apply(MSSUB11)
data['MSSUB12']=data['MSSubClass'].apply(MSSUB12)
data['MSSUB13']=data['MSSubClass'].apply(MSSUB13)
data['MSSUB14']=data['MSSubClass'].apply(MSSUB14)
data['MSSUB15']=data['MSSubClass'].apply(MSSUB15)
data['MSSUB16']=data['MSSubClass'].apply(MSSUB16)

data.drop("MSSubClass", axis=1, inplace = True)

#MSZoning
def MSZ1(MSZ):
    if MSZ=="A":
        return 1
    else:
        return 0
def MSZ2(MSZ):
    if MSZ=="C":
        return 1
    else:
        return 0
def MSZ3(MSZ):
    if MSZ=="FV":
        return 1
    else:
        return 0
def MSZ4(MSZ):
    if MSZ=="I":
        return 1
    else:
        return 0
def MSZ5(MSZ):
    if MSZ=="RH":
        return 1
    else:
        return 0
def MSZ6(MSZ):
    if MSZ=="RL":
        return 1
    else:
        return 0
def MSZ7(MSZ):
    if MSZ=="RP":
        return 1
    else:
        return 0
def MSZ8(MSZ):
    if MSZ=="RM":
        return 1
    else:
        return 0
data["MSZ1"]=data["MSZoning"].apply(MSZ1)
data["MSZ2"]=data["MSZoning"].apply(MSZ2)
data["MSZ3"]=data["MSZoning"].apply(MSZ3)
data["MSZ4"]=data["MSZoning"].apply(MSZ4)
data["MSZ5"]=data["MSZoning"].apply(MSZ5)
data["MSZ6"]=data["MSZoning"].apply(MSZ6)
data["MSZ7"]=data["MSZoning"].apply(MSZ7)
data["MSZ8"]=data["MSZoning"].apply(MSZ8)

data.drop("MSZoning", axis=1, inplace = True)

#street
def STgrv(st):
    if st=='Grvl':
        return 1
    else:
        return 0
def STpav(st):
    if st=='Pave':
        return 1
    else:
        return 0
data["STgrv"]=data["Street"].apply(STgrv)
data["STpav"]=data["Street"].apply(STpav)

data.drop("Street", axis=1, inplace = True)


#Alley
def AL1(st):
    if st=='Grvl':
        return 1
    else:
        return 0
def AL2(st):
    if st=='Pave':
        return 1
    else:
        return 0
def AL3(st):
    if st=='NA':
        return 1
    else:
        return 0
data["AL1"]=data["Alley"].apply(AL1)
data["AL2"]=data["Alley"].apply(AL2)
data["Al3"]=data["Alley"].apply(AL3)

data.drop("Alley", axis=1, inplace = True)

#LotShape
def Reg(lotsp):
    if lotsp=="Reg":
        return 1
    else:
        return 0
def IR1(lotsp):
    if lotsp=="IR1":
        return 1
    else:
        return 0
def IR2(lotsp):
    if lotsp=="IR2":
        return 1
    else:
        return 0
def IR3(lotsp):
    if lotsp=="IR3":
        return 1
    else:
        return 0
data["Reg"]=data['LotShape'].apply(Reg)
data["IR1"]=data['LotShape'].apply(IR1)
data["IR2"]=data['LotShape'].apply(IR2)
data["IR3"]=data['LotShape'].apply(IR3)

data.drop("LotShape", axis=1, inplace = True)

#landcontour

def LC1(LC):
    if LC=="lv1":
        return 1
    else:
        return 0
def LC2(LC):
    if LC=="Bnk":
        return 1
    else:
        return 0
def LC3(LC):
    if LC=="HLS":
        return 1
    else:
        return 0
def LC4(LC):
    if LC=="LOW":
        return 1
    else:
        return 0

data['LC1']=data['LandContour'].apply(LC1)
data['LC2']=data['LandContour'].apply(LC2)
data['LC3']=data['LandContour'].apply(LC3)
data['LC4']=data['LandContour'].apply(LC4)

data.drop("LandContour", axis=1, inplace = True)

#Utilities
def UTL1(UTL):
    if UTL=="AllPub":
        return 1
    else:
        return 0
def UTL2(UTL):
    if UTL=="NoSewr":
        return 1
    else:
        return 0
def UTL3(UTL):
    if UTL=="NoSewa":
        return 1
    else:
        return 0
def UTL4(UTL):
    if UTL=="ELO":
        return 1
    else:
        return 0

data['UTL1']=data['Utilities'].apply(UTL1)
data['UTL2']=data['Utilities'].apply(UTL2)
data['UTL3']=data['Utilities'].apply(UTL3)
data['UTL4']=data['Utilities'].apply(UTL4)

data.drop("Utilities", axis=1, inplace = True)

#LotConfig
def LotC1(LC):
    if LC=='Insider':
        return 1
    else:
        return 0
def LotC2(LC):
    if LC=='Corner':
        return 1
    else:
        return 0
def LotC3(LC):
    if LC=='CulDSac':
        return 1
    else:
        return 0
def LotC4(LC):
    if LC=='FR2':
        return 1
    else:
        return 0
def LotC5(LC):
    if LC=='FR3':
        return 1
    else:
        return 0

data['LotC1']=data['LotConfig'].apply(LotC1)
data['LotC2']=data['LotConfig'].apply(LotC2)
data['LotC3']=data['LotConfig'].apply(LotC3)
data['LotC4']=data['LotConfig'].apply(LotC4)
data['LotC5']=data['LotConfig'].apply(LotC5)

data.drop("LotConfig", axis=1, inplace = True)

#landSlope

def LS1(LS):
    if LS=="Gtl":
        return 1
    else:
        return 0
def LS2(LS):
    if LS=="Mod":
        return 1
    else:
        return 0
def LS3(LS):
    if LS=="Sev":
        return 1
    else:
        return 0

data['LS1']=data['LandSlope'].apply(LS1)
data['LS2']=data['LandSlope'].apply(LS2)
data['LS3']=data['LandSlope'].apply(LS3)

data.drop("LandSlope", axis=1, inplace = True)

#Neighborhood

def NG1(N):
    if N=="Blmngtn":
        return 1
    else:
        return 0
def NG2(N):
    if N=="Blueste":
        return 1
    else:
        return 0
def NG3(N):
    if N=="BrDale":
        return 1
    else:
        return 0
def NG4(N):
    if N=="BrkSide":
        return 1
    else:
        return 0
def NG5(N):
    if N=="ClearCr":
        return 1
    else:
        return 0
def NG6(N):
    if N=="CollgCr":
        return 1
    else:
        return 0
def NG7(N):
    if N=="Crawfor":
        return 1
    else:
        return 0
def NG8(N):
    if N=="Edwards":
        return 1
    else:
        return 0
def NG9(N):
    if N=="Gilbert":
        return 1
    else:
        return 0
def NG10(N):
    if N=="IDOTRR":
        return 1
    else:
        return 0
def NG11(N):
    if N=="MeadowV":
        return 1
    else:
        return 0
def NG12(N):
    if N=="Mitchel":
        return 1
    else:
        return 0
def NG13(N):
    if N=="Names":
        return 1
    else:
        return 0
def NG14(N):
    if N=="NoRidge":
        return 1
    else:
        return 0
def NG15(N):
    if N=="NPkVill":
        return 1
    else:
        return 0
def NG16(N):
    if N=="NridgHt":
        return 1
    else:
        return 0
def NG17(N):
    if N=="NWAmes":
        return 1
    else:
        return 0
def NG18(N):
    if N=="OldTown":
        return 1
    else:
        return 0
def NG19(N):
    if N=="SWISU":
        return 1
    else:
        return 0
def NG20(N):
    if N=="Sawyer":
        return 1
    else:
        return 0
def NG21(N):
    if N=="SawyerW":
        return 1
    else:
        return 0
def NG22(N):
    if N=="Somerst":
        return 1
    else:
        return 0
def NG23(N):
    if N=="StoneBr":
        return 1
    else:
        return 0
def NG24(N):
    if N=="Timber":
        return 1
    else:
        return 0
def NG25(N):
    if N=="Veenker":
        return 1
    else:
        return 0

data['NG1']=data['Neighborhood'].apply(NG1)
data['NG2']=data['Neighborhood'].apply(NG2)
data['NG3']=data['Neighborhood'].apply(NG3)
data['NG4']=data['Neighborhood'].apply(NG4)
data['NG5']=data['Neighborhood'].apply(NG5)
data['NG6']=data['Neighborhood'].apply(NG6)
data['NG7']=data['Neighborhood'].apply(NG7)
data['NG8']=data['Neighborhood'].apply(NG8)
data['NG9']=data['Neighborhood'].apply(NG9)
data['NG10']=data['Neighborhood'].apply(NG10)
data['NG11']=data['Neighborhood'].apply(NG11)
data['NG12']=data['Neighborhood'].apply(NG12)
data['NG13']=data['Neighborhood'].apply(NG13)
data['NG14']=data['Neighborhood'].apply(NG14)
data['NG15']=data['Neighborhood'].apply(NG15)
data['NG16']=data['Neighborhood'].apply(NG16)
data['NG17']=data['Neighborhood'].apply(NG17)
data['NG18']=data['Neighborhood'].apply(NG18)
data['NG19']=data['Neighborhood'].apply(NG19)
data['NG20']=data['Neighborhood'].apply(NG20)
data['NG21']=data['Neighborhood'].apply(NG21)
data['NG22']=data['Neighborhood'].apply(NG22)
data['NG23']=data['Neighborhood'].apply(NG23)
data['NG24']=data['Neighborhood'].apply(NG24)
data['NG25']=data['Neighborhood'].apply(NG25)

data.drop("Neighborhood", axis=1, inplace = True)


#Condition 1
def CN1(C):
    if C=="Artery":
        return 1
    else:
        return 0
def CN2(C):
    if C=="Feedr":
        return 1
    else:
        return 0
def CN3(C):
    if C=="Norm":
        return 1
    else:
        return 0
def CN4(C):
    if C=="RRNn":
        return 1
    else:
        return 0
def CN5(C):
    if C=="RRAn":
        return 1
    else:
        return 0
def CN6(C):
    if C=="PosN":
        return 1
    else:
        return 0
def CN7(C):
    if C=="PosA":
        return 1
    else:
        return 0
def CN8(C):
    if C=="RRNe":
        return 1
    else:
        return 0
def CN9(C):
    if C=="RRAe":
        return 1
    else:
        return 0

data['CN11']=data['Condition1'].apply(CN1)
data['CN12']=data['Condition1'].apply(CN2)
data['CN13']=data['Condition1'].apply(CN3)
data['CN14']=data['Condition1'].apply(CN4)
data['CN15']=data['Condition1'].apply(CN5)
data['CN16']=data['Condition1'].apply(CN6)
data['CN17']=data['Condition1'].apply(CN7)
data['CN18']=data['Condition1'].apply(CN8)
data['CN19']=data['Condition1'].apply(CN9)

data.drop("Condition1", axis=1, inplace = True)


#Condition 2

data['CN21']=data['Condition2'].apply(CN1)
data['CN22']=data['Condition2'].apply(CN2)
data['CN23']=data['Condition2'].apply(CN3)
data['CN24']=data['Condition2'].apply(CN4)
data['CN25']=data['Condition2'].apply(CN5)
data['CN26']=data['Condition2'].apply(CN6)
data['CN27']=data['Condition2'].apply(CN7)
data['CN28']=data['Condition2'].apply(CN8)
data['CN29']=data['Condition2'].apply(CN9)

data.drop("Condition2", axis=1, inplace = True)


#BldgType

def BD1(B):
    if B=="1Fam":
        return 1
    else:
        return 0
def BD2(B):
    if B=="2FmCon":
        return 1
    else:
        return 0

def BD3(D):
    if D=="Duplx":
        return 1
    else:
        return 0
def BD4(D):
    if D=="TwnhsE":
        return 1
    else:
        return 0
def BD5(D):
    if D=="TwnhsI":
        return 1
    else:
        return 0

data["BD1"]=data["BldgType"].apply(BD1)
data["BD2"]=data["BldgType"].apply(BD2)
data["BD3"]=data["BldgType"].apply(BD3)
data["BD4"]=data["BldgType"].apply(BD4)
data["BD5"]=data["BldgType"].apply(BD5)

data.drop("BldgType", axis=1, inplace = True)

#HouseStyle

def HS1(H):
    if H=="1Story":
        return 1
    else:
        return 0
def HS2(H):
    if H=="1.5Fin":
        return 1
    else:
        return 0
def HS3(H):
    if H=="1.5Unf":
        return 1
    else:
        return 0
def HS4(H):
    if H=="2Story":
        return 1
    else:
        return 0
def HS5(H):
    if H=="2.5Fin":
        return 1
    else:
        return 0
def HS6(H):
    if H=="2.5Unf":
        return 1
    else:
        return 0
def HS7(H):
    if H=="SFoyer":
        return 1
    else:
        return 0
def HS8(H):
    if H=="SLvl":
        return 1
    else:
        return 0

data["HS1"]=data["HouseStyle"].apply(HS1)
data["HS2"]=data["HouseStyle"].apply(HS2)
data["HS3"]=data["HouseStyle"].apply(HS3)
data["HS4"]=data["HouseStyle"].apply(HS4)
data["HS5"]=data["HouseStyle"].apply(HS5)
data["HS6"]=data["HouseStyle"].apply(HS6)
data["HS7"]=data["HouseStyle"].apply(HS7)
data["HS8"]=data["HouseStyle"].apply(HS8)

data.drop("HouseStyle", axis=1, inplace = True)

#OverallQual

def OQ1(O):
    if O==1:
        return 1
    else:
        return 0
def OQ2(O):
    if O==2:
        return 1
    else:
        return 0
def OQ3(O):
    if O==3:
        return 1
    else:
        return 0
def OQ4(O):
    if O==4:
        return 1
    else:
        return 0
def OQ5(O):
    if O==5:
        return 1
    else:
        return 0
def OQ6(O):
    if O==6:
        return 1
    else:
        return 0
def OQ7(O):
    if O==7:
        return 1
    else:
        return 0
def OQ8(O):
    if O==8:
        return 1
    else:
        return 0
def OQ9(O):
    if O==9:
        return 1
    else:
        return 0
def OQ10(O):
    if O==10:
        return 1
    else:
        return 0

data["OQ1"]=data["OverallQual"].apply(OQ1)
data["OQ2"]=data["OverallQual"].apply(OQ2)
data["OQ3"]=data["OverallQual"].apply(OQ3)
data["OQ4"]=data["OverallQual"].apply(OQ4)
data["OQ5"]=data["OverallQual"].apply(OQ5)
data["OQ6"]=data["OverallQual"].apply(OQ6)
data["OQ7"]=data["OverallQual"].apply(OQ7)
data["OQ8"]=data["OverallQual"].apply(OQ8)
data["OQ9"]=data["OverallQual"].apply(OQ9)
data["OQ10"]=data["OverallQual"].apply(OQ10)

data.drop("OverallQual", axis=1, inplace = True)

#OverallCond

data["OC1"]=data["OverallCond"].apply(OQ1)
data["OC2"]=data["OverallCond"].apply(OQ2)
data["OC3"]=data["OverallCond"].apply(OQ3)
data["OC4"]=data["OverallCond"].apply(OQ4)
data["OC5"]=data["OverallCond"].apply(OQ5)
data["OC6"]=data["OverallCond"].apply(OQ6)
data["OC7"]=data["OverallCond"].apply(OQ7)
data["OC8"]=data["OverallCond"].apply(OQ8)
data["OC9"]=data["OverallCond"].apply(OQ9)
data["OC10"]=data["OverallCond"].apply(OQ10)

data.drop("OverallCond", axis=1, inplace = True)

#RoofStyle

def RS1(R):
    if R=="Flat":
        return 1
    else:
        return 0
def RS2(R):
    if R=="Gable":
        return 1
    else:
        return 0
def RS3(R):
    if R=="Gambrel":
        return 1
    else:
        return 0
def RS4(R):
    if R=="Hip":
        return 1
    else:
        return 0
def RS5(R):
    if R=="Mansard":
        return 1
    else:
        return 0
def RS6(R):
    if R=="Shed":
        return 1
    else:
        return 0

data["RS1"]=data["RoofStyle"].apply(RS1)
data["RS2"]=data["RoofStyle"].apply(RS2)
data["RS3"]=data["RoofStyle"].apply(RS3)
data["RS4"]=data["RoofStyle"].apply(RS4)
data["RS5"]=data["RoofStyle"].apply(RS5)
data["RS6"]=data["RoofStyle"].apply(RS6)

data.drop("RoofStyle", axis=1, inplace = True)

#RoofMatl

def RM1(R):
    if R=="ClyTile":
        return 1
    else:
        return 0
def RM2(R):
    if R=="CompShg":
        return 1
    else:
        return 0
def RM3(R):
    if R=="Membran":
        return 1
    else:
        return 0
def RM4(R):
    if R=="Metal":
        return 1
    else:
        return 0
def RM5(R):
    if R=="Roll":
        return 1
    else:
        return 0
def RM6(R):
    if R=="Tar&Grv":
        return 1
    else:
        return 0
def RM7(R):
    if R=="WdShake":
        return 1
    else:
        return 0
def RM8(R):
    if R=="WdShngl":
        return 1
    else:
        return 0

data["RM1"]=data["RoofMatl"].apply(RM1)
data["RM2"]=data["RoofMatl"].apply(RM2)
data["RM3"]=data["RoofMatl"].apply(RM3)
data["RM4"]=data["RoofMatl"].apply(RM4)
data["RM5"]=data["RoofMatl"].apply(RM5)
data["RM6"]=data["RoofMatl"].apply(RM6)
data["RM7"]=data["RoofMatl"].apply(RM7)
data["RM8"]=data["RoofMatl"].apply(RM8)

data.drop("RoofMatl", axis=1, inplace = True)

#Exterior1st

def ET11(E):
    if E=="AsbShng":
        return 1
    else:
        return 0
def ET12(E):
    if E=="AsphShn":
        return 1
    else:
        return 0
def ET13(E):
    if E=="BrkComm":
        return 1
    else:
        return 0
def ET14(E):
    if E=="BrkFace":
        return 1
    else:
        return 0
def ET15(E):
    if E=="CBlock":
        return 1
    else:
        return 0
def ET16(E):
    if E=="CemntBd":
        return 1
    else:
        return 0
def ET17(E):
    if E=="HdBoard":
        return 1
    else:
        return 0
def ET18(E):
    if E=="ImStucc":
        return 1
    else:
        return 0
def ET19(E):
    if E=="MetalSd":
        return 1
    else:
        return 0
def ET110(E):
    if E=="Other":
        return 1
    else:
        return 0
def ET111(E):
    if E=="Plywood":
        return 1
    else:
        return 0
def ET112(E):
    if E=="PreCast":
        return 1
    else:
        return 0
def ET113(E):
    if E=="Stone":
        return 1
    else:
        return 0
def ET114(E):
    if E=="Stucco":
        return 1
    else:
        return 0
def ET115(E):
    if E=="VinylSd":
        return 1
    else:
        return 0
def ET116(E):
    if E=="Wd Sdng":
        return 1
    else:
        return 0
def ET117(E):
    if E=="WdShing":
        return 1
    else:
        return 0

data["ET11"]=data["Exterior1st"].apply(ET11)
data["ET12"]=data["Exterior1st"].apply(ET12)
data["ET13"]=data["Exterior1st"].apply(ET13)
data["ET14"]=data["Exterior1st"].apply(ET14)
data["ET15"]=data["Exterior1st"].apply(ET15)
data["ET16"]=data["Exterior1st"].apply(ET16)
data["ET17"]=data["Exterior1st"].apply(ET17)
data["ET18"]=data["Exterior1st"].apply(ET18)
data["ET19"]=data["Exterior1st"].apply(ET19)
data["ET110"]=data["Exterior1st"].apply(ET110)
data["ET111"]=data["Exterior1st"].apply(ET111)
data["ET112"]=data["Exterior1st"].apply(ET112)
data["ET113"]=data["Exterior1st"].apply(ET113)
data["ET114"]=data["Exterior1st"].apply(ET114)
data["ET115"]=data["Exterior1st"].apply(ET115)
data["ET116"]=data["Exterior1st"].apply(ET116)
data["ET117"]=data["Exterior1st"].apply(ET117)

data.drop("Exterior1st", axis=1, inplace = True)

#Exterior2nd

data["ET21"]=data["Exterior2nd"].apply(ET11)
data["ET22"]=data["Exterior2nd"].apply(ET12)
data["ET23"]=data["Exterior2nd"].apply(ET13)
data["ET24"]=data["Exterior2nd"].apply(ET14)
data["ET25"]=data["Exterior2nd"].apply(ET15)
data["ET26"]=data["Exterior2nd"].apply(ET16)
data["ET27"]=data["Exterior2nd"].apply(ET17)
data["ET28"]=data["Exterior2nd"].apply(ET18)
data["ET29"]=data["Exterior2nd"].apply(ET19)
data["ET210"]=data["Exterior2nd"].apply(ET110)
data["ET211"]=data["Exterior2nd"].apply(ET111)
data["ET212"]=data["Exterior2nd"].apply(ET112)
data["ET213"]=data["Exterior2nd"].apply(ET113)
data["ET214"]=data["Exterior2nd"].apply(ET114)
data["ET215"]=data["Exterior2nd"].apply(ET115)
data["ET216"]=data["Exterior2nd"].apply(ET116)
data["ET217"]=data["Exterior2nd"].apply(ET117)

data.drop("Exterior2nd", axis=1, inplace = True)

#MasVnrType

def MV1(M):
    if M=="BrkCmn":
        return 1
    else:
        return 0
def MV2(M):
    if M=="BrkFace":
        return 1
    else:
        return 0
def MV3(M):
    if M=="CBlock":
        return 1
    else:
        return 0
def MV4(M):
    if M=="None":
        return 1
    else:
        return 0
def MV5(M):
    if M=="Stone":
        return 1
    else:
        return 0

data["MV1"]=data["MasVnrType"].apply(MV1)
data["MV2"]=data["MasVnrType"].apply(MV2)
data["MV3"]=data["MasVnrType"].apply(MV3)
data["MV4"]=data["MasVnrType"].apply(MV4)
data["MV5"]=data["MasVnrType"].apply(MV5)

data.drop("MasVnrType", axis=1, inplace = True)

#ExterQual

def EQ1(E):
    if E=="Ex":
        return 1
    else:
        return 0
def EQ2(E):
    if E=="Gd":
        return 1
    else:
        return 0
def EQ3(E):
    if E=="TA":
        return 1
    else:
        return 0
def EQ4(E):
    if E=="Fa":
        return 1
    else:
        return 0
def EQ5(E):
    if E=="Po":
        return 1
    else:
        return 0

data["EQ1"]=data["ExterQual"].apply(EQ1)
data["EQ2"]=data["ExterQual"].apply(EQ2)
data["EQ3"]=data["ExterQual"].apply(EQ3)
data["EQ4"]=data["ExterQual"].apply(EQ4)
data["EQ5"]=data["ExterQual"].apply(EQ5)

data.drop("ExterQual", axis=1, inplace = True)

#ExterCond

data["EC1"]=data["ExterCond"].apply(EQ1)
data["EC2"]=data["ExterCond"].apply(EQ2)
data["EC3"]=data["ExterCond"].apply(EQ3)
data["EC4"]=data["ExterCond"].apply(EQ4)
data["EC5"]=data["ExterCond"].apply(EQ5)

data.drop("ExterCond", axis=1, inplace = True)

#Foundation

def FND1(F):
    if F=="BrkTil":
        return 1
    else:
        return 0
def FND2(F):
    if F=="CBlock":
        return 1
    else:
        return 0
def FND3(F):
    if F=="PConc":
        return 1
    else:
        return 0
def FND4(F):
    if F=="Slab":
        return 1
    else:
        return 0
def FND5(F):
    if F=="Stone":
        return 1
    else:
        return 0
def FND6(F):
    if F=="Wood":
        return 1
    else:
        return 0

data["FND1"]=data["Foundation"].apply(FND1)
data["FND2"]=data["Foundation"].apply(FND2)
data["FND3"]=data["Foundation"].apply(FND3)
data["FND4"]=data["Foundation"].apply(FND4)
data["FND5"]=data["Foundation"].apply(FND5)
data["FND6"]=data["Foundation"].apply(FND6)

data.drop("Foundation", axis=1, inplace = True)

#BsmtQual

def BQ1(B):
    if B=="Ex":
        return 1
    else:
        return 0
def BQ2(B):
    if B=="Gd":
        return 1
    else:
        return 0
def BQ3(B):
    if B=="TA":
        return 1
    else:
        return 0
def BQ4(B):
    if B=="Fa":
        return 1
    else:
        return 0
def BQ5(B):
    if B=="Po":
        return 1
    else:
        return 0
def BQ6(B):
    if B=="NA":
        return 1
    else:
        return 0

data["BQ1"]=data["BsmtQual"].apply(BQ1)
data["BQ2"]=data["BsmtQual"].apply(BQ2)
data["BQ3"]=data["BsmtQual"].apply(BQ3)
data["BQ4"]=data["BsmtQual"].apply(BQ4)
data["BQ5"]=data["BsmtQual"].apply(BQ5)
data["BQ6"]=data["BsmtQual"].apply(BQ6)

data.drop("BsmtQual", axis=1, inplace = True)

#BsmtCond

data["BC1"]=data["BsmtCond"].apply(BQ1)
data["BC2"]=data["BsmtCond"].apply(BQ2)
data["BC3"]=data["BsmtCond"].apply(BQ3)
data["BC4"]=data["BsmtCond"].apply(BQ4)
data["BC5"]=data["BsmtCond"].apply(BQ5)
data["BC6"]=data["BsmtCond"].apply(BQ6)

data.drop("BsmtCond", axis=1, inplace = True)

#BsmtExposure

def BE1(B):
    if B=="Gd":
        return 1
    else:
        return 0
def BE2(B):
    if B=="Av":
        return 1
    else:
        return 0
def BE3(B):
    if B=="Mn":
        return 1
    else:
        return 0
def BE4(B):
    if B=="No":
        return 1
    else:
        return 0
def BE5(B):
    if B=="NA":
        return 1
    else:
        return 0

data["BE1"]=data["BsmtExposure"].apply(BE1)
data["BE2"]=data["BsmtExposure"].apply(BE2)
data["BE3"]=data["BsmtExposure"].apply(BE3)
data["BE4"]=data["BsmtExposure"].apply(BE4)
data["BE5"]=data["BsmtExposure"].apply(BE5)

data.drop("BsmtExposure", axis=1, inplace = True)

#BsmtFinType1

def BF1(B):
    if B=="GLQ":
        return 1
    else:
        return 0
def BF2(B):
    if B=="ALQ":
        return 1
    else:
        return 0
def BF3(B):
    if B=="BLQ":
        return 1
    else:
        return 0
def BF4(B):
    if B=="Rec":
        return 1
    else:
        return 0
def BF5(B):
    if B=="LwQ":
        return 1
    else:
        return 0
def BF6(B):
    if B=="Unf":
        return 1
    else:
        return 0
def BF7(B):
    if B=="NA":
        return 1
    else:
        return 0

data["BF11"]=data["BsmtFinType1"].apply(BF1)
data["BF12"]=data["BsmtFinType1"].apply(BF2)
data["BF13"]=data["BsmtFinType1"].apply(BF3)
data["BF14"]=data["BsmtFinType1"].apply(BF4)
data["BF15"]=data["BsmtFinType1"].apply(BF5)
data["BF16"]=data["BsmtFinType1"].apply(BF6)
data["BF17"]=data["BsmtFinType1"].apply(BF7)

data.drop("BsmtFinType1", axis=1, inplace = True)

#BsmtFinType2

data["BF21"]=data["BsmtFinType2"].apply(BF1)
data["BF22"]=data["BsmtFinType2"].apply(BF2)
data["BF23"]=data["BsmtFinType2"].apply(BF3)
data["BF24"]=data["BsmtFinType2"].apply(BF4)
data["BF25"]=data["BsmtFinType2"].apply(BF5)
data["BF26"]=data["BsmtFinType2"].apply(BF6)
data["BF27"]=data["BsmtFinType2"].apply(BF7)

data.drop("BsmtFinType2", axis=1, inplace = True)

#Heating

def HT1(H):
    if H=="Floor":
        return 1
    else:
        return 0
def HT2(H):
    if H=="GasA":
        return 1
    else:
        return 0
def HT3(H):
    if H=="GasW":
        return 1
    else:
        return 0
def HT4(H):
    if H=="Grav":
        return 1
    else:
        return 0
def HT5(H):
    if H=="OthW":
        return 1
    else:
        return 0
def HT6(H):
    if H=="Wall":
        return 1
    else:
        return 0

data["HT1"]=data["Heating"].apply(HT1)
data["HT2"]=data["Heating"].apply(HT2)
data["HT3"]=data["Heating"].apply(HT3)
data["HT4"]=data["Heating"].apply(HT4)
data["HT5"]=data["Heating"].apply(HT5)
data["HT6"]=data["Heating"].apply(HT6)

data.drop("Heating", axis=1, inplace = True)

#HeatingQC

data["HTQ1"]=data["HeatingQC"].apply(BQ1)
data["HTQ2"]=data["HeatingQC"].apply(BQ2)
data["HTQ3"]=data["HeatingQC"].apply(BQ3)
data["HTQ4"]=data["HeatingQC"].apply(BQ4)
data["HTQ5"]=data["HeatingQC"].apply(BQ5)

data.drop("HeatingQC", axis=1, inplace = True)

#CentralAir
data["CentralAir"]=data["CentralAir"].map({'N':0, 'Y':1})

#Electrical
def EC1(E):
    if E=="SBrkr":
        return 1
    else:
        return 0
def EC2(E):
    if E=="FuseA":
        return 1
    else:
        return 0
def EC3(E):
    if E=="FuseF":
        return 1
    else:
        return 0
def EC4(E):
    if E=="FuseP":
        return 1
    else:
        return 0
def EC5(E):
    if E=="Mix":
        return 1
    else:
        return 0

data["EC1"]=data["Electrical"].apply(EC1)
data["EC2"]=data["Electrical"].apply(EC2)
data["EC3"]=data["Electrical"].apply(EC3)
data["EC4"]=data["Electrical"].apply(EC4)
data["EC5"]=data["Electrical"].apply(EC5)

data.drop("Electrical", axis=1, inplace = True)

#KitchenQual

data["KQ1"]=data["KitchenQual"].apply(BQ1)
data["KQ2"]=data["KitchenQual"].apply(BQ2)
data["KQ3"]=data["KitchenQual"].apply(BQ3)
data["KQ4"]=data["KitchenQual"].apply(BQ4)
data["KQ5"]=data["KitchenQual"].apply(BQ5)

data.drop("KitchenQual", axis=1, inplace = True)

#Functional

def FU1(F):
    if F=="Typ":
        return 1
    else:
        return 0
def FU2(F):
    if F=="Min1":
        return 1
    else:
        return 0
def FU3(F):
    if F=="Min2":
        return 1
    else:
        return 0
def FU4(F):
    if F=="Mod":
        return 1
    else:
        return 0
def FU5(F):
    if F=="Maj1":
        return 1
    else:
        return 0
def FU6(F):
    if F=="Maj2":
        return 1
    else:
        return 0
def FU7(F):
    if F=="Sev":
        return 1
    else:
        return 0
def FU8(F):
    if F=="Sal":
        return 1
    else:
        return 0

data["FU1"]=data["Functional"].apply(FU1)
data["FU2"]=data["Functional"].apply(FU2)
data["FU3"]=data["Functional"].apply(FU3)
data["FU4"]=data["Functional"].apply(FU4)
data["FU5"]=data["Functional"].apply(FU5)
data["FU6"]=data["Functional"].apply(FU6)
data["FU7"]=data["Functional"].apply(FU7)
data["FU8"]=data["Functional"].apply(FU8)

data.drop("Functional", axis=1, inplace = True)

#FireplaceQu

data["FQ1"]=data["FireplaceQu"].apply(BQ1)
data["FQ2"]=data["FireplaceQu"].apply(BQ2)
data["FQ3"]=data["FireplaceQu"].apply(BQ3)
data["FQ4"]=data["FireplaceQu"].apply(BQ4)
data["FQ5"]=data["FireplaceQu"].apply(BQ5)
data["FQ6"]=data["FireplaceQu"].apply(BQ6)

data.drop("FireplaceQu", axis=1, inplace = True)

#GarageType

def GT1(G):
    if G=="2Types":
        return 1
    else:
        return 0
def GT2(G):
    if G=="Attchd":
        return 1
    else:
        return 0
def GT3(G):
    if G=="Basment":
        return 1
    else:
        return 0
def GT4(G):
    if G=="BuiltIn":
        return 1
    else:
        return 0
def GT5(G):
    if G=="CarPort":
        return 1
    else:
        return 0
def GT6(G):
    if G=="Detchd":
        return 1
    else:
        return 0
def GT7(G):
    if G=="NA":
        return 1
    else:
        return 0

data["GT1"]=data["GarageType"].apply(GT1)
data["GT2"]=data["GarageType"].apply(GT2)
data["GT3"]=data["GarageType"].apply(GT3)
data["GT4"]=data["GarageType"].apply(GT4)
data["GT5"]=data["GarageType"].apply(GT5)
data["GT6"]=data["GarageType"].apply(GT6)
data["GT7"]=data["GarageType"].apply(GT7)

data.drop("GarageType", axis=1, inplace = True)

#GarageFinish

def GF1(G):
    if G=="Fin":
        return 1
    else:
        return 0
def GF2(G):
    if G=="RFn":
        return 1
    else:
        return 0
def GF3(G):
    if G=="Unf":
        return 1
    else:
        return 0
def GF4(G):
    if G=="NA":
        return 1
    else:
        return 0

data["GF1"]=data["GarageFinish"].apply(GF1)
data["GF2"]=data["GarageFinish"].apply(GF2)
data["GF3"]=data["GarageFinish"].apply(GF3)
data["GF4"]=data["GarageFinish"].apply(GF4)

data.drop("GarageFinish", axis=1, inplace = True)

#GarageQual

data["GQ1"]=data["GarageQual"].apply(BQ1)
data["GQ2"]=data["GarageQual"].apply(BQ2)
data["GQ3"]=data["GarageQual"].apply(BQ3)
data["GQ4"]=data["GarageQual"].apply(BQ4)
data["GQ5"]=data["GarageQual"].apply(BQ5)
data["GQ6"]=data["GarageQual"].apply(BQ6)

data.drop("GarageQual", axis=1, inplace = True)

#GarageCond

data["GC1"]=data["GarageCond"].apply(BQ1)
data["GC2"]=data["GarageCond"].apply(BQ2)
data["GC3"]=data["GarageCond"].apply(BQ3)
data["GC4"]=data["GarageCond"].apply(BQ4)
data["GC5"]=data["GarageCond"].apply(BQ5)
data["GC6"]=data["GarageCond"].apply(BQ6)

data.drop("GarageCond", axis=1, inplace = True)

#PavedDrive

def PD1(P):
    if P=="Y":
        return 1
    else:
        return 0
def PD2(P):
    if P=="P":
        return 1
    else:
        return 0
def PD3(P):
    if P=="N":
        return 1
    else:
        return 0

data["PD1"]=data["PavedDrive"].apply(PD1)
data["PD2"]=data["PavedDrive"].apply(PD2)
data["PD3"]=data["PavedDrive"].apply(PD3)

data.drop("PavedDrive", axis=1, inplace = True)

#PoolQC

data["PQ1"]=data["PoolQC"].apply(BQ1)
data["PQ2"]=data["PoolQC"].apply(BQ2)
data["PQ3"]=data["PoolQC"].apply(BQ3)
data["PQ4"]=data["PoolQC"].apply(BQ4)
data["PQ5"]=data["PoolQC"].apply(BQ6)

data.drop("PoolQC", axis=1, inplace = True)

#Fence

def FN1(F):
    if F=="GdPrv":
        return 1
    else:
        return 0
def FN2(F):
    if F=="MnPrv":
        return 1
    else:
        return 0
def FN3(F):
    if F=="GdWo":
        return 1
    else:
        return 0
def FN4(F):
    if F=="MnWw":
        return 1
    else:
        return 0
def FN5(F):
    if F=="NA":
        return 1
    else:
        return 0


data["FN1"]=data["Fence"].apply(FN1)
data["FN2"]=data["Fence"].apply(FN2)
data["FN3"]=data["Fence"].apply(FN3)
data["FN4"]=data["Fence"].apply(FN4)
data["FN5"]=data["Fence"].apply(FN5)

data.drop("Fence", axis=1, inplace = True)

#MiscFeature

def MF1(M):
    if M=="Elev":
        return 1
    else:
        return 0
def MF2(M):
    if M=="Gar2":
        return 1
    else:
        return 0
def MF3(M):
    if M=="Othr":
        return 1
    else:
        return 0
def MF4(M):
    if M=="Shed":
        return 1
    else:
        return 0
def MF5(M):
    if M=="TenC":
        return 1
    else:
        return 0
def MF6(M):
    if M=="NA":
        return 1
    else:
        return 0

data["MF1"]=data["MiscFeature"].apply(MF1)
data["MF2"]=data["MiscFeature"].apply(MF2)
data["MF3"]=data["MiscFeature"].apply(MF3)
data["MF4"]=data["MiscFeature"].apply(MF4)
data["MF5"]=data["MiscFeature"].apply(MF5)
data["MF6"]=data["MiscFeature"].apply(MF6)

data.drop("MiscFeature", axis=1, inplace = True)

#SaleType

def ST1(S):
    if S=="WD":
        return 1
    else:
        return 0
def ST2(S):
    if S=="CWD":
        return 1
    else:
        return 0
def ST3(S):
    if S=="VWD":
        return 1
    else:
        return 0
def ST4(S):
    if S=="New":
        return 1
    else:
        return 0
def ST5(S):
    if S=="COD":
        return 1
    else:
        return 0
def ST6(S):
    if S=="Con":
        return 1
    else:
        return 0
def ST7(S):
    if S=="ConLw":
        return 1
    else:
        return 0
def ST8(S):
    if S=="ConLI":
        return 1
    else:
        return 0
def ST9(S):
    if S=="ConLD":
        return 1
    else:
        return 0
def ST10(S):
    if S=="Oth":
        return 1
    else:
        return 0

data["ST1"]=data["SaleType"].apply(ST1)
data["ST2"]=data["SaleType"].apply(ST2)
data["ST3"]=data["SaleType"].apply(ST3)
data["ST4"]=data["SaleType"].apply(ST4)
data["ST5"]=data["SaleType"].apply(ST5)
data["ST6"]=data["SaleType"].apply(ST6)
data["ST7"]=data["SaleType"].apply(ST7)
data["ST8"]=data["SaleType"].apply(ST8)
data["ST9"]=data["SaleType"].apply(ST9)
data["ST10"]=data["SaleType"].apply(ST10)

data.drop("SaleType", axis=1, inplace = True)

#SaleCondition

def SC1(S):
    if S=="Normal":
        return 1
    else:
        return 0
def SC2(S):
    if S=="Abnorml":
        return 1
    else:
        return 0
def SC3(S):
    if S=="AdjLand":
        return 1
    else:
        return 0
def SC4(S):
    if S=="Alloca":
        return 1
    else:
        return 0
def SC5(S):
    if S=="Family":
        return 1
    else:
        return 0
def SC6(S):
    if S=="Partial":
        return 1
    else:
        return 0

data["SC1"]=data["SaleCondition"].apply(SC1)
data["SC2"]=data["SaleCondition"].apply(SC2)
data["SC3"]=data["SaleCondition"].apply(SC3)
data["SC4"]=data["SaleCondition"].apply(SC4)
data["SC5"]=data["SaleCondition"].apply(SC5)
data["SC6"]=data["SaleCondition"].apply(SC6)

data.drop("SaleCondition", axis=1, inplace = True)

#
data["LotFrontage"].fillna(value=data["LotFrontage"].median(), inplace=True)
data["GarageYrBlt"].fillna(value=data["GarageYrBlt"].median(), inplace=True)
data["MasVnrArea"].fillna(value=data["MasVnrArea"].median(), inplace=True)
data.to_csv('TestOrganised.csv', header=True)


























    

