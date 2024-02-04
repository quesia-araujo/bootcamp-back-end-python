from conta import ContaCorrente, ContaCorrenteMulher
from cliente import Cliente
from banco import Banco
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
    conta1 = ContaCorrenteMulher(lista_clientes, 1234, 1000.00)
    conta1.deposito(2000)
    conta1.saque(100)
    conta1.saque(3000)
    banco_delas = Banco('Banco Delas')
    banco_delas.abre_conta(conta1)
    banco_delas.lista_contas()
except ValueError as e:
    print(e)



