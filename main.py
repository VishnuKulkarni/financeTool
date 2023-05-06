from qtpy.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from partition1 import Partition1
from partition2 import Partition2
from partition3 import Partition3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set main window title and size
        self.setWindowTitle('Large GUI')
        self.setFixedSize(1600, 900)

        # Create grid layout for partitions
        self.grid = QGridLayout()

        # Add partition widgets to grid layout
        self.grid.addLayout(Partition1(), 0, 0)
        self.grid.addLayout(Partition2(), 0, 1)
        self.grid.addLayout(Partition3(), 0, 2)

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


