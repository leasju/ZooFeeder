import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QComboBox, QPushButton, QLabel, QDialog, QHBoxLayout, QMessageBox, QCheckBox

# FOOD CONSUMED 
# Elefant: 4.5 veg, 6.5 herb
# Giraffe: 1.5 veg, 3.5 herb
# Gorilla: 2.5 veg, 1.0 herb
# Hippo: 1.5 veg, 2.5 herb
# Moose: 1.0 veg, 2.0 herb
# Wallaby:  1.0 veg, 2.0 herb
# Zebra: 1.5 veg, 1.0 herb
# Penguin: 2.0 fish


# Animal data: amount of food consumed (in kg)
animals = {
    'Elephant': {'veg': 4.5, 'herb': 6.5, 'fish': 0},
    'Giraffe': {'veg': 1.5, 'herb': 3.5, 'fish': 0},
    'Hippo': {'veg': 1.5, 'herb': 2.5, 'fish': 0},
    'Gorilla': {'veg': 2.5, 'herb': 1.0, 'fish': 0},
    'Moose': {'veg': 1.0, 'herb': 2.0, 'fish': 0},
    'Wallaby': {'veg': 1.0, 'herb': 2.0, 'fish': 0},
    'Zebra': {'veg': 1.5, 'herb': 1.0, 'fish': 0},
    'Penguin': {'veg': 0, 'herb': 0, 'fish': 2.0}
}

# Function to calculate the amount of briquettes needed
def calcular_briquetes(animais_selecionados, seguir_ordem):
    round_1_animals = []
    round_2_animals = []

    # Check if the order should be followed
    if seguir_ordem:
        round_1_animals = animais_selecionados[:2]
        round_2_animals = animais_selecionados[2:]
    else:
        round_1_animals = [animais_selecionados[0], animais_selecionados[2]]
        round_2_animals = [animais_selecionados[1], animais_selecionados[3]]

    # Function to sum the food needed for a list of animals
    def sum_food(animais_lista):
        food_total = {'veg': 0, 'herb': 0, 'fish': 0}
        for animal in animais_lista:
            food_total['veg'] += animals[animal]['veg']
            food_total['herb'] += animals[animal]['herb']
            food_total['fish'] += animals[animal]['fish']
        return food_total

    # Calculate food for each round
    round_1_food = sum_food(round_1_animals)
    round_2_food = sum_food(round_2_animals)

    # Function to convert food into briquettes
    def converter_briquetes(food):
        return {type_: (quantity // 3) + (1 if quantity % 3 > 0 else 0) for type_, quantity in food.items()}

    # Convert food to briquettes for each round
    round_1_briquettes = converter_briquetes(round_1_food)
    round_2_briquettes = converter_briquetes(round_2_food)

    # Function to calculate remaining space in the cart
    def calcular_sobrando(briquettes):
        total_briquettes = briquettes['veg'] + briquettes['herb'] + briquettes['fish'] + 1  # +1 for the fixed meat briquette
        return 8 - total_briquettes  # Assuming the cart can hold a maximum of 8 briquettes

    # Calculate remaining space for each round
    round_1_remaining = calcular_sobrando(round_1_briquettes)
    round_2_remaining = calcular_sobrando(round_2_briquettes)

    return (round_1_animals, round_1_briquettes, round_1_remaining), (round_2_animals, round_2_briquettes, round_2_remaining)

# Result window class
class ResultadoDialog(QDialog):
    def __init__(self, dados_round1, dados_round2):
        super().__init__()
        self.setWindowTitle("Results")

        # Window configuration
        self.setWindowIcon(QIcon("img/zoo_icon.png"))
        self.resize(300, 300)

        # Layout and data display
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Main label (Fixed title)
        label_title = QLabel("Round Results")
        font = QFont()
        font.setPointSize(16)
        label_title.setFont(font)
        label_title.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        layout.addWidget(label_title)

        # Function to add results for each round
        def add_round_results(round_num, animals_round, packets, remaining):
            # Create a larger font for round labels
            round_label = QLabel(f"Round {round_num}:")
            round_font = QFont()
            round_font.setPointSize(14)  # Set the font size for round labels
            round_label.setFont(round_font)
            layout.addWidget(round_label)

            # Add animals, food, and remaining space information
            label_animals = QLabel(f"Animals: {', '.join(animals_round)}")
            layout.addWidget(label_animals)
            
            # Construct the packets string to display as a list
            packets_list = (
                f"PACKETS:\n"
                f"{packets['veg']} vegetables\n"
                f"{packets['herb']} herbs\n"
                f"{packets['fish']} fish\n"
                f"1 fixed meat"
            )
            label_food = QLabel(packets_list)
            layout.addWidget(label_food)

            label_remaining = QLabel(f"{remaining} spaces left in the cart" if remaining > 0 else "Cart is full")
            layout.addWidget(label_remaining)

            # Add a horizontal line separator between rounds
            if round_num == 1: 
                separator = QLabel()  
                separator.setText("__________________________")  
                separator.setAlignment(Qt.AlignmentFlag.AlignCenter)  
                layout.addWidget(separator)

        # Add results for each round
        add_round_results(1, *dados_round1)
        add_round_results(2, *dados_round2)

# Main Window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        window = QWidget()
        self.setWindowTitle("ZooFeeder")

        # Window config and layout
        self.setWindowIcon(QIcon("img/zoo_icon.png"))
        self.setFixedSize(320, 280)  # Set fixed size for the window
        self.set_background_image("img/background.jpg")

        # Central widget configuration
        container = QWidget()
        self.setCentralWidget(container)
        self.layout = QVBoxLayout(container)

        # Main label (Fixed title)
        self.label = QLabel("Welcome to ZooFeeder!")
        self.layout.addWidget(self.label)
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)  

        self.label1 = QLabel("Manage the zoo animals' feeding with this calculator")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)  
        self.layout.addWidget(self.label1)

        # Add comboboxes for animal selection
        self.comboboxes = []
        self.comboBox()

        # Checkbox for following the order of animal selection
        self.follow_order_checkbox = QCheckBox("Follow order")
        self.follow_order_checkbox.setCheckable(True)
        self.layout.addWidget(self.follow_order_checkbox)

        # Button setup for sending data and clearing selections
        self.setup_buttons()

        # Status/feedback label
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.status_label)

    # Function to set a background image for the main window
    def set_background_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.background_label = QLabel(self)
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(False)
        self.background_label.setGeometry(0, 0, pixmap.width(), pixmap.height())
        self.background_label.lower()  # Ensure background is behind other widgets

    # Function to create and configure the comboboxes for animal selection
    def comboBox(self):
        for _ in range(4):
            combobox = QComboBox()
            combobox.addItem('Select')
            combobox.addItems(animals.keys())  # Populate combobox with animal names
            combobox.currentIndexChanged.connect(self.update_comboboxes)  # Connect to update function
            self.layout.addWidget(combobox)
            self.comboboxes.append(combobox)

    # Function to update comboboxes based on selected animals
    def update_comboboxes(self):
        selected_animals = {combobox.currentText() for combobox in self.comboboxes if combobox.currentIndex() != 0}
        for combobox in self.comboboxes:
            for i in range(combobox.count()):
                animal_name = combobox.itemText(i)
                if animal_name == 'Select':
                    continue  # Skip the 'Select' option
                # Enable/disable items based on selection
                combobox.model().item(i).setEnabled(animal_name not in selected_animals or combobox.currentText() == animal_name)

    # Function to send data for processing
    def send(self):
        send_data = [combobox.currentText() for combobox in self.comboboxes if combobox.currentIndex() != 0]

        # Check if exactly 4 different animals are selected
        if len(set(send_data)) != 4:
            QMessageBox.critical(self, "Error", "Select 4 different animals!")
            return

        # Check if order needs to be followed
        seguir_ordem = self.follow_order_checkbox.isChecked()
        dados_round1, dados_round2 = calcular_briquetes(send_data, seguir_ordem)

        # Display results in a dialog
        self.resultado_dialog = ResultadoDialog(dados_round1, dados_round2)
        self.resultado_dialog.exec()

    # Function to clear selections
    def clear(self):
        for combobox in self.comboboxes:
            combobox.setCurrentIndex(0)
        self.follow_order_checkbox.setChecked(False )
        self.status_label.setText("")  # Clear status label

    # Function to set up the buttons for sending data and clearing selections
    def setup_buttons(self):
        # Create a horizontal layout for the buttons
        button_layout = QHBoxLayout()

        # Button to calculate food
        self.send_button = QPushButton("Calculate")
        self.send_button.clicked.connect(self.send)  # Connect to send function
        button_layout.addWidget(self.send_button)
        self.send_button.setFixedSize(100, 30)  # Set fixed size for the button

        # Button to clear selections
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear)  # Connect to clear function
        button_layout.addWidget(self.clear_button)
        self.clear_button.setFixedSize(100, 30)  # Set fixed size for the button

        # Add the button layout to the main layout
        self.layout.addLayout(button_layout)

# Main function to run the application
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()