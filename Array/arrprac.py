#extend array
from array import *
arr1=array('i',[1,2,3,4,5,6])
print(arr1)
arr2=array('i',[11])
arr1.extend(arr2)
print(arr1)
arr1.append(11)
arr1.append(11)
arr1.append(11)
arr1.append(11)
print(arr1)
print(arr1.count(11))