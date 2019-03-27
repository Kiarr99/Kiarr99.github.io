# A list element that stores a value of type T.
class ListElement:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:

    # creates an empty list.
    def __init__(self):
        self.__head = ListElement()
        self.__size = 0 # Because the list is empty nummer of nodes is zero
        self.__tail = ListElement()

    # Insert the given element at the beginning of this list..
    def addfirst(self, data):
        new_node = ListElement(data)

        if self.__size == 0:
            self.__head = new_node
            self.__tail = new_node

        else:
            new_node.next = self.__head
            self.__head = new_node
        self.__size += 1

    def addlast(self, data):
        new_node = ListElement(data)

        if self.__size == 0:
            self.__head = new_node
            self.__tail = new_node

        else:
            self.__tail.next = new_node
            self.__tail = new_node

        self.__size += 1

    def get(self, index):
        if index > self.__size or index <= 0:
            return None
        else:
            current_node = self.__head
            for i in range(1,index):
                current_node = current_node.next
            return current_node.data

    def removefirst(self):

        if self.__size == 0:
            return None
        else:
            return_first_element = self.__head.data
            self.__head = self.__head.next
            self.__size -= 1
            return return_first_element
    def clear(self):
        self.__head = ListElement()
        self.__tail = ListElement()
        self.__size = 0

    def size(self):
        return self.__size
    def string(self):
        array = [None] * self.__size
        for i in range(0,self.__size):
            array[i] = self.get(i+1)

        return str(array)

ls = LinkedList()
ls.addfirst(10)
ls.addfirst(20)
