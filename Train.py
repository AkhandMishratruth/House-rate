import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
import matplotlib.pyplot as plt

#val=[]
data = pd.read_csv("OrganisedData.csv")
test = pd.read_csv("TestOrganised.csv")
y=data["SalePrice"]
X=data.drop(["SalePrice"], axis=1)
X=data.drop(["Id","SalePrice","MSSUB13", "MSZ1", "MSZ2", "MSZ4","MSZ7","Al3", "LC4", "UTL2", "UTL3", "UTL4","LotC1","NG13", "CN28", "BD2", "BD3", "BD5", "ET110", "ET112","ET23","ET26","ET212", "ET217", "MV3", "EQ5", "BQ5", "BQ6","BC1", "BC6","BC5","BF17","BF27","KQ5","FU8","FQ6","GT7","GF4","GQ6","GC6","PQ3","PQ5","FN5","MF1","MF6","IR3","LC1", "BE5", "OC10","ST3"] , axis=1)
test_x=test.drop(["Id","MSSUB13", "MSZ1", "MSZ2", "MSZ4","MSZ7","Al3", "LC4", "UTL2", "UTL3", "UTL4","LotC1","NG13", "CN28", "BD2", "BD3", "BD5", "ET110", "ET112","ET23","ET26","ET212", "ET217", "MV3", "EQ5", "BQ5", "BQ6","BC1", "BC6","BC5","BF17","BF27","KQ5","FU8","FQ6","GT7","GF4","GQ6","GC6","PQ3","PQ5","FN5","MF1","MF6","IR3","LC1", "BE5", "OC10","ST3"] , axis=1)
test_x.fillna(test_x.median(),inplace=True)
#test_x.to_csv("test_x.csv", index=False)
X=(X-np.mean(X))/np.std(X)
#X.to_csv("temp.csv")
X, x_test, y, y_test = train_test_split(X,y, test_size=0.33,random_state=42)

#for i in np.arange(0.5,1000,0.5):
clf=linear_model.Ridge(alpha=26.6)
clf.fit(X,y)
#val.append(clf.score(x_test,y_test))
#    print i
##    print "Training score"
##    print clf.score(X,y)
##    print clf.score(x_test,y_test)

ans=clf.predict(test_x)
ans_data=pd.DataFrame({"Id":test["Id"], "SalePrice":ans})

ans_data.to_csv("ans.csv", index=False)
##
##plt.plot(np.arange(0.5, 1000, 0.5), val)
##plt.show()
