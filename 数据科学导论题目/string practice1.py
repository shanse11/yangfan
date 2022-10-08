s=input("please enter a string:")
last=None
count = 1
max = 1
a=None
for i in s:
    if i==last:
        count+=1
    else:
        max=max(count,max)
        count=1
        a=last
    last=i
if count>max:
    a=last
    max=max(count,max)
print(max,a)
