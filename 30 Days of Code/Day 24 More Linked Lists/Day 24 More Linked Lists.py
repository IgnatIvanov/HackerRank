class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        if head is None:
            return head
        
        values = []
        if len(values) == 0:
            values.append(head.data)
        cur_head = head    
        while True:
            if cur_head.next == None:
                return head
            if cur_head.next.data in values:
                if cur_head.next.next == None:
                    cur_head.next = None
                else:
                    cur_head.next = cur_head.next.next
            else:
                values.append(cur_head.next.data)
                cur_head = cur_head.next

mylist= Solution()