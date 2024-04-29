import streamlit as st
from graph import generate_graph
from plot import display_graph_plots
from plot import display_graph_stats
from plot import display_distributions
from plot import display_ref_url


def initialize_page():
    st.title('Graph Analytics Explained')
    pass


def initialize_params():

    global sb
    sb = st.sidebar

    global graph_type, n, r
    n = 0
    r = 0
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

        G = generate_graph(graph_type, n, r)

        display_graph_plots(G, graph_type)
        display_graph_stats(G)
        display_distributions(G)
        display_ref_url()
