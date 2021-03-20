import networkx as nx 
from pyvis.network import Network
import matplotlib.pyplot as plt 


class Graph():

    def __init__(self):
        graph = nx.Graph()

    def load_csv(self, filename):
        pass

    def load_pkl(self, filename):
        pass

    def load_graphml(self, filename):
        pass

    def add_edge(start_node, end_node, weight=1):
        self.graph.add_edge((start_node, end_node, {'weight': weight}))

    def add_verticses(iterator):
        self.graph.add_nodes_from(iterator)

    def add_vertics(vertics):
        self.graph.add_node(vertics)

    def remove_edge(start_node, end_node):
        self.graph.remove_node((start_node, start_node))

    def set__node_attributes(node, attributes):
        for key, value in attributes.items():
            self.graph[node][key] = value