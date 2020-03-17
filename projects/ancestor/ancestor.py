
# helper function to return a child
def get_parent(ancestors, node):
    # check each parent / child
    for (parent, child) in ancestors:
        # if node is valid child, return parent
        if child == node:
            return parent

def earliest_ancestor(ancestors, starting_node, count = 0):
    # call helper function to return parent,
    parent = get_parent(ancestors, starting_node)
    # if no parent then starting node is the end
    if parent is None:
        # if count is 0, there is no ancestors
        if count == 0:
            return -1
        # otherwise return the ancestors
        else:
            return starting_node
    # if parent then repeat process
    return earliest_ancestor(ancestors, parent, 1)