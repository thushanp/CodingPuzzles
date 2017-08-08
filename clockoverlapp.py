import datetime as dt, numpy as np
print("At what times do clock hands point in opp. directions?\n")
p = 24/22
for h in np.arange(p/2, 24, p): 
	print(dt.timedelta(hours=h))

print("\n")

print("At what times do clock hands overlap?\n")
p = 24/22
for h in np.arange(0, 24, p): 
	print(dt.timedelta(hours=h))