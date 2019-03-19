#!/usr/bin/env python3

# Node class
class Node:
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = date

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def get_length(self):
        return self.length

    def clear_list(self):
        self.head = None

    def insert_node_start(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.length += 1

    def insert_node_end(self, data):
        new_node = Node(data)
        current = self.head
        if current == None:
            self.head = new_node
            new_node.set_next(None)
        else:
            previous = None
            while(current != None):
                previous = current
                current = current.get_next()
            previous.set_next(new_node)
        self.length += 1

    def dump_list(self):
        current = self.head
        while(current != None):
            print("Node: {}".format(current.get_data()))
            current = current.get_next()

    def find_node(self, val):
        current = self.head
        while(current != None):
            if current.get_data() == val:
                return current
            else:
                current = current.get_next()
        return None

    def deleteAt(self, idx):
        if idx > self.length - 1 or idx < 0:
            print("Index out of range")
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            i = 0
            node = self.head
            while i < idx - 1:
                node = node.get_next()
                i += 1
            node.set_next(node.get_next().get_next())
        self.length -= 1

if __name__ == '__main__':
    # create a linked list and insert some items
    itemlist = LinkedList()
    itemlist.insert_node_end(38)
    itemlist.insert_node_end(49)
    itemlist.insert_node_end(13)
    itemlist.insert_node_end(15)
    print("Length is: {}".format(itemlist.get_length()))
    itemlist.dump_list()
    itemlist.deleteAt(3)
    itemlist.dump_list()
    print("Item is: {}".format(itemlist.find_node(13)))
    print("Item is: {}".format(itemlist.find_node(22)))
    print("Length is: {}".format(itemlist.get_length()))
