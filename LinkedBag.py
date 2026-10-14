class Node:
    def __init__ (self,item,next):
        self.item = item
        self.next = next
class LinkedListBag:
    def __init__(self):
        self.first = None
        self.size = 0

    def Insert(self, item):
        if (self.Exists(item) == True):
            return False
        self.first = Node(item, self.first)
        self.size += 1

    def Exists(self, item):
        current = self.first
        while(current != None):
            if item == current.item:
                return True
            current = current.next
        return False
    
    def Size(self):
        return self.size
    
    def __iter__(self):
        current = self.first
        while current != None:
            yield current.item
            current = current.next
        
    def Delete(self, item):
        if self.Exists(item) == False:      # make sure the item is in the list
            return False
        if item == self.first.item:         # deletes the item if it is the first one
            self.first = self.first.next
            self.size -= 1
            return True
        
        current = self.first
        while(current is not None):                 #goes through the list always looking ahaid one
            if current.next.item == item:
                current.next = current.next.next    # if the one ahaid is the item we skip its node completely
                self.size -= 1                      # and we decrement the count
                return True
            current = current.next
        return False                                
            
    def Retrive(self, item):
        current = self.first
        while(current != None):
            if(current.item == item):
                return current.item
            current = current.next
        return None