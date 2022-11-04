from PyQt5.QtWidgets import *
import sys,os
from PyQt5 import QtWidgets as qtw
from buscarVendaTela import Ui_Form
from testebancosqlite import executarSelect as sel
from testebancosqlite import conexaoBanco as conexao
from sqlite3 import Error
from datetime import datetime
import main


class buscarVenda(qtw.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        a = ''
        self.setupUi(self)
        self.tableprod.setColumnWidth(0,150) #### Setar o tamanho da coluna
        self.venid.editingFinished.connect(self.buscarVendas)
        self.ultimo.clicked.connect(self.ultimoItem)
        self.primeiro.clicked.connect(self.primeiroItem)
        self.proximo.clicked.connect(self.proximoItem)
        self.anterior.clicked.connect(self.anteriorItem)
        self.voltarTela.clicked.connect(self.fecharTela)
        #self.cadcliente.clicked.connect(self.cadcliente)
        self.show()

    def fecharTela(self):
        self.close()


    def buscarVendas(self):
        try:
            codigo = self.venid.text()
            con = conexao()
            c = con.cursor()
            c.execute(" SELECT * FROM vendas where ven_id = (?)", (codigo,))
            con.commit()
            resultado = c.fetchall()
            c.close()
            print(resultado)
            flag = "0"
        except Error as e:
            print(e)
            flag = "1"
        pass

        if(flag == "0"):
            ############## Recebendo Valores ######################
            vencli = resultado[0][1]
            vendata = resultado[0][4]
            venvalorliquido = resultado[0][2]
            vendesc = resultado[0][3]
            if(vendesc == "None"):
                vendesc = 0
            elif(vendesc == ""):
                vendesc = 0
            ventotal = float(venvalorliquido) + float(vendesc)
            print(vendata)


            ############## Buscar nome CLiente #################
            if(vencli !=''):
                try:
                    con = conexao()
                    c = con.cursor()
                    c.execute(" SELECT cli_nome FROM clientes where cli_id = (?)", (vencli,))
                    con.commit()
                    clinome = c.fetchall()
                    c.close()
                except Error as e:
                    print(e)
                    flag = "1"
                pass
            else:
                flag = "1"
            if(flag == "0"):
                self.clinome.setText(str(clinome[0][0]))
            else:
                self.clinome.setText("")

            if((vendesc == '') or (vendesc == 'None') ):
                self.clinome.setText("")
            else:
                self.descontos.setText(str(vendesc))

            ############## Colocando Valores nos campos ######################
            self.totalvenda.setText(str(ventotal))
            self.totalpagar.setText(str(venvalorliquido))
            self.datavend.setText((str(vendata)))
            self.inserirProd()

    def inserirProd(self):
        rowcount = 0
        venid = self.venid.text()

        try:
            con = conexao()
            c = con.cursor()
            c.execute(" SELECT prod_id, item_qtd FROM itensvenda where ven_id = (?)", (venid,))
            con.commit()
            itemvenda = c.fetchall()
            c.close()
            flag = "0"
        except Error as e:
            print(e)
            flag = "1"
        pass
        print(itemvenda)
        if(flag == "0"):
            for row in range(len(itemvenda)):
                codigo = itemvenda[row][0]
                qtde = itemvenda[row][1]
                print(codigo)
                print(qtde)
                try:
                    con = conexao()
                    c = con.cursor()
                    c.execute(" SELECT prod_cod, prod_desc, prod_preco FROM produtos where prod_id = (?)", (codigo,))
                    con.commit()
                    resultado = c.fetchall()
                    c.close()
                    flag = "0"
                except Error as e:
                    print(e)
                    flag = "1"
                pass

                if (flag == "0"):
                    preco = float(resultado[0][2])
                    total = preco * qtde
                    print(rowcount)
                    self.tableprod.setRowCount(rowcount + 1)
                    self.tableprod.setItem(rowcount, 0, QTableWidgetItem(resultado[0][0]))
                    self.tableprod.setItem(rowcount, 1, QTableWidgetItem(resultado[0][1]))
                    self.tableprod.setItem(rowcount, 2, QTableWidgetItem(str(qtde)))
                    self.tableprod.setItem(rowcount, 3, QTableWidgetItem(str(resultado[0][2])))
                    self.tableprod.setItem(rowcount, 4, QTableWidgetItem(str(total)))
                    rowcount = rowcount + 1
                else:
                    QMessageBox.information(self, "Info", "Erro adicionar produtos")
        else:
            QMessageBox.information(self, "Info", "Erro adicionar produtos")

    def ultimoItem(self):
        try:
            con = conexao()
            c = con.cursor()
            c.execute(" SELECT * FROM vendas order by ven_id DESC")
            con.commit()
            resultado = c.fetchall()
            c.close()
            self.venid.setText(str(resultado[0][0]))
            self.buscarVendas()
        except Exception as e:
            print(e)
        pass

    def primeiroItem(self):
        try:
            con = conexao()
            c = con.cursor()
            c.execute(" SELECT * FROM vendas")
            con.commit()
            resultado = c.fetchone()
            c.close()
            self.venid.setText(str(resultado[0]))
            self.buscarVendas()
        except Exception as e:
            print(e)
        pass

    def proximoItem(self):
        try:
            con = conexao()
            c = con.cursor()
            c.execute(" SELECT * FROM vendas order by ven_id DESC")
            con.commit()
            ultimo = c.fetchall()
            c.close()
            ultimo = ultimo[0][0]
            ultimo = int(ultimo)
        except Exception as e:
            print(e)
        pass
        resultado = self.venid.text()
        if (resultado == ""):
            resultado = 0
        resultado = int(resultado)
        if(resultado < ultimo):
            resultado = int(resultado) + 1
            self.venid.setText(str(resultado))
            self.buscarVendas()
        else:
            QMessageBox.information(self, "Info", "Produto Não Localizado")

    def anteriorItem(self):
        resultado = self.venid.text()
        if (resultado == ""):
            resultado = 1
        resultado = int(resultado)
        if (resultado > 1):
            resultado = resultado - 1
            self.venid.setText(str(resultado))
            self.buscarVendas()
        else:
            QMessageBox.information(self, "Info", "Produto Não Localizado")


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = buscarVenda()
    sys.exit(app.exec_())
