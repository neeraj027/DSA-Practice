class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+=' -> '
            temp_node=temp_node.next
        return result

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
        
    def insert(self,value,index):
        new_node=Node(value)
        if index<0 or index>self.length:
            return False
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        
        elif index==0:
            new_node.next=self.head
            self.head=new_node
        else:
            temp_node=self.head
            for i in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length+=1
        return True
    def search(self,target):
        temp=self.head
        while temp:
            if temp.value==target:
                return True
            temp=temp.next
        return False
    def get(self,index):
        if index==-1:
            return self.tail
        if index<-1 or index>=self.length:
            return None
        current=self.head
        for i in range(index):
            current=current.next
        return current
        
    
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    
    def pop_first(self):
        popped_node=self.head
        if self.head is None:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
            return popped_node
        else:
            self.head=self.head.next
            popped_node.next=None
        self.length-=1
        return popped_node
    

    def pop1(self):
        popped_node=self.tail
        if self.tail is None:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
            return popped_node.value
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            self.tail=temp
            temp.next=None
        self.length-=1
        return popped_node.value

    def remove(self,index):
        if index>=self.length or index<0:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop1()
        prev_node=self.get(index-1)
        popped_node=prev_node.next
        prev_node.next=popped_node.next
        popped_node.next=None
        self.length-=1
        return popped_node
    
    def delete_all(self):
        self.head=None
        self.tail=None
        self.length=0


new_list=LinkedList()
lst=[50,10,20,30,90]
for i in range(5):
    new_list.append(lst[i])

print(new_list)
new_list.append(44)
print(new_list)
new_list.delete_all()
print(new_list.tail)
# get_val=new_list.get(2).value
# print(get_val)
# popped=new_list.pop1()
# print(f'popped value:{popped}')
# print(new_list)