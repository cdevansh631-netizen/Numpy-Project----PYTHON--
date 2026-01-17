#4️⃣ Salary Management System

import numpy as np
Employee=np.array(["Ajay","Dev","Mayank","Harit","Aman"])
Salary=np.array([60000,50000,70000,20000,60000])
Total_Salary=np.sum(Salary)
Average_Salary=np.mean(Salary)
Highest_Paid_Employee=Employee[Salary==np.max(Salary)]
Lowest_Paid_Employee=Employee[Salary==np.min(Salary)]
Earning_more_than_Average=Employee[Salary>Average_Salary]

print("TOTAL SALARY EXPENSE :",Total_Salary)
print("Average Salary OF EMPLOYEES :",Average_Salary)
print("HIGHEST PAID EMPLOYEE :"," , ".join(Highest_Paid_Employee))
print("LOWEST PAID EMPLOYEE :"," , ".join(Lowest_Paid_Employee))
print("EMPLOYEE EARNING MORE THAN AVERAGE SALARY :"," , ".join(Earning_more_than_Average))

