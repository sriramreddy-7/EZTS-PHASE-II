# create a stack with user input extarct only even input and display 
stack=[]
empty='Stack Is Empty'
print('\n--Stack Operations Display Even Or Odd--\n')
def push():
    n=int(input('Enter the How many element need to add:'))
    for i in range(0,n):
        key=int(input('Enter the Element :'))
        stack.append(key)
    print('Inserted Sucessfully')
    display()

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
        t=int(input('1-EVEN | 2-ODD\n'))
        flag=0
        if t==1:
            for i in stack:
                if i%2==0:
                    print('[',i,']',end='')
                    flag=1
                else:
                    continue
            if flag!=1:
                print('No Even Element is Existed in the List!')
            print()    
        elif t==2:
            for i in stack:
                if i%2!=0:
                    print('[',i,']',end='')
                    flag=1
                else:
                    continue
            if flag!=1:
                print('No Odd Element is Existed in the List!')
            print()
        else:
            print('Choose Correct Option')
        

while 1:
    print('1.PUSH\n2.POP\n3.DISPLAY\n4.QUIT')
    ch=int(input('Enter the Choice: '))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print('Please enter the correct option!')
        