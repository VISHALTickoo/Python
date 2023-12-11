
# a=10
# b=20

# print("sum of 2 int ",a+b)
# print("sub of 2 int ",a-b)
# print("mul of 2 int ",a*b)
# print("div of 2 int ",a/b)


# if else conditions

# a= int(input())

# if(a%2==0):
#     print("even")
# else:
#     print("odd")

a=[]
b=[]
for i in range(0,20):
    if(i%2==0):
        a.append(i)
    else:
       b.append(i)
print("even",a)
print("odd",b)


# import math

# print("WELCOME TO MINI CALCULATOR ")

# print("ENTER THE TWO numbers ")
# a=int(input())
# b=int(input())

# print("SELECT THE OPERATION TO PERFORM ")
# print("add , sub , mul , div ,rem, log")
# x=str(input())
# x=x.lower()

# if(x=="add"):
#     print("add is ",a+b)
# if(x=="sub"):
#     print("sub is ",a-b)
# if(x=="mul"):
#      print("mul is ",a*b)
# if(x=="div"):
#      print("div is ",a/b)
# if(x=="rem"):
#     print("rem is ",a%b)
# if(x=="log"):
#     print("log is ",math.log(a))
#     print("log is ",math.log(b))


n=int(input("enter the length of array"))
a=[]
for i in range(0,n):
    a.append(int(input()))
# a.sort()
print(a)
for i in range(0,n-1):
  for j in range(0,n-1-i):
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
print(a)