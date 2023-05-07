from PyQt5.QtWidgets import QDialog
from qtpy.QtWidgets import QVBoxLayout, QLabel, QFrame, QPushButton, QTextEdit, QCheckBox, QLineEdit, QComboBox

class Partition1(QVBoxLayout):
    CONNECTED = False
    selected_option = "none"
    def __init__(self):
        super().__init__()

        # Create label for partition
        self.label = QLabel('Dashboard')
        self.label.setFixedSize(200, 15)
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Box)

        # Create button, checkbox, text input, dropdown menu, and text display area in partition
        self.button1 = QPushButton('Connect')
        self.button1.clicked.connect(self.Connect)

        #self.checkbox = QCheckBox('Checkbox')
        #self.textinput = QLineEdit()

        self.dropdown_label = QLabel('List of BiSi')
        self.dropdown = QComboBox()
        self.dropdown.addItems(self.GetBisiList())
        self.selected_option = self.dropdown.currentText()
        self.dropdown.activated.connect(self.GetNameOfBisiSelected)

        # Create line separator
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line2 = QFrame()
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)

        self.dropdown_label_ppl = QLabel('List of People')
        self.dropdown_ppl = QComboBox()
        #self.dropdown_ppl.addItems(self.GetPplList()) #this shud fetch data from db based on BiSI name selected
        self.selected_option_ppl = self.dropdown_ppl.currentText()
        self.dropdown_ppl.activated.connect(self.GetNameOfPersonSelected)


        self.textdisplay = QTextEdit()

        # Add button, checkbox, text input, dropdown menu, and text display area to partition layout
        self.addWidget(self.label)
        self.addWidget(self.button1)

        self.addWidget(self.line)

        #self.addWidget(self.checkbox)
        #self.addWidget(self.textinput)

        self.addWidget(self.dropdown_label)
        self.addWidget(self.dropdown)

        self.addWidget(self.line2)


        self.addWidget(self.dropdown_label_ppl)
        self.addWidget(self.dropdown_ppl)

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
            bisilist = ["aa","bb","cc"] # SAL : call the 'ListOfBisi' api here
        else:
            bisilist = ['Not Connected'] #VK : default list when not connected to db. Think over it
        return bisilist

    def GetNameOfBisiSelected(self):
        text = self.dropdown.currentText()
        print(text)
        self.GetPplList()
        return text

    def GetPplList(self):
        if Partition1.CONNECTED:
            ppllist = ["pp1","pp2","pp3"] # SAL : call the 'ListOfPll' api here for specific bisi
        else:
            ppllist = ['Not Connected'] #VK : default list when not connected to db. Think over it
        # Clear the current items in the drop-down menu
        self.dropdown_ppl.clear()
        self.dropdown_ppl.addItems(ppllist)

    def GetNameOfPersonSelected(self):
        personName = self.dropdown_ppl.currentText()
        print(personName)
        return personName