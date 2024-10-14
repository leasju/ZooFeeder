import tkinter as tk
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from tkinter import ttk, messagebox

# Dados dos animais: quantidades de comida consumida (em kg)
animais = {
    'Elefante': {'veg': 4.5, 'herb': 6.5, 'fish': 0},
    'Girafa': {'veg': 1.5, 'herb': 1.5, 'fish': 0},
    'Hipopotamo': {'veg': 2.5, 'herb': 2.5, 'fish': 0},
    'Gorila': {'veg': 2.5, 'herb': 1.0, 'fish': 0},
    'Alce': {'veg': 1.0, 'herb': 2.0, 'fish': 0},
    'Canguru': {'veg': 1.0, 'herb': 1.0, 'fish': 0},
    'Zebra': {'veg': 1.5, 'herb': 1.0, 'fish': 0},
    'Pinguim': {'veg': 0, 'herb': 0, 'fish': 2.0}
}
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPalette, QBrush, QPixmap, QIcon  # Main Window Style
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QComboBox, QPushButton, QLabel, QDialog, QHBoxLayout


# WINDOWS

# Result window
class ResultadoDialog(QDialog):
    def __init__(self, dados):
        super().__init__()
        self.setWindowTitle("Calc")

        # Window configuration
        self.setWindowIcon(QIcon("img/zoo_icon.png"))
        self.resize(250, 200)

        # Layout and data display
        layout = QVBoxLayout()  # Create the layout here
        self.setLayout(layout)  # Set the layout for the dialog

        # Main label (Fixed title)
        self.label = QLabel("Results")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        layout.addWidget(self.label)

        # Display selected animals
        label = QLabel("Animals selected:")
        layout.addWidget(label)

        for item in dados:
            label_animal = QLabel(item)
            layout.addWidget(label_animal)


        # Set the layout to the dialog
        self.setLayout(layout)

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
        self.label1 = QLabel("Manage the zoo animals' feeding with this calculator")
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


# FUNCTIONS

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

# Função para calcular a quantidade de briquetes
def calcular_briquetes(animais_selecionados, seguir_ordem):
    # Inicializa os dois rounds
    round_1_animais = []
    round_2_animais = []
    
    # Verifica se precisa seguir a ordem
    if seguir_ordem:
        round_1_animais = animais_selecionados[:2]
        round_2_animais = animais_selecionados[2:]
    else:
        round_1_animais = [animais_selecionados[0], animais_selecionados[2]]
        round_2_animais = [animais_selecionados[1], animais_selecionados[3]]
    
    # Função auxiliar para somar comida
    def somar_comida(animais_lista):
        comida_total = {'veg': 0, 'herb': 0, 'fish': 0}
        for animal in animais_lista:
            comida_total['veg'] += animais[animal]['veg']
            comida_total['herb'] += animais[animal]['herb']
            comida_total['fish'] += animais[animal]['fish']
        return comida_total
    
    # Calcular comida total para cada round
    round_1_comida = somar_comida(round_1_animais)
    round_2_comida = somar_comida(round_2_animais)
    
    # Função para converter kg em briquetes (1 briquete = 3 kg)
    def converter_briquetes(comida):
        return {tipo: (quantidade // 3) + (1 if quantidade % 3 > 0 else 0) for tipo, quantidade in comida.items()}
    
    # Converte a quantidade de comida total em briquetes
    round_1_briquetes = converter_briquetes(round_1_comida)
    round_2_briquetes = converter_briquetes(round_2_comida)
    
    # Função para calcular briquetes sobrando
    def calcular_sobrando(briquetes):
        total_briquetes = briquetes['veg'] + briquetes['herb'] + briquetes['fish'] + 1  # +1 para o briquete de carne fixo
        return 8 

    # Calcula os espaços sobrando no carrinho
    round_1_sobrando = calcular_sobrando(round_1_briquetes)
    round_2_sobrando = calcular_sobrando(round_2_briquetes)

    # Função para exibir o resultado em uma caixa de diálogo
    def exibir_resultado(round_num, animais_round, briquetes, sobrando):
        resultado = f"Round {round_num}:\n"
        resultado += f"Animais: {', '.join(animais_round)}\n"
        resultado += f"{briquetes['veg']} briquetes de vegetais\n"
        resultado += f"{briquetes['herb']} briquetes de erva\n"
        resultado += f"{briquetes['fish']} briquetes de peixe\n"
        resultado += f"1 carne (fixo)\n"
        if sobrando > 0:
            resultado += f"Sobrando {sobrando} espaços no carrinho\n"
        else:
            resultado += "Carrinho completo\n"
        return resultado

    # Exibe os resultados
    resultado_final = exibir_resultado(1, round_1_animais, round_1_briquetes, round_1_sobrando)
    resultado_final += exibir_resultado(2, round_2_animais, round_2_briquetes, round_2_sobrando)
    messagebox.showinfo("Resultado", resultado_final)

# Função chamada ao clicar no botão de calcular
def ao_clicar():
    selecionados = [combo_animal1.get(), combo_animal2.get(), combo_animal3.get(), combo_animal4.get()]
    if len(set(selecionados)) != 4:
        messagebox.showerror("Erro", "Selecione 4 animais diferentes!")
        return
    seguir_ordem = var_seguir_ordem.get()
    calcular_briquetes(selecionados, seguir_ordem)

# Configurando a interface gráfica
janela = tk.Tk()
janela.title("Calculadora de Briquetes")

# Criação dos rótulos e campos de seleção
tk.Label(janela, text="Selecione os 4 animais:").grid(row=0, column=0, columnspan=2)

animais_lista = list(animais.keys())

combo_animal1 = ttk.Combobox(janela, values=animais_lista)
combo_animal2 = ttk.Combobox(janela, values=animais_lista)
combo_animal3 = ttk.Combobox(janela, values=animais_lista)
combo_animal4 = ttk.Combobox(janela, values=animais_lista)

combo_animal1.grid(row=1, column=0)
combo_animal2.grid(row=1, column=1)
combo_animal3.grid(row=2, column=0)
combo_animal4.grid(row=2, column=1)

# Checkbox para seguir a ordem dos animais
var_seguir_ordem = tk.BooleanVar()
checkbox_ordem = tk.Checkbutton(janela, text="Seguir ordem dos animais", variable=var_seguir_ordem)
checkbox_ordem.grid(row=3, column=0, columnspan=2)

# Botão de calcular
botao_calcular = tk.Button(janela, text="Calcular Briquetes", command=ao_clicar)
botao_calcular.grid(row=4, column=0, columnspan=2)

# Inicia a janela
janela.mainloop()
