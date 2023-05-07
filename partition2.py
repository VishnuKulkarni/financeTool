from qtpy.QtWidgets import QVBoxLayout, QLabel, QFrame, QPushButton, QTextEdit, QCheckBox, QLineEdit, QComboBox

import common
from partition3 import Partition3
from partition4 import Partition4

class Partition2(QVBoxLayout):

    def __init__(self):
        super().__init__()

        # Create label for partition
        self.label = QLabel('PERSON DETAILS')
        self.label.setFixedSize(200, 15)
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Box)

        # Create button, checkbox, text input, dropdown menu, and text display area in partition
        self.button = QPushButton('Button')
        self.checkbox = QCheckBox('Checkbox')
        self.textinput = QLineEdit()

        #self.dropdown = QComboBox()
        #self.dropdown.addItems(['Option 1', 'Option 2', 'Option 3'])


        #self.dropdown_label_ppl = QLabel('List of People')
        #self.dropdown_ppl = QComboBox()
        #self.dropdown_ppl.addItems(self.GetPplList()) #this shud fetch data from db based on BiSI name selected
        #self.selected_option_ppl = self.dropdown_ppl.currentText()
        #self.dropdown_ppl.activated.connect(self.GetNameOfPersonSelected)


        self.textdisplay_partition2 = QTextEdit()

        # Add button, checkbox, text input, dropdown menu, and text display area to partition layout
        self.addWidget(self.label)
        self.addWidget(self.button)
        self.addWidget(self.checkbox)
        self.addWidget(self.textinput)

        #self.addWidget(self.dropdown_label_ppl)
        #self.addWidget(self.dropdown_ppl)

        self.addWidget(self.textdisplay_partition2)
        self.addWidget(self.frame)

