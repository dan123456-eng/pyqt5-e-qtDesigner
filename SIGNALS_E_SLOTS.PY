#ESTAMOS ESTUDANDO SOBRE SIGNALS E SLOTS (SINAIS E SLOT(=MÉTODO)) __ CALLBACKS NÃO SÃO  UTILIZADOS
#ESTUDAR POR ESSE LINK:https://medium.com/@wilfilho/conhecendo-o-coracao-e-as-arterias-do-pyqt5-22ba4187531

import  sys
from pyqt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QHBoxLayout, QMessageBox
# SÃO CLASSES DO QT5 QApplication, QWidget, QPushButton, QTextEdit, QHBoxLayout, QMessageBox

# class Window(QWidget) # ESSE QWIDGET FOI HERDADO --- ESSSA É BASICAMENTE A JANELA DO PROJETO


class Window(QWidget): # JANELA
    def __init__(self, parent=None):
        super(Window, self).__init__()
        root = QApplication([])
        app = Window()
        app.show()
        sys.exit(root.exec_())

    #def __init__(self, parent=None): 
       # super(Window, self).__init__() --> SÃO OS WIDGETS
        self.button = QPushButton("Exibir mensagem")
        self.button.clicked.connect(self.exibir) #connection activated ESSA É A FORMULA -->self.botao.clicked.connect(self.meu_metodo)
        self.line_edit = QLineEdit()
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

"""DEPOIS DE CRIARMOS A JANELA ACIMA PRECISAMOS FAZER O SEGUINTEprecisamos de um botão, um layout, uma área onde o usuário possa 
inserir o texto e um diálogo(neste caso será o MessageBox)"""
    def exibir(self): # O MÉTODO
        self.text = self.line_edit.text()
        self.messsage_box = QMessageBox.information(self,"Exemplo 1", self.text)