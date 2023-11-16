arr=[]
n=int(input('Enter N: '))
for i in range(n):
    item=int(input('enter number in list: '))
    arr.append(item)
sum=0
for j in range(len(arr)):
    sum += arr[j]
avg=sum/n
print(avg)
# print(sum)
# print(arr)

# mylist=[1,2,3,4,5,6]
# sum=0
# for i in range(len(mylist)):
#     sum += mylist[i]
# print(sum)