class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def set_link_node(self, link_node):
        self.link_node = link_node
    
    def get_value(self):
        return self.value
    
    def get_link_node(self):
        return self.link_node

first = Node("first")
second = Node("second")
third = Node("third")

first.set_link_node(second)
second.set_link_node(third)

# get link_node value
second_value = first.get_link_node().get_value()
third_value = second.get_link_node().get_value()

print(second_value, third_value)
