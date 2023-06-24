class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Queue:
    def __init__(self):
        self.head=None
        self.last=None
        
    def enqeue(self,data):
        if self.last is None:
            self.head =Node(data)
            self.last= self.head
            
        else:
            self.last.next=Node(data)
            self.last=self.last.next 
            
    def dequeue(self):
        if self.head is None:
            return None 
        else:
            to_return=self.head.data 
            self.head=self.head.next 
            return to_return


a_queue=Queue()
while True:
    print('Enqueue <value>')
    print('Dequeue')
    print('exit')
    do=input('What would you like to do').split()
    operation=do[0].strip().lower()
    if operation=='enqueue':
        a_queue.enqueue(int(do[1]))
    elif operation=='dequeue':
        dequeued=a_queue.dequeue()
        if dequeued is None:
            print('queue is empty')
        else:
            print('dequeued value',int(dequeued))
    elif operation=='quit':
        break
    
    