s=[]
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
        
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root 
        elif root.val <key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root 

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        s.append(root.val)
        inorder(root.right)
        
def search(root):
    key=int(input('Enter the Search Element: '))
    if root is None or root.val == key:
        print('Found')
        return root 
    
    if root.val< key:
        print('Not Found')
        return search(root.right)
   
    return search(root.left)
   
r=Node(50)
r=insert(r,100)
r=insert(r,70)
r=insert(r,50)
r=insert(r,60)
r=insert(r,9)
r=insert(r,-3)
# r=insert(r,75)
# r=insert(r,78)
inorder(r)
search(r)

#wap to create the program for above list and perform serach operation for the given number