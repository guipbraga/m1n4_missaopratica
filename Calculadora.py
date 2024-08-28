class Calculadora:
    def __init__(self, valorA, valorB, operacao):
        self.__valorA = valorA
        self.__valorB = valorB
        self.__operacao = operacao
    @property
    def valorA(self):
        return self.__valorA
    @valorA.setter
    def valorA(self, valorA):
        self.__valorA = valorA
    @property
    def valorB(self):
        return self.__valorB
    @valorB.setter
    def valorB(self, valorB):
        self.__valorB = valorB
    @property
    def operacao(self):
        return self.__operacao
    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao
       
    def validarOperacao(self, simbolo):
        operacoes_validas = ['+', '-', '*', '/']
        return simbolo in operacoes_validas

    def calcular(self):
        if not self.validarOperacao(self.operacao):
            print("Operação inválida!")
            return  
        
        if self.operacao == '+':
            resultado = self.valorA + self.valorB
        elif self.operacao == '-':
            resultado = self.valorA - self.valorB
        elif self.operacao == '*':
            resultado = self.valorA * self.valorB
        elif self.operacao == '/':
            if self.valorB == 0:
                print("Não é possível dividir por 0!")
                return 
            resultado = self.valorA / self.valorB
        return resultado

    def mostrarResultado(self):
        resultado = self.calcular()
        if resultado is not None:
            print(str(self.valorA) + ' ' + self.operacao + ' ' + str(self.valorB) + ' = ' + str(resultado))