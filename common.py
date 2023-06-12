#THIS FILE IS USED FOR FLAGS THAT ARE COMMON TO ALL OTHER CLASSES/FILES
from PyQt5.QtWidgets import QMessageBox

CONNECTED = False


def DisplayInfoPopUp(self, msg):
    # Create a QMessageBox with the information message

    self.msg_box.setIcon(QMessageBox.Information)
    self.msg_box.setText(msg)
    self.msg_box.setStyleSheet("QMessageBox { background-color: lightgray; color: green; }")
    self.msg_box.setWindowTitle('SUCCESS')
    self.msg_box.setStandardButtons(QMessageBox.Ok)

    # Show the information pop-up
    self.msg_box.exec_()

def DisplayErrorPopUp(self, msg):
    # Create a QMessageBox with the information message

    self.msg_box.setIcon(QMessageBox.Information)
    self.msg_box.setText(msg)
    self.msg_box.setStyleSheet("QMessageBox { background-color: red; color: red; }")
    self.msg_box.setWindowTitle('ERROR')
    self.msg_box.setStandardButtons(QMessageBox.Ok)

    # Show the information pop-up
    self.msg_box.exec_()

