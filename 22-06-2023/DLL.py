class Node:
    def __init__(self,data):
        self.data=data 
        self.previous=None
        self.next=None
        
class dll:
    def __init__(self):
        self.head=None
        
    def insert_at_beg(self):
        key=int(input('Enter the Data: '))
        n=Node(key)
        temp=self.head
        temp.previous=n
        n.next=temp
        self.head=n 
            
    def insert_end(self):
        key=int(input('Enter the Data: '))
        n=Node(key)
        temp=self.head
        
        while temp.next is not None:
            temp=temp.next 
        temp.next=n 
        n.prev=temp
        
    def insert_pos(self):
        pos=int(input('Enter the Position : '))
        data=int(input('Enter the Data : '))
        n=Node(data)
        temp=self.head
        for i in range(0,pos-1):
            temp=temp.next 
        n.previous=temp
        n.next=temp.next
        temp.next.previous=n 
        temp.next=n
        
    def delete_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    
    def delete_last(self):
        temp=self.head.next
        previous=self.head
        while temp.next is not None:
            temp=temp.next
            previous=previous.next
        previous.next=temp.next
        temp.next=None
    
    def delete_at_position(self):
        pos=int(input('Enter the Position:'))
        temp=self.head.next
        previous=self.head
        for i in range(1,pos-1):
            temp=temp.next
            previous=previous.next
        previous.next=temp.next
        temp.next=None
    
    
    def display(self):
        if self.head is None:
            print('Is Empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,'<-->',end='')
                temp=temp.next
            print('NULL')

l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
n3=Node(300)
n3.previous=n2
n2.next=n3
n4=Node(400)
n4.previous=n3
n3.next=n4
n5=Node(500)
n5.previous=n4
n4.next=n5
l.display()
print('\nInsert at Beg')
l.insert_at_beg()
l.display()
print('\nInsert at Last')
l.insert_end()
l.display()
print('\nInsert at Position')
l.insert_pos()
l.display()
print('\nDelete At Begining')
l.delete_beg()
l.display()
print('\nDelete At End')
l.delete_last()
l.display()
print('\nDelete At Position')
l.delete_at_position()
l.display()