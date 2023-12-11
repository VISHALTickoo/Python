# List1=[[1,3,4],
#        [2,3,9],
#        [5,6,7]]
# sum=0

# for m in List1:
#     for n in m:
#          print(n,end=" ")
#          sum=sum+n
#     print()
# print(sum)


# TWO LINES SUM

# for i in List1[2]:
#     sum+=i
# print(sum)

    # using list form
            # print(m)
            # n+=1
#             # breake

List1=[[1,3,4],
       [2,3,9],
       [5,6,7]]
sum=0
s=0
for m in List1:
    for n in m:
         print(n,end=" ")
         if(s%2==0):
          sum=sum+n
         s+=1
    print()
print(sum)
print(s)

# # reverse

# List1=[[1,3,4],
#        [2,3,9],
#        [5,6,7]]

# print("original list :"+str(List1))
# k=int(input("Enter row to reverse : "))
# res = []
