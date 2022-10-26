from node import Node 

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, element):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            self.head = Node(element)
        self._size = self,_size + 1

    def __len__(self):
        return self._size

    def get(self, index):
        pass
    def __getitem__(self):

lista = LinkedList()
lista.append(7)