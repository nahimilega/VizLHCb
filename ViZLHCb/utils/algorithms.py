import networkx as nx


'''
betweenness_centrality()
'''
def num_edges_rows(graph):
    """Find number of edges and nodes
    
    Args:
        graph: graph object if class Graph
    
    Returns:
        num_edges, num_nodes
    """
    return len(graph.graph.edges), len(graph.graph.nodes)


def s_metric(graph):
    """Returns the s-metric of graph
    """
    return nx.s_metric(graph.graph, normalized=False)


def global_efficiency(graph):
    """Returns the average global efficiency of the graph.
    """
    return nx.global_efficiency(graph.graph)


def is_connected(graph):
    """Returns True if the graph is connected, False otherwise.
    """
    return nx.is_connected(graph.graph)


def find_max_flow(graph, start, end):
    """
        Find a maximum single-commodity flow

        Args:
            graph: networkx graph object
            start: start node
            end: end node

        Returns:
            int: Flow value
    """
    try:
        flow_value, _ = nx.maximum_flow(graph.graph, start, end, capacity="weight")
        return flow_value
    except Exception as e:
        print("Error in Max flow computation ", e)
        return "NaN"


def shortest_path(graph, source, target):
    try:
        distance = nx.shortest_path_length(graph.graph, source=source, target=target, weight='weight')
        return distance
    except Exception as e:
        print("Error in shortest path computation ", e)
        return "NaN"
