from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QDialog, QScrollArea
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QFrame, QPushButton, QTextEdit, QCheckBox, QLineEdit, QComboBox
import common
from partition2 import Partition2
from partition3 import Partition3
from partition4 import Partition4
from functions import DBFunctions
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


class Partition1(QVBoxLayout):
    CONNECTED = False
    selected_option = "none"
    def __init__(self,partition2, partition4):
        super().__init__()

        self.partition2 = partition2
        self.partition4 = partition4

        # Create label for partition
        self.label = QLabel('DASHBOARD')
        self.label.setFont(QFont("Arial", 8, QFont.Bold))
        self.label.setFixedSize(200, 15)
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Box)

        # Create button, checkbox, text input, dropdown menu, and text display area in partition
        self.button1 = QPushButton('Connect')
        self.button1.setStyleSheet('QPushButton { background-color: gray; }')
        self.button1.clicked.connect(self.Connect)

        # Create QLabel widget and set its pixmap to the image you want to display
        image_label = QLabel()
        image_pixmap = QPixmap('C:/Users/jsrir/Downloads/financeTool-master/icon.jpg')
        # Set maximum height and width of the image
        image_pixmap = image_pixmap.scaled(400, 200)
        image_label.setPixmap(image_pixmap)

        #self.checkbox = QCheckBox('Checkbox')
        #self.textinput = QLineEdit()

        self.dropdown_label = QLabel('List of BiSi')
        self.dropdown = QComboBox()
        self.dropdown.addItems(self.GetBisiList())

        self.selected_option = self.dropdown.currentText()
        self.dropdown.activated.connect(self.GetNameOfBisiSelectedAndUpdatePplDropdown)

        # Create line separator
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line2 = QFrame()
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)

        self.textdisplay = QTextEdit()

        self.scroll = QScrollArea()
        self.textdisplay = QTextEdit()
        self.textdisplay.setReadOnly(True)  # make the display area read-only
        self.scroll.setWidget(self.textdisplay)
        self.scroll.setWidgetResizable(True)

        # Add clear button for text display area
        self.clear_button = QPushButton('Clear')
        self.clear_button.clicked.connect(self.ClearTextDisplay)

        # Add button, checkbox, text input, dropdown menu, and text display area to partition layout
        self.addWidget(self.label)
        self.addWidget(image_label)
        self.addWidget(self.button1)

        self.addWidget(self.line)

        #self.addWidget(self.checkbox)
        #self.addWidget(self.textinput)

        self.addWidget(self.dropdown_label)
        self.addWidget(self.dropdown)

        self.addWidget(self.line2)

        self.addWidget(self.scroll)

        self.addWidget(self.clear_button)

        self.addWidget(self.frame)


    def Connect(self):
        dbStatus = True  # @Sal: this flag should directly come form DB. Think How ?
        common.CONNECTED = dbStatus
        #SAL : add connection code here. After success set 'Partition1.CONNECTED = True'
        if common.CONNECTED:
            self.button1.setStyleSheet('QPushButton { background-color: green; }')
            print("connected")
        else:
            self.button1.setStyleSheet('QPushButton { background-color: red; }')

        # Clear the current items in the bisi drop-down menu
        self.dropdown.clear()
        self.dropdown.addItems(self.GetBisiList())

        #we need to update the drop downs in all other places of the gui here.
        # or just think of having 1 wrapper function to update all widgest as soon as connect =  true
        self.partition4.dropdown_partion4.clear()
        self.partition4.dropdown_partion4.addItems(self.GetBisiList())

    def GetBisiList(self):
        if common.CONNECTED:
            bisilist = DBFunctions.getAllBisisList() # SAL : call the 'ListOfBisi' api here
        else:
            bisilist = ['Not Connected'] #VK : default list when not connected to db. Think over it
        return bisilist

    def GetNameOfBisiSelectedAndUpdatePplDropdown(self):
        bisiName = self.dropdown.currentText()
        self.partition2.GetPplList(bisiName)
        bisi_dict = DBFunctions.getBisiDetailsByBisiName(bisiName)
        bisiHistory = DBFunctions.getBisiHistory(bisiName)
        print(bisiHistory)

        if bisi_dict:
            self.textdisplay.append(f"BC Name: {bisi_dict[0].get('bisiName', '')}")
            self.textdisplay.append(f"BC Status: {bisi_dict[0].get('bisiStatus', '')}")
            self.textdisplay.append(f"Sum Assured: {bisi_dict[0].get('bisiSumAssured', '')}")
            self.textdisplay.append(f"Total Months: {bisi_dict[0].get('bisiTotalMonths', '')}")
            self.textdisplay.append(f"Start Date: {bisi_dict[0].get('bisiStartDate', '')}")
            self.textdisplay.append(f"End Date: {bisi_dict[0].get('bisiEndDate', '')}")
            self.textdisplay.append(f"Number of People: {bisi_dict[0].get('bisiTotalPpl', '')}")
            self.textdisplay.append(f" DETAILS OF ALL THE MONTHS TILL NOW ")
            self.textdisplay.append(f"------------------------------------------------------------------")
        else:
            self.textdisplay.append("Error: Failed to retrieve B.C. details")

    def ClearTextDisplay(self):
        self.textdisplay.clear()


