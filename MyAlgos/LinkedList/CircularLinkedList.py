#!/usr/bin/env python3

# Node class
class CNode:
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __str__(self):
        return "Node[Data = {}]".format(self.data)

# Circular Linked List Class
class CLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get_length(self):
        return self.length

    def clear_list(self):
        self.head = None

    def dump_list(self):
        if self.head == None:
            print("List is empty")
            return
        else:
            current = self.head
            while current.get_next() != self.head:
                print(current)
                current = current.get_next()
            print(current)

    def insert_node_start(self, data):
        new_node = CNode(data)
        if self.head == None:
            self.head = new_node
            new_node.set_next(new_node)
        else:
            last_node = self.last_node()
            new_node.set_next(self.head)
            self.head = new_node
            last_node.set_next(new_node)
        self.length += 1

    def insert_node_end(self, data):
        new_node = CNode(data)
        if self.head == None:
            self.head = new_node
            new_node.set_next(new_node)
        else:
            new_node.set_next(self.head)
            last_node = self.last_node()
            last_node.set_next(new_node)
        self.length += 1

    def insert_node_at_index(self, data, idx):
        if idx < 0 or idx > self.length:
            print("Index out of range")
            return None
        elif idx == 0:
            self.insert_node_start(data)
        elif idx == self.length:
            self.insert_node_end(data)
        else:
            new_node = CNode(data)
            i = 0
            current = self.head
            while i < idx:
                previou = current
                current = current.get_next()
                i += 1
            new_node.set_next(current)
            previou.set_next(new_node)
        self.length += 1

    def delete_at_idx(self, idx):
        if idx < 0 or idx > self.length-1:
            print("Index out of range")
            return
        elif idx == 0:
            self.delete_at_start()
        elif idx == self.length-1:
            self.delete_at_end()
        else:
            current = self.head
            i = 0
            while i < idx:
                previou = current
                current = current.get_next()
                i += 1
            previous.set_next(current.get_next())
            current.set_next(None)
        self.length -= 1

    def last_node(self):
        if self.head == None:
            print("List id empty")
            return None
        else:
            current = self.head
            while current.get_next() != self.head:
                current = current.get_next()
            return current

    def delete_at_start(self):
        if self.head == None:
            print("List id empty")
            return
        else:
            if self.head.get_next() == self.head:
                self.head.set_next(None)
                self.head = None
            else:
                last_node = self.last_node()
                last_node.set_next(self.head.get_next())
                self.head = self.head.get_next()
            self.length -= 1

    def delete_at_end(self):
        if self.head == None:
            print("List id empty")
            return
        else:
            if self.head.get_next() == self.head:
                self.head.set_next(None)
                self.head = None
            else:
                current = self.head
                while current.get_next() != self.head:
                    previous = current
                    current = current.get_next()
                previous.set_next(self.head)
            self.length -= 1

if __name__=='__main__':
    itemlist = CLinkedList()
    itemlist.insert_node_start(11)
    itemlist.insert_node_start(12)
    itemlist.insert_node_start(13)
    itemlist.insert_node_start(14)
    print("Length is: {}".format(itemlist.get_length()))
    itemlist.dump_list()
    print("Last Node: {}".format(itemlist.last_node()))
    itemlist.insert_node_end(21)
    itemlist.insert_node_end(22)
    itemlist.insert_node_end(23)
    itemlist.insert_node_end(24)
    print("Length is: {}".format(itemlist.get_length()))
    itemlist.dump_list()
    print("Last Node: {}".format(itemlist.last_node()))
    itemlist.delete_at_start()
    itemlist.dump_list()
    print("Length is: {}".format(itemlist.get_length()))
    itemlist.delete_at_end()
    itemlist.dump_list()

    # print("------------------------")
    # itemlist2.insert_node_middle(15,2)
    # print("Length is: {}".format(itemlist2.get_length()))
    # itemlist2.dump_list_reverse()
    # print("------------------------")
    # print("Node is: {}".format(itemlist2.get_node_idx(3)))
    # print("Node is: {}".format(itemlist2.get_node_data(11)))
    # print("Delete Node: {}".format(itemlist2.delete_at_idx(2)))
    # itemlist2.dump_list_reverse()
    # print("------------------------")
    # itemlist2.dump_list()
    # print("Delete Node: {}".format(itemlist2.delete_with_data(12)))
    # itemlist2.dump_list()
    # print("------------------------")
    # itemlist2.dump_list_reverse()
