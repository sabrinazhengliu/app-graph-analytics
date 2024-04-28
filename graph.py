import networkx as nx
import itertools
import random


class Graph:

    def __init__(self, list_nodes=[], list_edges=[]) -> None:
        self.graph = nx.Graph()
        self.graph.add_nodes_from(list_nodes)
        self.graph.add_edges_from(list_edges)
        pass

    def __repr__(self) -> str:
        info = f"Graph ({self.n_nodes} nodes and {self.n_edges} edges)"
        return info


class RandomGraph:

    def __init__(self) -> None:
        super().__init__()
        list_nodes = self.generate_random_nodes()
        list_edges = self.generate_random_edges(list_nodes)
        self.graph.add_nodes_from(list_nodes)
        self.graph.add_edges_from(list_edges)
        pass

    @staticmethod
    def generate_random_nodes() -> list:
        n_nodes = random.randint(10, 100)       
        list_nodes = list(range(n_nodes))
        return list_nodes

    @staticmethod
    def generate_random_edges(list_nodes) -> list:
        n_nodes = len(list_nodes)
        n_edges = random.randint(0, int(n_nodes * (n_nodes - 1) / 2))
        list_pairs = list(itertools.combinations(list_nodes, r=2))
        rand_index = random.sample(range(len(list_pairs)), n_edges)
        list_edges = [
            pair for pair in list_pairs
            if list_pairs.index(pair) in rand_index
        ]
        return list_edges


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
