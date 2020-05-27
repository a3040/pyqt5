#https://stackoverflow.com/questions/62009400/radiobox-signal-confusion
# trigger signal 사용으로 인한 혼란




from PyQt5.QtWidgets import *


import sys


class ButtonWidget(QWidget):

    def __init__(self):
        super(ButtonWidget, self).__init__()

        groups = {"Functions": ("Sinus", "Cosines"),
                  "Colors": ("Red", "Green"),
                  "Lines": ("Solid", "Dashed")
                  }

        # Main Group
        main_group = QGroupBox("Operations")
        main_group_layout = QHBoxLayout()

        # loop on group names
        for group, buttons in groups.items():
            group_box = QGroupBox(group)
            group_box.setStyleSheet('border:1px solid black')
            group_layout = QVBoxLayout()
            for button_text in buttons:
                button = QRadioButton(button_text)
                button.setObjectName("radiobutton_%s" % button_text)

                button.toggled.connect(self.radio_func)
                #button.clicked.connect(self.radio_func)


                group_layout.addWidget(button)

            group_box.setLayout(group_layout)
            main_group_layout.addWidget(group_box)

        main_group.setLayout(main_group_layout)

        # Widget
        main_widget = QWidget()
        main_widget_layout = QVBoxLayout()
        main_widget.setLayout(main_widget_layout)
        main_widget_layout.addWidget(main_group)
        # Layout Set
        self.setLayout(main_widget_layout)

        self.show()

    def radio_func(self):
        radio_btn = self.sender()
        print(f"{radio_btn.text()}\n-------------------")

    """def radio_func(self, on):
        if on:
            radio_btn = self.sender()
            print(f"{radio_btn.text()}\n-------------------")"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = ButtonWidget()
    sys.exit(app.exec_())