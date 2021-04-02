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
        self.salvar.clicked.connect(self.addCliente)
        self.pushButton.clicked.connect(self.uploadImg)
        self.novo.clicked.connect(self.getEstados)
        #self.ultimo.clicked.connect(self.getEstados)
        self.estado.currentIndexChanged.connect(self.getCidades)
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


    def getEstados(self):
        try:
            con = conexao()
            c = con.cursor()
            c.execute("SELECT est_nome FROM estados")
            con.commit()
            resultado = c.fetchall()
            c.close()
            flag = 0
        except Error as e:
            flag = 1
            print(e)
            QMessageBox.information(self, "Info", "Erro ao indexar Estados")
        if(flag == 0):
            self.cidade.clear()
            self.estado.addItem("Escolha um Estado!!!")
            pos_i = 0  # variável provisória de índice
            for i in range(len(resultado)):  #passar por toda lista
                self.estado.addItem(resultado[i][0])
                pos_i = i  # guardamos o índice i
            return (pos_i)  # e retornamos o índice

    def getCidades(self):
        estadoid = self.estado.currentIndex()
        estadoid = int(estadoid)
        try:
            con = conexao()
            c = con.cursor()
            c.execute("SELECT cid_nome FROM cidades where est_id = (?)", (estadoid,))
            con.commit()
            resultado = c.fetchall()
            c.close()
            flag = 0
        except Error as e:
            flag = 1
            print(e)
            QMessageBox.information(self, "Info", "Erro ao indexar Cidades")

        if (flag == 0):
            self.cidade.clear()
            self.cidade.addItem("Escolha uma Cidade!!!")
            if(estadoid > 1):
                pos_i = 0  # variável provisória de índice
                for i in range(len(resultado)):  # passar por toda lista
                    self.cidade.addItem(resultado[i][0])
                    pos_i = i  # guardamos o índice i
                return (pos_i)  # e retornamos o índice

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
            cidNome = self.cidade.currentText()
            estId = self.estado.currentIndex()

            ###### Referência/ Limite ##############
            ref1 = self.ref1.text()
            tel1 = self.tel1.text()
            ref2 = self.ref2.text()
            tel2 = self.tel2.text()
            ref3 = self.ref3.text()
            tel3 = self.tel3.text()
            limite = self.limite.text()

            if(estId and cidNome !=""): ############ Pegando o ID da cidade ###########
                try:
                    con = conexao()
                    c = con.cursor()
                    c.execute(" SELECT cid_id FROM cidades where est_id= (?) AND cid_nome like (?)",(estId,cidNome,))
                    con.commit()
                    resultado = c.fetchall()
                    cidId = resultado[0][0]
                    print(cidId)
                    c.close()
                    flag = 0
                except Error as e:
                    flag = 1
                    print(e)
            else:
                QMessageBox.information(self, "Info", "Estado ou Cidade não Preenchidos")
            if(flag == 0):
                if ((end != "")): ########### Inserindo Endereço ##################
                    try:
                        con = conexao()
                        c = con.cursor()
                        c.execute(
                            """INSERT INTO endereco (end_nome, end_num, end_comp, end_cep, end_bairro, cid_id) 
                               VALUES (?,?,?,?,?,?)""",
                               (end, numCasa, comp, cep, bairro,cidId))
                        con.commit()
                        c.close()
                        flag = 0
                    except Error as e:
                        flag = 1
                        print(e)
                else:
                    QMessageBox.information(self, "Info", "Preencher Campos Obrigatórios")
                if(flag == 0):
                    con = conexao()
                    c = con.cursor()
                    c.execute(" SELECT * FROM endereco order by end_id DESC")
                    con.commit()
                    resultado = c.fetchall()
                    endId = resultado[0][0]
                    c.close()

                    if (name and cpf != ""): ########### Inserindo Cliente ##################
                        try:
                            con = conexao()
                            c = con.cursor()
                            c.execute(
                                """INSERT INTO clientes (cli_nome, cli_nomefan, cli_dtnasc, cli_rg, cli_cpf, cli_sexo, cli_obs, cli_emprego, cli_empresa, cli_empresacel, cli_salario, cli_estadocivil, cli_outrasrendas, cli_cel, cli_tel, end_id) 
                                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                                   (name, nameFan, dtNasc, rg, cpf, sexo, obser, profissao, empresa, empTel, salario, estCivil, outR, cliCel, cliTel, endId))
                            con.commit()
                            c.close()
                            QMessageBox.information(self, "Info", "Cliente Adicionado com Sucesso")
                        except Error as e:
                            print(e)
                            QMessageBox.information(self, "Info", "Erro ao adicionar Cliente")
                    else:
                        QMessageBox.information(self, "Info", "Preencher Campos Obrigatórios")
                else:
                    QMessageBox.information(self, "Info", "Erro ao Adicionar Endereço")
            else:
                QMessageBox.information(self, "Info", "Erro ao adicionar Cliente")

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = ClienteLogin()
    sys.exit(app.exec_())
