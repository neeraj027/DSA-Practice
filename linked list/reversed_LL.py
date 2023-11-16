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
        temp=self.head
        result=''
        while temp is not None:
            result+=str(temp.value)
            if temp.next is not None:
                result+=' -> '
            temp=temp.next
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

    def reverse(self):
        current_node=self.head
        prev_node=None
        while current_node is not None:
            next_node=current_node.next
            current_node.next=prev_node
            prev_node=current_node
            current_node=next_node
        self.head,self.tail=self.tail,self.head


new_list=LinkedList()

new_list.append(10)
new_list.append(2066)
new_list.append(2078)
new_list.append(204)
new_list.append(22)
new_list.append(550)
print(new_list)
new_list.reverse()
print(new_list)
