import sys,os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from produtoTela import Ui_Form
import fdb
import locale

class ProdCad(qtw.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        #tabwidget.setCurrentWidget(tabwidget.findChild(QWidget, tabname))
        #self.ui = Ui_Form()  ### Para não usar o .ui tem que declarar o 'Ui_Form' no parametro da classe
        #self.ui.setupUi(self)       self.setupUi(self)
        self.setupUi(self)
        locale.setlocale(locale.LC_ALL, '')  # Define o local

        self.primeiro.clicked.connect(self.addProd)
        self.ultimo.clicked.connect(self.ultimoItem)

        # Your code ends here
        self.show()

    def teste(self):
        print("deu boa")

    def addProd(self): #Adiciona o produto no Banco de Dados
            locale.setlocale(locale.LC_ALL, '')  # Define o local
        ##### Pegar Campos #############
            descricao = self.Descricao.text()
            codBarras = self.codBarras.text()
            undMedida = self.UndMedida.currentIndex()
            classe = self.classe.currentText()
            precocusto = self.precocusto.text()
            lucro = self.lucro.text()
            precofinal = self.precofinal.text()
            setor = self.setor.currentText()
            dtCad = self.dtCadProd.text()

            #### trocando separadores por ponto ####
            if (codBarras != ""):
                codBarras = codBarras.replace(',', '.')
            preco = locale.atof(precocusto, float)
            print (preco)

            # if (precocusto != ""):
             #   precocusto = precocusto.replace(',', '.')
           # print(precocusto)
            if (precofinal != ""):
                precofinal = precofinal.replace(',', '.')
            if (lucro != ""):
                lucro = lucro.replace(',', '.')
            if (dtCad != ""):
                dtCad = dtCad.replace('/', '.')

            cod1 = int(1)
            cod2 = int(1)
            if (descricao != ""):
                try:
                    con = fdb.connect(
                        host="localhost", database="C:/Users/God War/Documents/TCC/Banco de dados/gino14.FDB",
                        user='sysdba',
                        password='masterkey'
                    )

                    cur = con.cursor()
                    cur.execute("INSERT INTO t007_produtos (T005_NR_CODIGO, T006_NR_CODIGO, T007_CA_DESCRICAO, T007_NR_CODIGO_BARRAS, T007_NR_CUSTO) "
                                "VALUES (?,?,?,?,?)", (cod1, cod2, descricao, codBarras, preco)) ################# ESTOU TENtANDO INSERIR O PRECO
                    con.commit()
                    QMessageBox.information(self, "Info", "Produto Adicionado com Sucesso")
                    con.close
                except Exception as e: print(e)

                pass
            else:
                QMessageBox.information(self, "Info", "Preencher Campos Obrigatórios") 

    def alterarEstoque(self):
        try:
            con = fdb.connect(
                host="localhost", database="C:/Users/God War/Documents/TCC/Banco de dados/gino14.FDB",
                user='sysdba',
                password='masterkey'
            )

            cur = con.cursor()
            cur.execute("SELECT *FROM t007_produtos ORDER BY T007_NR_CODIGO DESC ")
            ultimoItem = cur.fetchall()[0]
            #cur.execute("select *from t007_produtos where T007_NR_CODIGO =" + str(ultimoItem[0]))
            #teste = cur.fetchall()[0]
            con.commit()
            QMessageBox.information(self, "Info", "Produto Adicionado com Sucesso")
            con.close
        except Exception as e:
            print(e)

        pass 

    def ultimoItem(self):
        try:
            con = fdb.connect(
                host="localhost", database="C:/Users/God War/Documents/TCC/Banco de dados/gino14.FDB",
                user='sysdba',
                password='masterkey'
            )

            cur = con.cursor()
            cur.execute("SELECT *FROM t007_produtos ORDER BY T007_NR_CODIGO DESC ")
            ultimoItem = cur.fetchall()[0][0]
            con.commit()
            con.close
            return ultimoItem
        except Exception as e:
            print(e)
        pass

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = ProdCad()
    sys.exit(app.exec_())
