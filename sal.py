import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('Position_Salaries.csv')
x = data.iloc[:,1:2].values  #or else x = data["Level"]
y = data.iloc[:,2].values  


plt.scatter(x,y,color='indigo')
#%matplotlib auto #execute this once


from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

linRegressor = LinearRegression()
linRegressor.fit(x,y)

#plt.plot(x,linRegressor.predict(x),color='yellow') #to plot the line
#plt.show()

polyFeatures = PolynomialFeatures(degree=2)  #degree let it be more than 1 to prevent straight line;to be more flexible to plot
 

newX = polyFeatures.fit_transform(x)

linRegressorNew = LinearRegression()
linRegressorNew.fit(newX,y)


plt.scatter(x,y,color='red')
plt.plot(x,linRegressorNew.predict(newX),'b')


y_pred = linRegressorNew.predict(newX)

plt.scatter(x,y,color='blue')
#plt.plot(x,linRegressor.predict(x),color='red')
plt.show()
 #below is to predict the salary for experience of 3.5  first we reshape it then  we transform the new values
z=[3.5]
news = np.array(z).reshape(1,-1)
y_newpred = linRegressor.predict(news)
news = polyFeatures.fit_transform(news)


a=linRegressorNew.score(newX,y)
l=[]
score=0
models=[]
i=2
while a < 0.99:
     polyFeatures = PolynomialFeatures(degree=i)
     newX = polyFeatures.fit_transform(x)
     linRegressorNew = LinearRegression()
     linRegressorNew.fit(newX,y)
     l.append(linRegressorNew.predict(newX,x))
     s.append(linRegressorNew.score(newX,y))
    
     plt.scatter(x,y,color='red')
     plt.plot(x,linRegressorNew.predict(newX))
     i+=1
plt.show()

l.append()
    
plt.subplot_adjust()