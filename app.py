import streamlit as st
from plot import plot_graph
import networkx as nx
import random


def initialize_page():
    st.title('Graph Analytics Explained')
    pass


def initialize_params():

    global sb
    sb = st.sidebar

    global graph_type, n, r
    options = ['Predefined Graph', 'Random Graph', 'Customized Graph']
    graph_type = sb.radio(label='Choose Graph Type:', options=options)

    if graph_type == 'Customized Graph':
        n = sb.slider(
            label='Choose Number of Nodes:',
            min_value=5, max_value=100, value=50, step=5
        )
        r = sb.slider(
            label='Choose Radius of Edge Generation:',
            min_value=0.05, max_value=1.0, value=0.15, step=0.05
        )
    pass


if __name__ == '__main__':

    initialize_page()
    initialize_params()

    if sb.button('Generate Graph'):
        
        if graph_type == 'Predefined Graph':
            G = nx.binomial_tree(8)
            pos = nx.spring_layout(G, seed=10)
            for i, _ in enumerate(G.nodes):
                G.nodes[i]['pos'] = pos[i]
        
        if graph_type == 'Random Graph': 
            n = random.randint(1, 100)   # return int between 1 and 100
            p = random.random()          # return float between 0 and 1
            G = nx.gnp_random_graph(n, p)
            pos = nx.spring_layout(G)
            for i, _ in enumerate(G.nodes):
                G.nodes[i]['pos'] = pos[i]

        if graph_type == 'Customized Graph':
            G = nx.random_geometric_graph(n, r)
        
        st.write(G)
        fig = plot_graph(G)
        st.plotly_chart(fig, use_containter_width=True)
