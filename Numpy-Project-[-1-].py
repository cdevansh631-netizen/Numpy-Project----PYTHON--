#NUMPY REAL TIME PROJECT:--
# 1️⃣ Sales Analysis System
# What you do
# You have:
# price = [10, 20, 30, 40]
# quantity = [3, 5, 2, 4]
# Use NumPy to:
# Find total sales of each product
# Find total revenue
# Find highest selling product
# You learn
# array, *, sum, max

import numpy as np
Prices=[20,93,20,59,65,34,23,50]
Sales=[4,4,4,5,6,6,9,3]
Arr=np.array([Prices,Sales])
Revenue=np.prod(Arr,axis=0)
C=np.max(Sales)
Index=np.argmax(Sales)
print("Total Sales of Each product :",Revenue)
print("Total Revenue :",np.sum(Revenue))
print("Highest Sales :",C,"Having index ",Index)





