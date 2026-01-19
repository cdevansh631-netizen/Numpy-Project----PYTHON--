# 🔟 Electricity Bill Analysis
# You have daily units used for 7 days.
# Find:
# Total units
# Average daily usage
# Days where usage was high (> threshold)
# Predict next month average(28 Days)
# Skills: sum, mean, conditions

import numpy as np
Days=np.array(["DAY 1","DAY 2","DAY 3","DAY 4","DAY 5","DAY 6","DAY 7"])
Units=np.array([14,5,22,9,13,15,12])
Threshold_usage=7
print("TOTAL UNITS USAGE :",np.sum(Units))
print("AVERAGE DAILY USES :",np.round(np.mean(Units),2))
print("DAYS WHEN USAGE MORE THAN THRESHOLD USAGE :",", ".join(Days[Units>Threshold_usage]))
print("NEXT MONTH AVERAGE USAGE :",np.round(28*np.mean(Units),2))



 