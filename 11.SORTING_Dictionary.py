import copy
mydict={'3':1 ,'2':3 , '1':2}
# sorteddict =dict(sorted(mydict.items()))
# print(sorteddict)

# sortboth =  dict(sorted(mydict.items(), key =lambda item: item[1]))  #0--key,1--value
# print(sortboth)



# # COPYING COLLECTION
# list1 = [1,2,3,4,5]
# copied_list = list1[:]
# print(copied_list)

# list11 = [1,2,3,4,5]
# copied_list1 = list(list11)
# print(copied_list1)

# list2 = [[1,2] [3,4,5]]

# list = [1,2,3,4,[6,7,[9,0],8]]
# list2 = copy.deepcopy(list)
# list2 = list[4][2]
# print(list2)

# Python3 Program to check whether a
# given key already exists in a dictionary.
 

def checkKey(dic, key):

    if key in dic.keys():

        print("Present, ", end =" ")

        print("value =", dic[key])

    else:

        print("Not present")

         
# Driver Code

dic = {100: 'arjun', 200:'karan', 300:'chand'}

key = 200
checkKey(dic, key)
 

# key = 'w'
# checkKey(dic, key)