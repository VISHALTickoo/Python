# 1)
#  Write a program for Merging two Dictionaries

# Example:
# Input:   3
# 1
# one
# 2  
# two
# 3
# three
# 2
# 4
# four
# 5
# Five

# Output: {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five'}




def merge_dict(dict1,dict2):
    merged={**dict1, **dict2}
    print(merged)
dict1={}
dict2={}
n=int(input("Enter the number of items in dict1 : "))
for i in range(n):
    key=input("Enter Key : ")
    value=input("Enter value: ")
    dict1[key]=value
m=int(input("Enter the number of items in dict2 : "))
for j in range(m):
    key=input("Enter Key : ")
    value=input("Enter value: ")
    dict2[key]=value
merge_dict(dict1,dict2)





# 2)
# You are given a string S. Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, 
# lowercase and uppercase characters.
# Input:  qA2
# Output: In the first line, print True if S has any alphanumeric characters. Otherwise, print False




#  2
str=input("Enter your string: ")
alphanumeric=any(s.isalnum() for s in str)
alphabetical=any(s.isalpha() for s in str)
digits=any(s.isdigit() for s in str)
lowercase=any(s.islower() for s in str)
uppercase=any(s.isupper() for s in str)
print(alphanumeric)
print(alphabetical)
print(digits)
print(lowercase)
print(uppercase)




# 3)
#  Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection.
#  She asked for your help. You pick the stamps one by one from a stack of  country stamps.
# Find the total number of distinct country stamps ?
# Input Format :
# The first line contains an integer N, the total number of country stamps.
# The next N lines contain the name of the country where the stamp is from.
# Output Format :
# Output the total number of distinct country stamps on a single line.

# Example:
# Input: 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France
# Output:
# 5


# 3
n=int(input("Enter The Total number of country stamps : "))
country_stamp=set()
for i in range(0,n):
    country_name=input("Enter the "+ str(i+1) +" country stamp Name : ")
    country_stamp.add(country_name.upper())
print("Total Number Of Distinct Country Stamps : ",len(country_stamp))







# 4)
# Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English 
# newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed
#  to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

# Input Format
# The first line contains the number of students who have subscribed to the English newspaper.
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper.
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

# Output Format
# Output the total number of students who are subscribed to the English newspaper only.










# 4
n=int(input("Enter total students of english :"))
english=set(map(int, input("Enter roll number of English students(seprated by space)").split()))
m=int(input("Enter total students of french :"))
french=set(map(int, input("Enter roll number of French students(seprated by space)").split()))
only_english=len(english-french)
print("Total number of students who are subscribed to the English newspaper : ",only_english)







# 5) 
# Write a Python program to implement a linear search algorithm to find the position of a specific element in a list.
#  Prompt the user to enter a list of numbers and a target value to search for. If the target value is found, print its position; 
# otherwise, print a message indicating that the value is not in the list.And print all occurrences of the target value in the list 
# along with their Positions.

# Input1 : 
# First line     - given list as “n”
# Second line - target
# Output 1:
# Find the target element and print the index position of the target  




# # 5
list=[]
index=[]
n=int(input("Enter Number of Elements in List = "))
for i in range (n):
    num=int(input("Enter element ="))
    list.append(num)
element=int(input("Enter Elements to find in list = "))
for j,item in enumerate(list):
    if item == element:
        index.append(j)
if index==[]:
    print("The target value ",element," is not in the list.")
else:
    print("The target value ",element,"  is found at positions:",index)



# 6)
#  Write a program to read a list of words and return the longest word.
# Input1:
# 4
# Apple
# Grape
# Kiwi
# Orange
# Output :
#  Orange




#6
list=[]
n=int(input("Enter Number of Elements in List = "))
for i in range (n):
    num=input("Enter element =")
    list.append(num)
longest_word=""
for j in list:
    if (len(j)>len(longest_word)):
        longest_word=j
print("Longest word :",longest_word)



# 7) Write a program to reverse k-th column in a matrix
# Input 1:
# Column no:1
# 11 12 13
# 14 15 16
# 17 18 19

# Output 1:
# 17 12 13
# 14 15 16
# 11 18 19




#7
matrix=[[11,12,13],[14,15,16],[17,18,19]]
# print(len(matrix))
print("Original Matrix : ")
for row in matrix:
    print(row)

k=int(input("Enter kth column = "))
k=k-1

column_values=[]
for row in matrix:
    column_values.append(row[k])

reversed_column=list(reversed(column_values))

for i in range(len(matrix)):
    matrix[i][k]=reversed_column[i]
print("Original Matrix : ")
for row in matrix:
    print(row)





# 8) Super Ascii String
# In the Byteland country a string "S" is said to be a SUPER ASCII string if and only if the count of each character in the
#  string is equal to its ASCII value.
# In the Byteland country ASCII code of 'a' is 1, 'b' is 2, ... 'z' is 26.
# Your task is to find out whether the given string is a SUPER ASCII string or not.
# Example:
# Input:
# abbccc
# Output:
# super ASCII
# aabbcc


#8
str=input()
char_count=[0]*26
ascii=True
for char in str:
    if('a'<=char<='z'):
        char_count[ord(char)-ord('a')]+=1
for i in range(26):
    if(char_count[i]!=0 and char_count[i]!=i+1):
        ascii=False
        break
if ascii==True:
    print("Super ASCII")
else:
    print("Not Super ASCII")




# ARMSTRONG /NOT

def is_armstrong_number(number):
  
    num_str = str(number)
    
    num_digits = len(num_str)
    
    armstrong_sum = 0
    
    
    for digit_char in num_str:
        digit = int(digit_char)  
        armstrong_sum += digit ** num_digits
    
    return number == armstrong_sum

# Input from the user
num = int(input("Enter an integer: "))

if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")




# Q write a program to create a mini calculator to perform the arithmetic operations only.(Only using by functions ) //[+ ,- , *, / ,%]


# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Function to perform modulo
def modulo(x, y):
    if y == 0:
        return "Error: Modulo by zero"
    return x % y

# Main function to get user input and perform calculations
def cal():
    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'modulo' for modulo")
        print("Enter 'quit' to end the program")
        
        user_input = input(": ")
        
        if user_input == "quit":
            break
        
        if user_input in ("add", "subtract", "multiply", "divide", "modulo"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if user_input == "add":
                print("Result:", add(num1, num2))
            elif user_input == "subtract":
                print("Result:", subtract(num1, num2))
            elif user_input == "multiply":
                print("Result:", multiply(num1, num2))
            elif user_input == "divide":
                print("Result:", divide(num1, num2))
            elif user_input == "modulo":
                print("Result:", modulo(num1, num2))
        else:
            print("Invalid input")

cal()



# Write a program to print the index values and   count vowels ( Case sensitive) in given Strings.
def count_vowels_and_print_indices(input_string):
    vowels = "AEIOUaeiou"

    vowel_counts = {vowel: 0 for vowel in vowels}

    # Iterate through the characters of the input string and count the vowels
    for i, char in enumerate(input_string):
        if char in vowels:
            vowel_counts[char] += 1

    # Print the vowel counts
    for vowel, count in vowel_counts.items():
        print(f"{vowel}: {count} occurrences")

    # Print the index values of vowels in the string
    for i, char in enumerate(input_string):
        if char in vowels:
            print(f"Index {i}: '{char}'")

# Input from the user
input_string = input("Enter a string: ")

# Call the function to count vowels and print their indices
count_vowels_and_print_indices(input_string)



# Write a program to remove duplicates elements in a given list.

def remove_duplicates(input_list):
    return list(set(input_list))

# Input list with duplicates
input_list = [1, 2, 2, 3, 4, 4, 5]

# Call the function to remove duplicates
result_list = remove_duplicates(input_list)

# Print the list without duplicates
print(result_list)

# ---------------------------------------

def remove_duplicates(input_list):
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list

# Input list with duplicates
input_list = [1, 2, 2, 3, 4, 4, 5]

# Call the function to remove duplicates
result_list = remove_duplicates(input_list)

# Print the list without duplicates
print(result_list)
