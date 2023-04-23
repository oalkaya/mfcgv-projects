from graph_cut import GraphCut
import numpy as np
from scipy.sparse import csr_matrix


def main():
    # TODO: Implement Task 1

    # Nodes = # non-source/sink vertices
    # Connections = # non-terminal edges
    g = GraphCut(nodes=3, connections=4)

    # Non-terminal edge capacities as adjacency matrix
    edges = np.array([
                [0, 1, 3, 2], # bidirectional edge between vertices 0-1
                [1, 2, 5, 1], # bidirectional edge between vertices 1-2
                ])

    g.set_pairwise(edges)   

    # Set the unaries
    unaries = np.array([
        [9, 4],  # vertex 1
        [7, 7],  # vertex 2
        [5, 8]   # vertex 3
    ])

    g.set_unary(unaries)

    # Minimize, returns maxflow
    print(g.minimize())

    # Get labels: False if node belongs to source, True if node belongs to sink
    print(g.get_labeling())


    # We get maxflow = 19 for this given graph. Manual calculation also confirms that.
    # A possible min cut is through the terminal edges between the vertices and sink, this is confirmed by the labeling returning [False False False]


if __name__ == '__main__':
    main()
