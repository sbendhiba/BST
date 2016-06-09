import drawtree

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.lvl= None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def children_count(self):
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def delete(self, data):
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
        if children_count == 0:
            if parent:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            else:
                self.data = None
        elif children_count == 1:
            if node.left:
                n = node.left
            else:
                n = node.right
            if parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            else:
                self.left = n.left
                self.right = n.right
                self.data = n.data
        else:
            parent = node
            successor = node.right
            while successor.left:
                parent = successor
                successor = successor.left
            node.data = successor.data
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right


    def tree_to_list(self, node):
        if node is None:
            return []
        return [node.data] + self.tree_to_list(node.left) + self.tree_to_list(node.right)

    def infixe(self, root):
        if root is not None:
            self.infixe(root.left)
            print(root.data)
            self.infixe(root.right)

    def prefixe(self, root):
        if root is not None:
            print(root.data)
            self.prefixe(root.left)
            self.prefixe(root.right)

    def postfixe(self, root):
        if root is not None:
            self.postfixe(root.left)
            self.postfixe(root.right)
            print(root.data)

    def profondeur(self, root):
        pile = []
        if root:
            pile.append(root)
            while (len(pile) != 0):
                node = pile.pop()
                print(node.data)
                if node.right:
                    pile.append(node.right)
                if node.left:
                    pile.append(node.left)



    def Tlenght(self, root):
        if (root.left is None and root.right is None):
            return 0
        else:
            tmp1 = 0
            tmp2 = 0
            if root.left:
                tmp1 = self.Tlenght(root.left)
            if root.right:
                tmp2 = self.Tlenght(root.right)
            return 1+ max(tmp1,tmp2)

    def Tweight(self, root):
        if (root.left is None and root.right is None):
            return 1
        else:
            tmp1 = 0
            tmp2 = 0
            if root.left:
                tmp1 = self.Tweight(root.left)
            if root.right:
                tmp2 = self.Tweight(root.right)
            return 1+ tmp1 + tmp2


    def largeur(self, root):
        file = []
        if root:
            print(root.data)
            file.append(root)
            while(len(file) != 0):
                node = file.pop(0)
                if node.left:
                    print(node.left.data)
                    file.append(node.left)
                if node.right:
                    print(node.right.data)
                    file.append(node.right)



root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

root.delete(10)


print('-----------  Largeur  ------------')

root.largeur(root)

print('----------  infixe   -------------')

root.infixe(root)

print('-----------   Prefixe   ------------')

root.prefixe(root)

print('---------    Postfixe --------------')

root.postfixe(root)

print('---------    Tree  --------------')

drawtree.draw_bst(root.tree_to_list(root))

print('---------    lenght  --------------')

print(root.Tlenght(root))

print('---------    Weight  --------------')

print(root.Tweight(root))

print('---------    Profondeur  --------------')


root.profondeur(root)

