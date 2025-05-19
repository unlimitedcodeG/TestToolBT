class NodeIter:
    def __init__(self, node):
        self.node = node
        self.current = node

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            result = self.current
            self.current = self.current.next
            return result

    def __iter__(self):
        return self


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

    def __iter__(self):
        return NodeIter(self)

    def __next__(self):
        if self.next is None:
            raise StopIteration
        else:
            return self.next

    def __len__(self):
        return len(self.data)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3


it = iter(node1)

first = next(it)

for node in it:
    print(node)
