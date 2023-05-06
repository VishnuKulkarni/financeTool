from PyQt5.QtWidgets import QDialog
from qtpy.QtWidgets import QVBoxLayout, QLabel, QFrame, QPushButton, QTextEdit, QCheckBox, QLineEdit, QComboBox

class Partition1(QVBoxLayout):
    CONNECTED = False
    def __init__(self):
        super().__init__()

        # Create label for partition
        self.label = QLabel('Partition 1')
        self.label.setFixedSize(200, 150)
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Box)

        # Create button, checkbox, text input, dropdown menu, and text display area in partition
        self.button1 = QPushButton('Connect')
        self.button1.clicked.connect(self.Connect)

        self.checkbox = QCheckBox('Checkbox')
        self.textinput = QLineEdit()
        self.dropdown = QComboBox()
        self.dropdown.addItems(self.GetBisiList())
        self.textdisplay = QTextEdit()

        # Add button, checkbox, text input, dropdown menu, and text display area to partition layout
        self.addWidget(self.label)
        self.addWidget(self.button1)
        self.addWidget(self.checkbox)
        self.addWidget(self.textinput)
        self.addWidget(self.dropdown)
        self.addWidget(self.textdisplay)
        self.addWidget(self.frame)


    def Connect(self):
        #SAL : add connection code here. After success set 'Partition1.CONNECTED = True'

        Partition1.CONNECTED = True
        print("connected")

        #if connection fails,set 'Partition1.CONNECTED = False'

        # Clear the current items in the drop-down menu
        self.dropdown.clear()
        self.dropdown.addItems(self.GetBisiList())

    def GetBisiList(self):
        if Partition1.CONNECTED:
            bisilist = ['aa','bb','cc'] # SAL : call the 'ListOfBisi' api here
        else:
            bisilist = ['a1a','b1b','c1c'] #VK : default list when not connected to db. Think over it
        return bisilist



