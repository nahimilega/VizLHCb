import networkx as nx 
from pyvis.network import Network
import matplotlib.pyplot as plt 
import yaml


class Graph():
    
    def __init__(self):
        self.graph = nx.Graph()
        self.default_label = 1

    def add_node(self, nodeLabel):
        '''Make a node in the graph, assign a number if the label not specified

        Args:
            nodeLabel: Node Label

        '''
        if nodeLabel != "":
            self.graph.add_node(nodeLabel)
        else:
            self.graph.add_node(str(self.default_label))
            self.default_label += 1

    def delete_node(self, nodeLabel):
        '''Delete a node in the graph, assign a number if the label not specified

        Args:
            nodeLabel: Node Label

        '''
        try:
            self.graph.remove_node(nodeLabel)
        except Exception as e:
            print("[ERROR] Issue in deleting node ", nodeLabel)
            print("The Error Message is ", e)

    def add_edge(self, start_node, end_node, weight=1):
        '''Mke an undirected edge in the graph

        Args:
            start_node: staring node 
            end_node: ending node
            weight: weight of the edge

        '''
        self.graph.add_edge(start_node, end_node, weight=weight)

    def delete_edge(self, start_node, end_node):
        try:
            self.graph.remove_edge(start_node, end_node)
        except Exception as e:
            print("[ERROR] Issue in deleting edge from", start_node, "to", end_node)
            print("The Error Message is ", e)

    def save_graph(self, filename, fileType):
        """Write graph to GML or Adjacency list or YML format
        
        Args:
            filename : File or filename to read
            fileType (str): Type of file to write, should be "GML Format" or "Adjacency list"
                            or "YAML"
        """
        if fileType == "GML Format":
            nx.write_gml(self.graph, filename+".gml")
        if fileType == "Adjacency list":
            nx.write_adjlist(self.graph, filename+".adjlist")
        if fileType == "YAML":
            nx.write_yaml(self.graph, filename + ".yaml")

    def load_graph(self, filename):
        """Read graph from GML or Adjacency list or YML format
        
        Args:
            filename : File or filename to read
        """
        try:
            file_extention = list(filename.split("."))[-1]
            if file_extention == "gml":
                self.graph = nx.read_gml(filename)
            if file_extention == "adjlist":
                self.graph = nx.read_adjlist(filename)
            if file_extention == "yaml":
                nx.read_yaml(filename)
        except Exception as e:
            print("Error in loading Graph file: The error is", e)

    def assign_node_title(self):
        centrality = nx.betweenness_centrality(self.graph)
        degree = self.graph.degree()
        args = {}
        for i in list(self.graph.nodes):
            args[i] = "Degree: {}<br> Centrality: {}".format(degree[i], centrality[i])
        nx.set_node_attributes(self.graph, args, 'title')


