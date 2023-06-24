n=int(input("Enter the List Size :"))
l=[]
flag=n
for i in range(0,n):
    x=input()
    l.append(x)
    n=n-1
while 1!=0:
    print("1.Insert")
    print('2.Search')
    print('3.Delete')
    print('4.Sort')
    print('5.Display')
    ch=int(input("Please Select Your Choice: "))
    if ch==1:
        if n>0:
            for i in range(0,n):
                x=input()
                l.append(x)
                flag=flag-1
        else:
            print('List Is out of range!Deleted Some Elements to Insert into List')
    elif ch==2:
        find=int(input("Enter the Search Element: "))
        fn=0
        for i in range(0,len(l)):
            if l[i]==find:
                fn=1
        if fn==1:
            print('Hurrah! Number if Found in the Database with Index position=',i)
        else:
            print("Number is not found!")
    elif ch==3:
        del_ele=int(input("Enter the Element to Delete :"))
        l.pop()
        print('Element is Deleted Successfully!')
    elif ch==4:
        l.sort()
        print('Sorted Sucessfully!')
        for i in range(0,len(l)):
            print(l[i],end="\n")
    elif ch==5:
        for i in range(0,len(l)):
            print(l[i],end="\n")
    else:
        print('Option Not Found!')