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


from core.Graph import Graph
from utils.algorithms import *


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

    '''
    def add_node_tab(self, vlay):
        box = CollapsibleBox("Add Node")
        vlay.addWidget(box)
        lay = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("Add Label")
        lay.addWidget(label)
        self.nodeLabel = QLineEdit(self)
        lay.addWidget(self.nodeLabel)


        self.create_node_button = QPushButton('Create Node')
        self.create_node_button.clicked.connect(self.create_node)
        lay.addWidget(self.create_node_button)
        box.setContentLayout(lay)

    @pyqtSlot()
    def create_node(self):
        """Add node, activated when button is pressed
        """
        nodeLabel = self.nodeLabel.text()
        self.graph.add_node(nodeLabel)
        self.reload_graph()
        self.nodeLabel.clear()
        self.populate_node_list()


    def delete_node_tab(self, vlay):
        box = CollapsibleBox("Delete Node")
        vlay.addWidget(box)
        lay = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("Selet Node")
        lay.addWidget(label)
        lay.addWidget(self.node_list)

        self.delete_node_button = QPushButton('Delete Node')
        self.delete_node_button.clicked.connect(self.remove_node)
        lay.addWidget(self.delete_node_button)
        box.setContentLayout(lay)


    @pyqtSlot()
    def remove_node(self):
        """Add node, activated when button is pressed
        """
        nodeLabel = self.node_list.currentText()
        self.graph.delete_node(nodeLabel)
        self.reload_graph()
        self.populate_node_list()


    ############### Edge operations

    def add_edge_tab(self, vlay):
        box = CollapsibleBox("Add Edge")
        vlay.addWidget(box)
        lay = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("Selet Start Node")
        lay.addWidget(label)
        lay.addWidget(self.node_list_add_start)

        label = QtWidgets.QLabel("Selet End Node")
        lay.addWidget(label)
        lay.addWidget(self.node_list_add_end)

        label = QtWidgets.QLabel("Weight")
        lay.addWidget(label)
        self.weight_input = QLineEdit(self)
        lay.addWidget(self.weight_input)

        self.add_edge_button = QPushButton('Add Edge')
        self.add_edge_button.clicked.connect(self.add_edge)
        lay.addWidget(self.add_edge_button)
        box.setContentLayout(lay)

    @pyqtSlot()
    def add_edge(self):
        """Delete Edge, activated when button is pressed
        """
        nodeLabel_start = self.node_list_add_start.currentText()
        nodeLabel_end = self.node_list_add_end.currentText()
        weight = self.weight_input.text()

        try:
            weight = float(weight)
            self.graph.add_edge(nodeLabel_start, nodeLabel_end, weight)
        except ValueError:
            print("Weight invalid, taking default value")
            self.graph.add_edge(nodeLabel_start, nodeLabel_end)

        self.reload_graph()
        self.weight_input.clear()
        self.populate_node_list()

    def remove_edge_tab(self, vlay):
        box = CollapsibleBox("Delete Edge")
        vlay.addWidget(box)
        lay = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("Selet Start Node")
        lay.addWidget(label)
        lay.addWidget(self.node_list_delete_start)

        label = QtWidgets.QLabel("Selet End Node")
        lay.addWidget(label)
        lay.addWidget(self.node_list_delete_end)

        self.delete_edge_button = QPushButton('Delete Edge')
        self.delete_edge_button.clicked.connect(self.remove_edge)
        lay.addWidget(self.delete_edge_button)
        box.setContentLayout(lay)

    @pyqtSlot()
    def remove_edge(self):
        """Delete Edge, activated when button is pressed
        """
        nodeLabel_start = self.node_list_delete_start.currentText()
        nodeLabel_end = self.node_list_delete_end.currentText()
        self.graph.delete_edge(nodeLabel_start, nodeLabel_end)

        self.load_graph()
        self.weight_input.clear()
        self.populate_node_list()
    '''
    ################################


    #######################################################################################################


    def loadPage(self):
        with open('curr.html', 'r') as f:
            html = f.read()
            self.webEngineView.setHtml(html)

    def load_graph(self):
        nt = Network('500px', '500px')
        nt.from_nx(self.graph.graph)
        nt.write_html('curr.html')
        self.loadPage()
        self.update()

def main():
    app = QApplication(sys.argv)
    ex = VisualizeGraph()
    sys.exit(app.exec_())







class CollapsibleBox(QtWidgets.QWidget):
    def __init__(self, title="", parent=None):
        super(CollapsibleBox, self).__init__(parent)

        self.toggle_button = QtWidgets.QToolButton(
            text=title, checkable=True, checked=False
        )
        self.toggle_button.setStyleSheet("QToolButton { border: none; }")
        self.toggle_button.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon
        )
        self.toggle_button.setArrowType(QtCore.Qt.RightArrow)
        self.toggle_button.pressed.connect(self.on_pressed)

        self.toggle_animation = QtCore.QParallelAnimationGroup(self)

        self.content_area = QtWidgets.QScrollArea(
            maximumHeight=0, minimumHeight=0
        )
        self.content_area.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        self.content_area.setFrameShape(QtWidgets.QFrame.NoFrame)

        lay = QtWidgets.QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.toggle_button)
        lay.addWidget(self.content_area)

        self.toggle_animation.addAnimation(
            QtCore.QPropertyAnimation(self, b"minimumHeight")
        )
        self.toggle_animation.addAnimation(
            QtCore.QPropertyAnimation(self, b"maximumHeight")
        )
        self.toggle_animation.addAnimation(
            QtCore.QPropertyAnimation(self.content_area, b"maximumHeight")
        )

    @pyqtSlot()
    def on_pressed(self):
        checked = self.toggle_button.isChecked()
        self.toggle_button.setArrowType(
            QtCore.Qt.DownArrow if not checked else QtCore.Qt.RightArrow
        )
        self.toggle_animation.setDirection(
            QtCore.QAbstractAnimation.Forward
            if not checked
            else QtCore.QAbstractAnimation.Backward
        )
        self.toggle_animation.start()

    def setContentLayout(self, layout):
        lay = self.content_area.layout()
        del lay
        self.content_area.setLayout(layout)
        collapsed_height = (
            self.sizeHint().height() - self.content_area.maximumHeight()
        )
        content_height = layout.sizeHint().height()
        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(500)
            animation.setStartValue(collapsed_height)
            animation.setEndValue(collapsed_height + content_height)

        content_animation = self.toggle_animation.animationAt(
            self.toggle_animation.animationCount() - 1
        )
        content_animation.setDuration(500)
        content_animation.setStartValue(0)
        content_animation.setEndValue(content_height)



if __name__ == '__main__':
    main()





"""
if __name__ == "main__"
'''
g = nx.Graph() 
  
g.add_edge(1, 2) 
g.add_edge(2, 3) 
g.add_edge(3, 4) 
g.add_edge(1, 4) 
g.add_edge(1, 5) 

nt = Network('500px', '500px')
#nt.show_buttons(filter_=['nodes'])
nt.from_nx(g)
nt.write_html('nx.html')

#nt.add_node(10,label="Node 0")

g.add_node(7)

#nt.from_nx(g)
nt.write_html('nx2.html')
'''

label = svr
title  =  ji show



nt.from_nx(g)
nt.show('nx.html')
save_graph(
)

### Update
write_html
#plt.savefig("filename.png") 
'''

"""
