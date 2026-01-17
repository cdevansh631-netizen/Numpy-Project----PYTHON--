#5️⃣ Product Inventory System

# You have product stock:
# stock = [50, 3, 20, 7, 100]
# Find:
# Products running low (stock < 10)
# Products in excess (stock > 50)
# You learn
# Boolean indexing


import numpy as np
Product=np.array(["Fortuner","Land_Cruiser","Innova","Hilux","Alto"])
Stocks=np.array([50,3,20,7,100])
print(" , ".join(Product[Stocks<10]),"having low stocks which is ",Stocks[Stocks<10])
print(" , ".join(Product[Stocks>50]),"Having excess stocks which is ",Stocks[Stocks>50])

 