# Simple BMI calculator
# Import necessary modules from PyQt6
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup
from PyQt6.QtGui import QIcon
import ui_bmiForm  # The generated UI file from Qt Designer
import sys

# Define the main class for the BMI Calculator
class BMI_Calculator(QMainWindow, ui_bmiForm.Ui_MainWindow): 
    def __init__(self, parent=None):  
        super().__init__(parent)  # Initialize the QMainWindow
        self.setupUi(self)        # Setup UI from the imported .ui file
        
        # Create a button group for the gender radio buttons
        self.btn_group = QButtonGroup()
        self.btn_group.addButton(self.gen)    # 'Man' radio button
        self.btn_group.addButton(self.gen_2)  # 'Woman' radio button
        
        # Connect the 'Calculate' button to the calculation function
        self.calculaterButton.clicked.connect(self.calculate)

        # Connect the button group to a function to store selected gender
        self.btn_group.buttonClicked.connect(self.radio_btn_click)
        
        self.radio_btn_state = ""  # Variable to store selected gender label
        
    def radio_btn_click(self, button):
        # Save the text of the selected radio button ("Man" or "Woman")
        self.radio_btn_state = button.text()

    def calculate(self):
        try:
            # Get mass (kg) and height (cm) from spin boxes
            mass = self.spinBoxMass.value()
            height = self.spinBoxHeight.value()

            # Calculate BMI using the standard formula
            bmi = mass / ((height / 100) ** 2)

            # Calculate ideal weight based on gender
            if self.radio_btn_state == "Man":
                i_mass = (height - 100) * 0.9
            elif self.radio_btn_state == "Woman":
                i_mass = (height - 100) * 0.85

            # Display the calculated BMI and ideal mass (formatted)
            self.bmi.setText(str(bmi)[:4])
            self.ideal_mass.setText(str(i_mass)[:4] + " kg")
        except:
            pass  # Fail silently if an error occurs (not recommended for production)
        
# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)                   # Create the application
    window = BMI_Calculator()                      # Instantiate the main window
    window.setWindowTitle("BMI Calculator")        # Set window title
    icon = QIcon("bmi_icon.png")                   # Set window icon (optional)
    window.setWindowIcon(icon)                     
    window.show()                                  # Show the application window
      
    sys.exit(app.exec())                           # Start the event loop
