# Eric Tweedie program assignment 2
# Create a program that repeatedly asks the user to enter a positive integer and stores/deletes it in the AVL tree until the user enters a negative number.
# User enters a number already in tree, delete it. If enters a number not in the tree, insert it.

# AVL Tree class
# Create a tree node
class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    # Function to insert a node
    def insert_node(self, root, data):
        # find the correct location and insert the node
        if not root:
            return TreeNode(data)
        elif data < root.data:
            root.left = self.insert_node(root.left, data)
        else:
            root.right = self.insert_node(root.right, data)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        
        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if data < root.left.data:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        
        if balanceFactor < -1:
            if data > root.right.data:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    
    # function to delete a node
    def delete_node(self, root, data):
        # find the node to be deleted and remove it
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)
        
        if root is None:
            return root
        
        # update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        
        balanceFactor = self.getBalance(root)

        # balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    
    # function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y
    
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y
    
    # get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    # get balance factor of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)
    
    def getMaxValueNode(self, root):
        if root is None or root.right is None:
            return root
        return self.getMaxValueNode(root.right)
    
    def printPreOrder(self, root):
        if not root:
            return
        print(root.data, end=" ")
        self.printPreOrder(root.left)
        self.printPreOrder(root.right)

    def printInOrder(self, root):
        if not root:
            return
        self.printInOrder(root.left)
        print(root.data, end=" ")
        self.printInOrder(root.right)
    
    def printPostOrder(self, root):
        if not root:
            return
        self.printPostOrder(root.left)
        self.printPostOrder(root.right)
        print(root.data, end=" ")

    # print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "      "
            else:
                print("L----", end="")
                indent += "|     "
            print(currPtr.data)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

    # function that asks repeatedly for the user to enter positive integers and inserts/deletes them in the AVL tree
    def user_input(self, root, currPtr, indent, last):
        '''Function that asks the user for a positive integer. If the integer is already 
        in the tree, the function deletes it. If the integer is not in the tree,
        the function adds the integer to the tree. After each deletion or insertion the tree is shown.
        If a negative integer the program ends.
        Input:
            x = user entered integer
        Output:
            insertion of the integer/ tree is shown
            or
            deletion of node in tree/ tree is shown'''
    
        while True:
            try:
                x = int(input("Enter a positive integer/ Enter a negative integer to quit: "))
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
                continue
            if x > 0:
                if self.search(root, x):
                    root = self.delete_node(root, x)
                    print("After Deletion of {}: ".format(x))
                    self.printHelper(root, indent, last)
                else:
                    root = self.insert_node(root, x)
                    print("After Insertion of {}: ".format(x))
                    self.printHelper(root, indent, last)
            elif x < 0:
                break

    def search(self, root, data):
        '''Function to search for a node in the AVL tree'''
        if root is None or root.data == data:
            return root
        if root.data < data:
            return self.search(root.right, data)
        return self.search(root.left, data)

def main():
    myTree = AVLTree()
    root = None
    nums = [33, 13, 52, 9, 21, 61, 8, 11]
    for num in nums:
        root = myTree.insert_node(root, num)
    myTree.printHelper(root, "", True)
    data = 13
    root = myTree.delete_node(root, data)
    print("After Deletion of {}: ".format(data))
    myTree.printHelper(root, "", True)
    data = 27
    root = myTree.insert_node(root, data)
    print("After Insertion of {}: ".format(data))
    myTree.printHelper(root, "", True)
    data = 17
    root = myTree.insert_node(root, data)
    print("After Insertion of {}: ".format(data))
    myTree.printHelper(root, "", True)
    myTree.user_input(root, data, "", True)
main()
