import random

START = None
END = None


def gerando_ambiente():
    global START, END

    ambiente = [['-' for _ in range(20)] for _ in range(20)]

    # Gera posições aleatórias para os obstáculos (|) e espaços livres (-)
    num_obstaculos = random.randint(40, 60)
    for _ in range(num_obstaculos):
        obs_x, obs_y = random.randint(0, 19), random.randint(0, 19)
        ambiente[obs_x][obs_y] = '|' if random.random() < 0.3 else '-'

    # Gera posições aleatórias para o ponto de partida ($) e ponto de chegada (@)
    start_x, start_y = random.randint(0, 19), random.randint(0, 19)
    end_x, end_y = random.randint(0, 19), random.randint(0, 19)
    ambiente[start_x][start_y] = '$'
    ambiente[end_x][end_y] = '@'
    START = (start_x, start_y)
    END = (end_x, end_y)

    return ambiente


def print_ambiente(ambiente):
    for linha in ambiente:
        print(' '.join(linha))


def procurar(ambiente, start, end):
    fila = [start]
    visitado = set()
    visitado.add(start)

    while fila:
        x, y = fila.pop(0)

        if (x, y) == end:
            return True

        new_x, new_y = movimentar_direcao(ambiente, (x, y), end)

        if (new_x, new_y) not in visitado and 0 <= new_x < len(ambiente) and 0 <= new_y < len(ambiente[0]) and ambiente[new_x][new_y] != '|':
            if ambiente[new_x][new_y] == '-':
                ambiente[new_x][new_y] = '.'
            visitado.add((new_x, new_y))
            fila.append((new_x, new_y))

    return False


def movimentar_direcao(ambiente, posicao_atual, posicao_chegada):
    new_x, new_y = posicao_atual
    if new_x > posicao_chegada[0]:
        while new_x > posicao_chegada[0] and ambiente[new_x - 1][new_y] != '|':
            new_x -= 1
            ambiente[new_x][new_y] = '.'

    elif new_x < posicao_chegada[0]:
        while new_x < posicao_chegada[0] and ambiente[new_x + 1][new_y] != '|':
            new_x += 1
            ambiente[new_x][new_y] = '.'

    if new_y > posicao_chegada[1]:
        while new_y > posicao_chegada[1] and ambiente[new_x][new_y - 1] != '|':
            new_y -= 1
            ambiente[new_x][new_y] = '.'

    elif new_y < posicao_chegada[1]:
        while new_y < posicao_chegada[1] and ambiente[new_x][new_y + 1] != '|':
            new_y += 1
            ambiente[new_x][new_y] = '.'

    return new_x, new_y


ambiente = gerando_ambiente()

print("Matriz inicial:")
print_ambiente(ambiente)

if procurar(ambiente, START, END):
    ambiente[END[0]][END[1]] = '@'
    print("\nCaminho encontrado:")
    print_ambiente(ambiente)
else:
    print("\nNão foi possível encontrar um caminho.")
