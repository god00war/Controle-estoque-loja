# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'produto.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(593, 402)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 611, 51))
        self.frame.setStyleSheet("background-color: rgb(1, 75, 98);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.editar = QtWidgets.QToolButton(self.frame)
        self.editar.setGeometry(QtCore.QRect(20, 10, 31, 31))
        self.editar.setStyleSheet("background-color: rgb(231, 225, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../qtdesigner/icons/editfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editar.setIcon(icon)
        self.editar.setIconSize(QtCore.QSize(25, 25))
        self.editar.setObjectName("editar")
        self.excluir = QtWidgets.QToolButton(self.frame)
        self.excluir.setGeometry(QtCore.QRect(80, 10, 31, 31))
        self.excluir.setStyleSheet("background-color: rgb(231, 225, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../qtdesigner/icons/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluir.setIcon(icon1)
        self.excluir.setIconSize(QtCore.QSize(25, 25))
        self.excluir.setObjectName("excluir")
        self.buscar = QtWidgets.QToolButton(self.frame)
        self.buscar.setGeometry(QtCore.QRect(140, 10, 31, 31))
        self.buscar.setStyleSheet("background-color: rgb(231, 225, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../qtdesigner/icons/buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buscar.setIcon(icon2)
        self.buscar.setIconSize(QtCore.QSize(25, 25))
        self.buscar.setObjectName("buscar")
        self.voltarTela = QtWidgets.QToolButton(self.frame)
        self.voltarTela.setGeometry(QtCore.QRect(540, 10, 31, 31))
        self.voltarTela.setStyleSheet("background-color: rgb(231, 225, 255);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../qtdesigner/icons/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.voltarTela.setIcon(icon3)
        self.voltarTela.setIconSize(QtCore.QSize(25, 25))
        self.voltarTela.setObjectName("voltarTela")
        self.estoque = QtWidgets.QToolButton(self.frame)
        self.estoque.setGeometry(QtCore.QRect(480, 10, 31, 31))
        self.estoque.setStyleSheet("background-color: rgb(231, 225, 255);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../qtdesigner/icons/box.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.estoque.setIcon(icon4)
        self.estoque.setIconSize(QtCore.QSize(25, 25))
        self.estoque.setObjectName("estoque")
        self.salvar = QtWidgets.QToolButton(self.frame)
        self.salvar.setGeometry(QtCore.QRect(420, 10, 31, 31))
        self.salvar.setStyleSheet("background-color: rgb(231, 225, 255);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../qtdesigner/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salvar.setIcon(icon5)
        self.salvar.setIconSize(QtCore.QSize(25, 25))
        self.salvar.setObjectName("salvar")
        self.cancelar = QtWidgets.QToolButton(self.frame)
        self.cancelar.setGeometry(QtCore.QRect(200, 10, 31, 31))
        self.cancelar.setStyleSheet("background-color: rgb(231, 225, 255);")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../qtdesigner/icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar.setIcon(icon6)
        self.cancelar.setIconSize(QtCore.QSize(25, 25))
        self.cancelar.setObjectName("cancelar")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 50, 611, 51))
        self.frame_2.setStyleSheet("background-color: rgb(1, 75, 98);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.novo = QtWidgets.QToolButton(self.frame_2)
        self.novo.setGeometry(QtCore.QRect(20, 10, 31, 31))
        self.novo.setStyleSheet("background-color: rgb(231, 225, 255);")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../qtdesigner/icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.novo.setIcon(icon7)
        self.novo.setIconSize(QtCore.QSize(25, 25))
        self.novo.setObjectName("novo")
        self.label_55 = QtWidgets.QLabel(self.frame_2)
        self.label_55.setGeometry(QtCore.QRect(380, 10, 81, 21))
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.frame_2)
        self.label_56.setGeometry(QtCore.QRect(480, 10, 91, 21))
        self.label_56.setObjectName("label_56")
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 10, 95, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.label_54 = QtWidgets.QLabel(self.layoutWidget)
        self.label_54.setStyleSheet("font-color: rgb(255, 255, 255);")
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_55.addWidget(self.label_54)
        self.codigo = QtWidgets.QLineEdit(self.layoutWidget)
        self.codigo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.codigo.setObjectName("codigo")
        self.horizontalLayout_55.addWidget(self.codigo)
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(189, 10, 161, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.primeiro = QtWidgets.QToolButton(self.layoutWidget_2)
        self.primeiro.setStyleSheet("background-color: rgb(231, 225, 255);")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../qtdesigner/icons/voltatd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.primeiro.setIcon(icon8)
        self.primeiro.setIconSize(QtCore.QSize(25, 25))
        self.primeiro.setObjectName("primeiro")
        self.horizontalLayout_56.addWidget(self.primeiro)
        self.anterior = QtWidgets.QToolButton(self.layoutWidget_2)
        self.anterior.setStyleSheet("background-color: rgb(231, 225, 255);")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../qtdesigner/icons/volta1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.anterior.setIcon(icon9)
        self.anterior.setIconSize(QtCore.QSize(25, 25))
        self.anterior.setObjectName("anterior")
        self.horizontalLayout_56.addWidget(self.anterior)
        self.proximo = QtWidgets.QToolButton(self.layoutWidget_2)
        self.proximo.setStyleSheet("background-color: rgb(231, 225, 255);")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../qtdesigner/icons/avanca1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.proximo.setIcon(icon10)
        self.proximo.setIconSize(QtCore.QSize(25, 25))
        self.proximo.setObjectName("proximo")
        self.horizontalLayout_56.addWidget(self.proximo)
        self.ultimo = QtWidgets.QToolButton(self.layoutWidget_2)
        self.ultimo.setStyleSheet("background-color: rgb(231, 225, 255);")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../qtdesigner/icons/avancatd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ultimo.setIcon(icon11)
        self.ultimo.setIconSize(QtCore.QSize(25, 25))
        self.ultimo.setObjectName("ultimo")
        self.horizontalLayout_56.addWidget(self.ultimo)
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(-10, -10, 611, 20))
        self.line.setStyleSheet("color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.compra = QtWidgets.QLabel(self.frame_2)
        self.compra.setGeometry(QtCore.QRect(376, 30, 81, 16))
        self.compra.setText("")
        self.compra.setObjectName("compra")
        self.atualizacao = QtWidgets.QLabel(self.frame_2)
        self.atualizacao.setGeometry(QtCore.QRect(480, 30, 91, 16))
        self.atualizacao.setText("")
        self.atualizacao.setObjectName("atualizacao")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(0, 100, 601, 291))
        self.frame_3.setStyleSheet("background-color: rgb(231, 225, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Cadastro = QtWidgets.QTabWidget(self.frame_3)
        self.Cadastro.setGeometry(QtCore.QRect(0, 0, 601, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cadastro.sizePolicy().hasHeightForWidth())
        self.Cadastro.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Cadastro.setFont(font)
        self.Cadastro.setIconSize(QtCore.QSize(25, 25))
        self.Cadastro.setObjectName("Cadastro")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget_14 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_14.setGeometry(QtCore.QRect(10, 130, 191, 24))
        self.layoutWidget_14.setObjectName("layoutWidget_14")
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout(self.layoutWidget_14)
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.label_48 = QtWidgets.QLabel(self.layoutWidget_14)
        self.label_48.setObjectName("label_48")
        self.horizontalLayout_48.addWidget(self.label_48)
        self.precocusto = QtWidgets.QLineEdit(self.layoutWidget_14)
        self.precocusto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.precocusto.setObjectName("precocusto")
        self.horizontalLayout_48.addWidget(self.precocusto)
        self.layoutWidget_11 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_11.setGeometry(QtCore.QRect(20, 50, 521, 24))
        self.layoutWidget_11.setObjectName("layoutWidget_11")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout(self.layoutWidget_11)
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.label_45 = QtWidgets.QLabel(self.layoutWidget_11)
        self.label_45.setObjectName("label_45")
        self.horizontalLayout_45.addWidget(self.label_45)
        self.descricao = QtWidgets.QLineEdit(self.layoutWidget_11)
        self.descricao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.descricao.setInputMask("")
        self.descricao.setObjectName("descricao")
        self.horizontalLayout_45.addWidget(self.descricao)
        self.layoutWidget_7 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_7.setGeometry(QtCore.QRect(10, 90, 261, 21))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.label_41 = QtWidgets.QLabel(self.layoutWidget_7)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_41.addWidget(self.label_41)
        self.undMedida = QtWidgets.QComboBox(self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undMedida.sizePolicy().hasHeightForWidth())
        self.undMedida.setSizePolicy(sizePolicy)
        self.undMedida.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.undMedida.setObjectName("undMedida")
        self.undMedida.addItem("")
        self.undMedida.addItem("")
        self.undMedida.addItem("")
        self.undMedida.addItem("")
        self.horizontalLayout_41.addWidget(self.undMedida)
        self.layoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 10, 231, 24))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_39 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_39.addWidget(self.label_39)
        self.codBarras = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.codBarras.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.codBarras.setText("")
        self.codBarras.setObjectName("codBarras")
        self.horizontalLayout_39.addWidget(self.codBarras)
        self.layoutWidget_9 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_9.setGeometry(QtCore.QRect(350, 130, 191, 24))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_9)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.precofinal = QtWidgets.QLineEdit(self.layoutWidget_9)
        self.precofinal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.precofinal.setObjectName("precofinal")
        self.horizontalLayout_2.addWidget(self.precofinal)
        self.gerarCod = QtWidgets.QToolButton(self.tab)
        self.gerarCod.setGeometry(QtCore.QRect(250, 10, 31, 31))
        self.gerarCod.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gerarCod.setIcon(icon7)
        self.gerarCod.setIconSize(QtCore.QSize(25, 25))
        self.gerarCod.setObjectName("gerarCod")
        self.layoutWidget_8 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_8.setGeometry(QtCore.QRect(290, 90, 251, 24))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.label_49 = QtWidgets.QLabel(self.layoutWidget_8)
        self.label_49.setObjectName("label_49")
        self.horizontalLayout_52.addWidget(self.label_49)
        self.classe = QtWidgets.QComboBox(self.layoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.classe.sizePolicy().hasHeightForWidth())
        self.classe.setSizePolicy(sizePolicy)
        self.classe.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.classe.setObjectName("classe")
        self.classe.addItem("")
        self.classe.addItem("")
        self.classe.addItem("")
        self.horizontalLayout_52.addWidget(self.classe)
        self.layoutWidget_15 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_15.setGeometry(QtCore.QRect(210, 130, 127, 24))
        self.layoutWidget_15.setObjectName("layoutWidget_15")
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout(self.layoutWidget_15)
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.label_53 = QtWidgets.QLabel(self.layoutWidget_15)
        self.label_53.setObjectName("label_53")
        self.horizontalLayout_49.addWidget(self.label_53)
        self.lucro = QtWidgets.QLineEdit(self.layoutWidget_15)
        self.lucro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lucro.setObjectName("lucro")
        self.horizontalLayout_49.addWidget(self.lucro)
        self.layoutWidget_6 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_6.setGeometry(QtCore.QRect(290, 10, 251, 24))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.label_50 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_50.setObjectName("label_50")
        self.horizontalLayout_50.addWidget(self.label_50)
        self.codAd = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.codAd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.codAd.setText("")
        self.codAd.setObjectName("codAd")
        self.horizontalLayout_50.addWidget(self.codAd)
        self.layoutWidget_12 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_12.setGeometry(QtCore.QRect(20, 210, 221, 24))
        self.layoutWidget_12.setObjectName("layoutWidget_12")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout(self.layoutWidget_12)
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.label_57 = QtWidgets.QLabel(self.layoutWidget_12)
        self.label_57.setObjectName("label_57")
        self.horizontalLayout_53.addWidget(self.label_57)
        self.dtCad = QtWidgets.QDateEdit(self.layoutWidget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtCad.sizePolicy().hasHeightForWidth())
        self.dtCad.setSizePolicy(sizePolicy)
        self.dtCad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dtCad.setObjectName("dtCad")
        self.horizontalLayout_53.addWidget(self.dtCad)
        self.layoutWidget_10 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_10.setGeometry(QtCore.QRect(40, 170, 201, 24))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.label_43 = QtWidgets.QLabel(self.layoutWidget_10)
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_43.addWidget(self.label_43)
        self.setor = QtWidgets.QComboBox(self.layoutWidget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setor.sizePolicy().hasHeightForWidth())
        self.setor.setSizePolicy(sizePolicy)
        self.setor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setor.setObjectName("setor")
        self.setor.addItem("")
        self.setor.addItem("")
        self.setor.addItem("")
        self.setor.addItem("")
        self.horizontalLayout_43.addWidget(self.setor)
        self.Cadastro.addTab(self.tab, "")

        self.retranslateUi(Form)
        self.Cadastro.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.editar.setText(_translate("Form", "Edit"))
        self.excluir.setText(_translate("Form", "Excluir"))
        self.buscar.setText(_translate("Form", "Buscar"))
        self.voltarTela.setText(_translate("Form", "Voltar"))
        self.estoque.setText(_translate("Form", "Buscar"))
        self.salvar.setText(_translate("Form", "Salvar"))
        self.cancelar.setText(_translate("Form", "Buscar"))
        self.novo.setText(_translate("Form", "(+)"))
        self.label_55.setText(_translate("Form", "Ultima Compra:"))
        self.label_56.setText(_translate("Form", "Ultima Atualização:"))
        self.label_54.setText(_translate("Form", "Código"))
        self.primeiro.setText(_translate("Form", "<<"))
        self.anterior.setText(_translate("Form", "<"))
        self.proximo.setText(_translate("Form", ">"))
        self.ultimo.setText(_translate("Form", ">>"))
        self.label_48.setText(_translate("Form", "Preço Custo"))
        self.label_45.setText(_translate("Form", "Descrição"))
        self.label_41.setText(_translate("Form", "Uni. Medida"))
        self.undMedida.setItemText(0, _translate("Form", "Unidade"))
        self.undMedida.setItemText(1, _translate("Form", "Caixa"))
        self.undMedida.setItemText(2, _translate("Form", "Peça"))
        self.undMedida.setItemText(3, _translate("Form", "Conjunto"))
        self.label_39.setText(_translate("Form", "Cod. Barras"))
        self.label_2.setText(_translate("Form", "Preço Final"))
        self.gerarCod.setText(_translate("Form", "Gerar"))
        self.label_49.setText(_translate("Form", "Classe"))
        self.classe.setItemText(0, _translate("Form", "Diverso"))
        self.classe.setItemText(1, _translate("Form", "Roupa"))
        self.classe.setItemText(2, _translate("Form", "Calçado"))
        self.label_53.setText(_translate("Form", "Lucro (%)"))
        self.label_50.setText(_translate("Form", "Cod. Adicional"))
        self.label_57.setText(_translate("Form", "Data Cad."))
        self.label_43.setText(_translate("Form", "Setor"))
        self.setor.setItemText(0, _translate("Form", "Masculino"))
        self.setor.setItemText(1, _translate("Form", "Feminino"))
        self.setor.setItemText(2, _translate("Form", "Infantil"))
        self.setor.setItemText(3, _translate("Form", "Calçado"))
        self.Cadastro.setTabText(self.Cadastro.indexOf(self.tab), _translate("Form", "Cadastro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
