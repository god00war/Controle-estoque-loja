from reportlab.pdfgen import canvas
from reportlab.platypus import Table,SimpleDocTemplate,Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import clienteCod
import produtoCod
import vendaCod
import webbrowser
from PIL import Image
from testebancosqlite import conexaoBanco as conexao
from sqlite3 import Error
pastaApp = os.path.dirname(__file__)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Manager")
        self.setGeometry(0, 0, 1350, 780)

        self.UI()
        self.show()

    def UI(self):
        self.toolBar()

    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        ###################Tool Bar Buttons################
        ###################Clientes############
        self.clientes = QAction(QIcon('icons/person-icon.png'), "Gerenciar Clientes", self)
        self.tb.addAction(self.clientes)
        self.clientes.triggered.connect(self.Relatorio)
        self.tb.addSeparator()
        ###################Produtos############
        self.produtos = QAction(QIcon('icons/product.png'), "Gerenciar Produtos", self)
        self.tb.addAction(self.produtos)
        self.produtos.triggered.connect(self.funcProd)
        self.tb.addSeparator()
        ###################Vendas############
        self.venda = QAction(QIcon('icons/shop-cart.png'), "Fazer Venda", self)
        self.tb.addAction(self.venda)
        self.venda.triggered.connect(self.funcVenda)
        self.tb.addSeparator()
        ##################

    @staticmethod
    def mp(milimetros):
        milimetros = milimetros / 0.35277
        return milimetros

    def Relatorio(self):
        rowcount = 0
        dti = ("2022/08/01")
        dtf = ("2022/09/01")

        try:
            con = conexao()
            c = con.cursor()
            c.execute(" SELECT * FROM vendas where  ven_data BETWEEN (?) AND (?)", (dti,dtf))
            con.commit()
            itemvenda = c.fetchall()
            c.close()
            flag = "0"
        except Error as e:
            print(e)
            flag = "1"
        pass
        print(itemvenda)
        self.CriarPdf(itemvenda)

    def CriarPdf(self, nomes):
        nome = nomes
        #nomes = [('cuzinho'), 'cu cuzao', 'cuzada violenta']
        eixo=100

        pdf=SimpleDocTemplate("Teste.pdf")
        flow_obj=[]
        styles= getSampleStyleSheet()
        tstyle=TableStyle([("GRID", (0,0),(-1,-1),.1,colors.red)])
        print(nome)
        t=Table(nome)
        print(t)
        t.setStyle(tstyle)
        flow_obj.append(t)
        pdf.build(flow_obj)


        #cnv = canvas.Canvas("alomundo.pdf")
        #for nome in nomes:
        #    cnv.drawString(self.mp(eixo), self.mp(50), nome)
        #    eixo += 20


        # table = Table(data)
        # elems = []
        # elems.append(table)

        #cnv.save()
        return 0
        # webbrowser.open("alomundo.pdf")

    # try:
    #    #cnv = canvas.Canvas(pastaApp+"\\teste.pdf", pagesize=A4)

    #       pdf.drawString(250, 350, "Teste")
    #        pdf.save
    #          print("passei")
    #       except:
    #            QMessageBox.information(self, "Info", "Não foi Possivel criar Relatório")
    def funcProd(self):
        self.newproduto = produtoCod.ProdCad()

    def funcVenda(self):
        self.venda = vendaCod.Venda()


def main():
    App = QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
