class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
        
    def detectAndRemoveLoop(self):
        if self.head:
            return
        if self.head.next is None:
            return
        slow_p=self.head
        fast_p=self.head
        
        while(slow_p and fast_p and fast_p,next):
            slow_p=slow_p.next
            fast_p=fast_p.next.next
            
            
            if slow_p == fast_p:
                print('Meeting Point: ',slow_p.data)
                slow_p = self.head
                
                while (slow_p.next != fast_p.next):
                    slow_p=slow_p.next
                    fast_p=fast_p.next
                    
                    
                print('Start of the loop ',fast_p.next.data)
                fast_p.next= None
    
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
            
llist=LinkedList()
llist.head=Node(50)
llist.head.next=Node(20)
llist.head.next.next=Node(15)
llist.head.next.next.next=Node(4)
llist.head.next.next.next.next=Node(10)

extra=Node(1)
llist.head.next.next.next.next.next=extra
extra.next=llist.head.next
llist.detectAndRemoveLoop()
print('Linked list after removing after loop:')
llist.printList()


def delete(self):
    temp=self.head
    self.head=temp.next
    temp.next=None


