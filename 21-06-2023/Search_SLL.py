class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head is None:
            print('Linked list is Empty!')
        else:
            temp=self.head
            while temp:
                print("->",temp.data,end=" ")
                temp=temp.next

    def insert_beginning(self):
        data=int(input('Enter the Element: '))
        nb=Node(data)
        nb.next=self.head
        self.head=nb
        
    def insert_end(self):
        data=int(input('Enter the Element: '))
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        ne.next=None
        
    def insert_at_position(self):
        pos=int(input('Enter the Position to Insert: '))
        data=int(input('Enter the Elemnt: '))
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        
        np.next=temp.next
        temp.next=np

    def delete_position(self):
        pos=int(input('Enter the Position to Delete: '))
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    
    def delete(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
    def delete_last(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    
    def search(self):
        key=int(input('Enter the Search Element :'))
        flag=0
        if self.head is None:
            print('Linked list is Empty!')
        else:
            temp=self.head
            while temp:
                if temp.data==key:
                    print("Key is Found->",key,end=" ")
                    flag=1
                    break
                else:
                    temp=temp.next
        if flag==0:
            print('Not Found!')
                            
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
obj.display()
print("\n------Insert_Begin-----")
obj.insert_beginning()
obj.insert_beginning()
obj.display()
obj.insert_end(1000)
print("\n------Insert_end-----")
obj.display()
print("\n------Delete_Position-[1]-----")
obj.delete_position()
obj.display()
print("\n------Delete_beg-----")
obj.delete()
obj.display()
print("\n------Del_end-----")
obj.delete_last()
obj.display()
print('\nSearching an Element')
obj.search()