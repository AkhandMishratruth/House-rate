import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn import ensemble
from sklearn import preprocessing
from sklearn import svm

val=[]
val2=[]
data = pd.read_csv("OrganisedPart2.csv")
data.set_index("Id", inplace=True)

test = pd.read_csv("TestOrganisedPart2.csv")
test_x=test.drop(["Id"],axis=1)
#test.set_index("Id", inplace=True)
y=data["SalePrice"]
X=data.drop(["SalePrice"], axis=1)
X=X.drop(['UTL'], axis=1)
#X=data.drop(["Id","SalePrice","MSSUB13", "MSZ1", "MSZ2", "MSZ4","MSZ7","Al3", "LC4", "UTL2", "UTL3", "UTL4","LotC1","NG13", "CN28", "BD2", "BD3", "BD5", "ET110", "ET112","ET23","ET26","ET212", "ET217", "MV3", "EQ5", "BQ5", "BQ6","BC1", "BC6","BC5","BF17","BF27","KQ5","FU8","FQ6","GT7","GF4","GQ6","GC6","PQ3","PQ5","FN5","MF1","MF6","IR3","LC1", "BE5", "OC10","ST3"] , axis=1)
#test_x=test.drop(["Id","MSSUB13", "MSZ1", "MSZ2", "MSZ4","MSZ7","Al3", "LC4", "UTL2", "UTL3", "UTL4","LotC1","NG13", "CN28", "BD2", "BD3", "BD5", "ET110", "ET112","ET23","ET26","ET212", "ET217", "MV3", "EQ5", "BQ5", "BQ6","BC1", "BC6","BC5","BF17","BF27","KQ5","FU8","FQ6","GT7","GF4","GQ6","GC6","PQ3","PQ5","FN5","MF1","MF6","IR3","LC1", "BE5", "OC10","ST3"] , axis=1)
#test_x.fillna(test_x.median(),inplace=True)
#test_x.to_csv("test_x.csv", index=False)


X=(X-np.mean(X))/np.std(X)
test_x=test_x.drop(['UTL'], axis=1)
test_x=(test_x-np.mean(test_x))/np.std(test_x)

poly=preprocessing.PolynomialFeatures(2)

X=poly.fit_transform(X)
test_x=poly.fit_transform(test_x)

#test_x.to_csv(".csv")
##X, x_test, y, y_test = train_test_split(X,y, test_size=0.30,random_state=42)

clf=linear_model.Ridge()
clf.fit(X,y)
print clf.score(X,y)

##rgr=svm.SVR(epsilon=)
##rgr.fit(X,y)
##print rgr.score(X,y)
##print rgr.score(x_test,y_test)

##rndf=ensemble.RandomForestRegressor()
##rndf.fit(X,y)
##print rndf.score(X,y)
##print rndf.score(x_test,y_test)

##print rndf.score(x_test,y_test)
##for i in np.arange(0,1000,100):
##    clf=linear_model.Ridge(alpha=i)
##    clf.fit(X,y)
##    val.append(clf.score(x_test,y_test))
##    val2.append(clf.score(X,y))
##    print i
##    print clf.score(x_test,y_test)
##    print "Training score"
##    print clf.score(X,y)
##    print clf.score(x_test,y_test)
##rgr=svm.SVR(epsilon=0.1)
##rgr.fit(X,y)
##print rgr.score(x_test,y_test)
##val.append(rgr.score(x_test,y_test))
##val2.append(rgr.score(X,y))
ans=clf.predict(test_x)
ans_data=pd.DataFrame({"Id":test["Id"], "SalePrice":ans})
##
ans_data.to_csv("ridge_poly.csv", index=False)

##plt.plot(np.arange(0, 1000, 100), val,'r' ,np.arange(0, 1000, 100), val2,'b')
##plt.show()

