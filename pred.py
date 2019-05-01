# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import gmplot 
import webbrowser
import math
import csv

# Importing the dataset
dataset = pd.read_csv('fld.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 2].values
dataset2 = pd.read_csv('data.csv')
X_test2 = dataset2.iloc[ :, :-1].values
y_test2 = dataset2.iloc[:, 2].values
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = tra
in_test_split(X, y, test_size = 0.01, random_state = 0)
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
X_test2 = sc_X.transform(X_test2)

#Naive Bayes
from sklearn.naive_bayes import GaussianNB
NBC = GaussianNB()
NBC.fit(X_train, y_train)
y_pred_test = NBC.predict(X_test2)
avg_svr = sum(y_pred_test)/len(y_pred_test)
print("severity of flood = ", avg_svr)

#plotting
input_file = open("safepoints.csv","r+")
reader_file = csv.reader(input_file)
value = len(list(reader_file))
input_file.close()

dataset2 = pd.read_csv('safepoints.csv')
latitude_list = dataset2.iloc[:, 0].values
longitude_list = dataset2.iloc[:, 1].values
crnt_lat = 20.851846
crnt_lon = 86.334188
gmap3 = gmplot.GoogleMapPlotter(20.851846, 86.334188 , 14) 
  
# scatter method of map object  
# scatter points on the google map 
gmap3.scatter( latitude_list, longitude_list, '#006400', 
                              size = 40, marker = False ) 
gmap3.scatter( [crnt_lat], [crnt_lon], '#8B0000', 
                              size = 40, marker = False ) 
  
dist = 1000000.0
lat,lon = 0.0,0.0
for i in range(int(value)-1):
    temp = math.sqrt((crnt_lat-latitude_list[i])**2+(crnt_lon-longitude_list[i])**2)
    if temp < dist:
        dist = temp
        lat = latitude_list[i]
        lon = longitude_list[i]
        
gmap3.scatter( [lat], [lon], '#0000FF', 
                              size = 50, marker = False ) 
  
gmap3.draw( "map13.html" ) 
webbrowser.open_new_tab("map13.html")
url = "https://www.google.co.in/maps/dir/"+str(crnt_lat)+","+str(crnt_lon)+"/"+str(lat)+","+str(lon)+"/"
webbrowser.open_new_tab(url)