import sys,os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import clienteTela
from PIL import Image
from clienteTela import Ui_Form
from testebancosqlite import executarSelect as sel
from testebancosqlite import conexaoBanco as conexao
from sqlite3 import Error
defaultImg ="product.png"
# testando git hub
class ClienteLogin(qtw.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        #tabwidget.setCurrentWidget(tabwidget.findChild(QWidget, tabname))
        #self.ui = Ui_Form()  ### Para não usar o .ui tem que declarar o 'Ui_Form' no parametro da classe
        #self.ui.setupUi(self)       self.setupUi(self)
        self.setupUi(self)
        self.primeiro.clicked.connect(self.addCliente)
        self.pushButton.clicked.connect(self.uploadImg)
        self.ultimo.clicked.connect(self.teste)
        # Your code ends here
        self.show()


    def uploadImg(self): # Abre os arquivos para procurar a imagem e a salva na pasta
        global defaultImg
        size = (256, 256)
        self.filename, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image Files (*.jpg *.png)")
        if ok:
            print(self.filename)
            defaultImg = os.path.basename(self.filename)
            print(defaultImg)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save("img/{0}".format(defaultImg))

    def teste(self):
        name = self.nome.text()
        dtCad = self.dtCad.text()
        print(dtCad)




    def addCliente(self): #Adiciona o cliente no Banco de Dados
            global defaultImg # Define uma variavel para a imagem do cliente

            ##### Dados Pessoais #############
            dtCad = self.dtCad.text()
            name = self.nome.text()
            nameFan = self.nomeFan.text()
            dtNasc = self.dtNasc.text()
            rg = self.rg.text()
            dtemiss = self.dateEdit.text()
            cpf = self.cpf.text()
            sexo = self.sexo.currentText()
            cnpj = self.cnpj.text()
            ie = self.le.text()
            obser = self.obs.toPlainText()
            cliTel = self.telefone.text()
            cliCel = self.celular_2.text()
            empresa = self.empresa.text()
            empTel = self.telEmp.text()
            profissao = self.profissao.text()
            salario = self.salario.text()
            estCivil = self.estCivil.text()
            outR = self.outrasRendas.text()

            ###### Endereço ########################
            end = self.end.text()
            numCasa = self.numero.text()
            comp = self.complemento.text()
            cep = self.cep.text()
            bairro = self.bairro.text()

            ###### Referência/ Limite ##############
            ref1 = self.ref1.text()
            tel1 = self.tel1.text()
            ref2 = self.ref2.text()
            tel2 = self.tel2.text()
            ref3 = self.ref3.text()
            tel3 = self.tel3.text()
            limite = self.limite.text()

            if (name and cpf != ""):
                try:
                    con = conexao()
                    c = con.cursor()
                    c.execute(
                        """INSERT INTO clientes (cli_nome, cli_nomefan, cli_dtnasc, cli_rg, cli_cpf, cli_sexo, cli_obs, cli_emprego, cli_empresa, cli_empresacel, cli_salario, cli_estadocivil, cli_outrasrendas, cli_cel, cli_tel) 
                           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                           (name, nameFan, dtNasc, rg, cpf, sexo, obser, profissao, empresa, empTel, salario, estCivil, outR, cliCel, cliTel))
                    con.commit()
                    c.close()
                    QMessageBox.information(self, "Info", "Cliente Adicionado com Sucesso")
                except Error as e:
                    print(e)
                    QMessageBox.information(self, "Info", "Erro ao adicionar Cliente")
            else:
                QMessageBox.information(self, "Info", "Preencher Campos Obrigatórios")


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = ClienteLogin()
    sys.exit(app.exec_())
