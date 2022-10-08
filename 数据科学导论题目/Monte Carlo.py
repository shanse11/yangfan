import random
from telnetlib import PRAGMA_HEARTBEAT
S=(1.0-0.0)*3
N=1000000
C=0
for i in range(N):
    x=random.uniform(0.0,1.0)
    y=random.uniform(0.0,3.0)
    if y <=x**2+x**3:
        C+=1
I=C*S/N
print(I)