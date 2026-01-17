#3️⃣ Temperature Data Analysis


#Using where,loop:-
import numpy as np
Days=np.array(["DAY1","DAY2","DAY3","DAY4","DAY5","DAY6","DAY7","DAY8","DAY","DAY10","DAY11","DAY12","DAY13","DAY14","DAY15","DAY16","DAY17","DAY18","DAY19","DAY20","DAY21","DAY22","DAY23","DAY24","DAY25","DAY26","DAY27","DAY28","DAY29","DAY30"])
Temp=np.array([22, 4, 24, 25, 26,27, 28, 29, 30, 311,32, 33, 34, 35, 36,35, 311, 33, 32,32,311,4,35,36,37,38,7,57,4,43])

Index_of_Hottest_Temp=np.where(Temp==np.max(Temp))[0]
Index_of_Collest_Temp=np.where(Temp==np.min(Temp))[0]
Average_temp=np.mean(Temp)
Temp_above_35=np.where(Temp>35)[0]
Hottest_day=[]
Collest_day=[]
Days_Above_35_degree=[]
for i in Index_of_Hottest_Temp:
    Hottest_day.append(str(Days[i]))
for i in Index_of_Collest_Temp:
    Collest_day.append(str(Days[i]))
for i in Temp_above_35:
    Days_Above_35_degree.append(str(Days[i]))

print("Hottest_Days :",Hottest_day)
print("Collest_Days :",Collest_day)
print("Average_Temp :",Average_temp)
print("Days Above 35 degree :",Days_Above_35_degree)



#Using boolean indexing:
Days=np.array(["DAY1","DAY2","DAY3","DAY4","DAY5","DAY6","DAY7","DAY8","DAY","DAY10","DAY11","DAY12","DAY13","DAY14","DAY15","DAY16","DAY17","DAY18","DAY19","DAY20","DAY21","DAY22","DAY23","DAY24","DAY25","DAY26","DAY27","DAY28","DAY29","DAY30"])
Temp=np.array([22, 4, 24, 25, 26,27, 28, 29, 30, 311,32, 33, 34, 35, 36,35, 311, 33, 32,32,311,4,35,36,37,38,7,57,4,43])

Hottest_days=Days[Temp==np.max(Temp)]
Collest_days=Days[Temp==np.min(Temp)]
Average_Temp=np.mean(Temp)
Day_temp_above_35=Days[Temp>=35]
print("Hottest_Days :",Hottest_days)
print("Collest_Days :",Collest_days)
print("Average_Temp :",Average_Temp)
print("Days Above 35 degree :",Day_temp_above_35)
