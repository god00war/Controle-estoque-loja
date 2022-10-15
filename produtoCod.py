import sys,os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets as qtw
from PyQt5.QtCore import *
from datetime import datetime
import alterarEstoqueCod
from produtoTela import Ui_Form
from testebancosqlite import executarSelect as sel
from testebancosqlite import conexaoBanco as conexao
from sqlite3 import Error
import time
import asyncio
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
        #self.primeiro.clicked.connect(self.)
        self.primeiro.clicked.connect(self.primeiroItem)
        self.anterior.clicked.connect(self.anteriorItem)
        self.proximo.clicked.connect(self.proximoItem)
        self.excluir.clicked.connect(self.teste)
        self.ultimo.clicked.connect(self.ultimoItem)
        self.editar.clicked.connect(self.liberarCampos)
        #self.codigo.editingFinished.connect(self.buscarCod)
        self.novo.clicked.connect(self.newProd)
        self.salvar.clicked.connect(self.addProd)
        self.voltarTela.clicked.connect(self.fecharTela)
        self.estoque.clicked.connect(self.altestoque)
        self.gerarCod.clicked.connect(self.codigobarra)
        self.lucro.editingFinished.connect(self.calcularporcentagem)
        self.cancelar.close()
        self.cancelar.clicked.connect(self.cancel)
        self.buscar.clicked.connect(self.buscarProdTab)
        self.codigo.returnPressed.connect(self.buscarCod)
        #self.codigo.bind("<Return>", self.buscarProduto)
        # Your code ends here
        with open("arqtemp.txt", "w") as arquivo: #Limpar arquivo
            a = arquivo.write("")
        self.show()

    def liberarCampos(self):
        msg = "Deseja Mesmo Alterar o Produto?"
        title = "Alterar Produto"
        valor = self.messagebox(msg, title)
        if valor == QMessageBox.Ok:
            self.editarCampos(True)

    def buscarCod(self):  ####### pega o codigo e chama buscar produto
        cod = self.codigo.text()
        if (cod != ''):
            self.buscarProduto(cod)


    def buscarProdTab(self): #chama tela de pesquisar produto
        self.busc =  buscarProdCod.buscarProd()
        self.worker = WorkedThread()
        self.worker.start()
        self.worker.update_archive.connect(self.buscarProduto)

    def codigobarra(self):
        a = self.codBarras.text()
        if(a[0] != "9"):
            a = '{:9>12}'.format(a)
            self.codBarras.setText(a)
        else:
            a = '{:8>12}'.format(a)
            self.codBarras.setText(a)

    def calcularporcentagem(self):
        lucro = self.lucro.text()
        precocusto = self.precocusto.text()
        if((lucro and precocusto != '')):
            if(lucro and precocusto != '0'):
                print(lucro)
                print(precocusto)
                lucro = lucro.replace(",", ".")  # substituindo "," por"."
                precocusto = precocusto.replace(",", ".")  # substituindo "," por"."
                print(lucro)
                print(precocusto)
                total = (float(precocusto) + (float(precocusto) * float(lucro) / 100))
                total = self.truncate(total,2)
                self.precofinal.setText(str(total))

    def teste(self):
        data = datetime.today()
        print(data)

    @staticmethod
    def truncate(num, n): #truncar float (Omitir N digitos depois da virgula)
        temp = str(num)
        for x in range(len(temp)):
            if temp[x] == '.':
                try:
                    return float(temp[:x + n + 1])
                except:
                    return float(temp)
        return float(temp)

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
        self.gerarCod.close()

        if(validador == ''): #se codigo está vazio
            ##### Pegar Campos #############
            descricao = self.descricao.text()
            codBarras = self.codBarras.text()
            undMedida = self.undMedida.currentText()
            classe = self.classe.currentText()
            precocusto = self.precocusto.text()
            precofinal = self.precofinal.text()
            setor = self.setor.currentText()
            dtCad = self.dtCad.text()
            if (precofinal and precocusto != ""): #calculando a porcentagem de lucro
                precofinal = precofinal.replace(",", ".")  # substituindo "," por"."
                precocusto = precocusto.replace(",", ".")  # substituindo "," por"."
                lucro = (((float(precofinal) - float(precocusto)) / float(precocusto) ) * 100) #variação percentual
                lucro = self.truncate(float(lucro), 2) #truncar 2 casas decimais

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
        flag= ""

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
            setor = self.setor.currentText()
            dtCad = self.dtCad.text()

            if (precofinal and precocusto != ""):
                precocusto = precocusto.replace(",",".") #substituindo "," por"."
                precofinal = precofinal.replace(",",".") #substituindo "," por"."
                lucro = (float(precofinal) / float(precocusto) - 1) * 100 #string to float
                lucro = self.truncate(lucro,2) #truncar 2 casas decimais

            try: # confere se tem algum cod de barras igual já cadastrado
                con = conexao()
                c = con.cursor()
                c.execute(" SELECT * FROM produtos where prod_cod like (?)", (codBarras,))
                con.commit()
                a = c.fetchone()
                if(a != None):
                    flag = str(a[0])
                c.close()
            except Error as e:
                print(e)

            if(flag == "" or flag == prodId): # se não tem nenhum codigo de barras igual / se o codigo de barras é do próprio produto
                if (descricao != ""):
                    try:
                        con = conexao()
                        c = con.cursor()
                        c.execute(" UPDATE produtos SET prod_desc = (?), prod_cod = (?), prod_med = (?), prod_classe = (?), prod_custo = (?), prod_preco = (?), prod_lucro = (?), prod_setor = (?), prod_dtcad = (?) WHERE prod_id = (?)",
                                  (descricao, codBarras, undMedida, classe, precocusto, precofinal, lucro, setor, dtCad, prodId))
                        con.commit()
                        c.close()
                        self.editarCampos(False)
                        QMessageBox.information(self, "Info", "Produto Alterado com Sucesso")
                    except Error as e:
                        print(e)
                else:
                    QMessageBox.information(self, "Info", "Preencher Campos Obrigatórios")
            else:
                QMessageBox.information(self, "Info", "Código de Barras já Existente")

    def cancel(self):
        msg = "Deseja Cancelar as Alterações?"
        title = "Cancelar Alterações"
        valor = self.messagebox(msg, title)
        if valor == QMessageBox.Ok:
            self.newProd()
            self.editarCampos(False)

    def buscarProduto(self, codigo): #busca produto e preenche campos
        if (codigo != ''):
            print("Buscar Produto")
            self.codigo.setText(str(codigo))
            try:
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
                precocusto = "{:.2f}".format(float(resultado[0][5])) # colocar 2 zeros depois da virgula
                precofinal = "{:.2f}".format(float(resultado[0][6])) # colocar 2 zeros depois da virgula

                ############# Inserindo valores nos Campos ############
                self.descricao.setText(str(resultado[0][1]))
                self.codBarras.setText(str(resultado[0][2]))
                self.precocusto.setText(str(precocusto))
                self.precofinal.setText(str(precofinal))
                self.dtCad.setDate(data)
                self.lucro.setText(str(resultado[0][9]))
                self.editarCampos(False)
                with open("arqtemp.txt", "w") as arquivo:  # Limpar arquivo
                    arquivo.write("")
                    arquivo.close()
            except Error as e:
                print(e)
                return e
            pass
        else:
            QMessageBox.information(self, "Info", "Código Não Encontrado")
    def editarCampos(self, campos):  # Habilitar ou desabilitar campos para a edição
        valor = bool(campos)
        ##################### Campos para Edição #####################
        self.undMedida.setEnabled(valor)
        self.classe.setEnabled(valor)
        self.setor.setEnabled(valor)
        self.descricao.setEnabled(valor)
        self.codBarras.setEnabled(valor)
        self.precocusto.setEnabled(valor)
        self.precofinal.setEnabled(valor)
        self.dtCad.setEnabled(valor)
        self.lucro.setEnabled(valor)
        self.codAd.setEnabled(valor)
        if (campos == False):
            self.codigo.setEnabled(True)
            self.cancelar.close()
            self.excluir.close()
            self.gerarCod.close()
            self.salvar.close()
            self.editar.show()
        else:
            self.codigo.setEnabled(False)
            self.cancelar.show()
            self.excluir.close()
            self.gerarCod.show()
            self.salvar.show()
            self.editar.close()

    def newProd(self): #limpa os campos e libera a edição
        data = datetime.today()
        self.dtCad.setDate(data)
        self.descricao.setText("")
        self.codBarras.setText("")
        self.precocusto.setText("")
        self.precofinal.setText("")
        self.lucro.setText("")
        self.codigo.setText("")
        self.editarCampos(True)

    def altestoque(self):
        msg = "Deseja Mesmo Alterar o Estoque?"
        title = "Alterar Estoque"
        valor = self.messagebox(msg,title)
        if valor== QMessageBox.Ok:
            item = self.codigo.text()
            arquivo = open("arqtemp.txt", "w")
            arquivo.write(item)
            arquivo.close()
            self.newproduto = alterarEstoqueCod.TelaEstoque()

    def ultimoItem(self):
        self.editarCampos(False) #desativa edição dos campos
        try:
            con = conexao()
            c = con.cursor()
            c.execute(" SELECT * FROM produtos order by prod_id DESC")
            con.commit()
            resultado = c.fetchall()
            c.close()
            self.buscarProduto((resultado[0][0]))
        except Exception as e:
            print(e)
        pass

    def primeiroItem(self):
        self.editarCampos(False) #desativa edição dos campos
        try:
            con = conexao()
            c = con.cursor()
            c.execute(" SELECT * FROM produtos")
            con.commit()
            resultado = c.fetchone()
            c.close()
            self.buscarProduto(resultado[0])
        except Exception as e:
            print(e)
        pass

    def proximoItem(self):
        self.editarCampos(False) #desativa edição dos campos
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
            self.buscarProduto(resultado)
        else:
            QMessageBox.information(self, "Info", "Produto Não Localizado")

    def anteriorItem(self):
        self.editarCampos(False) #desativa edição dos campos
        resultado = self.codigo.text()
        if (resultado == ""):
            resultado = 1
        resultado = int(resultado)
        if (resultado > 1):
            resultado = resultado - 1
            self.buscarProduto(resultado)
        else:
            QMessageBox.information(self, "Info", "Produto Não Localizado")


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
    w = ProdCad()
    sys.exit(app.exec_())
