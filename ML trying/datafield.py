import pandas as pd
import quandl
import math ,sklearn
import numpy as np
from sklearn import preprocessing, svm 
from sklearn.model_selection import cross_validate
from sklearn.linear_model import Ridge

#df = quandl.get('CHRIS/MGEX_MW6');
df = quandl.get('WIKI/GOOGL')
print(df.head());  #  print data header for clerification that upper line is running

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

df['HL_PCT']=(df['Adj. High']-df['Adj. Low'])/df['Adj. Low']*100.0;
df['PCT_change']=(df['Adj. Low']-df['Adj. High'])/df['Adj. High']*100.0;

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume',]];

#print(df.head()); 

forcast_col = 'Adj. Close'
df.fillna(-99999,inplace=True)

forcast_out = int(math.ceil(0.01*len(df)))

df['lable']=df[forcast_col].shift(-forcast_out)
df.dropna(inplace=True)
print(df.tail())
print('done \n\n\n')

x = np.array(df.drop(['label'],1))
y = np.array(df['label'])

x = preprocessing.scale(x)

#x = x[:-forcast_out+1]
#df.dropna(inplace=True)
y = np.array(df['label'])

x_train,x_test ,y_train,y_test = cross_validation.train_test_split(x,y,test_size=0.2)

clf = LinearRegression()
clf.fit(x_train,y_train)
accuracy = clf.score(x_test,y_test)
 
print(accuracy)

print()