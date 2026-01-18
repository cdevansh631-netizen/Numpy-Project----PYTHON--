# 9️⃣ Cricket (or Sports) Score Analyzer
# You have scores of a player in 10 matches.
# Find:
# Average score
# Highest score
# Matches where score > 50
# Consistency (std deviation)
# Skills: mean, max, filtering, std

import numpy as np
Matches=np.array(["MATCH 1","MATCH 2","MATCH 3","MATCH 4","MATCH 5","MATCH 6","MATCH 7","MATCH 8","MATCH 9","MATCH 10"])
Score=np.array([54,0,0,70,65,112,104,93,27,124])
print("AVERAGE SCORE IN LAST 10 MATCHES :",np.mean(Score))
print("HIGHEST SCORE :",np.max(Score))
print("MATCHES WHERE SCORE >50 :",", ".join(Matches[Score>50]))
print("CONSISTENCY :",np.round(np.std(Score),2))


