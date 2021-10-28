import tarfile
from typing import Deque, Any, Iterator
from collections import deque

# Classe que fara as validações e terá as funções utilizadas:
class Queue:
    # Função para criação da fila e definição de limite para a mesma
    def __init__(self, maxlen=10):
        self.__items: Deque[Any] = deque()
        self.maxlen = maxlen

    # Função para o enfileiramento e validação de número negativo ou fila cheia
    def enqueue(self, *items: int) -> None:
        for item in items:
            if self.maxlen == self.__items.__len__():
                break
            elif item < 0:
                break
            else:
                self.__items.append(item)

    # Função para o desinfileiramento
    def dequeue(self) -> int:
        if not self:
            raise IndexError('pop from empty queue')
        return self.__items.popleft()

    # Função para que seja possível coletar os dados da fila em string
    def __repr__(self) -> str:
        return str(self.__items)

    # Função que faz possível a leitura do tamanho da fila
    def __len__(self) -> int:
        return len(self.__items)

# Inico do programa
if __name__ == "__main__":
    # Variavel que recebe a classe
    fila = Queue()
    # Lista secundaria que listará valores pares
    filaPares = []

    # Laço de repetição para enfileiramento
    for i in range(25):
        fila.enqueue(i)

    print(fila)

    # Laço de repetição para desinfileiramento junto do retorno de valores pares
    for o in range(fila.__len__()):
        removido = fila.dequeue()
        if removido % 2 == 0:
            filaPares.append(removido)

    print(fila)
    print(filaPares)
