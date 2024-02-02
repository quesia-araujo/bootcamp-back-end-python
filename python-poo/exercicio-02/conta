from abc import ABC, abstractclassmethod
from cliente import Cliente

class ContaCorrente(ABC):
    def __init__(self, clientes):
        self.cliente = clientes
        self.saldo = 0
        self.operacoes = []

    @abstractclassmethod
    def saque(self, valor):
        pass

    def deposito(self, valor):
        self.saldo += valor
        print(f'Deposito: +{valor}')
        self.operacoes.append(f'DEPOSITO: +{valor}')

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
    def __init__(self, clientes):
        if all(cliente.sexo.lower() == 'feminino' for cliente in clientes):    
            super().__init__(clientes)
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
            self.operacoes.append(f'SAQUE: -{valor}')

    def cheque_especial(self):
        pass


###### TESTES ######
"""Definindo situações de teste:
1  - Adicionar um homem
2  - Adicionar uma mulher e homem
3  - Adicionar uma mulher
4  - Adicionar duas mulheres
"""

joao = Cliente('Joao da Silva', 994056, 1000.00, 'masculino')
maria = Cliente('Maria Silva', 999999, 1000.00, 'feminino')
rosana = Cliente('Rosana Oliveira', 988989, 2000.00, 'feminino')

"""
# testando criação de ContaCorrenteMulher com homem
try:
    lista_clientes = [joao]
    conta1 = ContaCorrenteMulher(lista_clientes)
    conta1.deposito(2000)
    conta1.saque(100)
    conta1.saque(3000)
    print(conta1)
except ValueError as e:
    print(e)

"""

"""
# testando criação de ContaCorrenteMulher com homem e mulher
lista_clientes = [maria, joao]

try:
    conta1 = ContaCorrenteMulher(lista_clientes)
    # conta1.deposito(2000)
    # conta1.saque(100)
    # conta1.saque(3000)
    print(conta1)
except ValueError as e:
    print(e)
"""

"""
# testando criação de ContaCorrenteMulher com mulher
lista_clientes = [maria]

try:
    conta1 = ContaCorrenteMulher(lista_clientes)
    conta1.deposito(2000)
    conta1.saque(100)
    conta1.saque(3000)
    print(conta1)
except ValueError as e:
    print(e)
"""

# testando criação de ContaCorrenteMulher com duas mulheres
lista_clientes = [maria, rosana]

try:
    conta1 = ContaCorrenteMulher(lista_clientes)
    conta1.deposito(2000)
    conta1.saque(100)
    conta1.saque(3000)
    print(conta1)
except ValueError as e:
    print(e)



