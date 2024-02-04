class Cliente:
    def __init__(self, nome, telefone, renda_mensal, sexo):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal
        self.sexo = sexo

    def __str__(self) -> str:
        return f'nome: {self.nome}, telefone: {self.telefone}, renda mensal: {self.renda_mensal}, sexo: {self.sexo}'

    ## Definir metodos getter e setter
        
joao = Cliente('Joao da Silva', 994056, 1000.00, 'masculino')
#maria = Cliente('Maria Silva', 999999, 1000.00)

print(joao)
#print(maria)