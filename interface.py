import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPalette, QBrush, QPixmap, QIcon  # Main Window Style
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QComboBox, QPushButton, QLabel, QDialog

# Result window
class ResultadoDialog(QDialog):
    def __init__(self, dados):
        super().__init__()
        self.setWindowTitle("Results")
        self.resize(250, 200) 

        # Layout e exibição dos dados enviados
        layout = QVBoxLayout()
        label = QLabel("Animals selected: ")
        layout.addWidget(label)

        # Exibir os dados selecionados
        for item in dados:
            label_animal = QLabel(item)
            layout.addWidget(label_animal)

        self.setLayout(layout)

# Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        window = QWidget()
        self.setWindowTitle("ZooFeeder")
        
        # Window icon
        self.setWindowIcon(QIcon("img/zoo_icon.png"))  
        
        # Window size
        self.setFixedSize(300, 250)  

        # Background config
        self.set_background_image("img/background.jpg")
        
        # Central widget config
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

        # Send button
        self.button = QPushButton("Send")
        self.button.clicked.connect(self.send)
        self.layout.addWidget(self.button)
        
        # Clear button
        self.button = QPushButton("Clear")
        self.button.clicked.connect(self.clear)
        self.layout.addWidget(self.button)
        
         # QLabel for status or feedback
        self.status_label = QLabel("")
        self.layout.addWidget(self.status_label)


    # Window background image function
    def set_background_image(self, image_path):
        # Carregar a imagem
        pixmap = QPixmap(image_path)
        # QLabel para a imagem de fundo
        self.background_label = QLabel(self)
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(False)  # Não escala a imagem
        self.background_label.setGeometry(0, 0, pixmap.width(), pixmap.height())
        self.background_label.lower()  # Put the image behind the other widgets 

    # Select animal function
    def comboBox(self):
        # Create comboboxes
        for _ in range(4):
            combobox = QComboBox()
            combobox.addItem('Selecione') # Placeholder
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

    # Function for remove the comboboxes which are not selected
    def current_text_changed(self, s):
        if s != 'Selecione':
            for combobox in self.comboboxes:
                if combobox != self.sender():
                    index = combobox.findText(s)
                    if index != -1:
                        combobox.removeItem(index)

    # Send form data function
    def send(self):
        # Coleta os dados selecionados das comboboxes, ignorando os que estão no índice 0 (placeholder "Selecione")
        send_data = [combobox.currentText() for combobox in self.comboboxes if combobox.currentIndex() != 0]
        
        # Verifica se algum combobox ainda está com o item "Selecione" (índice 0)
        if len(send_data) != len(self.comboboxes):
            self.status_label.setText("Selecione um opção válida")
            return
        print("Dados enviados:", send_data)
        
        # Update the status label text
        self.status_label.setText("Dados enviados com sucesso!")
            
        # Open a new window to show de results
        self.resultado_dialog = ResultadoDialog(send_data)
        self.resultado_dialog.exec()
                
    # Clean data function
    def clear(self):
        # Reseta cada combobox para o item "Selecione"
        for combobox in self.comboboxes:
            combobox.setCurrentIndex(0)  
        print("Formulário limpo com sucesso!")
            
        # Refresh label text
        self.status_label.setText("Formulário limpo com sucesso")
        

# Initialize the application
app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
