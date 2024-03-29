import sys,os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from datetime import datetime
import alterarEstoqueCod
from produtoTela import Ui_Form
from testebancosqlite import executarSelect as sel
from testebancosqlite import conexaoBanco as conexao
from sqlite3 import Error
from tkinter import *
import buscarProdCod
prodid = "0"

class ProdCad(qtw.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        #tabwidget.setCurrentWidget(tabwidget.findChild(QWidget, tabname))
        #self.ui = Ui_Form()  ### Para não usar o .ui tem que declarar o 'Ui_Form' no parametro da classe
        #self.ui.setupUi(self)       self.setupUi(self)
        self.setupUi(self)
        global flag
        flag = "0"
        #self.primeiro.clicked.connect(self.)
        self.primeiro.clicked.connect(self.primeiroItem)
        self.anterior.clicked.connect(self.anteriorItem)
        self.proximo.clicked.connect(self.proximoItem)
        self.ultimo.clicked.connect(self.ultimoItem)
        self.editar.clicked.connect(self.liberarCampos)
        self.codigo.editingFinished.connect(self.buscarCod)
        self.novo.clicked.connect(self.newProd)
        self.salvar.clicked.connect(self.addProd)
        self.voltarTela.clicked.connect(self.fecharTela)
        self.estoque.clicked.connect(self.altestoque)
        self.lucro.editingFinished.connect(self.calcularporcentagem)
        self.cancelar.close()
        self.cancelar.clicked.connect(self.cancel)
        self.buscar.clicked.connect(self.buscarProdTab)
        #self.codigo.bind("<Return>", self.buscarProduto)
        # Your code ends here
        self.show()

    def liberarCampos(self):
        msg = "Deseja Mesmo Alterar o Produto?"
        title = "Alterar Produto"
        valor = self.messagebox(msg, title)
        if valor == QMessageBox.Ok:
            self.habilitarCampos()
            self.codigo.setEnabled(False)
            self.cancelar.show()

    def buscarProdTab(self):
        self.buscar = buscarProdCod.buscarProd()

    def calcularporcentagem(self):
        lucro = self.lucro.text()
        precocusto = self.precocusto.text()
        if((lucro and precocusto != '')):
            if(lucro and precocusto != '0'):
                total = (float(precocusto) + (float(precocusto) * float(lucro) / 100))
                self.precofinal.setText(str(total))

    def teste(self):
        sq = " SELECT * FROM produtos"
        a = sel(sq)
        print(a)

    def fecharTela(self):
        self.close()

    def messagebox(self, msg, title):
        msgBox = QMessageBox()
        msgBox.setText(msg)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        value = msgBox.exec()
        return value

    def addProd(self): #Adiciona o produto no Banco de Dados
            validador = self.codigo.text()
            if(validador == ''):
                ##### Pegar Campos #############
                descricao = self.descricao.text()
                codBarras = self.codBarras.text()
                undMedida = self.undMedida.currentText()
                classe = self.classe.currentText()
                precocusto = self.precocusto.text()
                precofinal = self.precofinal.text()
                lucro = self.lucro.text()
                if (precofinal and precocusto != ""):
                    lucro = (float(precofinal) / float(precocusto) - 1) * 100
                    print (lucro)
                setor = self.setor.currentText()
                dtCad = self.dtCad.text()

                if (descricao != ""):
                    try:
                        con = conexao()
                        c = con.cursor()
                        c.execute("INSERT INTO produtos (prod_desc, prod_cod, prod_med, prod_classe, prod_custo, prod_preco, prod_lucro, prod_setor, prod_dtcad) VALUES (?,?,?,?,?,?,?,?,?)",
                                  (descricao, codBarras, undMedida, classe, precocusto, precofinal, lucro, setor, dtCad))
                        con.commit()
                        c.close()
                        QMessageBox.information(self, "Info", "Produto Adicionado com Sucesso")
                    except Error as e:
                        print(e)
                else:
                    QMessageBox.information(self, "Info", "Preencher Campos Obrigatórios")
            else:
                self.editProduto() ######### se tiver um produto selecionado, chama editProduto

    def editProduto(self):
        msg = "Confirma as alterações no Produto?"
        title = "Alterar Produto"
        valor = self.messagebox(msg, title)
        if valor == QMessageBox.Ok:
            ##### Pegar Campos #############
            prodId = self.codigo.text()
            descricao = self.descricao.text()
            codBarras = self.codBarras.text()
            undMedida = self.undMedida.currentText()
            classe = self.classe.currentText()
            precocusto = self.precocusto.text()
            precofinal = self.precofinal.text()
            lucro = self.lucro.text()
            if (precofinal and precocusto != ""):
                lucro = (float(precofinal) / float(precocusto) - 1) * 100
                print(lucro)
            setor = self.setor.currentText()
            dtCad = self.dtCad.text()

            if (descricao != ""):
                try:
                    con = conexao()
                    c = con.cursor()
                    c.execute(" UPDATE produtos SET prod_desc = (?), prod_cod = (?), prod_med = (?), prod_classe = (?), prod_custo = (?), prod_preco = (?), prod_lucro = (?), prod_setor = (?), prod_dtcad = (?) WHERE prod_id = (?)",
                              (descricao, codBarras, undMedida, classe, precocusto, precofinal, lucro, setor, dtCad, prodId))
                    con.commit()
                    c.close()
                    QMessageBox.information(self, "Info", "Produto Alterado com Sucesso")
                except Error as e:
                    print(e)
            else:
                QMessageBox.information(self, "Info", "Preencher Campos Obrigatórios")

    def cancel(self):
        self.newProd()
        self.codigo.setEnabled(True)

    def buscarCod(self): ####### pega o codigo e chama buscar produto
        cod = self.codigo.text()
        global prodid
        if(cod == ""):
            cod = prodid
        self.buscarProduto(cod)

    @staticmethod
    def buscarCodPesq(cod): ####### pega o codigo de buscarProdCod e coloca no campo
        global prodid
        prodid = cod
        self.ProdCad.buscarCod()

    def buscarProduto(self, codigo):
        try:
            global prodid
            prodid = codigo
            con = conexao()
            c = con.cursor()
            c.execute(" SELECT * FROM produtos where prod_id = (?)", (codigo,))
            con.commit()
            resultado = c.fetchall()
            c.close()

            ############## Recebendo Valores ######################
            undMedida = resultado[0][3]
            classe = resultado[0][4]
            setor = resultado[0][7]
            if (undMedida != ""):  ########### Setando o valor da Medida
                if (undMedida == "Unidade"):
                    undMedida = "0"
                elif (undMedida == "Caixa"):
                    undMedida = "1"
                elif (undMedida == "Peça"):
                    undMedida = "2"
                elif (undMedida == "Conjunto"):
                    undMedida = "3"
                else:
                    undMedida = "0"
                self.undMedida.setCurrentIndex(int(undMedida))

            if (classe != ""):  ########### Setando o valor da Classe
                if (classe == "Diverso"):
                    classe = "0"
                elif (classe == "Roupa"):
                    classe = "1"
                elif (classe == "Calçado"):
                    classe = "2"
                else:
                    classe = "0"
                self.classe.setCurrentIndex(int(classe))

            if (setor != ""):  ########### Setando o valor do setor
                if (setor == "Masculino"):
                    setor = "0"
                elif (setor == "Feminino"):
                    setor = "1"
                elif (setor == "Infantil"):
                    setor = "2"
                elif (setor == "Calçado"):
                    setor = "3"
                else:
                    setor = "0"
                self.setor.setCurrentIndex(int(setor))

            dtCad = resultado[0][8]
            print(dtCad)
            if (dtCad != ""):
                data = datetime.strptime(dtCad, '%d/%m/%Y')
            else:
                data = datetime.today()

            ############# Inserindo valores nos Campos ############
            self.descricao.setText(str(resultado[0][1]))
            self.codBarras.setText(str(resultado[0][2]))
            self.precocusto.setText(str(resultado[0][5]))
            self.precofinal.setText(str(resultado[0][6]))
            self.dtCad.setDate(data)
            self.lucro.setText(str(resultado[0][9]))
        except Error as e:
            print(e)
            return e
        pass

        ##################### Desabilitando os Campos para Edição #####################
        self.undMedida.setEnabled(False)
        self.classe.setEnabled(False)
        self.setor.setEnabled(False)
        self.descricao.setEnabled(False)
        self.codBarras.setEnabled(False)
        self.precocusto.setEnabled(False)
        self.precofinal.setEnabled(False)
        self.dtCad.setEnabled(False)
        self.lucro.setEnabled(False)

    def habilitarCampos(self):
        ##################### Habilitando os Campos para Edição #####################
        self.undMedida.setEnabled(True)
        self.classe.setEnabled(True)
        self.setor.setEnabled(True)
        self.descricao.setEnabled(True)
        self.codBarras.setEnabled(True)
        self.precocusto.setEnabled(True)
        self.precofinal.setEnabled(True)
        self.dtCad.setEnabled(True)
        self.lucro.setEnabled(True)

    def newProd(self):
        data = datetime.today()
        self.dtCad.setDate(data)
        self.descricao.setText("")
        self.codBarras.setText("")
        self.precocusto.setText("")
        self.precofinal.setText("")
        self.lucro.setText("")
        self.codigo.setText("")
        self.habilitarCampos()
        self.codigo.setEnabled(False)


    def altestoque(self):
        msg = "Deseja Mesmo Alterar o Estoque?"
        title = "Alterar Estoque"
        valor = self.messagebox(msg,title)
        if valor== QMessageBox.Ok:
            self.newproduto = alterarEstoqueCod.TelaEstoque()


    def retornarProdId(self):
        global prodid
        id = prodid
        return id

    def ultimoItem(self):
        try:
            con = conexao()
            c = con.cursor()
            c.execute(" SELECT * FROM produtos order by prod_id DESC")
            con.commit()
            resultado = c.fetchall()
            c.close()
            self.codigo.setText(str(resultado[0][0]))
            self.buscarCod()
        except Exception as e:
            print(e)
        pass

    def primeiroItem(self):
        try:
            con = conexao()
            c = con.cursor()
            c.execute(" SELECT * FROM produtos")
            con.commit()
            resultado = c.fetchone()
            c.close()
            self.codigo.setText(str(resultado[0]))
            self.buscarCod()
        except Exception as e:
            print(e)
        pass

    def proximoItem(self):
        try:
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
        resultado = self.codigo.text()
        if (resultado == ""):
            resultado = 0
        resultado = int(resultado)
        if(resultado < ultimo):
            resultado = int(resultado) + 1
            self.codigo.setText(str(resultado))
            self.buscarCod()
        else:
            QMessageBox.information(self, "Info", "Produto Não Localizado")



    def anteriorItem(self):
        resultado = self.codigo.text()
        if (resultado == ""):
            resultado = 1
        resultado = int(resultado)
        if (resultado > 1):
            resultado = resultado - 1
            self.codigo.setText(str(resultado))
            self.buscarCod()
        else:
            QMessageBox.information(self, "Info", "Produto Não Localizado")

"""
class TelaEstoque(qtw.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_AlterarEstoque
        self.ui.setupUi(self)
    def mudaJanela(self):
        self.tela = TelaEstoque()
        self.tela.show()
"""

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = ProdCad()
    sys.exit(app.exec_())
