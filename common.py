#THIS FILE IS USED FOR FLAGS THAT ARE COMMON TO ALL OTHER CLASSES/FILES
from PyQt5.QtWidgets import QMessageBox

CONNECTED = False


def InfoPopUp(self, msg):
    # Create a QMessageBox with the information message

    self.msg_box.setIcon(QMessageBox.Information)
    self.msg_box.setText(msg)
    self.msg_box.setWindowTitle('ALERT !!!')
    self.msg_box.setStandardButtons(QMessageBox.Ok)

    # Show the information pop-up
    self.msg_box.exec_()