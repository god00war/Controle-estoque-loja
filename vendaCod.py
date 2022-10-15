from PyQt5.QtWidgets import *
import sys,os
from PyQt5 import QtWidgets as qtw
from vendasTela import Ui_Form
from PyQt5.QtCore import *
from testebancosqlite import executarSelect as sel
from testebancosqlite import conexaoBanco as conexao
from sqlite3 import Error
from datetime import datetime
from buscarVendaCod import buscarVenda as bv
from produtoCod import ProdCad as pc
from clienteCod import ClienteLogin as ct
import buscarProdCod
import buscarCliCod
from decimal import Decimal
import time
import main


class Venda(qtw.QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.tableWidget.setColumnWidth(0,150) #### Setar o tamanho da coluna
        ################### EVENTOS ####################
        self.desconto.editingFinished.connect(self.somarTotal)  # terminar de editar
        self.desconto.editingFinished.connect(self.calctroco)
        self.recebido.editingFinished.connect(self.calctroco)
        self.descontoPorcen.editingFinished.connect(self.descontoPorcentagem)
        self.clibuscar.clicked.connect(self.buscarClienteTela)  # clicar
        self.voltarTela.clicked.connect(self.fecharTela)
        self.prodbuscar.clicked.connect(self.buscarProdTela)
        self.salvar.clicked.connect(self.addProd)
        self.buscar.clicked.connect(self.buscarVenda)
        self.cancel.clicked.connect(self.cancelarVenda)
        self.cadproduto.clicked.connect(self.produtoTela)
        self.cadcliente.clicked.connect(self.clienteTela)
        self.prodqtde.returnPressed.connect(self.addProdTable)  # apertar enter
        self.prodcod.returnPressed.connect(self.buscarCod)
        self.clicod.returnPressed.connect(self.buscarCliCod)

        self.salvar.close()
        self.cancel.close()
        self.show()

    def fecharTela(self):
        self.close()

    def buscarVenda(self): #### Chama a Tela Buscar Vendas
        self.buscar = bv()

    def produtoTela(self):  #### Chama a Tela de Produtos
        self.buscar = pc()

    def clienteTela(self):  #### Chama a Tela de Cliente
        self.buscar = ct()

    def buscarClienteTela(self):
        self.buscarCli = buscarCliCod.buscarCli() #chamando a tela de buscar cliente
        self.worker = WorkedThread()
        self.worker.start()
        self.worker.update_archive.connect(self.buscarCliente)

    def buscarProdTela(self):
        self.busc = buscarProdCod.buscarProd() #chamando a tela de buscar produto
        self.worker = WorkedThread()
        self.worker.start()
        self.worker.update_archive.connect(self.preencherProd)

    def messagebox(self, msg, title):
        msgBox = QMessageBox()
        msgBox.setText(msg)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        value = msgBox.exec()
        return value

    def cancelarVenda(self):
        msg = "Deseja Mesmo Cancelar a Venda?"
        title = "Cancelar Venda"
        valor = self.messagebox(msg, title)
        if valor == QMessageBox.Ok:
            row = self.tableWidget.rowCount()
            for row in range(row):
                self.tableWidget.removeRow(0)
            self.tableWidget.clearContents()
            self.desconto.setText("")
            self.descontoPorcen.setText("")
            self.total.setText("")
            self.valor.setText("")
            self.recebido.setText("")
            self.troco.setText("")
            self.clicod.setText("")
            self.clinome.setText("")
            self.limparProd()

    def limparProd(self):
        self.prodcod.setText("")
        self.prodqtde.setText("")
        self.prodcod.setText("")
        self.proddesc.setText("")
        self.prodpreco.setText("")

    def buscarCod(self):  #### pega o codigo e chama preencherProd
        cod = self.prodcod.text()
        if (cod != ''):
            print(cod)
            self.preencherProd(cod)

    def buscarCliCod(self):  ####### pega o codigo e chama buscarCliente
        cod = self.clicod.text()
        if (cod != ''):
            self.buscarCliente(cod)

    def preencherProd(self, var): #### buscando e preenchendo o produto
        codigo = var
        flag = 0
        try: #### buscando o ultimo produto cadastrado
            con = conexao()
            c = con.cursor()
            c.execute(" SELECT * FROM produtos order by prod_id DESC")
            con.commit()
            ultimo = c.fetchall()
            c.close()
            ultimo = ultimo[0][0]
            ultimo = int(ultimo)
        except Exception as e:
            print(e)
        pass
        if (codigo != '' ): #### Se produto não está vazio e é
            codigo = int(codigo)
            if(codigo < ultimo): #### se codigo não é menor que o ultimo produto cadastrado
                try:
                    con = conexao()
                    c = con.cursor()
                    c.execute(" SELECT prod_desc, prod_preco FROM produtos where prod_id = (?)", (codigo,))
                    con.commit()
                    resultado = c.fetchall()
                    c.close()
                except Error as e:
                    flag = 1
                    print(e)
                    return e
                pass
                if(flag == 0):
                    preco = "{:.2f}".format(resultado[0][1]) #### Dois zeros depois da virgula
                    self.proddesc.setText(str(resultado[0][0]))
                    self.prodpreco.setText(str(preco))
                    self.prodcod.setText(codigo)
                    self.prodqtde.setFocus()
                    with open("arqtemp.txt", "w") as arquivo:  # Limpar arquivo
                        arquivo.write("")
            else:
                QMessageBox.information(self, "Info", "Produto Não Localizado")
        else:
            QMessageBox.information(self, "Info", "Produto Não Localizado")
    @staticmethod
    def truncate(num, n):  # truncar float (Omitir N digitos depois da virgula)
        temp = str(num)
        for x in range(len(temp)):
            if temp[x] == '.':
                try:
                    return float(temp[:x + n + 1])
                except:
                    return float(temp)
        return float(temp)

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
            valor = "{:.2f}".format(valor) #### Dois zeros depois da virgula
            self.valor.setText(str(valor))

    def descontoPorcentagem(self):
        valor = self.valor.text()
        desconto = self.descontoPorcen.text()

        if (valor and desconto != ''):
            desconto = desconto.replace(",", ".")
            desconto = float(desconto) / 100
            desconto = Decimal(valor) * Decimal(desconto)
            total = Decimal(valor) - Decimal(desconto)
            total = "{:.2f}".format(float(total))  #### Dois zeros depois da virgula
            desconto = "{:.2f}".format(float(desconto))  #### Dois zeros depois da virgula
            self.total.setText(str(total))
            self.desconto.setText(str(desconto))


    def calctroco(self):
        valor = self.recebido.text()
        total = self.total.text()
        if (valor and total != ''):
            valor = valor.replace(",", ".")
            total = total.replace(",", ".")
            troco = Decimal(valor) - Decimal(total)
            troco = "{:.2f}".format(troco) #### Dois zeros depois da virgula
            self.troco.setText(str(troco))

    def somarTotal(self):
        valor = self.valor.text()
        desconto = self.desconto.text()

        if(valor and desconto != ''):
            desconto = desconto.replace(",",".")
            total = float(valor) - float(desconto)
            total = "{:.2f}".format(float(total))  #### Dois zeros depois da virgula
            desconto = "{:.2f}".format(float(desconto))  #### Dois zeros depois da virgula
            self.total.setText(str(total))
            self.desconto.setText(str(desconto))
        elif(valor != ''):
            desconto = 0
            total = valor
            total = "{:.2f}".format(float(total))  #### Dois zeros depois da virgula
            desconto = "{:.2f}".format(float(desconto))  #### Dois zeros depois da virgula
            self.total.setText(str(total))
            self.desconto.setText(str(desconto))

    def buscarCliente(self, var):
        cod = var
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
                    c.execute(" SELECT cli_id, cli_nome FROM clientes where cli_id = (?)", (cod,))
                    con.commit()
                    resultado = c.fetchall()
                    c.close()
                    flag = "0"
                except Error as e:
                    flag = "1"
                    print(e)
                if(flag == "0"):
                    print("passei buscar cliente 1")
                    self.clicod.setText(str(resultado[0][0]))
                    self.clinome.setText(resultado[0][1])
            else:
                QMessageBox.information(self, "Info", "Cliente Não Localizado")
            with open("arqtemp.txt", "w") as arquivo:  # Limpar arquivo
                arquivo.write("")

    def addProdTable(self): #### Adiciona o Produto na Tabela de Produtos
        self.cancel.show()
        self.salvar.show()
        rowcount = 0
        codigo = self.prodcod.text()
        qtde = self.prodqtde.text()
        if(qtde !=''):
            int(qtde)
        rowcount = self.tableWidget.rowCount()
        if(codigo !=''):
            if (qtde != ''):
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
                print("preco: ", preco)
                preco = "{:.2f}".format(preco)  # colocar 2 zeros depois da virgula
                print("preco: ", preco)
                total = Decimal(preco) * Decimal(qtde)
                total = self.truncate(total, 2) ### Deixar com duas casas decimais
                total = "{:.2f}".format(total) # colocar 2 zeros depois da virgula

                print("total: ",total)
                self.tableWidget.setRowCount(rowcount + 1)
                for row in range(len(resultado)):
                    self.tableWidget.setItem(rowcount, 0, QTableWidgetItem(resultado[0][0]))
                    self.tableWidget.setItem(rowcount, 1, QTableWidgetItem(resultado[0][1]))
                    self.tableWidget.setItem(rowcount, 2, QTableWidgetItem(str(qtde)))
                    self.tableWidget.setItem(rowcount, 3, QTableWidgetItem(str(preco)))
                    self.tableWidget.setItem(rowcount, 4, QTableWidgetItem(str(total)))
                self.somarValor()
                self.limparProd()
                self.somarTotal()
                self.prodcod.setFocus()
            else:
                QMessageBox.information(self, "Info", "Digite uma Quantidade")
        else:
            QMessageBox.information(self, "Info", "Preencha o Produto")


    def addProd(self): #salvando no banco da dados
        data = datetime.today()
        data = str(data)
        newdata = data[:4] + "/" + data[5:7] + "/" + data[8:10] #AAAA/MM/DD
        #newdata = data[8:10] + "/" + data[5:7] + "/" + data[:4]
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
                    except Error as e:
                        QMessageBox.information(self, "Info", "Erro ao Realizar a Venda")
                        print(e)
                self.tableWidget.clearContents()
                QMessageBox.information(self, "Info", "Venda Realizada com Sucesso")

class WorkedThread(QThread):
    update_archive = pyqtSignal(str)
    def run(self):
        print("dentro da thread")
        a = ""
        while (a == ""):
            arq = open("arqtemp.txt", "r")
            a = arq.read()
            a = str(a)
            arq.close()
            time.sleep(.15)
        self.update_archive.emit(a)
        pass

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = Venda()
    sys.exit(app.exec_())
