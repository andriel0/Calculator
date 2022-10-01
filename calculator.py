from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from design import Ui_CalcAndriel
import math
import string


class JanelaPrincipal(QMainWindow, Ui_CalcAndriel):
    def __init__(self):
        super().__init__()
        self.operacoes = ['+', '-', 'x', '/', '%', '√', '^']
        self.setupUi(self)
        self.bt0.clicked.connect(self.push0)
        self.bt1.clicked.connect(self.push1)
        self.bt2.clicked.connect(self.push2)
        self.bt3.clicked.connect(self.push3)
        self.bt4.clicked.connect(self.push4)
        self.bt5.clicked.connect(self.push5)
        self.bt6.clicked.connect(self.push6)
        self.bt7.clicked.connect(self.push7)
        self.bt8.clicked.connect(self.push8)
        self.bt9.clicked.connect(self.push9)
        self.soma.clicked.connect(self.somar)
        self.subtracao.clicked.connect(self.subtrair)
        self.multiplicacao.clicked.connect(self.multiplicar)
        self.divisao.clicked.connect(self.dividir)
        self.virgula.clicked.connect(self.virgular)
        self.inversao.clicked.connect(self.inverter)
        self.potencia.clicked.connect(self.elevar_quadrado)
        self.igual.clicked.connect(self.totalizar)
        self.div1porx.clicked.connect(self.divisor_de_1)
        self.raiz.clicked.connect(self.radiciar)
        self.porcentagem.clicked.connect(self.porcentar)
        self.clear_entry.clicked.connect(self.limpar_numero)
        self.clear.clicked.connect(self.limpar_visor)
        self.backspace.clicked.connect(self.apagar_ultimo)

    def inverter(self):
        cima = self.total_completo.text()
        baixo = '-' + self.visor.text()
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
    def push0(self):
        cima = self.total_completo.text() + '0'
        baixo = self.visor.text() + '0'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
    def push1(self):
        cima = self.total_completo.text() + '1'
        baixo = self.visor.text() + '1'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
    def push2(self):
        cima = self.total_completo.text() + '2'
        baixo = self.visor.text() + '2'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
    def push3(self):
        cima = self.total_completo.text() + '3'
        baixo = self.visor.text() + '3'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
    def push4(self):
        cima = self.total_completo.text() + '4'
        baixo = self.visor.text() + '4'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
    def push5(self):
        cima = self.total_completo.text() + '5'
        baixo = self.visor.text() + '5'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
    def push6(self):
        cima = self.total_completo.text() + '6'
        baixo = self.visor.text() + '6'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
    def push7(self):
        cima = self.total_completo.text() + '7'
        baixo = self.visor.text() + '7'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
    def push8(self):
        cima = self.total_completo.text() + '8'
        baixo = self.visor.text() + '8'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
    def push9(self):
        cima = self.total_completo.text() + '9'
        baixo = self.visor.text() + '9'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
    def virgular(self):
        cima = self.total_completo.text() + ','
        baixo = self.visor.text() + ','
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
    def totalizar(self):
        self.calcular('=')
    def somar(self):
        cima = self.total_completo.text() + '+'
        baixo = self.visor.text() + '+'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
        self.calcular()
    def subtrair(self):
        cima = self.total_completo.text() + '-'
        baixo = self.visor.text() + '-'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
        self.calcular()
    def multiplicar(self):
        cima = self.total_completo.text() + 'x'
        baixo = self.visor.text() + 'x'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
        self.calcular()
    def dividir(self):
        cima = self.total_completo.text() + '/'
        baixo = self.visor.text() + '/'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
        self.calcular()
    def divisor_de_1(self):
        pass
    def elevar_quadrado(self):
        cima= self.total_completo.text() + '^2'
        baixo = self.visor.text() + '^2'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
        self.calcular()
    def radiciar(self):
        cima = self.total_completo.text() + '√'
        baixo = self.visor.text() + '√'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
        self.calcular()
    def porcentar(self):
        cima = self.total_completo.text() + '%'
        baixo = self.visor.text() + '%'
        self.total_completo.setText(cima)
        self.visor.setText(baixo)
        self.calcular()
    def limpar_numero(self):
        self.visor.setText('')
    def limpar_visor(self):
        self.total_completo.setText('')
        self.visor.setText('')
    def apagar_ultimo(self):
        modificar = self.visor.text()
        modificado = list(modificar)
        modificar = ''
        if len(modificado)>0:
            del modificado[-1]
        for i in modificado:
            modificar += i
        self.total_completo.setText(modificar)
        self.visor.setText(modificar)
    def calcular(self, unico = ''):
        cont = 0
        conta = self.visor.text()
        for i in self.operacoes:
            if i in conta:
                cont += 1
        if ',' in conta:
            conta = conta.replace(',', '.')
        if cont == 1 and unico == '=':
            resultado = self.calculo(conta)
            self.visor.setText(resultado)
        elif cont == 1 and unico != '=':
            pass
        else:
            ultimo = conta[-1]
            conta = list(conta)
            del conta[-1]
            new = ''
            for n in conta:
                new += n
            resultado = self.calculo(new) + ultimo
            self.visor.setText(resultado)

    def calculo(self, oper):
        for numero in oper:
            if numero in self.operacoes and (numero != oper[0] or numero == '√'):
                a,b = oper.split(numero)
                match numero:
                    case '+':
                        resultado = float(a) + float(b)
                    case '-':
                        resultado = float(a) - float(b)
                    case 'x':
                        resultado = float(a) * float(b)
                    case '/':
                        resultado = float(a) / float(b)
                    case '^':
                        resultado = float(a) ** 2
                    case '√':
                        resultado = math.sqrt(float(b))

        resultado = str(round(resultado, 4))
        if '.' in resultado:
            resultado = resultado.replace('.', ',')
        return resultado


app = QApplication([])
janela = JanelaPrincipal()
janela.show()
app.exec_()