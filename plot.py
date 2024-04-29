import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import networkx as nx


def generate_node_trace(G: nx.Graph) -> go.Figure:

    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlOrRd_r',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2
        )
    )

    node_adjacencies = []
    node_text = []
    for node, adjacencies in enumerate(G.adjacency()):
        node_adjacencies.append(len(adjacencies[1]))
        node_text.append('# of connections: '+str(len(adjacencies[1])))

    node_trace.marker.color = node_adjacencies
    node_trace.text = node_text

    return node_trace


def generate_edge_trace(G: nx.Graph) -> go.Figure:

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']  # node 1 coord
        x1, y1 = G.nodes[edge[1]]['pos']  # node 2 coord
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    return edge_trace


def plot_graph(G: nx.Graph, graph_type: str) -> go.Figure:

    st.subheader('Graph Visualization')
    node_trace = generate_node_trace(G)
    edge_trace = generate_edge_trace(G)

    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title=f"{graph_type} - {str(G)}",
            titlefont_size=16,
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20, l=5, r=5, t=40),
            annotations=[dict(
                text="Network",
                showarrow=False,
                xref="paper",
                yref="paper",
                x=0.005,
                y=-0.002,
            )],
            xaxis=dict(
                showgrid=False, zeroline=False, showticklabels=False
            ),
            yaxis=dict(
                showgrid=False, zeroline=False, showticklabels=False
            )
        )
    )
    return fig


def display_graph_plots(G: nx.Graph, graph_type: str) -> None:
    fig = plot_graph(G, graph_type)
    st.plotly_chart(fig, use_containter_width=True)
    return


def _max(stat: dict) -> float:
    return round(max(dict(stat).values()), 4)


def display_graph_stats(G: nx.Graph) -> None:

    l1, v1 = 'Number of Nodes', G.number_of_nodes()
    l2, v2 = 'Number of Edges', G.number_of_edges()
    l3, v3 = 'Number of Components', nx.number_connected_components(G)
    l4, v4 = 'Graph Density', round(nx.density(G), 4)
    l5, v5 = 'Max Degree Adjacency', _max(G.degree())
    l6, v6 = 'Max Degree Centrality', _max(nx.degree_centrality(G))
    l7, v7 = 'Max Closeness Centrality', _max(nx.closeness_centrality(G))
    l8, v8 = 'Max Betweenness Centrality', _max(nx.betweenness_centrality(G))

    st.subheader('Graph Statistics')
    m1, m2, m3, m4 = st.columns([1] * 4)
    m1.metric(l1, v1)
    m2.metric(l2, v2)
    m3.metric(l3, v3)
    m4.metric(l4, v4)

    m5, m6, m7, m8 = st.columns([1] * 4)
    m5.metric(l5, v5)
    m6.metric(l6, v6)
    m7.metric(l7, v7)
    m8.metric(l8, v8)

    return


def plot_dist(data: dict, title: str) -> None:

    fig = px.histogram(
        dict(data).values(), nbins=10, hover_data={'variable': False}
    )
    fig.update_layout(
        title=title, xaxis_title=title, yaxis_title='Count',
        height=250, showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)
    return


def display_distributions(G: nx.Graph) -> None:

    st.subheader("Distributions of Node Centrality")
    plot_dist(G.degree(), 'Degree Adjacency')
    plot_dist(nx.degree_centrality(G), 'Degree Centrality')
    plot_dist(nx.closeness_centrality(G), 'Closeness Centrality')
    plot_dist(nx.betweenness_centrality(G), 'Betweenness Centrality')
    return


def display_ref_url() -> None:

    st.subheader('More Explanations')
    url = "https://sabrinazhengliu.medium.com/"
    url += "node-centrality-algorithms-explained-491720a7a74e"
    st.markdown(f"[{url}](%s)" % url)
    return
