import pandas as pd
import numpy as np
import pymongo
import matplotlib.pyplot as plt
import seaborn as sns
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydata_vision"]
mycol = mydb["my_data"]

time =[]
neutral =[]
happy=[]
sad =[]
angry =[]
disgusted =[]
fearful=[]
surprised=[]
time_d=[]


for i in mycol.find():
    time.append(i["time"])
    neutral.append(i["neutral"])
    happy.append(i["happy"])
    sad.append(i["sad"])
    disgusted.append(i["disgusted"])
    fearful.append(i["fearful"])
    angry.append(i["angry"])
    surprised.append(i["surprised"])

time = np.array(time)
neutral = np.array(neutral)
happy =np.array(happy)
sad = np.array(sad)
disgusted = np.array(disgusted)
fearful = np.array(fearful)
angry = np.array(angry)
surprised = np.array(surprised)

numpy_data = np.array([time,neutral,happy,sad,disgusted,fearful,angry,surprised])
all_data =[]
for i in range(len(time)):
	all_data.append([ time[i],neutral[i],happy[i],sad[i],disgusted[i],fearful[i],angry[i],surprised[i]])
df = pd.DataFrame(data=np.array(all_data),columns=["time","neutral","happy","sad","disgusted","fearful","angry","surprised"])
dff_agg = df.drop("time",axis=1).mean(axis = 0)
new_df = pd.DataFrame()
new_df["columns"]=df.drop("time",axis=1).columns
new_df["values"]= dff_agg.values
print(new_df)
new_df.plot(kind="bar")
plt.title("Types of emotions")
plt.ylabel('Intensity of emotion emitted')
plt.xlabel('Types of emotions')
sns.barplot(x="columns",y="values",data=new_df)

plt.show()