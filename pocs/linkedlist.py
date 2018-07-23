
"""
Playing around with some dunder methods
"""


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList():
    def __init__(self):
        self.root = None
        self.leaf = None

    def append(self, value):
        if self.root == None:
            self.root = Node(value) 
            self.leaf = self.root 
        else:
            new_node = Node(value)
            current_leaf = self.leaf
            current_leaf.next = new_node
            new_node.prev = current_leaf
            self.leaf = new_node

    def __str__(self):
        node = self.root
        content = ""
        while node != None:
            content += "{0}\n".format(str(node))
            node = node.next
        return content





if __name__ == '__main__':
    lst = LinkedList()
    lst.append(1)
    lst.append(3)
    print(lst)
    print("done")

