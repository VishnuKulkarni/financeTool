from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QDateEdit
from qtpy.QtWidgets import QVBoxLayout, QLabel, QFrame, QPushButton, QTextEdit, QCheckBox, QLineEdit, QComboBox

import common
from functions import DBFunctions

class Partition4(QVBoxLayout):
    def __init__(self):
        super().__init__()

        # Create label for partition
        self.label = QLabel('RECORD ENTRY')
        self.label.setFont(QFont("Arial", 8, QFont.Bold))
        self.label.setFixedSize(200, 15)
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Box)

        # Create button, checkbox, text input, dropdown menu, and text display area in partition
        self.button = QPushButton('Button')
        self.checkbox = QCheckBox('Checkbox')

        self.textinput1 = QLineEdit()
        #self.textinput1.setText('ACTIVE')
        self.textinput2 = QLineEdit()
        self.textinput3 = QLineEdit()
        # Create a QDateEdit widget
        self.encash_date_edit = QDateEdit()
        self.encash_date_edit.setCalendarPopup(True)

        self.textinput5 = QLineEdit()
        self.textinput6 = QLineEdit()
        self.textinput7 = QLineEdit()

        self.dropdown_label = QLabel('Select BiSi')
        self.dropdown_partion4 = QComboBox()
        self.dropdown_partion4.addItems(['Not Connected'])
        self.dropdown_partion4.activated.connect(self.GetNameOfBisiSelectedAndUpdatePplDropdown)

        self.textdisplay = QTextEdit()

        #create input fields
        self.textinput_label1 = QLabel('BiSi Status                 ')
        self.textinput_label2 = QLabel('Months Completed     ')
        self.textinput_label3 = QLabel('Current Encash Sum   ')
        self.textinput_label4 = QLabel('Current Encash Date  ')
        self.textinput_label5 = QLabel('Current Commission      ')
        self.textinput_label6 = QLabel('TBD                          ')

        # Create a horizontal layout for textinput_label and textinput
        input_layout1 = QHBoxLayout()
        input_layout2 = QHBoxLayout()
        input_layout3 = QHBoxLayout()
        input_layout4 = QHBoxLayout()
        input_layout5 = QHBoxLayout()
        input_layout6 = QHBoxLayout()
        #input_layout7 = QHBoxLayout()

        input_layout1.addWidget(self.textinput_label1)
        input_layout2.addWidget(self.textinput_label2)
        input_layout3.addWidget(self.textinput_label3)
        input_layout4.addWidget(self.textinput_label4)
        input_layout5.addWidget(self.textinput_label5)
        input_layout6.addWidget(self.textinput_label6)
        #input_layout7.addWidget(self.textinput_label7)

        input_layout1.addWidget(self.textinput1)
        input_layout2.addWidget(self.textinput2)
        input_layout3.addWidget(self.textinput3)
        input_layout4.addWidget(self.encash_date_edit)
        input_layout5.addWidget(self.textinput5)
        input_layout6.addWidget(self.textinput6)
        #input_layout7.addWidget(self.textinput7)

        self.dropdown_label_ppl = QLabel('Select person who encashed  ')
        self.dropdown_ppl = QComboBox()
        self.dropdown_ppl.addItems(['Not Connected'])

        # Add clear button for text display area
        self.button_RecordEntrySubmit = QPushButton('Submit')
        self.button_RecordEntrySubmit.setStyleSheet('background-color: gray; color: white;')
        self.button_RecordEntrySubmit.clicked.connect(self.Button_RecordEntrySubmit)

        # Add clear button for text display area
        self.clear_button = QPushButton('Clear')
        #self.clear_button.clicked.connect(self.ClearTextDisplay)

        # Add button, checkbox, text input, dropdown menu, and text display area to partition layout

        #self.addWidget(self.button)
        #self.addWidget(self.checkbox)
        self.addWidget(self.label)

        self.addWidget(self.dropdown_label)
        self.addWidget(self.dropdown_partion4)

        self.addLayout(input_layout1)
        self.addLayout(input_layout2)
        self.addLayout(input_layout3)
        self.addLayout(input_layout4)
        self.addLayout(input_layout5)
        self.addLayout(input_layout6)
        #self.addLayout(input_layout7)
        self.addWidget(self.dropdown_label_ppl)
        self.addWidget(self.dropdown_ppl)
        self.addWidget(self.button_RecordEntrySubmit)

        self.addWidget(self.textdisplay)
        self.addWidget(self.clear_button)
        self.addWidget(self.frame)

    def Button_RecordEntrySubmit(self):
        if (common.CONNECTED):
            bisiRecordEntryData = {
            'bisiName':self.dropdown_partion4.currentText(),
            'bisiStatus':self.textinput1.text(),
            'bisiMonthsCompleted':self.textinput2.text(),
            'bisiCurrentMonthEncashedSum':self.textinput3.text(),
            'bisiCurrentMonthEncashedDate':self.encash_date_edit.text(),
            'bisiCurrentComission':self.textinput1.text(),
            'personBisiNameWhichIsEncashed':self.dropdown_ppl.currentText() #name of person who encashed BC
                # @sal: for the above perone we have to make 'personBisiEncashStatus' = encashed. Think how?

            #@sal : you have to just write the "bisiRecordEntryData" dict to DB here. call your write API

            }

    def GetPplListPartition4(self,bisiName):
        if common.CONNECTED:
            pplList = DBFunctions.getAllUsersListByBisiName(bisiName)
        else:
            pplList = ['Not Connected']  # VK : default list when not connected to db. Think over it
        # Clear the current items in the ppl list  drop-down menu
        self.dropdown_ppl.clear()
        self.dropdown_ppl.addItems(pplList)
        return pplList

    def GetNameOfBisiSelectedAndUpdatePplDropdown(self):
        bisiName = self.dropdown_partion4.currentText()
        self.GetPplListPartition4(bisiName)

        #NOTE we may not need below detail. removeas per the need/not need

        # bisi_dict = DBFunctions.getBisiDetailsByBisiName(bisiName)
        # #DBFunctions.getBisiHistory(bisiName)
        #
        # if bisi_dict:
        #     self.textdisplay.append(f"BC Name: {bisi_dict[0].get('bisiName', '')}")
        #     self.textdisplay.append(f"BC Status: {bisi_dict[0].get('bisiStatus', '')}")
        #     self.textdisplay.append(f"Sum Assured: {bisi_dict[0].get('bisiSumAssured', '')}")
        #     self.textdisplay.append(f"Total Months: {bisi_dict[0].get('bisiTotalMonths', '')}")
        #     self.textdisplay.append(f"Start Date: {bisi_dict[0].get('bisiStartDate', '')}")
        #     self.textdisplay.append(f"End Date: {bisi_dict[0].get('bisiEndDate', '')}")
        #     self.textdisplay.append(f"Number of People: {bisi_dict[0].get('bisiTotalPpl', '')}")
        #     self.textdisplay.append(f" DETAILS OF ALL THE MONTHS TILL NOW ")
        #     self.textdisplay.append(f"------------------------------------------------------------------")
        # else:
        #     self.textdisplay.append("Error: Failed to retrieve B.C. details")
