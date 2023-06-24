queue=[]
empty='Queue Is Empty'
def enqueue():
    n=int(input('Enter the How many element need to add:'))
    for i in range(0,n):
        key=int(input('Enter the Element :'))
        queue.append(key)
    print('Inserted Sucessfully')
    print(queue)
def dequeue():
    if len(queue) == 0:
        print(empty)
    else:
        e=queue.pop(0)
        print('Deleted Sucessfully:',e)
        print(queue)  
    
def display():
    if len(queue) == 0:
        print(empty)
    else:  
        print('queue Elements')
        print(queue)
        
while 1:
    print('--Queue Operations --\n')
    print('1.Enqueue\n2.Dequeue\n3.Display\n4.Quit')
    ch=int(input('Enter the Choice: '))
    if ch==1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print('Please enter the correct option!')
        