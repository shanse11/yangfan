#方法一
import math
a=pow(2,1/2)
print(a)
#方法二
c=2
for i in range(0,c+1):
    if i**2<c and (i+1)**2>c:
        g=i
while(abs(g**2-c)>0.0001):
    g+=0.0001
print(g)
#方法三
i=0
c=2
m_max=c
m_min=0
g=(m_min+m_max)/2
while(abs(g**2-c)>0.00000001):
    if(g**2<c):
        m_min=g
    else:
        m_max=g
    g=(m_min+m_max)/2
    i+=1
print(g)