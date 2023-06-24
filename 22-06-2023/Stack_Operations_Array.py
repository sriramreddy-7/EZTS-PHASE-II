stack=[]
empty='Stack Is Empty'
def push():
    n=int(input('Enter the How many element need to add:'))
    for i in range(0,n):
        key=int(input('Enter the Element :'))
        stack.append(key)
    print('Inserted Sucessfully')
    print(stack)
def pop():
    if len(stack) == 0:
        print(empty)
    else:
        e=stack.pop()
        print('Deleted Sucessfully:',e)
        print(stack)  
    
def display():
    if len(stack) == 0:
        print(empty)
    else:  
        print('Stack Elements')
        print(stack)
        
def peek():
    if len(stack) == 0:
        print(empty)
    else:
        print(stack[-1])              

while 1:
    print('--Stack Operations --\n')
    print('1.PUSH\n2.POP\n3.DISPLAY\n4.PEEK\n5.QUIT')
    ch=int(input('Enter the Choice: '))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        peek()
    elif ch==5:
        break
    else:
        print('Please enter the correct option!')
        
        