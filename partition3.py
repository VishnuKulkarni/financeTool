from qtpy.QtWidgets import QVBoxLayout, QLabel, QFrame, QPushButton, QTextEdit, QCheckBox, QLineEdit, QComboBox

class Partition3(QVBoxLayout):
    def __init__(self):
        super().__init__()

        # Create label for partition
        self.label = QLabel('Partition 3')
        self.label.setFixedSize(200, 150)
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Box)

        # Create button, checkbox, text input, dropdown menu, and text display area in partition
        self.button = QPushButton('Button')
        self.checkbox = QCheckBox('Checkbox')
        self.textinput = QLineEdit()
        self.dropdown = QComboBox()
        self.dropdown.addItems(['Option 1', 'Option 2', 'Option 3'])
        self.textdisplay = QTextEdit()

        # Add button, checkbox, text input, dropdown menu, and text display area to partition layout
        self.addWidget(self.label)
        self.addWidget(self.button)
        self.addWidget(self.checkbox)
        self.addWidget(self.textinput)
        self.addWidget(self.dropdown)
        self.addWidget(self.textdisplay)
        self.addWidget(self.frame)
