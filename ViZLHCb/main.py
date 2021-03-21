
import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from ui.draw import DrawGraph
from ui.visualize import VisualizeGraph

class Window(QMainWindow):
    '''Main UI component of the application
    '''

    def __init__(self):
        super().__init__()
        self.title = "ViZLHCb"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.fileName = ""
        self.InitUI()

    def InitUI(self):
        '''Initilise UI componets
        '''
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        visualize_graph = QPushButton('Visualize Graph', self)
        visualize_graph.move(100, 100)
        visualize_graph.clicked.connect(self.visualize_graph_onClick)

        draw_graph = QPushButton('Draw/Edit Graph', self)
        draw_graph.setGeometry(100, 200, 100, 30)
        draw_graph.clicked.connect(self.draw_graph_onClick)

        self.select_file = QPushButton('Select graph file(to Visualize or edit)', self)
        self.select_file.clicked.connect(self.openFileNameDialog)
        self.select_file.setGeometry(100, 300, 400, 30)
        self.show()

    @pyqtSlot()
    def openFileNameDialog(self):
        '''Select file from File dialoge box, activated on click of select file
        '''
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(self,"Open file", "","All files (*)", options=options)
        self.select_file.setText('File Selected')

    @pyqtSlot()
    def visualize_graph_onClick(self):
        '''Switch window to Visualize mode
        '''
        self.statusBar().showMessage("Switched to VisualizeGraph")
        self.cams = VisualizeGraph(self.fileName) 
        self.cams.show()
        self.close()

    @pyqtSlot()
    def draw_graph_onClick(self):
        '''Switch window to Draw graph mode
        '''
        self.statusBar().showMessage("Switched to Draw")
        self.cams = DrawGraph(self.fileName) 
        self.cams.show()
        self.close()

'''    
class Window1(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Window1')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

        label1 = QLabel(value)
        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        self.button.setIconSize(QSize(200, 200))
        
        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Click me!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)
        
        layoutH = QHBoxLayout()
        layoutH.addWidget(label1)
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close() 
'''      


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
