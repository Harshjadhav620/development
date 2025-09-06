#Dounle circular linked list

class Node:
    def __init__(self,prev=None,items=None,next=None):
        self.prev=prev
        self.items=items
        self.next=next

class CDLL:
    def __init__(self,start=None):
        self.start=start 

    def is_empty(self):
        return self.start == None

    def insert_at_first (self,data):
        n=Node(None,data)
        if self.is_empty():
            n.next=n
            self.start=n
        else:
            n.next=n.prev
            self.start.next=self.start.next.next
            self.start=n

    def print_list(self):
            if not self.is_empty():
                temp=self.start
            while temp == self.start:
                print(temp.items,end=" ")
                temp=temp.next
            print(temp.items)        


D=CDLL()
D.insert_at_first(20)
D.print_list()
