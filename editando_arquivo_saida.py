# ESSE ARQUIVO ESTA ERDANDO DO  ARQUIVO DO COPIA_ARQUIVO_SAIDA

from PyQt5 import QtCore, QtGui, QtWidgets # PODERIA SER: from PyQt5.QtWidgtes import*

from copia_arquvo_saida import Ui_PROTETO_01 # EU IMPORTEI
import sys #ESSE MODULO FOI IMPORTADO 
from PyQt5.QtWidgets import * # ESSE MODULO FOI IMPORTADO
def retranslateUi(self, PROTETO_01): # ESSA FUNÇÃO  É UMA COPIA DA FUNÇÃO ORIGINAL
        _translate = QtCore.QCoreApplication.translate
        PROJETO_01.setWindowTitle(_translate("PROTETO_01", "Form"))
        self.pushButton.setText(_translate("PROTETO_01", "FAZ ALGO"))

# ESSA PARTE DO CODIGO  FAZ A COMUNICAÇÃO COM O PROJETO E MOSTRA A JANELA/OU AS JANELAS
class Window(QWidget): #A  CLASS Window POSSUI O QWidget COM HERANÇA
    def __init__(self, parent=None): # O  PARENT É PARA INDICAR QUE EXISTE UM FREME PAI
        super(Window, self).__init__() 
root = QApplication(sys.argv) # AQUI FOI CRIADO UMA INSTÂNCIA PARA O  QApplication
app = Window() # AQUI FOI CRIADA UMA INSTÂNCIA PARA A JANELA Window
app.show() # AQUI É MOSTRADA A INSTÂNCIA APP
sys.exit(root.exer_()) # AQUI É CRIADO UM LOOP IMFINITO QUE SO PODE SER FECHADO PELIO USUARIO
# ROOT É A RAIZ