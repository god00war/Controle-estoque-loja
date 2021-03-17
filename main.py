import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import clienteCod
from PIL import Image





class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Manager")
        self.setGeometry(0,0,1350,780)

        self.UI()
        self.show()

    def UI(self):
        self.toolBar()

    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        ###################Tool Bar Buttons################
        ###################Clientes############
        self.clientes = QAction(QIcon('icons/person-icon.png'),"Gerenciar Clientes",self)
        self.tb.addAction(self.clientes)
        self.clientes.triggered.connect(self.funcCliente)
        self.tb.addSeparator()
        ###################Produtos############
        self.produtos = QAction(QIcon('icons/product.png'), "Gerenciar Produtos", self)
        self.tb.addAction(self.produtos)
        self.tb.addSeparator()
        ###################Vendas############
        self.venda = QAction(QIcon('icons/shop-cart.png'), "Fazer Venda", self)
        self.tb.addAction(self.venda)
        self.tb.addSeparator()

    def funcCliente(self):
        self.newclientes = clienteCod.ClienteLogin()

def main():
    App=QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()