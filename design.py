# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalcAndriel(object):
    def setupUi(self, CalcAndriel):
        CalcAndriel.setObjectName("CalcAndriel")
        CalcAndriel.resize(331, 546)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        CalcAndriel.setPalette(palette)
        self.visor = QtWidgets.QLabel(CalcAndriel)
        self.visor.setGeometry(QtCore.QRect(10, 80, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.visor.setFont(font)
        self.visor.setStyleSheet("background-color: rgb(140, 246, 255);\n"
"color: rgb(0, 81, 255);")
        self.visor.setText("")
        self.visor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.visor.setWordWrap(True)
        self.visor.setObjectName("visor")
        self.inversao = QtWidgets.QPushButton(CalcAndriel)
        self.inversao.setGeometry(QtCore.QRect(10, 480, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.inversao.setFont(font)
        self.inversao.setObjectName("inversao")
        self.bt0 = QtWidgets.QPushButton(CalcAndriel)
        self.bt0.setGeometry(QtCore.QRect(90, 480, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.bt0.setFont(font)
        self.bt0.setObjectName("bt0")
        self.virgula = QtWidgets.QPushButton(CalcAndriel)
        self.virgula.setGeometry(QtCore.QRect(170, 480, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.virgula.setFont(font)
        self.virgula.setObjectName("virgula")
        self.igual = QtWidgets.QPushButton(CalcAndriel)
        self.igual.setGeometry(QtCore.QRect(250, 480, 70, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.igual.setFont(font)
        self.igual.setStyleSheet("background-color: rgb(24, 85, 197);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.igual.setObjectName("igual")
        self.bt1 = QtWidgets.QPushButton(CalcAndriel)
        self.bt1.setGeometry(QtCore.QRect(10, 420, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.bt1.setFont(font)
        self.bt1.setObjectName("bt1")
        self.bt3 = QtWidgets.QPushButton(CalcAndriel)
        self.bt3.setGeometry(QtCore.QRect(170, 420, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.bt3.setFont(font)
        self.bt3.setStyleSheet("")
        self.bt3.setObjectName("bt3")
        self.bt2 = QtWidgets.QPushButton(CalcAndriel)
        self.bt2.setGeometry(QtCore.QRect(90, 420, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.bt2.setFont(font)
        self.bt2.setObjectName("bt2")
        self.soma = QtWidgets.QPushButton(CalcAndriel)
        self.soma.setGeometry(QtCore.QRect(250, 420, 70, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.soma.setFont(font)
        self.soma.setObjectName("soma")
        self.bt4 = QtWidgets.QPushButton(CalcAndriel)
        self.bt4.setGeometry(QtCore.QRect(10, 360, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.bt4.setFont(font)
        self.bt4.setObjectName("bt4")
        self.bt5 = QtWidgets.QPushButton(CalcAndriel)
        self.bt5.setGeometry(QtCore.QRect(90, 360, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.bt5.setFont(font)
        self.bt5.setObjectName("bt5")
        self.subtracao = QtWidgets.QPushButton(CalcAndriel)
        self.subtracao.setGeometry(QtCore.QRect(250, 360, 70, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.subtracao.setFont(font)
        self.subtracao.setObjectName("subtracao")
        self.bt6 = QtWidgets.QPushButton(CalcAndriel)
        self.bt6.setGeometry(QtCore.QRect(170, 360, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.bt6.setFont(font)
        self.bt6.setObjectName("bt6")
        self.bt7 = QtWidgets.QPushButton(CalcAndriel)
        self.bt7.setGeometry(QtCore.QRect(10, 300, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.bt7.setFont(font)
        self.bt7.setObjectName("bt7")
        self.bt8 = QtWidgets.QPushButton(CalcAndriel)
        self.bt8.setGeometry(QtCore.QRect(90, 300, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.bt8.setFont(font)
        self.bt8.setObjectName("bt8")
        self.bt9 = QtWidgets.QPushButton(CalcAndriel)
        self.bt9.setGeometry(QtCore.QRect(170, 300, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.bt9.setFont(font)
        self.bt9.setObjectName("bt9")
        self.multiplicacao = QtWidgets.QPushButton(CalcAndriel)
        self.multiplicacao.setGeometry(QtCore.QRect(250, 300, 70, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.multiplicacao.setFont(font)
        self.multiplicacao.setObjectName("multiplicacao")
        self.div1porx = QtWidgets.QPushButton(CalcAndriel)
        self.div1porx.setGeometry(QtCore.QRect(10, 240, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.div1porx.setFont(font)
        self.div1porx.setObjectName("div1porx")
        self.potencia = QtWidgets.QPushButton(CalcAndriel)
        self.potencia.setGeometry(QtCore.QRect(90, 240, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.potencia.setFont(font)
        self.potencia.setObjectName("potencia")
        self.divisao = QtWidgets.QPushButton(CalcAndriel)
        self.divisao.setGeometry(QtCore.QRect(250, 240, 70, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.divisao.setFont(font)
        self.divisao.setObjectName("divisao")
        self.raiz = QtWidgets.QPushButton(CalcAndriel)
        self.raiz.setGeometry(QtCore.QRect(170, 240, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.raiz.setFont(font)
        self.raiz.setObjectName("raiz")
        self.porcentagem = QtWidgets.QPushButton(CalcAndriel)
        self.porcentagem.setGeometry(QtCore.QRect(10, 180, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.porcentagem.setFont(font)
        self.porcentagem.setObjectName("porcentagem")
        self.clear_entry = QtWidgets.QPushButton(CalcAndriel)
        self.clear_entry.setGeometry(QtCore.QRect(90, 180, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.clear_entry.setFont(font)
        self.clear_entry.setObjectName("clear_entry")
        self.backspace = QtWidgets.QPushButton(CalcAndriel)
        self.backspace.setGeometry(QtCore.QRect(250, 180, 70, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.backspace.setFont(font)
        self.backspace.setObjectName("backspace")
        self.clear = QtWidgets.QPushButton(CalcAndriel)
        self.clear.setGeometry(QtCore.QRect(170, 180, 65, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.total = QtWidgets.QLabel(CalcAndriel)
        self.total.setGeometry(QtCore.QRect(250, 0, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.total.setFont(font)
        self.total.setStyleSheet("color: rgb(7, 85, 255);")
        self.total.setObjectName("total")
        self.total_completo = QtWidgets.QLabel(CalcAndriel)
        self.total_completo.setGeometry(QtCore.QRect(10, 40, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.total_completo.setFont(font)
        self.total_completo.setText("")
        self.total_completo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_completo.setObjectName("total_completo")

        self.retranslateUi(CalcAndriel)
        QtCore.QMetaObject.connectSlotsByName(CalcAndriel)

    def retranslateUi(self, CalcAndriel):
        _translate = QtCore.QCoreApplication.translate
        CalcAndriel.setWindowTitle(_translate("CalcAndriel", "Calculadora"))
        self.inversao.setText(_translate("CalcAndriel", "+/-"))
        self.bt0.setText(_translate("CalcAndriel", "0"))
        self.virgula.setText(_translate("CalcAndriel", ","))
        self.igual.setText(_translate("CalcAndriel", "="))
        self.bt1.setText(_translate("CalcAndriel", "1"))
        self.bt3.setText(_translate("CalcAndriel", "3"))
        self.bt2.setText(_translate("CalcAndriel", "2"))
        self.soma.setText(_translate("CalcAndriel", "+"))
        self.bt4.setText(_translate("CalcAndriel", "4"))
        self.bt5.setText(_translate("CalcAndriel", "5"))
        self.subtracao.setText(_translate("CalcAndriel", "-"))
        self.bt6.setText(_translate("CalcAndriel", "6"))
        self.bt7.setText(_translate("CalcAndriel", "7"))
        self.bt8.setText(_translate("CalcAndriel", "8"))
        self.bt9.setText(_translate("CalcAndriel", "9"))
        self.multiplicacao.setText(_translate("CalcAndriel", "x"))
        self.div1porx.setText(_translate("CalcAndriel", "1/x"))
        self.potencia.setText(_translate("CalcAndriel", "x??"))
        self.divisao.setText(_translate("CalcAndriel", "/"))
        self.raiz.setText(_translate("CalcAndriel", "???"))
        self.porcentagem.setText(_translate("CalcAndriel", "%"))
        self.clear_entry.setText(_translate("CalcAndriel", "CE"))
        self.backspace.setText(_translate("CalcAndriel", "???"))
        self.clear.setText(_translate("CalcAndriel", "C"))
        self.total.setText(_translate("CalcAndriel", "Andriel\'s"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalcAndriel = QtWidgets.QWidget()
    ui = Ui_CalcAndriel()
    ui.setupUi(CalcAndriel)
    CalcAndriel.show()
    sys.exit(app.exec_())
