# ATM

# # #1    MERGED
def merged(dict1,dict2):
    merge={**dict1,**dict2}
    print(merge)
dict1={}
dict2={}

n=int(input("enter the no. of elements in dict1 :"))
for i in range(n):
    keys=input("eneter key ")
    value=input("enter value ")
    dict1[keys]=value
m=int(input("enter the no. of elements in dict2 :"))
for j in range(m):
    keys=input("eneter key ")
    value=input("enter value ")
    dict2[keys]=value
merged(dict1,dict2)  

# #2  ALPHA...
string =input("enter the string : ")
alphanumeric = any(s.isalnum() for s in string) 
alphabetical = any(s.isalpha() for s in string) 
digital = any(s.isdigit() for s in string) 
lower= any(s.islower() for s in string) 
upper = any(s.isupper() for s in string) 
print(alphanumeric)
print(alphabetical)
print(digital)
print(lower)
print(upper)


# #3. stamp

n=int(input("enter the total stamps of countries :"))
country_stamp=set()
for i in range(n):
    countryname = input(f"enter the {i+1} country name of the stamp : ")
    country_stamp.add(countryname.upper())
print("the total distinct country name ", len(country_stamp))

# #4.   newspaper
n=int(input("enter the english newspaper students : "))
eng=set(map(int, input("enter the roll no. for english subscribe students : ").split()))
m=int(input("enter the french newspaper students : "))
fren=set(map(int, input("enter the roll no. for french subscribe students : ").split()))
only_eng = len(eng-fren)
print("the students subscribe to eng only ",only_eng)



# #5. lsearch
# list=[]
# index=[]
# n=int(input("no. element : "))
# for i in range(n):
#     num=int(input("enetr no. :"))
#     list.append(num)
# m=int(input("enter vale to find : "))
# for j,item in enumerate(list):
#     if item==m:
#         index.append(j)
# if index==[]:
#    print(f"the element {m} not found in list")
# else:
#     print(f"element {m} found at index {index}")


# # #6.  word
# list=[]
# n=int(input("enter no of elements :"))
# for i in range(n):
#     num=input("enter data :")
#     list.append(num)
# longest=""
# for j in list:
#     if(len(j)>len(longest)):
#         longest=j
# print(longest)


# n= int(input("enetr th english stude,"))
# eng=set(map(int,input("enter the roll").split()))

# m= int(input("enetr th french stude,"))
# fre=set(map(int,input("enter the roll").split()))

# only_eng=len(eng-fre)
# print("only eng",only_eng)



n=int(input("enter the country stamp"))
country_stamp=set()
for i in range(n):
    countryname=input(f"enter the {i+1} country name")
    country_stamp.add(countryname.upper())
print(len(country_stamp))
# #7.matrix

# matrix = [[11,12,13],[14,15,16],[17,18,19]]

# print("o m")
# for rows in matrix:
#     print(rows)

# k=int(input("enetr column"))
# k=k-1

# colu_value=[]
# for rows in matrix:
#     colu_value.append(rows[k])

# reversed_column=list(reversed(colu_value))

# for j in range(len(matrix)):
#     matrix[j][k]=reversed_column[j]


# print("o m")
# for rows in matrix:
#     print(rows)



# # # #8.ascii
# str=input("")
# char_count=[0]*26
# ascii=True
# for char in str:
#     if('a'<=char<='z'):
#         char_count[ord(char)-ord('a')]+=1#-------------------------------character count
# for i in range(26):
#     if(char_count[i]!=0 and char_count[i]!=i+1):#--------------------------checking with asciii
#         ascii=False
#         break
# if ascii==True:
#     print("super ascii")
# else:
#     print("not super ascii")


# # 9.asrmstrong

# def armstrong(n):
#     num=str(n)
#     length=len(num)
#     sum=0

#     for char in num:
#         digit=int(char)
#         sum+=digit ** length

#     return n == sum
# n=int(input())
# if armstrong(n):
#     print(f"{n} is armstrong")
# else:
#     print("not")



# # 10.calcu
# def add(x,y):
#     return x+y
# def modulo(x,y):
#     if y==0:
#       return "error"
#     return x%y

# def cal():
#     while True:
#      print("options")

#      user = input("enter choic3e : ")
#      if user=="quit":
#         break
#      if user in("add","modulo"):
#       num=float(input(" "))
#       num2=float(input(" "))
     
#       if user=="add":
#         print("result ",add(num,num2))
#       elif user=="modulo":
#         print("result",modulo(num,num2))
#      else:
#         print("invalid")
# cal()


# # #11. vowels index  count
# def count_vowels_and_print_indices(input_string):
#     vowels = "AEIOUaeiou"

#     vowel_counts = {vowel: 0 for vowel in vowels} #------------------------------------

#     # Iterate through the characters of the input string and count the vowels
#     for i, char in enumerate(input_string):
#         if char in vowels:
#             vowel_counts[char] += 1

#     # Print the vowel counts
#     for vowel, count in vowel_counts.items():
#         print(f"{vowel}: {count} occurrences")

#     # Print the index values of vowels in the string
#     for i, char in enumerate(input_string):
#         if char in vowels:
#             print(f"Index {i}: '{char}'")

# # Input from the user
# input_string = input("Enter a string: ")

# # Call the function to count vowels and print their indices
# count_vowels_and_print_indices(input_string)



# # #12.  
# # Write a program to remove duplicates elements in a given list.

# def remove_duplicates(input_list):
#     return list(set(input_list))

# input_list = [1, 2, 2, 3, 4, 4, 5]

# result_list = remove_duplicates(input_list)

# print(result_list)








# # ascii

# str=input(" enter str : ")
# char_count=[0]*26
# ascii =True
# for char in str:
#     if('a'<=char<='z'):
#       char_count[ord(char)-ord('a')]+=1
# for i in range(26):
#     if(char_count[i]!=0 and char_count[i]!=i+1):
#         ascii=False
#         break
# if ascii==True:
#     print(f"{str} is a super asciii")
# else:
#     print("NOt super")




# # matrix
# m=[[11,2,3],[14,5,6],[17,8,9]]
# for row in m:
#     print(row)
# k=int(input("enter c"))
# k=k-1

# col_v=[]
# for row in m:
#     col_v.append(row[k])

# rev=list(reversed(col_v))

# for j in range(len(m)):
#     m[j][k]=rev[j]
# for row in m:
#     print(row)
# # ----------------
# def reversed_row(m,k):
#   if(k<0 or k>len(m)):
#     print("INVALID")
#     return
#   else:
#     m[k] =m[k][::-1]


# m=[[11,2,3],[14,5,6],[17,8,9]]
# for row in m:
#     print(row)
# k=int(input("enter r"))
# k=k-1

# reversed_row(m,k)
# for row in m:
#     print(row)



# vowels index value and count value

# def counti(str):
#     vowels="AEIOUaeiou"

#     vowel_count={vowel:0 for vowel in vowels}

#     for i,char in enumerate(str):
#         if char in vowels:
#             vowel_count[char]+=1
    
#     for vowel,char in vowel_count.items():
#         print(f"{vowel}:{char}  occcurence")

#     for i,char in enumerate(str):
#         if char in vowels:
#             print(f"index{i}:{char}")
# str=input("")
# counti(str)
