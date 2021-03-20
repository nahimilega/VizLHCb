import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

import networkx as nx 
from pyvis.network import Network
import matplotlib.pyplot as plt 
  


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        g = nx.Graph() 
        
        g.add_edge(1, 2) 
        g.add_edge(2, 3) 
        g.add_edge(3, 4) 
        g.add_edge(1, 4) 
        g.add_edge(1, 5) 
        #nx.draw(g, with_labels = True) 

        self.grp = g

        self.nt = Network('500px', '500px')
        #self.nt.show_buttons(filter_=['nodes'])


        self.nt.from_nx(self.grp)
        self.nt.save_graph('nx.html')




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