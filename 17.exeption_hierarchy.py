# exception hierarchy
# relation between the exceptions
arr = [1,2,2,3,4,5]
ans = 0
for i in range(len(arr)):
    ans = ans ^ arr[i]
for i in range(len(arr)):
    ans = ans ^ i

print(ans)
