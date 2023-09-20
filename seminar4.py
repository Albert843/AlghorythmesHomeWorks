# ------------------------ Seminar 4 --------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        res = f'значение нашего узла: {self.value} '
        if self.left:
            res += f'значение левого: {self.left.value} '
        if self.right:
            res += f'значение правого: {self.right.value} '
        return res
    
class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)
     
    def add(self, value):
        """
              Функция добавления элемента 
                    value: значение для добавления

        """
        # if value > self.root.value:
        #     self.root.right = Node(value)
        # elif value < self.root.value:
        #     self.root.left = Node(value)
        
        res = self.search(self.root, value)
        if res[0] is None:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
            else:
                res[1].left = new_node
        else:
            print("Хватит")
        
    def search(self, node, value, parent=None):
        if node == None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)
        
    def countNodes(self):
        """
            Подсчёт количества элементов бинарного дерева
        """
        counter = 0
        current = self.root
        while current is not None:
            counter += 1
            current = current.right
        return counter
    
    def delete_(self, current_node, value):
        """
              Функция удаления элемента 
                    value: значение для удаления
                    current_node: текущий узел

        """
        if not current_node:
            return current_node
        elif value < current_node.value:
            current_node.left = self.delete_(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.delete_(current_node.right, value)
        else:
            if not current_node.left:
                return current_node.right
            elif not current_node.right:
                return current_node.left
            else:
                min_node = self.find_min_(current_node.right)
                current_node.value = min_node.data
                current_node.right = self.delete_(current_node.right, min_node.data)
        return current_node
        
bt = BinaryTree(5)
bt.add(10)
bt.add(15)
bt.add(3)
bt.add(4)
print(bt.root) 
print(bt.root.left)
print(bt.root.right)
print(bt.countNodes())

# print(bt.search(bt.root, 8)[1])
