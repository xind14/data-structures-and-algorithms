def find_maximum_value(self):
    nodes = self.in_order()

    if not nodes:  
        return None  

    max_value = nodes[0]

    for node_value in nodes[1:]:
        if node_value > max_value:
            max_value = node_value

    return max_value