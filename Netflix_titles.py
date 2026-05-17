import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

df = pd.read_csv('/Users/mirac/Desktop/Veri/netflix_titles.csv', parse_dates=["date_added"])

#step_1: Detectet and fill na values.
#print(df.isnull().sum())

df["director"] = df['director'].fillna("unknown")
df["cast"] = df['cast'].fillna("unknown")
df["country"] = df['country'].fillna("unknown")

df = df.dropna()


#step_2: split year and month columns.
month=[]
for i in df["date_added"]:
    a=re.split(r'\s*,\s*',i)
    month.append(a[0])

df["month_added"] = month


years=[]
for i in df["date_added"]:
    a=re.split(r'\s*,\s*',i)
    years.append(a[1])

df["year_added"] = years


#step_3: pie graphic for Movie and TV Series ratio.
#plt.pie(df["type"].value_counts(),colors=["blue","purple"],labels=["Movie","TV Series"],startangle=90,autopct='%1.1f%%')


#step_4: Bar graphics about Movie and TV Series categories.
liste=[]
for i in df["listed_in"].str.split(r"[,&]"):
    for a in i:
        liste.append(a)

yeniliste=list(set(liste))

sozluk=dict()
for i in yeniliste:
    sozluk[i]=int(df["listed_in"].str.contains(i).sum())

TVsozluk=dict()
for i,a in sozluk.items():
    if "TV" in i:
        TVsozluk[i]=a
del TVsozluk["TV Shows"]


Moviesozluk=dict()
for i,a in sozluk.items():
    if "Movie" in i:
        Moviesozluk[i]=a
del Moviesozluk["Movies"]

"""
plt.figure(figsize=(18,10))
#sns.barplot(x=Moviesozluk.values(),y=Moviesozluk.keys())
#sns.barplot(x=TVsozluk.values(),y=TVsozluk.keys())
sns.barplot(x=sozluk.values(),y=sozluk.keys())
plt.show()
"""

#step_5: 
Mliste=[]
for i in df["duration"].str.split(r" "):
    if i[1]=="min":
        Mliste.append(i[0])


plt.figure(figsize=(25,6))
sns.histplot(x=Mliste)
plt.show()


L=[]
for i in Mliste:
    L.append(int(i))

ortalama = sum(L)/len(L)

#print(ortalama)
