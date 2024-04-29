import streamlit as st
from graph import make_graph
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

    url = 'https://github.com/sabrinazhengliu/graph-analytics-explained'
    sb.markdown(f"[Code Repo]({url})")

    global graph_type, n, p, r, e
    n, p, r, e = 0, 0, 0, 0

    options = [
        'Predefined Graph - Binomial Tree',
        'Random Graph',
        'Random Probability Graph - G(n, p)',
        'Random Geometric Graph - G(n, r)',
        'Random Customized Graph - G(n, e)',
    ]

    graph_type = sb.radio(label='Choose Graph Type:', options=options)

    if graph_type.endswith('G(n, p)'):
        n = sb.slider(
            label='Choose Number of Nodes:',
            min_value=5, max_value=100, value=50, step=1
        )
        p = sb.slider(
            label='Choose Probability of Edge Generation:',
            min_value=0.0, max_value=1.0, value=0.15, step=0.05
        )

    if graph_type.endswith('G(n, r)'):
        n = sb.slider(
            label='Choose Number of Nodes:',
            min_value=5, max_value=100, value=50, step=1
        )
        r = sb.slider(
            label='Choose Radius of Edge Generation:',
            min_value=0.05, max_value=1.0, value=0.15, step=0.05
        )

    def _max_edges(n_nodes):
        return int(n_nodes * (n_nodes - 1) / 2)

    if graph_type.endswith('G(n, e)'):
        n = sb.slider(
            label='Choose Number of Nodes:',
            min_value=5, max_value=100, value=50, step=1
        )
        e = sb.slider(
            label='Choose Number of Edges:',
            min_value=0, max_value=_max_edges(n), value=100, step=1
        )

    pass


if __name__ == '__main__':

    initialize_page()
    initialize_params()

    if sb.button('Generate Graph'):

        G = make_graph(graph_type, n, p, r, e)

        display_graph_plots(G, graph_type)
        display_graph_stats(G)
        display_distributions(G)
        display_ref_url()
