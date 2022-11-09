import sys,os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets as qtw
from PyQt5.QtCore import *
from datetime import datetime
from caixaTela import Ui_Form
from testebancosqlite import conexaoBanco as conexao
from sqlite3 import Error
from decimal import Decimal
from tkinter import *
from PIL import Image,ImageTk
import pypdfium2 as pdfium
prodid = "0"
pastaApp = os.path.dirname(__file__)
from reportlab.platypus import Table,SimpleDocTemplate,Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

class Caixa(qtw.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.relatorio.clicked.connect(self.Relatorio)
        self.tabelabuscar.clicked.connect(self.BuscarVendas)
        self.addconta.clicked.connect(self.OpenPdf)

        self.show()

    @staticmethod
    def Getdata(int):
        data = datetime.today()
        print(data)
        if (int == 1):
            data = str(data)
            newdata = data[8:10] + "/" + data[5:7] + "/" + data[:4]  # DD/MM/AAAA
        if (int == 2):
            newdata = data  # DD/MM/AAAA
        return newdata

    def PreencherCampos(self, tab):
        rowcount = self.tableprod_2.rowCount()
        recebido = 0
        pago = 0
        print(rowcount)
        if(rowcount > 0):
            for rowcount in range(len(tab)): #### somando os valores recebidos
                varRec = self.tableprod_2.item(rowcount,3).text()
                varPag = self.tableprod_2.item(rowcount,4).text()

                recebido = Decimal(float(recebido)) + Decimal(float(varRec))
                pago = Decimal(float(pago)) + Decimal(float(varPag))

            total = Decimal(recebido) - Decimal(pago)
            recebido = "{:.2f}".format(recebido) #### Dois zeros depois da virgula
            pago = "{:.2f}".format(pago) #### Dois zeros depois da virgula
            total = "{:.2f}".format(total) #### Dois zeros depois da virgula


            self.recebido.setText(str(recebido))
            self.pago.setText(str(pago))
            self.saldoAtual.setText(str(total))



    def BuscarVendas(self):
        rowcount = 0
        dti = self.dataIncial.text()
        dtf = self.dataFinal.text()
        if (dtf == "01/01/2000"):
            a = self.Getdata(2)
            self.dataIncial.setDate(a)
            self.dataFinal.setDate(a)
            a = str(a)
            dti = a[:10]
            dtf = a[:10]
            dti = dti[:4] + "/" + dti[5:7] + "/" + dti[8:10] #AAAA/MM/DD
            dtf = dtf[:4] + "/" + dtf[5:7] + "/" + dtf[8:10] #AAAA/MM/DD
        else:
            dti = dti[6:] + "/" + dti[3:5] + "/" + dti[:2]  # AAAA/MM/DD
            dtf = dtf[6:] + "/" + dtf[3:5] + "/" + dtf[:2]  # AAAA/MM/DD

        if(dti !=""):
            try:
                con = conexao()
                c = con.cursor()
                c.execute(" SELECT * FROM vendas where  ven_data BETWEEN (?) AND (?) order by ven_data DESC", (dti, dtf))
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
            for row in range(len(resultado)):
                hora = resultado[row][4]
                data = resultado[row][4]
                valor = resultado[row][2]
                pgt = resultado[row][5]
                data = data[8:10] + "/" + data[5:7] + "/" + data[:4]  # DD/MM/AAAA
                hora = hora[11:]
                total = 10
                print(hora)
                print(data)
                print(valor)

                if (flag == "0"):

                    print(rowcount)
                    self.tableprod_2.setRowCount(rowcount + 1)
                    self.tableprod_2.setItem(rowcount, 0, QTableWidgetItem(str(data)))
                    self.tableprod_2.setItem(rowcount, 1, QTableWidgetItem(str(hora)))
                    self.tableprod_2.setItem(rowcount, 2, QTableWidgetItem(str(pgt)))
                    self.tableprod_2.setItem(rowcount, 3, QTableWidgetItem(str(valor)))
                    self.tableprod_2.setItem(rowcount, 4, QTableWidgetItem(str(total)))
                    rowcount = rowcount + 1
                else:
                    flag == "1"
                    QMessageBox.information(self, "Info", "Erro adicionar produtos")
            if (flag == "0"):
                self.PreencherCampos(resultado)

    @staticmethod
    def mp(milimetros):
        milimetros = milimetros / 0.35277
        return milimetros

    def OpenPdf(self):
        # Load a document
        filepath = "Teste.pdf"
        pdf = pdfium.PdfDocument(filepath)

        # render a single page (in this case: the first one)
        page = pdf.get_page(0)
        pil_image = page.render_to(
            pdfium.BitmapConv.pil_image,
        )
        pil_image.save("output.jpg")

        # render multiple pages concurrently (in this case: all)
        page_indices = [i for i in range(len(pdf))]
        renderer = pdf.render_to(
            pdfium.BitmapConv.pil_image,
            page_indices=page_indices,
        )
        for image, index in zip(renderer, page_indices):
            image.save("output_%02d.jpg" % index)
        ############# GUI ###########
        window = Tk()
        window.geometry("1360x750")
        frame = Frame(window, width=1360, height=750)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)

        # Create an object of tkinter ImageTk
        img = ImageTk.PhotoImage(Image.open("output.jpg"))

        # Create a Label Widget to display the text or Image
        label = Label(frame, image=img)
        label.pack()
        window.mainloop()

    def Relatorio(self):
        rowcount = 0
        dtio = self.dataIncial.text()
        dtfo = self.dataFinal.text()
        dti = dtio[6:] + "/" + dtio[3:5] + "/" + dtio[:2]  # AAAA/MM/DD
        dtf = dtfo[6:] + "/" + dtfo[3:5] + "/" + dtfo[:2]  # AAAA/MM/DD

        try:
            con = conexao()
            c = con.cursor()
            c.execute(" SELECT * FROM vendas where  ven_data BETWEEN (?) AND (?) order by ven_data DESC", (dti, dtf))
            con.commit()
            itemvenda = c.fetchall()
            c.close()
            flag = "0"
        except Error as e:
            print(e)
            flag = "1"
        pass
        print(itemvenda)
        if(flag=="0"):
            dinheiro = 0
            debito = 0
            for row in range(len(itemvenda)):
                tipopgt = itemvenda[row][5]
                valor = itemvenda[row][2]
                if(tipopgt == "Dinheiro"):
                    dinheiro = dinheiro + valor
                elif(tipopgt == "Débito"):
                    debito = debito + valor
        self.CriarPdf(itemvenda,dtio,dtfo,dinheiro,debito)

    def CriarPdf(self, nomes,dti,dtf,din,deb):
        dinheiro = str(din)
        debito = str(deb)
        credito="49.00"
        despesas="42.00"
        receitas="50.00"
        totalRecebido= Decimal(float(din)) + Decimal(float(deb)) + Decimal(float(credito)) + Decimal(float(receitas))
        totalRecebido = "{:.2f}".format(totalRecebido)  #### Dois zeros depois da virgula
        totalRecebido = str(totalRecebido)
        saldoAtual = Decimal(float(totalRecebido)) - Decimal(float(despesas))
        saldoAtual = "{:.2f}".format(saldoAtual)  #### Dois zeros depois da virgula
        saldoAtual = str(saldoAtual)
        #nome = nomes
        # nomes = [('cuzinho'), 'cu cuzao', 'cuzada violenta']
        eixo = 100
        data = [['DATA',"HISTÓRICO","RECEBIDO","PAGO"],
                [""+dtf+"",'VENDAS EM DINHEIRO:',""+dinheiro+"","00.00"],
                [""+dtf+"",'VENDAS NO DÉBITO',""+debito+"","00.00"],
                [""+dtf+"",'VENDAS NO CRÉDITO',""+credito+"","00.00"],
                [""+dtf+"",'DESPESAS','00.00',""+despesas+""],
                [""+dtf+"",'OUTRAS RECEITAS',""+receitas+"","00.00"],
                ["TOTAL RECEBIDO",""+totalRecebido+"","TOTAL PAGO",""+despesas+""],
                ["",'',"SALDO ATUAL",""+saldoAtual+""]]

        pdf = SimpleDocTemplate("Teste.pdf")
        flow_obj = []
        styles = getSampleStyleSheet()
        tstyle = TableStyle([('BOX', (0,0), (-1,-1), 0.25, colors.black),# espessura linhas externa
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),# espessura linhas interna
                       ('ALIGN',(1,1),(-3,-3),'LEFT'),
                       ('TOPPADDING', (0, 0), (-1, -1),5),
                       ('BOTTOMPADDING', (0, 0), (-1, -1),5),
                       ('FONTSIZE',(0,0),(-1,-1),15),
                       ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                       ('TEXTCOLOR',(0,0),(1,-1),colors.black),])
        print(data)
        t = Table(data)
        print(t)
        t.setStyle(tstyle)

        style = ParagraphStyle('heading1',
                                fontName='Helvetica-Bold',
                                fontSize=20,
                                textColor=colors.black,
                                spaceBefore=5,
                                spaceAfter=20,
                                leading=20)

        flow_obj.append(Paragraph('RELATÓRIO FECHAMENTO DE CAIXA', style))
        flow_obj.append(Paragraph('CONTA: ', style))
        flow_obj.append(Paragraph('PERIODO DE '+dti+" A "+dtf+"", style))

        flow_obj.append(t)  # adiciona a tabela à variavel elements

        pdf.build(flow_obj)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = Caixa()
    sys.exit(app.exec_())
