# 8️⃣ Monthly Expense Tracker
# You have expenses for:
# Food, Rent, Travel, Shopping, Bills
# for 12 months.
# Use NumPy to:
# Find total yearly expense
# Average monthly expense
# Most expensive month
# Category with highest spending
# Skills: sum, mean, axis, max
import numpy as np
Expenses_category=np.array(["Food","Rent","Travel","Shopping","Bills"])
Month=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
Expenses=np.array([[2200,6000,2200,3500,2500],[2000,987,3000,4443,2343],[2334,5542,9980,3450,8796],[2300,2200,4400,5500,6000],[330,220,6000,4900,4326],
[2200,6000,2200,3500,2500],[2000,3000,980,4443,2343],[2334,5542,9980,3450,8796],[2300,2200,4400,5500,6000],[330,220,6000,4900,4326],[2300,2200,4400,5500,6000],[330,220,6000,4900,4326]])
Total_Yearly_Expenses=(np.sum(Expenses))
Average_Monthly_Expenses=np.round(np.mean(Expenses,axis=1),2)
Most_Expensive_Month=np.argmax(np.mean(Expenses,axis=1))
Category_most_Expenses=np.sum(Expenses,axis=0)
print("YEARLY EXPENSES :",Total_Yearly_Expenses)
print("AVERAGE MONTHLY EXPENSES :",Average_Monthly_Expenses)
print("MOST EXPENSES MONTH :",Month[Most_Expensive_Month])
print("CATEGORY WITH MOST EXPENSES :",",".join(Expenses_category[Category_most_Expenses==np.max(Category_most_Expenses)]))