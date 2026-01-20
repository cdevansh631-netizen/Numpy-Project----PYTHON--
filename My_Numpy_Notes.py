import numpy as np
# l1=np.array([2,6,4])
# l2=np.array([4,9,7])
# print(l1*l2)


#Slicing:(-1-)

# arr=np.array([[54,78,1,6],[87,9,43,54]])
# print(arr[0])  #[54,78,1,6]
# print(arr[1,2]) #43
# print(arr[1,0:2]) #[87 9]
# print(arr[0,1:3]) #[78 1]
# print(np.array([arr[0,1:3],arr[1,0:2]]))  #[[78 1] [87 9]]




#Attribute:(-2-)
# arr=np.array([[54,78,1,6],[87,9,43,54]])
# print(np.shape(arr))   #(row,column)--(2,4)
# print(np.size(arr))    #No of element---8
# print(np.ndim(arr))    #No of dimension.
# print(arr.dtype)       #data type



#Insepecting in an array:(-3-)
#arr=np.array([[54,78,1,6],[87,9,43,54]])
#print(len(arr))          #2
#print(arr.astype(float))   #covert float into int and int into float not for string.




#Funtion/mathematical operation on array:(-4-)
# A=np.array([23,45,75,34])
# B=np.array([4,32,1,39])

# #ADDITION:
# print(A+B)
# print(np.add(A,B))

# #SUBSTRACTION:
# print(A-B)
# print(np.subtract(A,B))

# #MUTIPLICATION:
# print(A*B)
# print(np.multiply(A,B))

# #Division:
# print(A/B)
# print(np.divide(A,B))

# #Power:
# arr1=np.array([7,9,3])
# arr2=np.array([2])
# print(np.power(arr1,arr2))

# #Sq--R00t:
# arr1=np.array([9,64,81])
# print(np.sqrt(arr1))






#Combining and Splitting an array:(-5-)

#Concatenate:
# A=np.array([[23,4],[84,2]])
# B=np.array([[23,4],[7,9]])
#print(np.concatenate([A,B])) #By default axis=0..ie-column
# print(np.hstack([A,B]))   #  By default axis=0.column concatenation.
# print(np.concatenate([A,B],axis=1))  #By default axis=1 ir-rows
# print(np.vstack([A,B]))    #By default axis=1..vertical concatenation.

#SPITTING OF AN ARRAY :
#1-D:--
# A=np.array([[87,43,21,9,87,21,5]])
# X=np.array_split(A,5,axis=1)
# print(X)
#2-D
# A=np.array([[87,43,21],[9,21,5]])
# X=np.array_split(A,4,axis=0)
# print(X)






#ADDING AN REMOVING ELEMENT IN ARRAY:(-6-)

#append:-
#1-D:
#a=np.array([65,98,78,23])
#print(np.append(a,99))
#print(np.append(a,[47,9]))
#2-D:
# a=np.array([[98,45,90,2],[98,35,19,4]])
# print(np.append(a,[8,6])) #firstly convert 2D int 1D then add elenents it..8,6


#Inserting:
#1D:-
# a=np.array([98,78,4,8])
# print(np.insert(a,2,99))  #(array,indx,value)
#2D:-
# a=np.array([[56,98,21],[9,1,5]])
#print(np.insert(a,2,[12,34],axis=1))   #vertically..NO of row==no inserted
#print(np.insert(a,2,[12,7,6],axis=0))    #horizontally.....NO of column==no inserted
#print(np.insert(a,[1,2],59,axis=0))    #  

#deleting:
#a=np.array([[56,98,21],[9,1,5]])
#print(np.delete(a,1,axis=1))
#print(np.delete(a,0,axis=0))



 

#SORT FILTER AND SEARCH:(-7-)

#Sorting:--sort in acc order:
#arr=np.array([12,3,45,3,64,75,34])
#print(np.sort(arr))
#orint(np.argsort(arr)) #Give indices of sorted array

#Searching:-give index of searched number:-
#ar=np.array([12,3,45,3,64,75,34])
#print(np.where(ar==3))

#Search sorted:
#ax=np.array([1,3,5,8,90])
#print(np.searchsorted(ax,))#array sorted hona chauiya:

#Fillter:--
#np.where(fd)[0])  #GIVE index in filtering case here fd Avg>20 ie.condition
#np.where(Avg>20,"PAss","FAil")   #Return pass if satisfy condition else fail
# ar=np.array([20,30,40,50])
# #1--:
# fs=[True,False,True,False]
# new=ar[fs]
# print(new)
#2--:
# fd=ar>49
# new=ar[fd]
# print(new)






#Agregate function:--(-8-)
# arr=np.array([1,4,4,5,6,7,8,9,23,45,9])
# #1--sum Gives
# print(np.sum(arr))
# #2--give maximum:
# print(np.max(arr))
# print(np.argmax(arr)) # Arr ma max value ka index dega.
# #3__give min:
# print(np.min(arr))
# #4--No of element in array:
# print(np.size(arr))
# #5--mean
# print(np.mean(arr))
# #5--commmulative sum:
# print(np.cumsum(arr))
# #6--Cummulatiive product:
# print(np.cumprod(arr))


#example:
# product=np.array([12,4,5,7,34,6,94,6])
# price=np.array([10,20,30,40,10,23,9,5])
#print(product,"\n",price)
# c=np.cumprod([product,price],axis=0)
# print(c)
# print(c[1].sum())




#Statical function:(-9-)

#Statical function:---
# Food=[12,4,57,64,2,78,24,57,24,24,67]
# A=np.array(Food)
#1--mean-
# print(np.mean(A))

#2-median:
# print(np.median(A))#firstly sort then calculate median:--

#3-mode:mode naam ka function hi hota import krna pdta ha ek liberary sa:ie-statistics:--
# import statistics as st
# print(st.mode(A))

#4:-standard deviation-[sd]:--how much our value fluctuate form mean value:
# print(np.std(A))
# 5-:variance:sd=root of var
# print(np.var(A))

#6:-Cofficiend of co-relation:-
#-1 Represent inversly proprtional relation:
#+1 Represent proportional relationshhip:
#0 mean no relationship.
# Tobacoo_consumption=[10,55,30,90,50,60]
# Death=[2,17,7,8,14,16]
# print(np.corrcoef([Tobacoo_consumption,Death]))




#Changing Row and column acocurding to our choice:(10)
# import numpy as np
# A=np.array([12,44,64,2,7,34])
# A.shape=(3,2)
# print(A)
#print(np.reshape(A,(3,2)))



#print NO of Zeros/one u want in 1D/more--D:(-11-)
# import numpy as np
# print(np.ones((1,4)))
# print(np.zeros((6,8)))
#print(np.zeros((2,3,5)))   #(no of time,rows,column)

#print(numpy.identity(3))#print identity tringle.
# print(numpy.eye(8,8,k=-4))#k-+ve for upper tringle/ k>-vefor lower tringle.





#Floor,ceil,rint:-(-12-)

# arr=np.array([1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9])
# print(np.floor(arr)) #convert into floor either its 1.1 or 1.9 it give 1-[1.,2.,3.,4.,5.,6.,7.,8.,9.,10.]
# print(np.ceil(arr))  #convert into ceil either its 2.3 or 2.9 it give 3-[2.,3.,4.,5.,6.,7.,8.,10.]
# print(np.rint(arr))  #proper roud off each value as in math




#Sum and products along axisess:(-13-)

#For Sum:
# A=np.array([[2,4],[3,7]])
# print(np.sum(A,axis=0))  #[5,11]
# print(np.sum(A,axis=1))  #[6,10]
# print(np.sum(A,axis=None))  #16
# print(np,sum(A))            #16

#For Product:
# A=np.array([[2,4],[3,7]])
# print(np.prod(A,axis=0))  #[6,28]  
# print(np.prod(A,axis=1))  #[8,21]
# print(np.prod(A,axis=None)) #168
# print(np.prod(A))  #168

#for Max:-[-SIMILIER FOR MIN-]
# A=np.array([[2,4],[3,7]])
# print(np.max(A,axis=0)) #[3,7]
# print(np.max(A,axis=1)) #[4,7]
# print(np.max(A,axis=None)) #7
# print(np.max(A)) #7   




#Inner And Outer Product:- (-14-)
# A=np.array([[1,4]])
# B=np.array([[1,2]])
# print(np.inner(A,B))  #[Scaler/Dot Product]
# print(np.outer(A,B))  #[a1b1 a1b2 /n a2b1 a2b1]




#POLYNOMIAL ATTRIBUTES-(Applicable in 1D only)-(-15-)

#1-(POLY)
# arr=np.array([-2,-5])
# print(np.poly(arr)) #It give Cofficient of a polynomial if -2,-5 are roots of polynomial.

#2-(roots):--
# arr=np.array([1,7,10])
# print(np.roots(arr)) #it give Root of polynomial if 1,7,10 are Coff of polynomial.

#3-(polyint):--
# arr=np.array([3,2,1])
# print(np.polyint(arr)) #Take [3,2,1] as Coff of polynomial then integerate it hence give Coff of integerated polynomial.+c=0(Default)

#4-(polyder):--
# arr=np.array([1,1,1,1])
# print(np.polyder(arr)) #Take [1,1,1,1] as Coff of polynomial then derevate it hence give Coff of derivated polynomial.

#5-(polyval):
# arr=np.array([1,-2,0,2])
# print(np.polyval(arr,4)) #value of polynomial at specific value.

#6-(polyfit):--
# A=np.array([1,2,3,4])
# B=np.array([2,5,10,17])
# print(np.round(np.polyfit(A,B,2),1))   #Polyfit Establist a relation BW A and B and give us COFF of poly function.
# print(np.poly1d(np.round(np.polyfit(A,B,2),1)))   #[-poly1d-]give poly in this form y=x2+1

#7-(Poly-add/division/multiply/subtract):-
# arr1=np.poly1d([1,2,6])
# arr2=np.poly1d([2,3,6,7])
# print(np.polyadd(arr1,arr2)) #Add both polynomial.
# print(np.polydiv(arr2,arr1))   #give division of 2 poly in form ((Quoient),remainder())
# print(np.polymul(arr1,arr2))    #mltiply 2 polynomial.
# print(np.polysub(arr1,arr2))     #Subtract

#POLYMUL:--
# a=np.array([1,2,6])
# b=np.array([2,3,6,7])
# print(np.polymul(a,b))  _#[-You can do same as you do above with this it give output in this [number] form-]





#Determinent,eigen value/vector ,inverse-[-16-]
# ar1=np.array([[1,2],[2,1]])
#1-(-Determinent-)
# print(np.round((np.linalg.det(ar1)),2))    #Give Determinant..

#2-(-Eigen value-)
# Val,Vector=np.linalg.eig(ar1)
# print(Val)
# print(Vector)
# print(np.linalg.eig(ar1)) #It always give eigen vector and Eigen Value Simultaneously.

#3-(-inverse-)
# print(np.linalg.inv(ar1))  #inverse of matrix..










