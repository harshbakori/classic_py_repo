import pandas as pd
import quandl


#df = quandl.get('CHRIS/MGEX_MW6');
df = quandl.get('WIKI/GOOGL');
print(df.head());  #  print data header for clerification that upper line is running

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

df['HL_PCT']=(df['Adj. High']-df['Adj. Low'])/df['Adj. Low']*100.0;
df['PCT_change']=(df['Adj. Low']-df['Adj. High'])/df['Adj. High']*100.0;


df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume',]];

print(df.head());
