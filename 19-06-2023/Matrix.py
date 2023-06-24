#get one l as input, display diagonal elements and non diagonal and upward diagonal elements


# l=[7, 8, 9, 6, 3, 5, 2, 1, 4]
# # for i in range(0,9):
# #     l.append(int(input('')))

# print(l)

for i in range(0,9):
    x=3
    while x!=0:
        print(l[i],end=" ")
        x=x-1
    print("\n")
r=int(input("Enter no of the rows:"))
c=int(input("Enter no of the columns:"))
matrix=[]
for i in range(r):
    a=[]
    for i in range(c):
        x=int(input("Enter the item:"))
        a.append(x)
    matrix.append(a)
print("The Matrix is:")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
print("The diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i==j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Non diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i!=j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Upper diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i<j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Lower diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i>j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Transpose Matrix is:")
for i in range(r):
    for j in range(c):
        print(matrix[j][i],end=" ")
    print()
print("The Addition ")
    
# r=int(input('Enter No.of Rows: '))
# c=int(input('Enter No.of Rows: '))
# m=[][]
# for i in range(r):
#     for j in range(c):
        
