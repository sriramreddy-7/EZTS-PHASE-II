pq=[]
while True:
    print('\n1.ADD\n2.REMOVE\n3.DISPLAY\n4.QUIT\n')
    ch=int(input('Enter your Choice: '))
    if ch==1:
        n=int(input('How many Details need to add:'))
        for i in range(0,n):
            n=int(input())
            m=input()
            pq.append((n,m))
        print('Sucessfully Added')
    elif ch==2:
        pq.sort(reverse=True) 
        pq.pop()
        print(pq)
    elif ch==3:
        pq.sort(reverse=True)    
        print(pq)
    elif ch==4:
        break
    else:
        print('Enter the Correct Options!')
    
