from PyQt5.QtGui import QFont
from qtpy.QtWidgets import QVBoxLayout,QApplication,  QLabel, QFrame, QPushButton, QTextEdit, QCheckBox, QLineEdit, QComboBox

import common
from partition3 import Partition3
from partition4 import Partition4
from functions import DBFunctions


class Partition2(QVBoxLayout):
    selected_option_ppl = "none"

    def __init__(self):
        super().__init__()

        # Create label for partition
        self.label = QLabel('PERSON DETAILS')
        self.label.setFont(QFont("Arial", 8, QFont.Bold))
        self.label.setFixedSize(200, 15)
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Box)

        # Create button, checkbox, text input, dropdown menu, and text display area in partition
        self.button = QPushButton('Button')
        self.checkbox = QCheckBox('Checkbox')
        self.textinput = QLineEdit()

        self.dropdown_label_ppl = QLabel('List of People')
        self.dropdown_ppl = QComboBox()
       
        self.dropdown_ppl.addItems(['Not nnected']) #this shud fetch data from db based on BiSI name selected

        self.selected_option_ppl = self.dropdown_ppl.currentText()
        self.dropdown_ppl.activated.connect(self.DisplayPersonDetails)

        self.textdisplay_partition2 = QTextEdit()

        # Add clear button for text display area
        self.clear_button = QPushButton('Clear')
        self.clear_button.clicked.connect(self.ClearTextDisplay)

        # Add button, checkbox, text input, dropdown menu, and text display area to partition layout
        self.addWidget(self.label)
        self.addWidget(self.button)
        self.addWidget(self.checkbox)
        self.addWidget(self.textinput)

        self.addWidget(self.dropdown_label_ppl)
        self.addWidget(self.dropdown_ppl)

        self.addWidget(self.textdisplay_partition2)

        self.addWidget(self.clear_button)

        self.addWidget(self.frame)

    def GetPplList(self,bisiName):
        if common.CONNECTED:
            pplList = DBFunctions.getAllUsersListByBisiName(bisiName)  
            # SAL : call the 'ListOfPll' api here for specific bisi
        else:
            pplList = ['Not nnected']  # VK : default list when not connected to db. Think over it

        # Clear the current items in the ppl list  drop-down menu
        self.dropdown_ppl.clear()
        self.dropdown_ppl.addItems(pplList)

        return pplList

    def DisplayPersonDetails(self):
        personName = self.GetNameOfPersonSelected()

        #VK: Figure out a way to bring bisi Name from Partition 1
        person_dict = DBFunctions.getUserDetailsByUserNameAndBisiName(personName,'bisi1') 

        # VK: Set the text display area's text from the above dict
        self.textdisplay_partition2.append(f"Person Name: {personName}")
        self.textdisplay_partition2.append(f"Person's address : {personName}")
        self.textdisplay_partition2.append(f"Person's phone : {personName}")
        self.textdisplay_partition2.append(f"Person's encash status : {personName}")
        self.textdisplay_partition2.append(f"Encash value : {personName}")
        self.textdisplay_partition2.append(f"TBD : {personName}")
        self.textdisplay_partition2.append(f"------------------------------------------------------------------")
        self.textdisplay_partition2.append(f"Coming from db: {person_dict}")



    def GetNameOfPersonSelected(self):
        personName = self.dropdown_ppl.currentText()
        print(personName)
        return personName

    def ClearTextDisplay(self):
        self.textdisplay_partition2.clear()