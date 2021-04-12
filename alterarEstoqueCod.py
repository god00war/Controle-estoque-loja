import produtoCod
import sys,os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets as qtw
from estoqueTela import Ui_AlterarEstoque
from testebancosqlite import conexaoBanco as conexao


class TelaEstoque(qtw.QWidget, Ui_AlterarEstoque):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.alterar.clicked.connect(self.altEstoque)
        self.cancelar.clicked.connect(self.fecharTela)
        self.show()

    def fecharTela(self):
        self.close()

    def altEstoque(self):
        id = produtoCod.ProdCad.retornarProdId(self) ######### buscando O ultimo Id que foi selecionado
        print(id)
        quant = self.codigo.text()
        if (id !="" and id != "0"):
            try:
                con = conexao()
                c = con.cursor()
                c.execute(" UPDATE produtos SET prod_est = (?) WHERE prod_id = (?)", (quant,id))
                con.commit()
                c.close()
                QMessageBox.information(self, "Info", "Estoque alterado com Sucesso")
                self.close()
            except Exception as e:
                QMessageBox.information(self, "Info", "Erro ao alterar Estoque")
                print(e)
            pass
        else:
            QMessageBox.information(self, "Info", "Preencha o Código do Produto")

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = TelaEstoque()
    sys.exit(app.exec_())
