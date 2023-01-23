def choice_feature(nodes, i1, Center_node, Relay_Node, Relay_G_Node):
    """
    This function determines the nodes features.
    You can use algorithms or models for determining features in this function.
    Based on network topology the id of the node is passed to this function for determining node features.

    0 sink node
    1 just relay node
    2 just generator node
    3 relay and generator
    4 low power node
    5 friend and relay node
    6 friend node
    """
    
    if i1 == Center_node: 
        nodes[i1].feature = 0
    else:
        for i in range(len(Relay_Node)):  # Based on network topology we choose the nodes' feature 
            if i1 == Relay_Node[i]:
                nodes[i1].feature = 3
                break
            else:
                nodes[i1].feature = 2
