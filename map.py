import random
# Parâmetros do mapa

tamanho_matriz = 20
recorrencia_obstaculos = 0.1


def generate_map(size, recorrencia_obstaculos, inicio, chegada):
    map = []
    for linha in range(size):
        row = []
        for coluna in range(size):
            if (linha, coluna) == inicio:
                row.append('$')
            elif (linha, coluna) == chegada:
                row.append('@')
            elif random.random() < recorrencia_obstaculos:
                row.append('|')  # Obstáculo
            else:
                row.append('_')  # Espaço livre
        map.append(row)
    return map


def posicionar(tamanho_matriz):
    linha = random.randint(0, tamanho_matriz - 1)
    coluna = random.randint(0, tamanho_matriz - 1)

    return (linha, coluna)


def print_map(map):
    for row in map:
        print(' '.join(row))


chegada = posicionar(tamanho_matriz)
inicio = posicionar(tamanho_matriz)
print(chegada)
print(inicio)

# Gerar e imprimir o mapa
map = generate_map(tamanho_matriz, recorrencia_obstaculos, inicio, chegada)
print_map(map)
