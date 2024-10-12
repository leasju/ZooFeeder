import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QComboBox, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        window = QWidget()
        self.setWindowTitle("ZooFeeder")
        window.setGeometry(200, 100, 280, 100)

        # Configuração central do widget
        container = QWidget()
        self.setCentralWidget(container)
        self.layout = QVBoxLayout(container)

        label = QLabel("Welcome to ZooFeeder!")
        label.move(60, 15)
        
        self.layout.addWidget(label)

        
        # Adicionar label e botão
        self.label = QLabel("Selecione os animais")
        self.layout.addWidget(self.label)
       

        # Adicionar comboboxes
        self.comboBox()

    def comboBox(self):
        # Criação dos comboboxes
        combobox1 = QComboBox()
        combobox1.addItem('Selecione')
        combobox1.addItem('Elefante')
        combobox1.addItem('Girafa')
        combobox1.addItem('Hipopotamo')
        combobox1.addItem('Gorila')
        combobox1.addItem('Alce')
        combobox1.addItem('Canguru')
        combobox1.addItem('Zebra')
        combobox1.addItem('Pinguim')

        combobox2 = QComboBox()
        combobox2.addItems(['Selecione','Elefante', 'Girafa', 'Hipopotamo', 'Gorila', 'Alce', 'Canguru', 'Zebra', 'Pinguim'])

        combobox3 = QComboBox()
        combobox3.addItems(['Selecione','Elefante', 'Girafa', 'Hipopotamo', 'Gorila', 'Alce', 'Canguru', 'Zebra', 'Pinguim'])

        combobox4 = QComboBox()
        combobox4.addItems(['Selecione','Elefante', 'Girafa', 'Hipopotamo', 'Gorila', 'Alce', 'Canguru', 'Zebra', 'Pinguim'])

        # Conectar o sinal de mudança de texto a um método
        combobox1.currentTextChanged.connect(self.current_text_changed)
        combobox2.currentTextChanged.connect(self.current_text_changed)
        combobox3.currentTextChanged.connect(self.current_text_changed)
        combobox4.currentTextChanged.connect(self.current_text_changed)

        # Adicionar comboboxes ao layout
        self.layout.addWidget(combobox1)
        self.layout.addWidget(combobox2)
        self.layout.addWidget(combobox3)
        self.layout.addWidget(combobox4)

    def mudar_texto(self):
        self.label.setText("Texto mudou!")

    def current_text_changed(self, s):
        print("Current text: ", s)

# Inicializar a aplicação
app = QApplication(sys.argv)
w = MainWindow()
w.show()  # Certifique-se de que a janela é exibida antes de entrar no loop
sys.exit(app.exec())  # Utilizando sys.exit para garantir um fechamento correto
