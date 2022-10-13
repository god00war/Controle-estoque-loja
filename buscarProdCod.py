from functools import partial

import produtoCod
from PyQt5.QtWidgets import *
import sys,os
from PyQt5 import QtWidgets as qtw
from buscarProdTela import Ui_Form
from testebancosqlite import executarSelect as sel
from testebancosqlite import conexaoBanco as conexao
from sqlite3 import Error
from PyQt5 import QtCore

from datetime import datetime
import main


class buscarProd(qtw.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        a = ''
        self.setupUi(self)
        self.tableprod.setColumnWidth(0,150) #### Setar o tamanho da coluna
        self.pesqnome.clicked.connect(self.buscarProdNome)
        self.pesqcontem.clicked.connect(self.buscarProdNome)
        self.pesqcod.clicked.connect(self.buscarProdCod)
        self.tableprod.cellDoubleClicked.connect(self.on_click)
        self.show()

    @QtCore.pyqtSlot(int, int) ###### obtendo o item clicado da tabela
    def on_click(self, row):
        item = self.tableprod.item(row, 4)
        item = item.text()
        a = item
        arquivo = open("arqtemp.txt", "w")
        arquivo.write(item)
        arquivo.close()
        self.fecharTela()

    def fecharTela(self):
        self.close()
   # def buscarCod(self): ####### pega o codigo e chama buscar produto
      #  cod = self.codigo.text()
      #  global prodid
      #  if(cod == ""):
       #     cod = prodid
    #    self.buscarProduto(cod)
    #
    #def mandarCod(self, item):
     #   cod = item
     #   print(cod)
      #  partial(self.vendaCod.buscarCodPesqV, cod ) #tentando mandar informação para vendasCod
      #  self.vendaCod.buscarCodPesqV(cod)

    def verificarOrdem(self):
        nomecresc = self.nomecresc.isChecked()
        nomedecres = self.nomedecres.isChecked()
        menorpreco = self.menorpreco.isChecked()
        maiorpreco = self.maiorpreco.isChecked()
        semestoque = self.semestoque.isChecked()


        if (nomecresc == True):
            return 1
        elif (nomedecres == True):
            return 2
        elif (menorpreco == True):
            return 3
        elif (maiorpreco == True):
            return 4
        elif (semestoque == True):
            return 5
        else:
            return 1

    def buscarProdCod(self): #Buscar Produto Pelo Codigo
        ordem = self.verificarOrdem()
        nome = self.codigo.text()
        rowcount = 0

        if(ordem == 1): #nome crescente
            try:
                con = conexao()
                c = con.cursor()
                c.execute(" SELECT prod_cod, prod_desc, prod_custo, prod_preco, prod_est, prod_id FROM produtos where prod_cod = (?) order by prod_desc", (nome,))
                con.commit()
                resultado = c.fetchall()
                c.close()
                print(resultado)
                flag = "0"
            except Error as e:
                print(e)
                flag = "1"
            pass
        elif(ordem ==2): #nome decrescente
            try:
                con = conexao()
                c = con.cursor()
                c.execute(" SELECT prod_cod, prod_desc, prod_custo, prod_preco, prod_est, prod_id FROM produtos where prod_cod = (?) order by prod_desc DESC", (nome,))
                con.commit()
                resultado = c.fetchall()
                c.close()
                print(resultado)
                flag = "0"
            except Error as e:
                print(e)
                flag = "1"
            pass
        elif (ordem == 3): #menor preco
            try:
                con = conexao()
                c = con.cursor()
                c.execute(" SELECT prod_cod, prod_desc, prod_custo, prod_preco, prod_est, prod_id FROM produtos where prod_cod = (?) order by prod_preco", (nome,))
                con.commit()
                resultado = c.fetchall()
                c.close()
                print(resultado)
                flag = "0"
            except Error as e:
                print(e)
                flag = "1"
            pass
        elif (ordem == 4): #maior preço
            try:
                con = conexao()
                c = con.cursor()
                c.execute(" SELECT prod_cod, prod_desc, prod_custo, prod_preco, prod_est, prod_id FROM produtos where prod_cod = (?) order by prod_preco DESC", (nome,))
                con.commit()
                resultado = c.fetchall()
                c.close()
                print(resultado)
                flag = "0"
            except Error as e:
                print(e)
                flag = "1"
            pass
        elif (ordem == 5): #sem estoque
            try:
                con = conexao()
                c = con.cursor()
                c.execute(" SELECT prod_cod, prod_desc, prod_custo, prod_preco, prod_est, prod_id FROM produtos where prod_cod = (?) AND prod_est = '0'", (nome,))
                con.commit()
                resultado = c.fetchall()
                c.close()
                print(resultado)
                flag = "0"
            except Error as e:
                print(e)
                flag = "1"
            pass
        else:
            print(ordem)

        if(flag == "0"):
            self.tableprod.setRowCount(len(resultado))
            for row in range(len(resultado)):
                self.tableprod.setItem(row, 0, QTableWidgetItem(str(resultado[row][0])))
                self.tableprod.setItem(row, 1, QTableWidgetItem(str(resultado[row][1])))
                self.tableprod.setItem(row, 2, QTableWidgetItem(str(resultado[row][4])))
                self.tableprod.setItem(row, 3, QTableWidgetItem(str(resultado[row][2])))
                self.tableprod.setItem(row, 4, QTableWidgetItem(str(resultado[row][3])))
                self.tableprod.setItem(row, 5, QTableWidgetItem(str(resultado[row][5]))) ############

    def buscarProdNome(self): #Buscar Produto Pelo Nome
        ordem = self.verificarOrdem()
        nome = self.nome.text()
        if(nome != ""):
            nome = nome + "%"
        else:
            nome = self.contem.text()
            nome = "%" + nome + "%"
        rowcount = 0

        if(ordem == 1):
            try:
                con = conexao()
                c = con.cursor()
                c.execute(" SELECT prod_cod, prod_desc, prod_custo, prod_preco, prod_est, prod_id FROM produtos where prod_desc like (?) order by prod_desc", (nome,))
                con.commit()
                resultado = c.fetchall()
                c.close()
                print(resultado)
                flag = "0"
            except Error as e:
                print(e)
                flag = "1"
            pass
        elif(ordem ==2):
            try:
                con = conexao()
                c = con.cursor()
                c.execute(" SELECT prod_cod, prod_desc, prod_custo, prod_preco, prod_est, prod_id FROM produtos where prod_desc like (?) order by prod_desc DESC", (nome,))
                con.commit()
                resultado = c.fetchall()
                c.close()
                print(resultado)
                flag = "0"
            except Error as e:
                print(e)
                flag = "1"
            pass
        elif (ordem == 3):
            try:
                con = conexao()
                c = con.cursor()
                c.execute(" SELECT prod_cod, prod_desc, prod_custo, prod_preco, prod_est, prod_id FROM produtos where prod_desc like (?) order by prod_preco", (nome,))
                con.commit()
                resultado = c.fetchall()
                c.close()
                print(resultado)
                flag = "0"
            except Error as e:
                print(e)
                flag = "1"
            pass
        elif (ordem == 4):
            try:
                con = conexao()
                c = con.cursor()
                c.execute(" SELECT prod_cod, prod_desc, prod_custo, prod_preco, prod_est, prod_id FROM produtos where prod_desc like (?) order by prod_preco DESC", (nome,))
                con.commit()
                resultado = c.fetchall()
                c.close()
                print(resultado)
                flag = "0"
            except Error as e:
                print(e)
                flag = "1"
            pass
        elif (ordem == 5):
            try:
                con = conexao()
                c = con.cursor()
                c.execute(" SELECT prod_cod, prod_desc, prod_custo, prod_preco, prod_est, prod_id FROM produtos where prod_desc like (?) AND prod_est = '0'", (nome,))
                con.commit()
                resultado = c.fetchall()
                c.close()
                print(resultado)
                flag = "0"
            except Error as e:
                print(e)
                flag = "1"
            pass
        else:
            print(ordem)

        if(flag == "0"):
            self.tableprod.setRowCount(len(resultado))
            for row in range(len(resultado)):
                self.tableprod.setItem(row, 0, QTableWidgetItem(str(resultado[row][0])))
                self.tableprod.setItem(row, 1, QTableWidgetItem(str(resultado[row][1])))
                self.tableprod.setItem(row, 2, QTableWidgetItem(str(resultado[row][2])))
                self.tableprod.setItem(row, 3, QTableWidgetItem(str(resultado[row][3])))
                self.tableprod.setItem(row, 4, QTableWidgetItem(str(resultado[row][5])))
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = buscarProd()
    sys.exit(app.exec_())

