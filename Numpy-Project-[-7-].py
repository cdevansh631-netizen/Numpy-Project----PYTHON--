
#7️⃣ Profit & Loss Calculator
#You have:
# cost = [50, 40, 60, 30]
# sell = [70, 30, 80, 20]
# Find:
# Profit or loss for each product
# Total profit
# Product with highest profit
# You learn
# Subtraction, sum, max
 
import numpy as np
Product=np.array(["ICE-CREAM","SHAKE","TOFEE","MANGO"])
Cost=np.array([50,40,60,30])
Sell=np.array([70,30,80,20])
A=np.subtract(Sell,Cost)
print("Profit of",",".join(Product[A>=0]),"having selling price",Sell[A>0],"and Cost",Cost[A>0],"is",A[A>=0])
print("Loss of",",".join(Product[A<0]),"having selling price",Sell[A<0],"and Cost",Cost[A<0],"is",A[A<0])
print("Total Profit :",np.sum(A))
print("Product with Highest Profit :",Product[A==np.max(A)],"With",np.max(A))