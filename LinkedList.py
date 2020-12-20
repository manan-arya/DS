class LinkedList:
    def __init__(self):
        self.__head = self.Node()
        self.__length = 0

    #to-be deprecated
    def length(self):
        temp = self.__head
        length = 0
        while(temp != None):
            temp = temp._get_next()
            length += 1
        return length

    def insertatbeginning(self,data):
        new = self.Node()
        new._set_data(data)

        if self.__length == 0:
            self.__head = new
            
        else:
            new._set_next(self.__head)
            self.__head = new

        self.__length+=1

    def insertatend(self,data):
        new = self.Node()
        new._set_data(data)
        self.__length+=1
        if self.__head._get_data() == None:
            self.__head = new
            return
        temp = self.__head
        while(temp._has_next()):
            temp = temp._get_next()

        temp._set_next(new)

    def print(self):
        temp = self.__head
        while(temp):
            print(temp._get_data())
            temp = temp._get_next()


    class Node:
        def __init__(self):
            self.__data = None
            self.__next = None

        def _get_data(self):
            return self.__data

        def _set_data(self,data):
            self.__data = data

        def _get_next(self):
            return self.__next

        def _set_next(self,next_node):
            self.__next = next_node

        def _has_next(self):
            return self.__next != None


