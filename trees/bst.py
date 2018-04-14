

class node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


class tree:
    def __init__(self, root = None):
        self.root = root

    def append(self, new_node):
        if self.root == None:
            self.root = new_node
        else:
            self._append(self.root, new_node)
        
    # recursive function to find where the node needs to be
    def _append(self, node, new_node):
        if node == None:
            return new_node
        if  new_node.value < node.value:
            node.left = self._append(node.left, new_node)
        elif new_node.value > node.value:
            node.right = self._append(node.right, new_node)
        return node


    def find(self, value):
        if self.root != None:
            return self._find(self.root, value)

    def _find(self, node, value):
        if node == None:
            return False
        if node.value == value:
            return True

        if value < node.value:
            return self._find(node.left, value)
        elif value > node.value:
            return self._find(node.right, value)

        return False

    def pre_order_print(self):
        self._pre_order_print(self.root)

    # recursive function to print the tree
    def _pre_order_print(self, node):
        print(node.value)

        if node.left != None:
            self._pre_order_print(node.left)

        if node.right != None:
            self._pre_order_print(node.right)
           

        

if __name__ == '__main__':
    t = tree()
    t.append(node(10))
    t.append(node(5))
    t.append(node(20))
    t.append(node(1))
    t.append(node(6))
    t.append(node(15))
    t.pre_order_print()
    print(t.find(6))

