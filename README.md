# Graph Analytics Explained

https://graph-analytics-explained-sabrinazhengliu.streamlit.app/

This web app allows users beginning to explore graph analytics to quickly generate several types of graphs to understand their visual and statistical characteristics. As node centrality statistics are the most important aspect of graph analytics, several types of node centrality in addition to a few core metrics as each graph is produced. The adjacency matrix is available to download for each graph produced. 

## Types of Graphs Supported
#### Predefined Graph
The Predefined Graph is a Binomial Tree of order 8, produced with `binomial_tree()` graph generator from `networkx` library. The layout used in the visualization is produced using fixed random seed to reproduce the same display every time. 

#### Random Graph
The Random Graph is a G(n, p) Configuration Graph with parameters *n* (number of nodes) and *p* (probability of edge generation), produced with `gnp_random_graph()` graph generator from `networkx` library. Both parameters are randomly selected to generate this graph.

#### Random Probability Graph - G(n, p)
The Random Probability Graph is the same as above Random Graph, except that it allows the user to select the parameters.

#### Random Geomatric Graph - G(n, r)
The Random Geometric Graph is a Geometric Graph with parameters *n* (number of nodes) and *r* (radius at which edge should be generated), produced with `random_geometric_graph()` graph generator from `networkx` library. It allows the user to select the parameters.

#### Random Customized Graph - G(n, e)
The Random Customized Graph allows the user to produce a graph using two parameters, *n* (number of nodes) and *e* (number of edges). The edges are randomly generated using the existing nodes. A self-defined subclass of `Graph` object from `networkx` library is created to support the creation of this type of graph. See details in [graph.py](graph.py)

## Graph Visualization
The graph visualization is rendered with the `plotly` library. The visualization is interactive, and applied with a color map that indicates the number of node adjacencies. 

## Graph Statistics
Below the visualization displays the basic graph statistics, including:
* number of nodes
* number of edges
* number of connected components
* graph density
* max degree adjacency
* max degree centrality
* max closeness centrality
* max betweenness centrality

Below the statistics summary displays the histogram of the above four node centrality metrics. It can be seen that degree adjacency and degree centrality are always correlated, while other types of centralities each have their own distributions. 

For more explanations on node centrality algorithms, please visit this 
[article on Medium](https://sabrinazhengliu.medium.com/node-centrality-algorithms-explained-491720a7a74e)
