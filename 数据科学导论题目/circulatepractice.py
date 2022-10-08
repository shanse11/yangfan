l=[1,2,3,4,5]
#for循环倒序输出
for i in range(len(l)):
    print(l[len(l)-i-1])
#用while循环倒序输出
i = len(l)-1
while i >= 0 :
    print(l[i])
    i-=1
#使用切片法倒序输出
print(l[::-1])