class Funcionarios:
    def __init__(self,nome,salario):
        self.nome=nome
        self.salario=salario
    
    def aumentarSalario(self,porcentagem):
        novoSalario=self.salario + self.salario*(porcentagem/100)
        return novoSalario

jeni=Funcionarios(input("digite o nome do funcionario" ),int(input('digite o salario do funcionário')))
novoSalario=jeni.aumentarSalario(int(input("digite a porcentagem de aumento do funcionario")))
print(f'novo salario de {jeni.nome}: {novoSalario}')