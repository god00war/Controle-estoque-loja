from functools import partial

import produtoCod
from PyQt5.QtWidgets import *
import sys,os
from PyQt5 import QtWidgets as qtw
from buscarCliTela import Ui_Form
from testebancosqlite import executarSelect as sel
from testebancosqlite import conexaoBanco as conexao
from sqlite3 import Error
from PyQt5 import QtCore

from datetime import datetime
import main


class buscarCli(qtw.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        a = ''
        self.setupUi(self)
        self.tableprod.setColumnWidth(0,150) #### Setar o tamanho da coluna
        self.pesqnome.clicked.connect(self.buscarCliNome)
        self.tableprod.cellDoubleClicked.connect(self.on_click)

        self.show()

    def fecharTela(self):
        self.close()

    @QtCore.pyqtSlot(int, int)  ###### obtendo o item clicado da tabela
    def on_click(self, row):
        item = self.tableprod.item(row, 0)
        item = item.text()
        print(item)
        arquivo =open("arqtemp.txt","w")
        arquivo.write(item)
        arquivo.close()
        self.fecharTela()

    def verificarOrdem(self):
        nomecresc = self.nomecresc.isChecked()
        nomedecres = self.nomedecres.isChecked()


        if (nomecresc == True):
            return 1
        elif (nomedecres == True):
            return 2
        else:
            return 1

    def buscarCliNome(self): #Buscar Cliente pelo Nome
        ordem = self.verificarOrdem()
        nome = self.nome.text()
        if (nome != ""):
            nome = nome + "%"
        else:
            nome = self.contem.text()
            nome = "%" + nome + "%"
        rowcount = 0
        if (ordem == 1):
            try:
                con = conexao()
                c = con.cursor()
                c.execute(
                    " SELECT cli_id, cli_nome, cli_cpf, cli_cel FROM clientes where cli_nome like (?) order by cli_nome",
                    (nome,))
                con.commit()
                resultado = c.fetchall()
                c.close()
                print(resultado)
                flag = "0"
            except Error as e:
                print(e)
                flag = "1"
            pass
        elif (ordem == 2):
            try:
                con = conexao()
                c = con.cursor()
                c.execute(
                    " SELECT cli_id, cli_nome, cli_cpf, cli_cel FROM clientes where cli_nome like (?) order by cli_nome DESC",
                    (nome,))
                con.commit()
                resultado = c.fetchall()
                c.close()
                print(resultado)
                flag = "0"
            except Error as e:
                print(e)
                flag = "1"
            pass

        if (flag == "0"):
            self.tableprod.setRowCount(len(resultado))
            for row in range(len(resultado)):
                self.tableprod.setItem(row, 0, QTableWidgetItem(str(resultado[row][0])))
                self.tableprod.setItem(row, 1, QTableWidgetItem(str(resultado[row][1])))
                self.tableprod.setItem(row, 2, QTableWidgetItem(str(resultado[row][2])))
                self.tableprod.setItem(row, 3, QTableWidgetItem(str(resultado[row][3])))
                #self.tableprod.setItem(row, 4, QTableWidgetItem(str(resultado[row][3])))
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = buscarCli()
    sys.exit(app.exec_())
