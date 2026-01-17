#6️⃣ Exam Result Processing

# You have 12 students marks.
# Find:
# Pass count (marks ≥ 40)
# Fail count
# Top 3 students
# Class average
# You learn
# Sorting, slicing, conditions


import numpy as np
Names=np.array(["Arushi", "Devansh", "Mayank", "Harit","Aman", "Ajay", "Riya", "Sakshi","Karan","Neha","Tanmay","Priya"])
Marks=np.array([56,76,8,19,37,80,26,80,19,70,76,11])
Passed=Names[Marks>=40]
Failed=Names[Marks<40]
Top_3=np.argsort(Marks)[::-1][0:3]
print("PASSED STUDENT :"," ,".join(Passed),"ie -",np.size(Passed),"Students")
print("FAILED STUDENT :"," ,".join(Failed),"ie -",np.size(Failed),"Students")
print("AVERAGE MARKS :",np.mean(Marks))
print("TOP 3 STUDENT :",",".join(Names[Top_3]),"Having MARKS",Marks[Top_3],"respectively")