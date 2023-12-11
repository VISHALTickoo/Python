# LIST

# ARRAY  --- STATIC ( CANNOT CHANGE REMOVE OR ADD)
# LIST. 

# arr[5] = {1,2,3,4,5}
# listt =[n]


# characteristics
#  ordered  ,  mutable -add/rem., heterogeneous , dynamic  , indexed



# 5 types of iteration : 
# for loop using variable
# for loop using range
# while
# list comprehension
# enumeration
# print("            select the iteration         ")


# print("enter the choice : ")
# n=int(input())

#  first method of itertion

# lis = [101,122,21,3]
# for i in lis:
#     print(i)

# # # # second way of iteration 

# leng = len(lis)
# print(leng)

# for i in range(leng):
#     print(lis[i])

# # using while
# i=0
# while i < leng:
#     print(lis[i])
#     i+=1

# # reduce time complexity we use comprehension

# [print(i) for i in lis]



# # enumerate to print/take two inputs in for loop 
# for i ,val in enumerate(lis):
#     print(i,",",val)

#     # another way
# for i in range(leng):
#     print(f"index : {i}   element : {lis[i]}")


# # DICTIONARY

# dict ={
#        "fruit1": "orange",
#        "fruit2": "apple",
#        "fruit3": "grapes"
# }
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# for i,j in dict.items():
#     print("Dictionary values :",j)

# dict1={1:"vishal","2":2000,"1":20,"1":60}
# print(dict1.items())

# dict2={1:40,3:20}
# print(dict2.items())



dic={}
dic["1"]="vishal"
dic["2"]="bknf"
del dic["1"]
print(dic)


d={"key1":1,"key2":2}
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for i in d.items():
    print(i)




# DIVIDE AND CONQER (logn)