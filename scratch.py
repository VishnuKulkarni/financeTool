from qtpy.QtWidgets import QApplication, QDialog, QTabWidget, QVBoxLayout, QWidget, QLabel

class MyTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()

        # Create the tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        # Add content to each tab
        self.tab1.layout = QVBoxLayout()
        self.tab1.label = QLabel("Tab 1 Content")
        self.tab1.layout.addWidget(self.tab1.label)
        self.tab1.setLayout(self.tab1.layout)

        self.tab2.layout = QVBoxLayout()
        self.tab2.label = QLabel("Tab 2 Content")
        self.tab2.layout.addWidget(self.tab2.label)
        self.tab2.setLayout(self.tab2.layout)

        self.tab3.layout = QVBoxLayout()
        self.tab3.label = QLabel("Tab 3 Content")
        self.tab3.layout.addWidget(self.tab3.label)
        self.tab3.setLayout(self.tab3.layout)

        # Add the tabs to the tab widget
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")


class MyGUI(QDialog):
    def __init__(self):
        super().__init__()

        # Create the tab widget
        self.tab_widget = MyTabWidget()

        # Set the main layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])
    gui = MyGUI()
    gui.show()
    app.exec()
