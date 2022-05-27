class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    '''
    Here is the code for adding node
    '''

    def add_node(self, data):
        if self.data == data:
            print("Already present")
        else:
            if data < self.data:
                if self.left:
                    self.left.add_node(data)
                else:
                    self.left = BST(data)
            else:
                if self.right:
                    self.right.add_node(data)
                else:
                    self.right = BST(data)

    def finding_node(self, value):
        if self.data == value:
            return True

        else:

            if self.data < value:
                if self.left:
                    return self.left.finding_node(value)
                else:
                    return False
            else:
                if self.right:
                    return self.right.finding_node(value)
                else:
                    return False

    def postorder_traversal(self):
        """
        First it will visit Left node then
        it will visit Right node and finally 
        it will visit Root node  and display a
        list in specific order
        """
        elements = []
        if self.left:
            elements += self.left.postorder_traversal()

        if self.right:
            elements += self.right.postorder_traversal()

        elements.append(self.data)
        return elements

    def Pre_Order_Traversal(self):
        """
        First it will visit Root node then
        it will visit Left node and finally 
        it will visit Right node  and display a
        list in specific order
        """
        elements = [self.data]
        if self.left:
            elements += self.left.Pre_Order_Traversal()
        if self.left:
            elements += self.left.Pre_Order_Traversal()

        return elements
        """
    This method will give
    the Max value of tree
    """

    def Find_Maximum_Node(self):
        if self.right is None:
            return self.data
        return self.right.Find_Maximum_Node()

    """
    This method will give
    the Min value of tree
    """

    def Find_Minimum_Node(self):
        if self.left is None:
            return self.data
        return self.left.Find_Minimum_Node()

    def calculate_Sum_Of_Nodes(self):
        left_sum = self.left.calculate_Sum_Of_Nodes() if self.left else 0
        right_sum = self.right.calculate_Sum_Of_Nodes() if self.right else 0
        return self.data + left_sum + right_sum


def Build_Tree(elements):
    print(elements)
    root = BST(elements[0])

    for i in range(1, len(elements)):
        root.add_node(elements[i])

    print(root.postorder_traversal())
    print(root)


Build_Tree([5, 2, 4, 6, 8, 9])
