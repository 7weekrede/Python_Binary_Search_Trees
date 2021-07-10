class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    def insert(self,data):
        if self.key is None:
            self.key = BST(data)
        if self.key == data:
            return
        if self.key < data:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
        else:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
    def search(self,data):
        if self.key is None:
            print("Tree is Empty!")
            return
        if self.key == data:
            print("Node is Found")
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not Present in the Tree")
        elif self.key < data:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not Present in the Tree")
    def pre_order_traversal(self):
        print(self.key," ",end = " ")
        if self.lchild:
            self.lchild.pre_order_traversal()
        if self.rchild:
            self.rchild.pre_order_traversal()
    def in_order_traversal(self):
        if self.lchild:
            self.lchild.in_order_traversal()
        print(self.key, " ", end=" ")
        if self.rchild:
            self.rchild.in_order_traversal()
    def post_order_traversal(self):
        if self.lchild:
            self.lchild.post_order_traversal()
        if self.rchild:
            self.rchild.post_order_traversal()
        print(self.key, " ", end=" ")
    def delete(self,data,current):
        if self.key is None:
            print("Tree is Empty!")
        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.delete(data,current)
            else:
                print("Node is not Present in the Tree")
        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data,current)
            else:
                print("Node is not Present in the Tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == current:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == current:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,current)
        return self
    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("Minimum Node : ",current.key)
    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("Maximum Node : ",current.key)
def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)


root = BST(100)
list = [1,76,422,235,12,72,27,23,82,982,763,346,21,102,74,104,94]
for i in list:
    root.insert(i)
'''if count(root)>1:
    root.delete(100,root.key)
else:
    print("Can't Perform The Deletion Operation")'''
root.max_node()
root.min_node()
