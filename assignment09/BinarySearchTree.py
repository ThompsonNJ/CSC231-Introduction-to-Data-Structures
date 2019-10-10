class BinaryNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        raddr = laddr = None
        if self.left:
            laddr = 'BinaryNode at '+hex(id(self.left))
        if self.right:
            raddr = 'BinaryNode at '+hex(id(self.right))
        return '<BinaryNode at {}, data: {}, left: {}, right: {}>'.format(hex(id(self)), self.data, laddr, raddr)


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def insert(self, item):
        if self.root is not None:
            curr = self.root
            done = False
            while not done:
                if item < curr.data:
                    if curr.left is None:
                        self.size += 1
                        curr.left = BinaryNode(item)
                        done = True
                    else:
                        curr = curr.left
                elif item > curr.data:
                    if curr.right is None:
                        self.size += 1
                        curr.right = BinaryNode(item)
                        done = True
                    else:
                        curr = curr.right
                else:
                    done = True
        else:
            self.size += 1
            self.root = BinaryNode(item)

    def delete(self, item):
        if self.root is None:
            raise ValueError("The tree is already empty.")
        else:
            found, curr, parent = self._locate_node(item)
            if found:
                self.size -= 1
                if curr.left is not None and curr.right is not None:
                    successor, succ_parent = self._find_inorder_successor(curr)
                    curr.data = successor.data
                    curr = successor
                    parent = succ_parent
                    
                if curr.left is not None:
                    subtree = curr.left
                else:
                    subtree = curr.right
                    
                if parent is None:
                    self.root = subtree
                elif parent.left == curr:
                    parent.left = subtree
                else:
                    parent.right = subtree
                    
        

    def _find_inorder_successor(self, node):
        curr = node.right
        parent = node
        while curr.left is not None:
            parent = curr
            curr = curr.left
        return curr, parent
    
    def _locate_node(self, item):
        found = False
        curr = self.root
        parent = None
        while curr is not None and not found:
            if item == curr.data:
                found = True
            elif item > curr.data:
                parent = curr
                curr = curr.right
            else:
                parent = curr
                curr = curr.left

        return found, curr, parent
    
    def __contains__(self, item):
        found = False
        curr = self.root
        while curr is not None and not found:
            if item == curr.data:
                found = True
            elif item > curr.data:
                curr = curr.right
            else:
                curr = curr.left
                
        return found

    # you said this was fine since I already did it            
    def height(self, node):
        if self.size in [0,1]:
            return 0
        elif node is None:
            return -1
        else:
            left_depth = self.height(node.left)
            right_depth = self.height(node.right)

            if left_depth > right_depth:
                return left_depth+1
            else:
                return right_depth+1

    def __len__(self):
        return self.size
           
    def preorder_traversal(self, node=None):
        curr = node
        if node is None:
            curr = self.root
            
        print(curr)
        if curr.left is not None:
            self.preorder_traversal(curr.left)
        if curr.right is not None:
           self.preorder_traversal(curr.right)
           
    def inorder_traversal(self, node=None):
        curr = node
        if node is None:
            curr = self.root

        if curr.left is not None:
            self.inorder_traversal(curr.left)
        print(curr)
        if curr.right is not None:
            self.inorder_traversal(curr.right)
    
    def postorder_traversal(self, node=None):
        curr = node
        if node is None:
            curr = self.root
            
        if curr.left is not None:
            self.postorder_traversal(curr.left)
        if curr.right is not None:
           self.postorder_traversal(curr.right)
        print(curr) 

tree = BinarySearchTree()
tree.insert(8)
tree.insert(5)
tree.insert(11)
tree.insert(9)
tree.insert(3)
tree.insert(7)

tree.delete(8)
tree.preorder_traversal()
