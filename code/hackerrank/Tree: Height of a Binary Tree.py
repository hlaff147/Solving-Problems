class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 
    
    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def height(root):
    if root is None:
        return -1
    
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1

def main():
    tree = BinarySearchTree()
    n = int(input())
    
    values = list(map(int, input().split()))
    for value in values:
        tree.create(value)
    
    print(height(tree.root))

if __name__ == "__main__":
    main()