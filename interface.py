import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPalette, QBrush, QPixmap, QIcon  # Main Window Style
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QComboBox, QPushButton, QLabel, QDialog

class ResultadoDialog(QDialog):
    def __init__(self, dados):
        super().__init__()
        self.setWindowTitle("Results")
        self.resize(250, 200) 

        # Layout e exibição dos dados enviados
        layout = QVBoxLayout()
        label = QLabel("Animals select:")
        layout.addWidget(label)

        # Exibir os dados selecionados
        for item in dados:
            label_animal = QLabel(item)
            layout.addWidget(label_animal)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        window = QWidget()
        self.setWindowTitle("ZooFeeder")
        
        # Window icon
        self.setWindowIcon(QIcon("img/icon1.png"))  
        
        # Window size
        self.setFixedSize(300, 250)  

        # Background config
        self.set_background_image("img/back1.jpg")
        
        # Configuração central do widget
        container = QWidget()
        self.setCentralWidget(container)
        self.layout = QVBoxLayout(container)
        
        # Criar a QLabel principal e adicionar ao layout
        self.label = QLabel("Welcome to ZooFeeder!")
        self.layout.addWidget(self.label)

        # Label font size
        fonte = QFont()
        fonte.setPointSize(16)
        self.label.setFont(fonte)
        
        # Add other labels to layout
        self.label1 = QLabel("Gerencie a alimentação dos animais do zoológico")
        self.label2 = QLabel("Select the animals: ")
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label2)

        # Add comboboxes
        self.comboboxes = []
        self.comboBox()

        # Definir e adicionar o botão de enviar ao layout
        self.button = QPushButton("Send")
        self.button.clicked.connect(self.enviar_dados)
        self.layout.addWidget(self.button)

    # Window background image function
    def set_background_image(self, image_path):
        # Carregar a imagem
        pixmap = QPixmap(image_path)
        # Redimensionar a imagem para o tamanho da janela, mantendo a proporção
        pixmap = pixmap.scaled(self.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        
        # Configurar a imagem de fundo com QPalette
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)

    # Select animal function
    def comboBox(self):
        # Create comboboxes
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

    # Send data function
    def enviar_dados(self):
        # Coleta os dados selecionados das comboboxes
        dados_selecionados = [combobox.currentText() for combobox in self.comboboxes]
        # Verifica se há algum item 'Selecione' e remove-o da lista
        dados_selecionados = [item for item in dados_selecionados if item != 'Select']
        print("Dados enviados:", dados_selecionados)
        
        # Refresh label text
        self.label.setText("Dados enviados com sucesso!")
        
        # Open a new window to show de results
        self.resultado_dialog = ResultadoDialog(dados_selecionados)
        self.resultado_dialog.exec()

# Initialize the application
app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
