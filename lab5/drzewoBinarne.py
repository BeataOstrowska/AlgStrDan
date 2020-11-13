from typing import Any, Callable

class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        #s = ""
        #s += "value: " + str(self.value) + "\n"
        #s += "left_child : " + str(self.left_child.value) + "\n"
        #s += "right_child: " + str(self.right_child.value) + "\n"
        return str(self.value)

    def is_leaf(self):
        if self.left_child == None and self.right_child == None:
            return True
        return False

    def add_left_child(self, value):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit = [] ):
        if self.left_child:         
           self.left_child.traverse_in_order(visit)
        visit.append(self.value)
        if self.right_child:
           self.right_child.traverse_in_order(visit)
        return visit
                    
    def traverse_post_order(self, visit = [] ):
        if self.left_child:         
           self.left_child.traverse_post_order(visit) 
        if self.right_child:
           self.right_child.traverse_post_order(visit)
        visit.append(self.value)
        return visit
   
    def  traverse_pre_order(self,visit = []):
        visit.append(self.value)
        if self.left_child:         
           self.left_child.traverse_pre_order(visit) 
        if self.right_child:
           self.right_child.traverse_pre_order(visit)
        return visit

    def __print__(self):
        return self.__repr__()
    
    def show(self,value,level=0):
        if self.left_child:
            self.left_child.show(value, level+1)
        print(' '* 3* level+ '-->',self.value)
        if self.right_child:
            self.right_child.show(value,level+1)

class BinaryTree:
    def __init__(self, value):
        self.root = BinaryNode(value)
    def traverse_in_order(self, visit = []):
        return self.root.traverse_in_order(visit)        
    def traverse_post_order(self, visit = []):
        return self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit = []):
        return self.root.traverse_pre_order(visit) 
    def show(self):
        self.root.show(0)
         
 

tree = BinaryTree()
tree.add__(10) 
assert tree.root.value == 10
tree.root.add_left_child(9)
tree.root.add_right_child(2)
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(3)
tree.root.right_child.add_left_child(4)
tree.root.right_child.add_right_child(6)

assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False

assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True

#print(tree.root)

print(tree.root.left_child.traverse_in_order())
print(tree.root.right_child.traverse_post_order())
print(tree.root.traverse_pre_order())

print(tree.traverse_in_order())
print(tree.traverse_post_order())
print(tree.traverse_pre_order())
tree.show()