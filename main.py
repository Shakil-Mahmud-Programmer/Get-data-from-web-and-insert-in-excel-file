import pandas as pd
df=pd.read_html('https://en.wikipedia.org/wiki/FIFA_World_Rankings')

df1 = df[0].iloc[2:23]
df1=pd.DataFrame(df1)
df1.reset_index(inplace=True)
df1=df1.drop('index',axis='columns')
df1.rename(columns={0:'Rank',1:'change',2:'Teams',3:'Points'},inplace=True)
df1.drop(0,axis=0,inplace=True)
df1.reset_index(inplace=True)
df1.to_excel('Data.xlsx')

df2=df[1]
df2.to_excel('Data1.xlsx')
df[3].to_excel('Data2.xlsx')
df[4].to_excel('Data3.xlsx')