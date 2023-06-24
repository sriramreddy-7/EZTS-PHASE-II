class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def inOrder(root):
    current = root
    stack =[]
    done=0
    while True:
        if current is not None:
            stack.append(current)
            current=current.left 
        elif (stack):
            current=stack.pop()
            print(current.data,end=' ')
            current=current.right
        else:
            break
    print()
    
    
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right =Node(5)

inOrder(root)
'''
every node is lesser than its parent if its lying at left side every node is greater than its parent if it is lying on right side'''
'''50
30                  
10
15
16
500
300
200
1
2
3'''

'''7 ,35,-4,-9,8,62,0,-25,25,16,17,77,-39,100'''
