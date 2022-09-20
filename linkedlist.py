class Node:
    'forgot somathing'
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def push(head, data):
    n = Node(data)
    n.next = head
    return n

def build_one_two_three():
    n = Node(1)
    n.next = Node(2)
    n.next.next = Node(3)
    return n

def get_nth(node, index):
    while node.next!=None:
        print(node.data)
        if node.data == index+1:
            return node
        node = node.next
    return node

print(get_nth(build_one_two_three(), 0).data)