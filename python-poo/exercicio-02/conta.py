from abc import ABC, abstractclassmethod
from cliente import Cliente


class ContaCorrente(ABC):
    def __init__(self, clientes, numero, saldo=0):
        self.cliente = clientes
        self.numero = numero
        self.saldo = saldo
        self.operacoes = []

    @abstractclassmethod
    def saque(self, valor):
        pass

    def resumo(self):
        print(f'CC Número: {self.numero} Saldo: {self.saldo}')

    def deposito(self, valor):
        self.saldo += valor
        print(f'Deposito: +{valor}')
        self.operacoes.append(["DEPOSITO", valor])
    
    def extrato(self):
        print(f'Extrato CC Número: {self.numero}\nSaldo: {self.saldo}')
        print(self.operacoes)

    def __str__(self) -> str:
        clientes_str = '\n '.join(str(cliente) for cliente in self.cliente)
        return f'cliente(s):\n {clientes_str}, \nsaldo: {self.saldo}, \noperações: {self.operacoes}'
    
    """
    ############### APRENDIZADO ################
    def __str__(self) -> str:
        return f'cliente(s):\n {self.cliente}, \nsaldo: {self.saldo}, \noperações: {self.operacoes}'

    # Usar {self.cliente} diretamente, está tentando imprimir a lista de objetos Cliente diretamente, o que resulta na exibição padrão do Python para objetos (como <cliente.Cliente object at 0x...>).

    # Na implementação correta, é preciso percorrer a lista de clientes e chamar o método __str__ de cada objeto Cliente para obter uma representação de string adequada. 
    """

class ContaCorrenteMulher(ContaCorrente):
    def __init__(self, clientes, numero, saldo=0):
        if all(cliente.sexo.lower() == 'feminino' for cliente in clientes):    
            super().__init__(clientes, numero, saldo)
            self.cheque_especial = 0
        else:
            raise ValueError('A ContaCorrenteMulher só pode ser criada para clientes do sexo feminino.')

    def saque(self, valor):
        if valor > self.saldo:
            print(f'Saldo Insuficiente!')
            return False
        else:
            self.saldo -= valor
            print(f'Saque: -{valor}')
            self.operacoes.append(["SAQUE", valor])

    def cheque_especial(self):
        pass


