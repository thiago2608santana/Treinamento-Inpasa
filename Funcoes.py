import numpy as np

def calcular_expressao_matematica(valor1: float, valor2:float) -> float:

    expressao1 = valor1 + valor2
    expressao2 = np.sqrt(expressao1)

    return np.round(expressao2,2)

def imprimir_um_nome(nome: str) -> None:

    print(f'O nome inserido foi: {nome}')