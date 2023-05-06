from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel, \
    QPushButton, QLineEdit, QComboBox, QCheckBox, QTextEdit


class Partition1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        label1 = QLabel("Partition 1, Label 1")
        button1 = QPushButton("Partition 1, Button 1")
        button2 = QPushButton("Partition 1, Button 2")

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(button1)
        layout.addWidget(button2)

        self.setLayout(layout)

class Partition2(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        label1 = QLabel("Partition 2, Label 1")
        checkbox1 = QCheckBox("Partition 2, Checkbox 1")
        textbox1 = QLineEdit("Partition 2, Textbox 1")
        dropdown1 = QComboBox()
        dropdown1.addItem("Option 1")
        dropdown1.addItem("Option 2")
        dropdown1.addItem("Option 3")

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(checkbox1)
        layout.addWidget(textbox1)
        layout.addWidget(dropdown1)

        self.setLayout(layout)

class Partition3(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        label1 = QLabel("Partition 3, Label 1")
        textdisplay1 = QTextEdit("Partition 3, Text Display 1")
        dropdown1 = QComboBox()
        dropdown1.addItem("Option 1")
        dropdown1.addItem("Option 2")
        dropdown1.addItem("Option 3")

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(textdisplay1)
        layout.addWidget(dropdown1)

        self.setLayout(layout)

class MyTabWidget(QTabWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")

        self.initUI()

    def initUI(self):
        # Tab 1
        partition1 = Partition1(self)
        partition2 = Partition2(self)
        partition3 = Partition3(self)

        tab1_layout = QHBoxLayout()
        tab1_layout.addWidget(partition1)
        tab1_layout.addWidget(partition2)
        tab1_layout.addWidget(partition3)

        self.tab1.setLayout(tab1_layout)

        # Tab 2
        label2 = QLabel("This is Tab 2")
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(label2)

        self.tab2.setLayout(tab2_layout)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.setGeometry(100, 100, 1200, 600)

        self.tabWidget = MyTabWidget(self)
        self.setCentralWidget(self.tabWidget)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
