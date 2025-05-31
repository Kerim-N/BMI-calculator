# from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup
from PyQt6.QtGui import QIcon
import ui_bmiForm, sys

class BMI_Calculator(QMainWindow, ui_bmiForm.Ui_MainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        self.btn_group = QButtonGroup()
        self.btn_group.addButton(self.gen)
        self.btn_group.addButton(self.gen_2)
        
        self.calculaterButton.clicked.connect(self.calculate)
        self.btn_group.buttonClicked.connect(self.radio_btn_click)
        self.radio_btn_state = ""
        
    def radio_btn_click(self, button):
        self.radio_btn_state = button.text()

    def calculate(self):
        try:
            mass = self.spinBoxMass.value()
            height = self.spinBoxHeight.value()
            bmi = mass/((height/100)**2)

            if self.radio_btn_state == "Man":
                i_mass = (height-100)*0.9
            elif self.radio_btn_state == "Woman":
                i_mass = (height-100)*0.85

            self.bmi.setText(str(bmi)[:4])
            self.ideal_mass.setText(str(i_mass)[:4] + " kg")
        except:
            pass
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMI_Calculator()
    window.setWindowTitle("BMI Calculator")
    icon = QIcon("bmi_icon.png")
    window.setWindowIcon(icon)
    window.show()
    
    sys.exit(app.exec())