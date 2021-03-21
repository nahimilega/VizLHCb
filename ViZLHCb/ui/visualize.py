import sys
sys.path.append('..')
import networkx as nx 
from pyvis.network import Network
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QMainWindow, QTextEdit, QLineEdit, QComboBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import pyqtSlot
import PyQt5.QtWidgets as QtWidgets
from PyQt5 import *
import random

import networkx as nx 
from pyvis.network import Network

from ViZLHCb.ui.CollapsibleBox import CollapsibleBox
from ViZLHCb.core.Graph import Graph
from ViZLHCb.utils.algorithms import *


class VisualizeGraph(QMainWindow):

    def __init__(self, fileName, parent=None):
        super().__init__()
        self.graph = Graph()
        self.graph.load_graph(fileName)
        self.graph.assign_node_title()
        self.node_list = list(map(str, list(self.graph.graph.nodes)))
        self.initUI()
        

    def initUI(self):
        """Initilise UI
        """
        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)

        self.load_graph()
        
        self.make_collapsable_box()
        self.setGeometry(50, 50, 1200, 800)
        self.setWindowTitle('Visualizer')

        self.show()


    def make_collapsable_box(self):
        """Make the left option box
        """

        dock = QtWidgets.QDockWidget("Options")
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
        scroll = QtWidgets.QScrollArea()
        dock.setWidget(scroll)
        content = QtWidgets.QWidget()
        scroll.setWidget(content)
        scroll.setWidgetResizable(True)
        vlay = QtWidgets.QVBoxLayout(content)

        self.show_info_tab(vlay)
        self.shortest_path_tab(vlay)
        self.max_flow_tab(vlay)
        '''
        self.add_node_tab(vlay)
        self.delete_node_tab(vlay)
        self.add_edge_tab(vlay)
        self.remove_edge_tab(vlay)
        self.save_tab(vlay)
        '''
        vlay.addStretch()

    def show_info_tab(self, vlay):
        num_edges, num_nodes = num_edges_rows(self.graph)

        box = CollapsibleBox("General Info")
        vlay.addWidget(box)
        lay = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("No. edges: {}".format(num_edges))
        lay.addWidget(label)

        label = QtWidgets.QLabel("No. Nodes: {}".format(num_nodes))
        lay.addWidget(label)

        label = QtWidgets.QLabel("S metric: {}".format(s_metric(self.graph)))
        lay.addWidget(label)

        label = QtWidgets.QLabel("Global Efficiency: {}".format(global_efficiency(self.graph)))
        lay.addWidget(label)

        box.setContentLayout(lay)


    def shortest_path_tab(self, vlay):
        '''Populate UI component of max flow
        '''
        box = CollapsibleBox("Compute Shortest parh")
        vlay.addWidget(box)
        lay = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel("Select Source")
        lay.addWidget(label)

        self.shortest_path_scr = QComboBox()
        self.shortest_path_scr.addItems(self.node_list)
        lay.addWidget(self.shortest_path_scr)

        label = QtWidgets.QLabel("Select Target")
        lay.addWidget(label)

        self.shortest_path_trgt = QComboBox()
        self.shortest_path_trgt.addItems(self.node_list)
        lay.addWidget(self.shortest_path_trgt)

        self.shortest_path_ans = QtWidgets.QLabel("")
        lay.addWidget(self.shortest_path_ans)

        self.shortest_path_button = QPushButton('Find Max Flow')
        self.shortest_path_button.clicked.connect(self.find_shortest_path)
        lay.addWidget(self.shortest_path_button)

        box.setContentLayout(lay)

    @pyqtSlot()
    def find_shortest_path(self):
        source = self.shortest_path_scr.currentText()
        target = self.shortest_path_trgt.currentText()
        length = shortest_path(self.graph, source, target)
        self.shortest_path_ans.setText(str(length))
        self.update()

    def max_flow_tab(self, vlay):
        '''Populate UI component of max flow
        '''
        box = CollapsibleBox("Compute Max flow")
        vlay.addWidget(box)
        lay = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel("Select Source")
        lay.addWidget(label)

        self.max_flow_scr = QComboBox()
        self.max_flow_scr.addItems(self.node_list)
        lay.addWidget(self.max_flow_scr)

        label = QtWidgets.QLabel("Select Target")
        lay.addWidget(label)

        self.max_flow_trgt = QComboBox()
        self.max_flow_trgt.addItems(self.node_list)
        lay.addWidget(self.max_flow_trgt)

        self.max_flow_ans = QtWidgets.QLabel("")
        lay.addWidget(self.max_flow_ans)

        self.max_flow_button = QPushButton('Find Max Flow')
        self.max_flow_button.clicked.connect(self.max_flow)
        lay.addWidget(self.max_flow_button)

        box.setContentLayout(lay)

    @pyqtSlot()
    def max_flow(self):
        '''Compute and update max flow, activate when button is pressed
        '''
        source = self.max_flow_scr.currentText()
        target = self.max_flow_trgt.currentText()
        flow = find_max_flow(self.graph, source, target)
        self.max_flow_ans.setText(str(flow))
        self.update()


    def loadPage(self):
        with open('curr.html', 'r') as f:
            html = f.read()
            self.webEngineView.setHtml(html)

    def load_graph(self):
        nt = Network('800px', '1000px')
        nt.from_nx(self.graph.graph)
        nt.write_html('curr.html')
        self.loadPage()
        self.update()

def main():
    app = QApplication(sys.argv)
    ex = VisualizeGraph()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
