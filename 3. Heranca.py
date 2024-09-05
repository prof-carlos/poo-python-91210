from abc import ABC, abstractmethod
import os

os.system("cls || clear")

class Funcionario(ABC):
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    @abstractmethod # Decorador
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nSalário: {self.salario:.2f}"
            f"\nSalário final: {self.salario_final():.2f}"
            )
    
class Motoboy(Funcionario):
    # Acréscimo de 10%.
    BONIFICACAO = 1.1 

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado


class Engenheiro(Funcionario):
    # Acréscimo de 20%.
    BONIFICACAO = 1.2

    def __init__(self, nome: str, salario: float, crea: str) -> None:
        super().__init__(nome, salario)
        self.crea = crea

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCREA: {self.crea}"
                )


# Instanciando classes.
motoboy_1 = Motoboy("Jose", 1000)
print(motoboy_1)

engenheiro_1 = Engenheiro("Marta", 1000.0, "4652132")
print(engenheiro_1)