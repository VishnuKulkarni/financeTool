from qtpy.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from partition1 import Partition1
from partition2 import Partition2
from partition3 import Partition3
from partition4 import Partition4

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set main window title and size
        self.setWindowTitle('Large GUI')
        self.setFixedSize(1700, 900)

        # Create grid layout for partitions
        self.grid = QGridLayout()

        # Add partition widgets to grid layout
        
        partition2 = Partition2()
        self.grid.addLayout(partition2, 0, 1)
        self.grid.addLayout(Partition1(partition2), 0, 0)
        self.grid.addLayout(Partition3(), 0, 2)
        self.grid.addLayout(Partition4(), 0,3)

        # Create central widget and set grid layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.grid)

        # Set main window central widget
        self.setCentralWidget(self.central_widget)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


