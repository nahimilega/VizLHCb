import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

import networkx as nx 
from pyvis.network import Networkimport sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QMainWindow, QTextEdit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import pyqtSlot
import PyQt5.QtWidgets as QtWidgets
from PyQt5 import *
import random

import networkx as nx 
from pyvis.network import Network

from Graph import Graph
import algorithms
class VisualizeGraph(QMainWindow):

    def __init__(self):
        super().__init__()
        self.graph = Graph() 
        self.initUI()

    def initUI(self):
        """Initilise UI
        """
        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        self.make_collapsable_box()
        self.setGeometry(50, 50, 1200, 800)

        self.setWindowTitle('Visualize Newtork')
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
        self.info_tab(vlay)
        
        for i in range(10):
            box = CollapsibleBox("Collapsible Box Header-{}".format(i))
            vlay.addWidget(box)
            lay = QtWidgets.QVBoxLayout()
            for j in range(8):
                label = QtWidgets.QLabel("{}".format(j))
                color = QtGui.QColor(*[random.randint(0, 255) for _ in range(3)])
                label.setStyleSheet(
                    "background-color: {}; color : white;".format(color.name())
                )
                label.setAlignment(QtCore.Qt.AlignCenter)
                lay.addWidget(label)

            box.setContentLayout(lay)
        vlay.addStretch()

    def add_node_tab(self, vlay):
        box = CollapsibleBox("Add Node")
        vlay.addWidget(box)
        lay = QtWidgets.QVBoxLayout()
        for j in range(8):
            label = QtWidgets.QLabel("{}".format(j))
            color = QtGui.QColor(*[random.randint(0, 255) for _ in range(3)])
            label.setStyleSheet(
                "background-color: {}; color : white;".format(color.name())
            )
            label.setAlignment(QtCore.Qt.AlignCenter)
            lay.addWidget(label)

        box.setContentLayout(lay)

    def delete_node_tab(self):
        pass

    def add_edge_tab(self):
        pass
    def delete_edge_tab(self):
        pass

    def loadPage(self):

        with open('nx2.html', 'r') as f:
            html = f.read()
            self.webEngineView.setHtml(html)

    def button_clicked(self):
        #self.label.setText("you pressed the button")
        self.nt.add_node(10,label="Node 0")
        self.nt.write_html('nx.html')
        self.update()
        self.loadPage()

    '''
    def side_bar()
        #self.webEngineView.reload()

    '''


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
import matplotlib.pyplot as plt 
  

from Graph import Graph

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        g = nx.Graph() 


        

        vbox = QVBoxLayout(self)

        self.webEngineView = QWebEngineView()
        self.loadPage()

        vbox.addWidget(self.webEngineView)

        self.setLayout(vbox)


        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QWebEngineView')

        self.b1 = QPushButton(self)
        self.b1.setText("click me!")
        self.b1.clicked.connect(self.button_clicked)
        self.show()

    def loadPage(self):

        with open('nx.html', 'r') as f:
            html = f.read()
            self.webEngineView.setHtml(html)

    def button_clicked(self):
        #self.label.setText("you pressed the button")


        self.nt.add_node(10,label="Node 0")
        self.nt.write_html('nx.html')
        
        self.update()
        self.loadPage()
        #self.webEngineView.reload()

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()