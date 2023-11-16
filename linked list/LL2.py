class Node1:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList1:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):
        new_node=Node1(value)
        self.head=new_node
        self.tail=new_node



hello=LinkedList1()
hello.append(10)
print(hello.head.value)