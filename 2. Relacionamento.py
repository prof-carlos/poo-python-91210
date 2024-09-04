import os

os.system("cls || clear") # Limpa o terminal.

# Criando a classe Aluno.
class Aluno: 
    # Criando um construtor.
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade}"
    

# Instanciar classe.
aluno = Aluno("Marta", 22)

print(aluno.exibir_dados())