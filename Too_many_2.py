import pandas as pd
import numpy as np

data=pd.read_csv('test.csv')

data.set_index('Id', inplace=True)

data.rename(columns={"MSZoning":"MSZ"},inplace=True)
data["MSZ"]=data["MSZ"].map({'A':10, 'C':20, 'FV':30, 'I':40, 'RH':50, 'RL':60, 'RP':70, 'RM':80})

data.rename(columns={"Street":"STR"},inplace=True)
data["STR"]=data["STR"].map({'Grvl':20, 'Pave':10})

data.rename(columns={"Alley":"ALY"},inplace=True)
data["ALY"]=data["ALY"].map({'Grvl':20, 'Pave':30})
data["ALY"].fillna(value=10, inplace=True)

data.rename(columns={"LotShape":"LTS"},inplace=True)
data["LTS"]=data["LTS"].map({'Reg':10, 'IR1':20,'IR2':30,'IR3':40})

data.rename(columns={"LandContour":"LDC"},inplace=True)
data["LDC"]=data["LDC"].map({'Lvl':10, 'Bnk':20,'HLS':30,'Low':40})

data.rename(columns={"Utilities":"UTL"},inplace=True)
data["UTL"]=data["UTL"].map({'AllPub':10, 'NoSewr':20,'NoSeWa':30,'ELO':40})

data.rename(columns={"LotConfig":"LTC"},inplace=True)
data["LTC"]=data["LTC"].map({'Inside':10, 'Corner':20,'CulDSac':30,'FR2':40, 'FR3':50})

data.rename(columns={"LandSlope":"LDS"},inplace=True)
data["LDS"]=data["LDS"].map({'Gtl':10,'Mod':30,'Sev':40})

data.rename(columns={"Neighborhood":"NBH"},inplace=True)
data["NBH"]=data["NBH"].map({'Blmngtn':10, 'Blueste':20, 'BrDale':30, 'BrkSide':40, 'ClearCr':50, 'CollgCr':60, 'Crawfor':70, 'Edwards':80, 'Gilbert':90, 'IDOTRR':100,'MeadowV':110,'Mitchel':120,'Names':130,'NoRidge':140,'NPkVill':150,'NridgHt':160,'NWAmes':170,'OldTown':180,'SWISU':190,'Sawyer':200,'SawyerW':210,'Somerst':220,'StoneBr':230,'Timber':240,'Veenker':250})

data.rename(columns={"Condition1":"CD1"},inplace=True)
data["CD1"]=data["CD1"].map({'Artery':10, 'Feedr':20, 'Norm':30, 'RRNn':40, 'RRAn':50, 'PosN':60, 'PosA':70, 'RRNe':80,'RRAe':90})

data.rename(columns={"Condition2":"CD2"},inplace=True)
data["CD2"]=data["CD2"].map({'Artery':10, 'Feedr':20, 'Norm':30, 'RRNn':40, 'RRAn':50, 'PosN':60, 'PosA':70, 'RRNe':80,'RRAe':90})

data.rename(columns={"BldgType":"BDT"},inplace=True)
data["BDT"]=data["BDT"].map({'1Fam':10, '2FmCon':20, 'Duplx':30, 'TwnhsE':40, 'TwnhsI':50})

data.rename(columns={"HouseStyle":"HSL"},inplace=True)
data["HSL"]=data["HSL"].map({'1Story':10, '1.5Fin':20, '15Unf':30, '2Story':40, '2.5Fin':50, '2.5Unf':60, 'SFoyer':70, 'SLvl':80})

data.rename(columns={"OverallQual":"OQL"},inplace=True)

data.rename(columns={"OverallCond":"OCD"},inplace=True)

data.rename(columns={"RoofStyle":"RSL"},inplace=True)
data["RSL"]=data["RSL"].map({'Flat':10, 'Gable':20, 'Gambrel':30, 'Hip':40, 'Mansard':50, 'Shed':60})

data.rename(columns={"RoofMatl":"RML"},inplace=True)
data["RML"]=data["RML"].map({'ClyTile':10, 'CompShg':20, 'Membran':30, 'Metal':40, 'Roll':50, 'Tar&Grv':60,'WdShake':70,'WdShngl':80})

data.rename(columns={"Exterior1st":"EX1"},inplace=True)
data["EX1"]=data["EX1"].map({'AsbShng':10, 'AsphShn':20, 'BrkComm':30, 'BrkFace':40, 'CBlock':50, 'CemntBd':60, 'HdBoard':70, 'ImStucc':80, 'MetalSd':90, 'Other':100,'Plywood':110,'PreCast':120,'Stone':130,'Stucco':140,'VinylSd':150,'Wd Sdng':160,'WdShing':170})

data.rename(columns={"Exterior2nd":"EX2"},inplace=True)
data["EX2"]=data["EX2"].map({'AsbShng':10, 'AsphShn':20, 'BrkComm':30, 'BrkFace':40, 'CBlock':50, 'CemntBd':60, 'HdBoard':70, 'ImStucc':80, 'MetalSd':90, 'Other':100,'Plywood':110,'PreCast':120,'Stone':130,'Stucco':140,'VinylSd':150,'Wd Sdng':160,'WdShing':170})

data.rename(columns={"MasVnrType":"MVT"},inplace=True)
data["MVT"]=data["MVT"].map({'BrkCmn':10, 'BrkFace':20, 'CBlock':30, 'None':40, 'Stone':50})

data.rename(columns={"ExterQual":"EXQ"},inplace=True)
data["EXQ"]=data["EXQ"].map({'Ex':50, 'Gd':40, 'TA':30, 'Fa':20, 'Po':10})

data.rename(columns={"ExterCond":"EXC"},inplace=True)
data["EXC"]=data["EXC"].map({'Ex':50, 'Gd':40, 'TA':30, 'Fa':20, 'Po':10})

data.rename(columns={"Foundation":"FND"},inplace=True)
data["FND"]=data["FND"].map({'BrkTil':10, 'CBlock':20, 'PConc':30, 'Slab':40,'Stone':50,'Wood':60})

data.rename(columns={"BsmtQual":"BSQ"},inplace=True)
data["BSQ"]=data["BSQ"].map({'Ex':50, 'Gd':40, 'TA':30, 'Fa':20, 'Po':10,'NA':0})

data.rename(columns={"BsmtCond":"BSC"},inplace=True)
data["BSC"]=data["BSC"].map({'Ex':50, 'Gd':40, 'TA':30, 'Fa':20, 'Po':10,'NA':0})

data.rename(columns={"BsmtExposure":"BSE"},inplace=True)
data["BSE"]=data["BSE"].map({'Gd':50, 'Av':40, 'Mn':30, 'No':20,'NA':10})

data.rename(columns={"BsmtFinType1":"BFT1"},inplace=True)
data["BFT1"]=data["BFT1"].map({'GLQ':60, 'ALQ':50, 'BLQ':40, 'Rec':30,'LwQ':20,'Unf':10,'NA':0})

data.rename(columns={"BsmtFinType2":"BFT2"},inplace=True)
data["BFT2"]=data["BFT2"].map({'GLQ':60, 'ALQ':50, 'BLQ':40, 'Rec':30,'LwQ':20,'Unf':10,'NA':0})

data.rename(columns={"Heating":"HTN"},inplace=True)
data["HTN"]=data["HTN"].map({'Floor':60, 'GasA':50, 'GasW':40, 'Grav':30,'OthW':20,'Wall':10})

data.rename(columns={"HeatingQC":"HQC"},inplace=True)
data["HQC"]=data["HQC"].map({'Ex':50, 'Gd':40, 'TA':30, 'Fa':20, 'Po':10})

data.rename(columns={"CentralAir":"CNA"},inplace=True)
data["CNA"]=data["CNA"].map({'N':0, 'Y':10})

data.rename(columns={"Electrical":"ELT"},inplace=True)
data["ELT"]=data["ELT"].map({'SBrkr':50, 'FuseA':40, 'FuseF':30, 'FuseP':20, 'Mix':10})

data.rename(columns={"KitchenQual":"KTQ"},inplace=True)
data["KTQ"]=data["KTQ"].map({'Ex':50, 'Gd':40, 'TA':30, 'Fa':20, 'Po':10})

data.rename(columns={"Functional":"FNL"},inplace=True)
data["FNL"]=data["FNL"].map({'Typ':80, 'Min1':70, 'Min2':60, 'Mod':50, 'Maj1':40,'Maj2':30,'Sev':20,'Sal':10})

data.rename(columns={"FireplaceQu":"FPQ"},inplace=True)
data["FPQ"]=data["FPQ"].map({'Ex':50, 'Gd':40, 'TA':30, 'Fa':20, 'Po':10,'NA':0})

data.rename(columns={"GarageType":"GRT"},inplace=True)
data["GRT"]=data["GRT"].map({'2Types':60, 'Attchd':50, 'Basment':40, 'BuiltIn':30, 'CarPort':20,'Detchd':10,'NA':0})

data.rename(columns={"GarageFinish":"GRF"},inplace=True)
data["GRF"]=data["GRF"].map({'Fin':10, 'RFn':20, 'Unf':30,'NA':0})

data.rename(columns={"GarageQual":"GRQ"},inplace=True)
data["GRQ"]=data["GRQ"].map({'Ex':50, 'Gd':40, 'TA':30, 'Fa':20, 'Po':10,'NA':0})

data.rename(columns={"GarageCond":"GRC"},inplace=True)
data["GRC"]=data["GRC"].map({'Ex':50, 'Gd':40, 'TA':30, 'Fa':20, 'Po':10,'NA':0})

data.rename(columns={"PavedDrive":"PVD"},inplace=True)
data["PVD"]=data["PVD"].map({'Y':10, 'P':20, 'N':30})

data.rename(columns={"PoolQC":"PQC"},inplace=True)
data["PQC"]=data["PQC"].map({'Ex':40, 'Gd':30, 'TA':20, 'Fa':10,'NA':0})

data.rename(columns={"Fence":"FNC"},inplace=True)
data["FNC"]=data["FNC"].map({'GdPrv':40, 'MnPrv':30, 'GdWo':20, 'MnWw':10,'NA':0})

data.rename(columns={"MiscFeature":"MFT"},inplace=True)
data["MFT"]=data["MFT"].map({'Elev':50, 'Gar2':40, 'Othr':30, 'Shed':20,'TenC':10,'NA':0})

data.rename(columns={"SaleType":"SLT"},inplace=True)
data["SLT"]=data["SLT"].map({'WD':10, 'CWD':20, 'VWD':30, 'New':40,'COD':50,'Con':60,'ConLw':70,'ConLI':80,'ConLD':90,'Oth':10})

data.rename(columns={"SaleCondition":"SLC"},inplace=True)
data["SLC"]=data["SLC"].map({'Normal':10, 'Abnorml':20, 'AdjLand':30, 'Alloca':40,'Family':50,'Partial':60})

##data["LotFrontage"].fillna(value=data["LotFrontage"].median(), inplace=True)
##data["MSZ"].fillna(value=data["MSZ"].median(), inplace=True)
##data["GarageYrBlt"].fillna(value=data["GarageYrBlt"].median(), inplace=True)
##data["MasVnrArea"].fillna(value=data["MasVnrArea"].median(), inplace=True)
data=data.fillna(value=data.median())
data.to_csv('TestOrganisedPart2.csv', header=True)



































