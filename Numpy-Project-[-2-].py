#2️⃣ Student Marks Analyzer
# You have marks of students in subjects:
# marks = [[70, 80, 60],
#          [90, 85, 88],
#          [50, 45, 60]]
# Find:
# Average marks per student
# Average per subject
# Highest scorer
# Failed students
# You learn
# axis, mean, max, filtering
import numpy as np
Marks=np.array([[70,80,60],[11,2,8],[50,45,60]])
AVGMARK=np.mean(Marks,axis=1)
AVGSUB=np.mean(Marks,axis=0)
Highest_Score=np.round(np.max(AVGMARK),2)
fd=AVGMARK<21


print("AVERAGE MARKS OF STUDENTS : ",np.round(AVGMARK,2))
print("AVERAGE MARKS PER SUBJECT : ",np.round(AVGSUB,2))
print("HIGHEST SCORER :",Highest_Score,'HAVING INDEX',np.argmax(AVGMARK))
print("STUDENT GOT FAILED : ",AVGMARK[fd],"HAVING INDEX",np.where(fd)[0])
