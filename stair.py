from dbus import ValidationException


def stair(n):
    if n >= 1:
        for i in range(1, n + 1):
            output = ' ' * (n  - i) + '*' * i
            print(output)
                
    else:
        raise ValueError("Por favor, digite um número inteiro maior ou igual a 1!")

# Exemplo de chamada de função para uma escada de tamanho 3.

if __name__ == "__main__":
    stair(3)
