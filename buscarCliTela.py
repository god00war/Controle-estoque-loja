# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscarCli.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(632, 446)
        self.tableprod = QtWidgets.QTableWidget(Form)
        self.tableprod.setGeometry(QtCore.QRect(0, 150, 631, 301))
        self.tableprod.setObjectName("tableprod")
        self.tableprod.setColumnCount(4)
        self.tableprod.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableprod.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableprod.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableprod.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableprod.setHorizontalHeaderItem(3, item)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 651, 151))
        self.frame.setStyleSheet("background-color: rgb(1, 75, 98);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.contem = QtWidgets.QLineEdit(self.frame)
        self.contem.setGeometry(QtCore.QRect(80, 70, 261, 31))
        self.contem.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contem.setInputMask("")
        self.contem.setObjectName("contem")
        self.label_40 = QtWidgets.QLabel(self.frame)
        self.label_40.setGeometry(QtCore.QRect(20, 70, 61, 31))
        self.label_40.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_40.setObjectName("label_40")
        self.nome = QtWidgets.QLineEdit(self.frame)
        self.nome.setGeometry(QtCore.QRect(80, 30, 261, 31))
        self.nome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nome.setInputMask("")
        self.nome.setObjectName("nome")
        self.label_39 = QtWidgets.QLabel(self.frame)
        self.label_39.setGeometry(QtCore.QRect(30, 30, 51, 31))
        self.label_39.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_39.setObjectName("label_39")
        self.pesqnome = QtWidgets.QToolButton(self.frame)
        self.pesqnome.setGeometry(QtCore.QRect(350, 30, 31, 31))
        self.pesqnome.setStyleSheet("background-color: rgb(231, 225, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../qtdesigner/icons/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pesqnome.setIcon(icon)
        self.pesqnome.setIconSize(QtCore.QSize(25, 25))
        self.pesqnome.setObjectName("pesqnome")
        self.pesqcontem = QtWidgets.QToolButton(self.frame)
        self.pesqcontem.setGeometry(QtCore.QRect(350, 70, 31, 31))
        self.pesqcontem.setStyleSheet("background-color: rgb(231, 225, 255);")
        self.pesqcontem.setIcon(icon)
        self.pesqcontem.setIconSize(QtCore.QSize(25, 25))
        self.pesqcontem.setObjectName("pesqcontem")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(510, 10, 81, 16))
        self.label.setObjectName("label")
        self.nomecresc = QtWidgets.QRadioButton(self.frame)
        self.nomecresc.setGeometry(QtCore.QRect(510, 30, 82, 17))
        self.nomecresc.setObjectName("nomecresc")
        self.nomedecres = QtWidgets.QRadioButton(self.frame)
        self.nomedecres.setGeometry(QtCore.QRect(510, 50, 91, 17))
        self.nomedecres.setObjectName("nomedecres")
        self.cpf = QtWidgets.QLineEdit(self.frame)
        self.cpf.setGeometry(QtCore.QRect(80, 110, 261, 31))
        self.cpf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cpf.setInputMask("")
        self.cpf.setObjectName("cpf")
        self.label_41 = QtWidgets.QLabel(self.frame)
        self.label_41.setGeometry(QtCore.QRect(40, 110, 31, 31))
        self.label_41.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_41.setObjectName("label_41")
        self.pesqcpf = QtWidgets.QToolButton(self.frame)
        self.pesqcpf.setGeometry(QtCore.QRect(350, 110, 31, 31))
        self.pesqcpf.setStyleSheet("background-color: rgb(231, 225, 255);")
        self.pesqcpf.setIcon(icon)
        self.pesqcpf.setIconSize(QtCore.QSize(25, 25))
        self.pesqcpf.setObjectName("pesqcpf")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableprod.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Cod"))
        item = self.tableprod.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nome"))
        item = self.tableprod.horizontalHeaderItem(2)
        item.setText(_translate("Form", "CPF"))
        item = self.tableprod.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Número"))
        self.label_40.setText(_translate("Form", "Contém"))
        self.label_39.setText(_translate("Form", "Nome"))
        self.pesqnome.setText(_translate("Form", "Excluir"))
        self.pesqcontem.setText(_translate("Form", "Excluir"))
        self.label.setText(_translate("Form", "Ordenar Por:"))
        self.nomecresc.setText(_translate("Form", "Nome A-Z"))
        self.nomedecres.setText(_translate("Form", "Nome Z-A"))
        self.label_41.setText(_translate("Form", "CPF"))
        self.pesqcpf.setText(_translate("Form", "Excluir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
