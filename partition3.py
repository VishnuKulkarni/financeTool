from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QDateEdit, QMessageBox
from qtpy.QtWidgets import QVBoxLayout, QLabel, QFrame, QPushButton, QTextEdit, QCheckBox, QLineEdit, QComboBox

import common


class Partition3(QVBoxLayout):
    def __init__(self):
        super().__init__()

        # Create label for partition
        self.label = QLabel('ADD NEW BiSi')
        self.label.setFont(QFont("Arial", 8, QFont.Bold))
        self.label.setFixedSize(200, 15)
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Box)

        # Create button, checkbox, text input, dropdown menu, and text display area in partition
        self.button_bisi_submit = QPushButton('Submit')
        self.button_bisi_submit.setStyleSheet('background-color: gray; color: white;')
        self.button_bisi_submit.clicked.connect(self.Button_bisi_submit)

        self.checkbox = QCheckBox('Checkbox')

        self.msg_box = QMessageBox()

        #create input fields
        self.textinput_label1 = QLabel('BiSi Name    ')
        self.textinput_label2 = QLabel('Total Months')
        self.textinput_label3 = QLabel('Start Date    ')
        self.textinput_label4 = QLabel('End Date      ')
        self.textinput_label5 = QLabel('Sum            ')
        self.textinput_label6 = QLabel('Comission    ')
        self.textinput_label7 = QLabel('Total People ')
        self.textinput_label8 = QLabel('BiSi Status    ')
        self.textinput_label9 = QLabel('T B D           ')
        self.textinput_label10 = QLabel('First Name   ')
        self.textinput_label11 = QLabel('Last Name    ')
        self.textinput_label12 = QLabel('DOB            ')
        self.textinput_label13 = QLabel('Phone No     ')
        self.textinput_label14 = QLabel('Address       ')
        self.textinput_label15 = QLabel('Aadhar        ')
        self.textinput_label16 = QLabel('TBD            ')
        self.textinput_label17 = QLabel('TBD            ')
        self.textinput_label18 = QLabel('TBD            ')

        self.textinput1 = QLineEdit()
        self.textinput2 = QLineEdit()

        # Create a QDateEdit widget
        self.start_date_edit = QDateEdit()
        self.start_date_edit.setCalendarPopup(True)

        self.end_date_edit = QDateEdit()
        self.end_date_edit.setCalendarPopup(True)

        self.rec_entry_date_edit = QDateEdit()
        self.rec_entry_date_edit.setCalendarPopup(True)

        self.textinput5 = QLineEdit()
        self.textinput6 = QLineEdit()
        self.textinput7 = QLineEdit()
        self.textinput8 = QLineEdit()
        self.textinput9 = QLineEdit()



        # Create line separator
        self.line1 = QFrame()
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)
        self.line2 = QFrame()
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)

        self.label10 = QLabel('ADD NEW PERSON')
        self.label10.setFont(QFont("Arial", 8, QFont.Bold))
        self.label10.setFixedSize(200, 15)

        self.dropdown_label = QLabel('Select BiSi')
        self.dropdown = QComboBox()
        self.dropdown.addItems(['Option 1', 'Option 2', 'Option 3'])

        #record entry details
        self.textinput10 = QLineEdit()
        self.textinput11 = QLineEdit()
        self.textinput12 = QLineEdit()
        self.textinput13 = QLineEdit()
        self.textinput14 = QLineEdit()
        self.textinput15 = QLineEdit()
        self.textinput16 = QLineEdit()
        self.textinput17 = QLineEdit()
        self.textinput18 = QLineEdit()


        #self.textdisplay = QTextEdit()

        # Add clear button for text display area
        self.submit_button = QPushButton('Submit')
        self.submit_button.setStyleSheet('background-color: gray; color: white;')
        #self.submit_button.clicked.connect(self.Submit)

        # Create a horizontal layout for textinput_label and textinput
        input_layout1 = QHBoxLayout()
        input_layout2 = QHBoxLayout()
        input_layout3 = QHBoxLayout()
        input_layout4 = QHBoxLayout()
        input_layout5 = QHBoxLayout()
        input_layout6 = QHBoxLayout()
        input_layout7 = QHBoxLayout()
        input_layout8 = QHBoxLayout()
        input_layout9 = QHBoxLayout()
        input_layout10 = QHBoxLayout()
        input_layout11 = QHBoxLayout()
        input_layout12 = QHBoxLayout()
        input_layout13 = QHBoxLayout()
        input_layout14 = QHBoxLayout()
        input_layout15 = QHBoxLayout()
        input_layout16 = QHBoxLayout()
        input_layout17 = QHBoxLayout()
        input_layout18 = QHBoxLayout()

        input_layout1.addWidget(self.textinput_label1)
        input_layout2.addWidget(self.textinput_label2)
        input_layout3.addWidget(self.textinput_label3)
        input_layout4.addWidget(self.textinput_label4)
        input_layout5.addWidget(self.textinput_label5)
        input_layout6.addWidget(self.textinput_label6)
        input_layout7.addWidget(self.textinput_label7)
        input_layout8.addWidget(self.textinput_label8)
        input_layout9.addWidget(self.textinput_label9)
        input_layout10.addWidget(self.textinput_label10)
        input_layout11.addWidget(self.textinput_label11)
        input_layout12.addWidget(self.textinput_label12)
        input_layout13.addWidget(self.textinput_label13)
        input_layout14.addWidget(self.textinput_label14)
        input_layout15.addWidget(self.textinput_label15)
        input_layout16.addWidget(self.textinput_label16)
        input_layout17.addWidget(self.textinput_label17)
        input_layout18.addWidget(self.textinput_label18)

        input_layout1.addWidget(self.textinput1)
        input_layout2.addWidget(self.textinput2)
        input_layout3.addWidget(self.start_date_edit)
        input_layout4.addWidget(self.end_date_edit)
        input_layout5.addWidget(self.textinput5)
        input_layout6.addWidget(self.textinput6)
        input_layout7.addWidget(self.textinput7)
        input_layout8.addWidget(self.textinput8)
        input_layout9.addWidget(self.textinput9)
        input_layout10.addWidget(self.textinput10)
        input_layout11.addWidget(self.textinput11)
        input_layout12.addWidget(self.textinput12)
        input_layout13.addWidget(self.textinput13)
        input_layout14.addWidget(self.textinput14)
        input_layout15.addWidget(self.textinput15)
        input_layout16.addWidget(self.textinput16)
        input_layout17.addWidget(self.textinput17)
        input_layout18.addWidget(self.textinput18)

        # Add button, checkbox, text input, dropdown menu, and text display area to partition layout
        self.addWidget(self.label)

        #self.addWidget(self.checkbox)

        self.addLayout(input_layout1)
        self.addLayout(input_layout2)
        self.addLayout(input_layout3)
        self.addLayout(input_layout4)
        self.addLayout(input_layout5)
        self.addLayout(input_layout6)
        self.addLayout(input_layout7)
        self.addLayout(input_layout8)
        self.addLayout(input_layout9)

        self.addWidget(self.button_bisi_submit)

        self.addWidget(self.line1)
        self.addWidget(self.label10)
        self.addWidget(self.line2)


        self.addWidget(self.dropdown_label)
        self.addWidget(self.dropdown)

        self.addLayout(input_layout10)
        self.addLayout(input_layout11)
        self.addLayout(input_layout12)
        self.addLayout(input_layout13)
        self.addLayout(input_layout14)
        self.addLayout(input_layout15)
        self.addLayout(input_layout16)
        self.addLayout(input_layout17)
        self.addLayout(input_layout18)


        #self.addWidget(self.textdisplay)
        self.addWidget(self.submit_button)
        self.addWidget(self.frame)





    def Button_bisi_submit(self):
        if (common.CONNECTED):
            newBisiData = {
                'bisiName': self.textinput1.text(),
                'bisiStatus': self.textinput8.text(),
                'bisiStartDate': self.start_date_edit.text(),
                'bisiEndDate': self.end_date_edit.text(),
                'bisiSumAssured': self.textinput5.text(),
                'bisiComission': self.textinput6.text(),
                'bisiTotalPpl': self.textinput7.text(),
                'bisiTotalMonths': self.textinput2.text()

            }
            common.InfoPopUp(self,'data submitted')
        else:
            common.InfoPopUp(self, 'PLEASE get online 1st')


        #sal - call you db write function and write these fields

