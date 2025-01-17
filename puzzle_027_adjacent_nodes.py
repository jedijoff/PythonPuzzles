#/usr/bin/env python3

def adjacent_nodes(adj_matrix: list[list[int]], start_node: int):
    """
    This function returns a list of nodes that are adjacent to the
    start_node in the adjacency matrix.

    :param adj_matrix: A list of lists representing the adjacency matrix
    :param start_node: The node to find the adjacent nodes to.
    :return: A list of nodes that are adjacent to the start_node.
    """
    return [i for i, x in enumerate(adj_matrix[start_node]) if x == 1]


# Example function calls
print(adjacent_nodes([[0, 1, 1, 0],
                                [1, 0, 0, 1],
                                [1, 0, 0, 1],
                                [0, 1, 1, 0]], 1))
print(adjacent_nodes([[1, 1, 1, ],
                                [1, 0, 0, ],
                                [1, 0, 0, ]], 0))
