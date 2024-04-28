import streamlit as st
from plot import plot_graph
import networkx as nx


def initialize_page():
    st.title('Graph Analytics Dashboard')
    pass


def max_edges(n_nodes):
    return int(n_nodes * (n_nodes - 1) / 2)


def initialize_params():

    global sb
    sb = st.sidebar

    global graph_type
    options = ['Predefined Graph', 'Random Graph', 'Customized Graph']
    graph_type = sb.radio(label='Choose Graph Type:', options=options)

    n_nodes = sb.slider(
        label='Choose Number of Nodes:',
        min_value=5, max_value=100, value=10, step=5
    )
    n_edges = sb.slider(
        label='Choose Number of Edges:',
        min_value=0, max_value=max_edges(n_nodes), value=n_nodes-1, step=1
    )
    pass


if __name__ == '__main__':

    initialize_page()
    initialize_params()

    if sb.button('Generate Graph'):
        G = nx.random_geometric_graph(100, 0.2)

        fig = plot_graph(G)
        st.pyplot(fig=fig, use_containter_width=True)
