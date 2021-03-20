import sys,os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import clienteTela
from PIL import Image
from clienteTela import Ui_Form
import fdb
import pandas as pd
import locale
import datetime as dt
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
        locale.setlocale(locale.LC_ALL, '')  # Define o local
        #index = self.tabwidget.indexOf(0)
        #self.setCurrentIndex(0)
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
        dtCad = dtCad.replace('/','.')
        print(dtCad)




    def addCliente(self): #Adiciona o cliente no Banco de Dados
            global defaultImg # Define uma variavel para a imagem do cliente

            ##### Dados Pessoais #############
            dtCad = self.dtCad.text()
            dtCad = dtCad.replace('/', '.') #Troca '/' por '.'
            name = self.nome.text()
            nameFan = self.nomeFan.text()
            dtNasc = self.dtNasc.text()
            dtNasc = dtNasc.replace('/', '.')
            rg = self.rg.text()
            dtemiss = self.dateEdit.text()
            dtemiss = dtemiss.replace('/', '.')
            cpf = self.cpf.text()
            sexo = self.sexo.currentText()
            cnpj = self.cnpj.text()
            ie = self.le.text()
            obser = self.obs.toPlainText()
            #print(dtemiss)
            cliTel = self.telefone.text()
            cliCel = self.celular_2.text()
            empresa = self.empresa.text()
            empTel = self.telEmp.text()
            profissao = self.profissao.text()
            salario = self.salario.text()
            estCivil = self.estCivil.text()
            outR = self.outrasRendas.text()
            #locale.setlocale(locale.LC_ALL, '')  # Define o local
            #outRen = locale.atof(outR, float)
            #outrasR = '24141,41'
            #print(outrasR)
            #outR = outRen.astype(float)
            #outR = pd.read_csv(outRen, delimiter=";", decimal=",")
            #outR = locale.atof(outrasR,float) #Troca o float para o padrao local
            #outR = '{:,2f}'.format(outRen)
           # print(outR)



            ###### Endereço ########################
            end = self.end.text()
            end = str(end)
            print(end)
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
            if (salario != ""):
                salario = salario.replace(',', '.')
            if (limite != ""):
                limite = limite.replace(',', '.')

            if (name and end != ""):
                try:
                    con = fdb.connect(
                        host="localhost", database="C:/Users/God War/Documents/TCC/Banco de dados/gino14.FDB",
                        user='sysdba',
                        password='masterkey'
                    )

                    cur = con.cursor()
                    cur.execute(
                        "INSERT INTO T001_CLIENTE (T001_DT_CADASTRO, T001_CA_NOME, T001_CA_NOME_FANTASIA, T001_DT_NASCIMENTO, T001_CA_RG, T001_DT_EMISSAO_RG, T001_CA_CPF, T001_CA_SEXO, T001_CA_CNPJ, T001_CA_IE, T001_CA_OBS, T001_CA_TELEFONE, T001_CA_CELULAR, T001_CA_EMPRESA, T001_CA_TEL_EMPRESA, T001_CA_PROFISSAO, T001_CA_ESTADO_CIVIL, T001_NR_SALARIO, T001_CA_ENDERECO) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (dtCad, name, nameFan, dtNasc, rg, dtemiss, cpf, sexo, cnpj, ie, obser, cliTel, cliCel, empresa, empTel, profissao, estCivil, salario, end))
                    con.commit()
                    QMessageBox.information(self, "Info", "Cliente Adicionado com Sucesso")
                    con.close
                except Exception as e: print(e)
                    #QMessageBox.information(self, "Info", "Erro ao Adicionar Cliente")
                pass
            else:
                QMessageBox.information(self, "Info", "Preencher Campos Obrigatórios")


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = ClienteLogin()
    sys.exit(app.exec_())
