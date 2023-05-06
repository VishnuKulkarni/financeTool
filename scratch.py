from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QComboBox


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the display text area
        self.display_text = QTextEdit(self)
        self.display_text.setPlainText('Hello world!')

        # Create the dropdown menu
        self.dropdown = QComboBox(self)
        self.update_dropdown()

        # Create the layout and add the widgets
        vbox = QVBoxLayout()
        vbox.addWidget(self.display_text)
        vbox.addWidget(self.dropdown)
        self.setLayout(vbox)

    def update_dropdown(self):
        # Clear the dropdown menu
        self.dropdown.clear()

        # Get the text from the display text area
        text = self.display_text.toPlainText()

        # Add some items to the dropdown menu
        self.dropdown.addItem('Item 1')
        self.dropdown.addItem('Item 2')
        self.dropdown.addItem('Item 3')

        # Add the text from the display text area to the dropdown menu
        self.dropdown.addItem(text)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
