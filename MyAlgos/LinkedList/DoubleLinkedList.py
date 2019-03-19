#!/usr/bin/env python3

# Double Lisnked List
class DNode:
    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def set_next(self, next_node):
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def has_next(self):
        return self.next_node != None

    def set_prev(self, prev_node):
        self.prev_node = prev_node

    def get_prev(self):
        return self.prev_node

    def has_prev(self):
        return self.prev_node != None

    def __str__(self):
        return "Node[Data = {}]".format(self.data)

# Double linked list class
class DLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def get_length(self):
        return self.length

    def clear_list(self):
        self.head = None
        self.tail = None

    def insert_node_start(self, data):
        new_node = DNode(data)
        current = self.head
        if current == None:
            self.tail = new_node
        else:
            current.set_prev(new_node)
            new_node.set_next(current)
        self.head = new_node
        self.length += 1

    def insert_node_end(self, data):
        new_node = DNode(data)
        current = self.tail
        if current == None:
            self.head = new_node
        else:
            current.set_next(new_node)
            new_node.set_prev(current)
        self.tail = new_node
        self.length += 1

    def insert_node_middle(self, data, idx):
        if idx > self.length and idx < 0:
            print("List index out of range")
            return None
        elif idx == 0:
            self.insert_node_start(data)
        elif idx == self.length:
            self.insert_node_end(data)
        else:
            new_node = DNode(data)
            current = self.get_node_idx(idx)
            new_node.set_prev(current.get_prev())
            new_node.set_next(current)
            current.get_prev().set_next(new_node)
            current.set_prev(new_node)
        self.length += 1

    def get_node_idx(self, idx):
        if idx > self.length - 1 and idx < 0:
            print("List index out of range")
            return None
        current = self.head
        if current == None:
            return None
        while idx > 0:
            current = current.get_next()
            if current == None:
                break
            idx -= 1
        return current

    def get_node_data(self, data):
        if self.head == None:
            return None
        current = self.head
        while current != None:
            if current.get_data() == data:
                 return current
            current = current.get_next()
        return None

    def dump_list(self):
        current = self.head
        while current != None:
            print("Node: {}".format(current.get_data()))
            current = current.get_next()

    def dump_list_reverse(self):
        current = self.tail
        while current != None:
            print("Node: {}".format(current.get_data()))
            current = current.get_prev()

    def delete_at_idx(self, idx):
        if idx > self.length - 1 and idx < 0:
            print("List index out of range")
            return None
        current = self.get_node_idx(idx)
        if idx == 0:
            self.head = current.get_next()
            self.head.set_prev(None)
            current.set_next(None)
        elif idx == self.length - 1:
            self.tail = current.get_prev()
            current.set_prev(None)
            self.tail.set_next(None)
        else:
            current.get_prev().set_next(current.get_next())
            current.get_next().set_prev(current.get_prev())
            current.set_prev(None)
            current.set_next(None)
        self.length -= 1
        return current

    def delete_with_data(self, data):
        current = self.get_node_data(data)
        if current == None:
            print("No node found with data {}".format(data))
            return None
        elif self.head == current:
            self.head = current.get_next()
            self.head.set_prev(None)
            current.set_next(None)
        elif self.tail == current:
            self.tail = current.get_prev()
            current.set_prev(None)
            self.tail.set_next(None)
        else:
            current.get_prev().set_next(current.get_next())
            current.get_next().set_prev(current.get_prev())
            current.set_prev(None)
            current.set_next(None)
        self.length -= 1
        return current


if __name__ == '__main__':
    # create a linked list and insert some items
    itemlist2 = DLinkedList()
    itemlist2.insert_node_start(11)
    itemlist2.insert_node_start(12)
    itemlist2.insert_node_start(13)
    itemlist2.insert_node_start(14)
    print("Length is: {}".format(itemlist2.get_length()))
    itemlist2.dump_list()
    print("------------------------")
    itemlist2.insert_node_middle(15,2)
    print("Length is: {}".format(itemlist2.get_length()))
    itemlist2.dump_list_reverse()
    print("------------------------")
    print("Node is: {}".format(itemlist2.get_node_idx(3)))
    print("Node is: {}".format(itemlist2.get_node_data(11)))
    print("Delete Node: {}".format(itemlist2.delete_at_idx(2)))
    itemlist2.dump_list_reverse()
    print("------------------------")
    itemlist2.dump_list()
    print("Delete Node: {}".format(itemlist2.delete_with_data(12)))
    itemlist2.dump_list()
    print("------------------------")
    itemlist2.dump_list_reverse()
