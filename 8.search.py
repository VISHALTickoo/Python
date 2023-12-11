# LINERA SEARCH 
lis = [1,2,3,43,4]
x=int(input("ENTER ELEMENT : "))
for i in range(len(lis)):
     if(lis[i]==x):
        print("element found at index",i)
        break
else:
        print("element not found")


# BINARY SEARCH      (DIVIDE & CONCQER)

# def binary(list2,x):
#  some=-1
#  i=0
#  j=len(list2)-1
#  while i <= j:
#   mid =(i+j)//2
#   if(list2[mid]==x):
#     some==x
#     break
#   elif(list2[mid]>x):
#         j=mid-1
#   else:
#         i=mid+1
#   return some

# list2 = [1,2,3,4,5,6,7,8,9,10]
# x=int(input("ENTER ELEMENT : "))

# res= binary(list2,x)
# if(res==-1):
#     print("The Element is not found")  
# else:
#     print("Found")



def bsearch(a,t,n):
  start=0
  end=n-1

  while start<=end:
   mid=(start+end)//2
   if(a[mid]==t):
    return mid
   elif(a[mid]>t):
    end=end-1
   else:
    start=start+1
  return -1  

a=[]
n= int(input("Enter the no. of elements in an array:"))
for i in range(0,n):
  z=int(input())
  a.append(z)
# print(a)  

t=int(input("enter the target : "))
result=bsearch(a,t,n)

if result!=-1:
  print(f"Element {t} found at index {result}")
else:
    print(f"Element {t} not found in array")




