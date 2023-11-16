import array
arr=array.array('i',[0,1,2,3,4,5,6,7,8,9])
def traverseArr(array):
    for i in range (len(array)):
        print(array[i])
traverseArr(arr)