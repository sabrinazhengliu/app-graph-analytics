import networkx as nx
import itertools
import random


class Graph:

    def __init__(self, list_nodes=[], list_edges=[]) -> None:
        self.graph = nx.Graph()
        self.graph.add_nodes_from(list_nodes)
        self.graph.add_edges_from(list_edges)
        self.n_nodes = len(list_nodes)
        self.n_edges = len(list_edges)
        pass

    def __repr__(self) -> str:
        info = f"Graph ({self.n_nodes} nodes and {self.n_edges} edges)"
        return info


class RandomGraph:
    def __init__(self) -> None:
        super.init()
        pass


class CustomizedGrpah:
    def __init__(self) -> None:
        pass


if __name__ == '__main__':

    g = Graph()

    n_nodes = 10
    n_edges = n_nodes - 1
    list_nodes = list(range(n_nodes))
    list_pairs = list(itertools.combinations(list_nodes, r=2))
    rand_index = random.sample(range(len(list_pairs)), n_edges)
    list_edges = [p for p in list_pairs if list_pairs.index(p) in rand_index]

    print(list_edges)
    g = Graph(list_nodes, list_edges)
    print(g)
