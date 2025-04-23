import math
L=eval(input("Enter the lower limit:"))
U=eval(input("Enter the upper limit:"))
H=eval(input("Enter the height:"))
x=[]
y=[]
x.append(L)
while L<U:
    L=L+H
    R=round(L,2)
    x.append(R)
print(x)
for i in x:
    L=math.log(i)
    R=round(L,4)
    y.append(R)
print(y)
e=[]
o=[]
length=len(y)
for j in range(2,length,2):
    e.append(y[j])
    
for k in range(1,length,2):
    o.append(y[k])
s1=sum(e)
s2=sum(o)
s3=(y[0]+y[length-1])
f=s3+(2*s1)+(4*s2)
h=H/3
ans=f*h
ans=round(ans,4)
print("answer",ans)
