from PyQt5.QtWidgets import *
import sys,os
from PyQt5 import QtWidgets as qtw
from vendasTela import Ui_Form
from testebancosqlite import executarSelect as sel
from testebancosqlite import conexaoBanco as conexao
from sqlite3 import Error
from datetime import datetime
from buscarVendaCod import buscarVenda as bv
import main


class Venda(qtw.QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.tableWidget.setColumnWidth(0,150) #### Setar o tamanho da coluna
        rowcount = self.prodbuscar.clicked.connect(self.addProdTable)
        self.voltarTela.clicked.connect(self.fecharTela)
        self.prodcod.editingFinished.connect(self.preencherProd)
        self.desconto.editingFinished.connect(self.somarTotal)
        self.recebido.editingFinished.connect(self.calctroco)
        self.clicod.editingFinished.connect(self.buscarCliente)
        self.salvar.clicked.connect(self.addProd)
        self.buscar.clicked.connect(self.buscarVenda)
        #self.cadcliente.clicked.connect(self.cadcliente)
        self.show()

    #def cadcliente(self):
        #self.newclientes = main.funcCliente()

    def fecharTela(self):
        self.close()

    def buscarVenda(self):
        self.buscar = bv()

    def limparProd(self):
        self.prodcod.setText("")
        self.prodqtde.setText("")
        self.prodcod.setText("")
        self.proddesc.setText("")
        self.prodpreco.setText("")

    def preencherProd(self):
        codigo = self.prodcod.text()
        if (codigo != ''):
            try:
                con = conexao()
                c = con.cursor()
                c.execute(" SELECT prod_desc, prod_preco FROM produtos where prod_id = (?)", (codigo,))
                con.commit()
                resultado = c.fetchall()
                c.close()
                print(resultado[0])
            except Error as e:
                print(e)
                return e
            pass
            self.proddesc.setText(str(resultado[0][0]))
            self.prodpreco.setText(str(resultado[0][1]))

    def somarValor(self):
        valor = 0
        rowcount = self.tableWidget.rowCount()
        if(rowcount != ''):
            for row in range(rowcount):
                vlr = self.tableWidget.item(row,4)
                vlr = vlr.text()
                vlr = float(vlr)
                #vlr = float(vlr)
                valor = valor + vlr
            self.valorbruto.setText(str(valor))

    def calctroco(self):
        valor = self.recebido.text()
        total = self.total.text()
        if (valor and total != ''):
            troco = float(valor) - float(total)
            self.troco.setText(str(troco))

    def somarTotal(self):
        valor = self.valorbruto.text()
        desconto = self.desconto.text()

        if(valor and desconto != ''):
            total = float(valor) - float(desconto)
            self.total.setText(str(total))
        elif(valor != ''):
            total = valor
            self.total.setText(str(total))

    def buscarCliente(self):
        cod = self.clicod.text()
        if(cod != ''):
            cod = int(cod)
            try:
                con = conexao()
                c = con.cursor()
                c.execute(" SELECT * FROM clientes order by cli_id DESC")
                con.commit()
                ultimo = c.fetchall()
                c.close()
                ultimo = ultimo[0][0]
                ultimo = int(ultimo)
            except Exception as e:
                print(e)
            pass
            if(cod < ultimo):
                try:
                    con = conexao()
                    c = con.cursor()
                    c.execute(" SELECT cli_nome FROM clientes where cli_id = (?)", (cod,))
                    con.commit()
                    resultado = c.fetchall()
                    c.close()
                    flag = "0"
                except Error as e:
                    flag = "1"
                    print(e)
                if(flag == "0"):
                    self.clinome.setText(resultado[0][0])
            else:
                QMessageBox.information(self, "Info", "Cliente Não Localizado")


    def addProdTable(self):
        rowcount = 0
        codigo = self.prodcod.text()
        qtde = int(self.prodqtde.text())
        rowcount = self.tableWidget.rowCount()
        print(rowcount)
        try:
            con = conexao()
            c = con.cursor()
            c.execute(" SELECT prod_cod, prod_desc, prod_preco FROM produtos where prod_id = (?)", (codigo,))
            con.commit()
            resultado = c.fetchall()
            c.close()
            print(resultado[0])
        except Error as e:
            print(e)
            return e
        pass
        preco = float(resultado[0][2])
        total = preco * qtde
        self.tableWidget.setRowCount(rowcount + 1)
        for row in range(len(resultado)):
            self.tableWidget.setItem(rowcount, 0, QTableWidgetItem(resultado[0][0]))
            self.tableWidget.setItem(rowcount, 1, QTableWidgetItem(resultado[0][1]))
            self.tableWidget.setItem(rowcount, 2, QTableWidgetItem(str(qtde)))
            self.tableWidget.setItem(rowcount, 3, QTableWidgetItem(str(resultado[0][2])))
            self.tableWidget.setItem(rowcount, 4, QTableWidgetItem(str(total)))
        self.somarValor()
        self.limparProd()
        self.somarTotal()

    def addProd(self):
        data = datetime.today()
        data = str(data)
        newdata = data[8:10] + "/" + data[5:7] + "/" + data[:4]
        cliente = self.clicod.text()
        valor = self.valorbruto.text()
        total = self.total.text()
        desconto = self.desconto.text()
        formapgt = self.formapgt.currentText()
        rowcount = self.tableWidget.rowCount()
        print(rowcount)

        if((valor and total != '') and (rowcount != 0)):
            try:
                con = conexao()
                c = con.cursor()
                c.execute(
                    """INSERT INTO vendas (cli_id, ven_valor, ven_desc, ven_pgt, ven_data) 
                       VALUES (?,?,?,?,?)""",
                    (cliente, total, desconto, formapgt, newdata))
                con.commit()
                c.close()
                flag = "0"
            except Error as e:
                flag = "1"
                print(e)

            if(flag == "0"):
                try:
                    con = conexao()
                    c = con.cursor()
                    c.execute(" SELECT * FROM vendas order by ven_id DESC")
                    con.commit()
                    resultado = c.fetchall()
                    c.close()
                    venid = str(resultado[0][0])
                except Exception as e:
                    flag = "1"
                    print(e)
                pass

            if(flag == "0"):
                for row in range(rowcount):
                    qtd = self.tableWidget.item(row, 2)
                    qtd = qtd.text()
                    prodid = self.tableWidget.item(row, 0)
                    prodid = prodid.text()
                    print(qtd)
                    print(prodid)
                    try:
                        con = conexao()
                        c = con.cursor()
                        c.execute(
                            """INSERT INTO itensvenda (ven_id, prod_id, item_qtd) 
                               VALUES (?,?,?)""",
                            (venid, prodid, qtd))
                        con.commit()
                        c.close()
                        QMessageBox.information(self, "Info", "Venda Realizada com Sucesso")
                    except Error as e:
                        QMessageBox.information(self, "Info", "Erro ao Realizar a Venda")
                        print(e)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = Venda()
    sys.exit(app.exec_())
