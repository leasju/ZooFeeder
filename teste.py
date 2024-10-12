import sys
from PyQt6.QtGui import QFont # Fontes
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QComboBox, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        window = QWidget()
        self.setWindowTitle("ZooFeeder")
        
        
        
        # Define o tamanho da janela (largura, altura)
        self.resize(235, 180)  # Ajuste os valores conforme necessário


        # Configuração central do widget
        container = QWidget()
        self.setCentralWidget(container)
        self.layout = QVBoxLayout(container)
        label = QLabel("Bem-vindo ao ZooFeeder!")
        label.move(60, 15)
        self.layout.addWidget(label)

        # Definir o tamanho da fonte para a QLabel
        fonte = QFont()
        fonte.setPointSize(16)  # Altere este valor para aumentar ou diminuir o tamanho da fonte
        label.setFont(fonte)
        
        # Adicionar label e botão
        self.label1 = QLabel("Gerencie a alimentação dos animais do zoológico")
        self.label2 = QLabel("Selecione os animais")
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label2)

        # Adicionar comboboxes
        self.comboboxes = []
        self.comboBox()

        # Definir e adicionar o botão de enviar
        self.button = QPushButton("Enviar")
        self.button.clicked.connect(self.enviar_dados)
        self.layout.addWidget(self.button)

    def comboBox(self):
        # Criação dos comboboxes
        for _ in range(4):
            combobox = QComboBox()
            combobox.addItem('Selecione')
            combobox.addItem('Elefante')
            combobox.addItem('Girafa')
            combobox.addItem('Hipopotamo')
            combobox.addItem('Gorila')
            combobox.addItem('Alce')
            combobox.addItem('Canguru')
            combobox.addItem('Zebra')
            combobox.addItem('Pinguim')
            combobox.currentTextChanged.connect(self.current_text_changed)
            self.layout.addWidget(combobox)
            self.comboboxes.append(combobox)

    def current_text_changed(self, s):
        if s != 'Selecione':
            for combobox in self.comboboxes:
                if combobox != self.sender():
                    index = combobox.findText(s)
                    if index != -1:
                        combobox.removeItem(index)

    def enviar_dados(self):
        # Coleta os dados selecionados das comboboxes
        dados_selecionados = [combobox.currentText() for combobox in self.comboboxes]
        # Verifica se há algum item 'Selecione' e remove-o da lista
        dados_selecionados = [item for item in dados_selecionados if item != 'Selecione']
        print("Dados enviados:", dados_selecionados)
        self.label.setText("Dados enviados com sucesso!")

# Inicializar a aplicação
app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
