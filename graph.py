import networkx as nx
import itertools
import random


class CustomizedGrpah(nx.Graph):

    def __init__(self, n_nodes, n_edges) -> None:
        super().__init__()
        list_nodes = self.generate_list_nodes(n_nodes)
        list_edges = self.generate_list_edges(n_edges, list_nodes)
        self.add_nodes_from(list_nodes)
        self.add_edges_from(list_edges)
        pass

    @staticmethod
    def generate_list_nodes(n_nodes: int) -> list:
        return list(range(n_nodes))

    @staticmethod
    def generate_list_edges(n_edges, list_nodes) -> list:
        list_pairs = list(itertools.combinations(list_nodes, r=2))
        rand_index = random.sample(range(len(list_pairs)), n_edges)
        list_edges = [
            pair for pair in list_pairs
            if list_pairs.index(pair) in rand_index
        ]
        return list_edges


def make_graph(
        graph_type: str, n: int, p: float, r: float, e: int
) -> nx.Graph:

    def _apply_layout(G, seed=None):
        pos = nx.spring_layout(G, seed=seed)
        for i, _ in enumerate(G.nodes):
            G.nodes[i]['pos'] = pos[i]
        return G

    if graph_type.startswith('Predefined'):
        G = nx.binomial_tree(8)
        G = _apply_layout(G, seed=10)

    if graph_type == 'Random Graph':
        n = random.randint(1, 100)   # return int between 1 and 100
        p = random.random()          # return float between 0 and 1
        G = nx.gnp_random_graph(n, p)
        G = _apply_layout(G)

    if graph_type.endswith('G(n, r)'):
        G = nx.random_geometric_graph(n, r)

    if graph_type.endswith('G(n, p)'):
        G = nx.gnp_random_graph(n, p)
        G = _apply_layout(G)

    if graph_type.endswith('G(n, e)'):
        G = CustomizedGrpah(n, e)
        G = _apply_layout(G)

    return G


if __name__ == '__main__':

    G = CustomizedGrpah(100, 99)
