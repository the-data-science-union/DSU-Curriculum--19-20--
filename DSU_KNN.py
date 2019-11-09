##KNN Algorithm





import pandas as pd
import numpy as np
##import the csv file from EpiCollect 5
data = pd.read_csv("gg.csv")


##make into Dataframe
data = pd.DataFrame(data)


#Make the qunatitative measures the explanatory variables (x variables)
#Make the response variable the plant family classification
#No qualitative measures? Still useful! Why is that? Could we include it?
X = data.iloc[:, [7,8,9]].values
y = data.iloc[:, 3].values


#Preprocessing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

#We replace the "test" data with the data of the unknown speciman 
X_test = np.array([[16,3,1],[40,2,3],[28,5,2],[38,3,1],[42,4,8]])

#Scale the data for better estimation of overall prediction
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)



#Imply the classification algorithm
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=1)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

#Lets see!
y_pred