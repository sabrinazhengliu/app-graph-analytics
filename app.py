import streamlit as st
from graph import Graph
from graph import RandomGraph
from graph import CustomizedGrpah


def initialize_page():
    st.title('Graph Analytics Dashboard')
    pass


def n_edges_limit(n_nodes):
    return n_nodes * (n_nodes - 1) / 2


def initialize_params():
    global graph_type
    options = ['Predefined Graph', 'Random Graph' 'Customized Graph']
    graph_type = st.radio(options)
    n_nodes = st.slider(
        label='Choose Number of Nodes:',
        min_value=5, max_value=100, value=10, step=5
    )
    n_edges = st.slider(
        label='Choose Number of Edges:',
        min_value=0, max_value=n_edges_limit, value=n_nodes - 1, step=1
    )
    pass


if __name__ == '__main__':

    initialize_page()
    initialize_params()

    if st.button('Generate Graph'):

        st.write('ok!')
