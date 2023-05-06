from PyQt5.QtWidgets import QCheckBox, QGridLayout, QPushButton, QLabel

grid_layout = QGridLayout()

# Add widgets to the grid
widget1 = QPushButton('Button 1')
widget2 = QLabel('Label 1')
widget3 = QCheckBox('Checkbox 1')

grid_layout.addWidget(widget1, 0, 0)  # Add widget1 to row 0, column 0
grid_layout.addWidget(widget2, 0, 1)  # Add widget2 to row 0, column 1
grid_layout.addWidget(widget3, 1, 0, 1, 2)  # Add widget3 to row 1, column 0, spanning 1 row and 2 columns

# Set the grid layout for the parent widget
parent_widget.setLayout(grid_layout)
