from collections import deque
class TreeNode:

    def __init__(self, value) -> None:
        self.value = value
        self.leftnode:[TreeNode | None] = None
        self.rightnode:[TreeNode | None] = None


    
def level_order(root: TreeNode | None) -> list[int]:
    """Level Transver"""
    # initialize queue and add root node
    queue: deque[TreeNode] = deque()
    queue.append(root)
    # initialize a new list to store queue
    res = []
    while queue:
        node: TreeNode = queue.popleft()
        res.append()
        if node.leftnode:
            queue.append(node.leftnode)
        if node.rightnode:
            queue.append(node.rightnode)
    return res

res = []
def pre_order(root: TreeNode | None):
    """Preorder traversal"""
    if root is None:
        return
    # Access priority: root node -> left subtree -> right subtree
    res.append(root.value)
    pre_order(root=root.leftnode)
    pre_order(root=root.rightnode)

def in_order(root: TreeNode | None):
    """Inorder traversal"""
    if root is None:
        return
    # Access priority: left subtree -> root node -> right subtree
    in_order(root=root.leftnode)
    res.append(root.value)
    in_order(root=root.rightnode)

def post_order(root: TreeNode | None):
    """PostOrder traversal"""
    if root is None:
        return
    post_order(root=root.leftnode)
    post_order(root=root.rightnode)
    res.append(root.value)
    

def search(root: TreeNode | None, num: int) -> TreeNode | None:
    """seacrh node"""
    cur: TreeNode | None = root
    while cur:
        if cur.value < num:
            cur = cur.leftnode
        elif cur.value > num:
            cur = cur.rightnode
        else:
            break
    return cur

def insert(root: TreeNode | None, num: int):
    if root is None:
        return
    cur, pre = root, None
    while cur:
        if cur.value == num:
            return
        
        pre = cur
        if cur.value > num:
            cur = cur.leftnode
        elif cur.value < num:
            cur = cur.rightnode
    
    node =TreeNode(num)
    if pre.value > num:
        pre.leftnode = node
    elif pre.value < num:
        pre.rightnode = node


def remove(root: TreeNode | None, num: int):
    """remove node"""
    # If binary tree is empty, return in advance
    if root is None:
        return
    
    cur, pre = root, None
    while cur:
        if cur.value == num:
            break

        pre = cur
        if cur.value > num:
            cur = cur.leftnode
        elif cur.value < num:
            cur = cur.rightnode

        # If there is no node's value is num, return direactly
        if cur is None:
            return
        
        # child node number is 0 or 1
        if cur.leftnode is None or cur.rightnode is None:
            child = cur.leftnode or cur.rightnode
            if cur != root:
                if pre.leftnode == cur:
                    pre.leftnode = child
                else:
                    pre.rightnode = child
        # child node number is 2
        else:
            # through in order traversal to get next node
            tmp: TreeNode = cur.rightnode
            while tmp.leftnode:
                tmp = tmp.leftnode
            remove(tmp.value)
            cur.value = tmp.value