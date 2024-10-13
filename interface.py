import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPalette, QBrush, QPixmap, QIcon  # Main Window Style
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QComboBox, QPushButton, QLabel, QDialog, QHBoxLayout

# Result window
class ResultadoDialog(QDialog):
    def __init__(self, dados):
        super().__init__()
        self.setWindowTitle("Results")
        self.resize(250, 200)
        
        # Window config and layout
        self.setWindowIcon(QIcon("img/zoo_icon.png"))
        self.setFixedSize(300, 250)
    

        # Central widget config
        container = QWidget()
        self.setCentralWidget(container)
        self.layout = QVBoxLayout(container)


        # Layout and data display
        layout = QVBoxLayout()
        label = QLabel("Animals selected:")
        
        layout.addWidget(label)
        
        # Show selected data
        for item in dados:
            label_animal = QLabel(item)
            layout.addWidget(label_animal)
            


# Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        window = QWidget()
        self.setWindowTitle("ZooFeeder")

        # Window config and layout
        self.setWindowIcon(QIcon("img/zoo_icon.png"))
        self.setFixedSize(300, 250)
        self.set_background_image("img/background.jpg")

        # Central widget config
        container = QWidget()
        self.setCentralWidget(container)
        self.layout = QVBoxLayout(container)

        # Main label (Fixed title)
        self.label = QLabel("Welcome to ZooFeeder!")
        self.layout.addWidget(self.label)
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        # Add other labels to the layout
        self.label1 = QLabel("Manage the zoo animals' feeding")
        self.label2 = QLabel("Select the animals:")
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label2)

        # Add comboboxes
        self.comboboxes = []
        self.comboBox()

        # Button setup
        self.setup_buttons()

        # Status/feedback label
        self.status_label = QLabel("")
        self.layout.addWidget(self.status_label)

    # Window background image function
    def set_background_image(self, image_path):
        # Load the image
        pixmap = QPixmap(image_path)
        # QLabel for the background image
        self.background_label = QLabel(self)
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(False)  # Do not scale the image
        self.background_label.setGeometry(0, 0, pixmap.width(), pixmap.height())
        self.background_label.lower()  # Put the image behind other widgets

    # Function to create comboboxes
    def comboBox(self):
        # Create comboboxes
        for _ in range(4):
            combobox = QComboBox()
            combobox.addItem('Selecione')  # Placeholder
            combobox.addItem('Elephant')
            combobox.addItem('Giraffe')
            combobox.addItem('Hippopotamus')
            combobox.addItem('Gorilla')
            combobox.addItem('Moose')
            combobox.addItem('Kangaroo')
            combobox.addItem('Zebra')
            combobox.addItem('Penguin')
            combobox.currentTextChanged.connect(self.current_text_changed)
            self.layout.addWidget(combobox)
            self.comboboxes.append(combobox)

    # Function to remove options that are already selected in another combobox
    def current_text_changed(self, s):
        if s != 'Selecione':
            for combobox in self.comboboxes:
                if combobox != self.sender():
                    index = combobox.findText(s)
                    if index != -1:
                        combobox.removeItem(index)

    # Send form data function
    def send(self):
        # Collect selected data from the comboboxes, ignoring the ones with index 0 ("Selecione" placeholder)
        send_data = [combobox.currentText() for combobox in self.comboboxes if combobox.currentIndex() != 0]

        # Check if any combobox is still at the "Selecione" item (index 0)
        if len(send_data) != len(self.comboboxes):
            self.status_label.setText("Please select a valid option")
            return
        print("Data sent:", send_data)

        # Update the status label text
        self.status_label.setText("Data sent successfully!")

        # Open a new window to show the results
        self.resultado_dialog = ResultadoDialog(send_data)
        self.resultado_dialog.exec()

    # Clear form data function
    def clear(self):
        # Reset each combobox to the "Selecione" item
        for combobox in self.comboboxes:
            combobox.setCurrentIndex(0)
        print("Form cleared successfully!")

        # Refresh the status label text
        self.status_label.setText("Form cleared successfully")

    # Function to set up the buttons
    def setup_buttons(self):
        # Create a horizontal layout for the buttons
        button_layout = QHBoxLayout()

        # "Send" button
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send)
        button_layout.addWidget(self.send_button)

        # "Clear" button
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear)
        button_layout.addWidget(self.clear_button)

        # Add the button layout to the main layout
        self.layout.addLayout(button_layout)

# Initialize the application
app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
