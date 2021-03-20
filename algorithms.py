import networkx as nx

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
    flow_value, _ = nx.maximum_flow(graph, start, end, capacity="weight")
    return flow_value

def find_radius(graph):
    algorithms.distance_measures.radius