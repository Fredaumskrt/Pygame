# import pygame
# import copy
# import heapq
# import time

# # Configurações
# WIDTH, HEIGHT = 300, 300
# GRID_SIZE = WIDTH // 3
# FPS = 30
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # Função para imprimir o estado do puzzle
# def print_state(state):
#     for row in state:
#         print(row)
#     print()

# # Função para encontrar a posição do zero no estado do puzzle
# def find_zero(state):
#     for i in range(len(state)):
#         for j in range(len(state[i])):
#             if state[i][j] == 0:
#                 return i, j

# # Função para encontrar a posição de um valor no estado do puzzle
# def find_position(state, value):
#     for i in range(len(state)):
#         for j in range(len(state[i])):
#             if state[i][j] == value:
#                 return i, j

# # Função para atualizar a tela
# def update_display(screen, state):
#     screen.fill(WHITE)
#     draw_grid(screen, state)
#     pygame.display.flip()
#     pygame.time.delay(500)  # Adiciona um pequeno atraso para visualização

# # Algoritmo de busca por largura
# def breadth_first_search(initial_state, goal_state, screen):
#     frontier = [initial_state]
#     explored = set()

#     while frontier:
#         current_state = frontier.pop(0)
#         explored.add(tuple(map(tuple, current_state)))

#         if current_state == goal_state:
#             return current_state

#         zero_row, zero_col = find_zero(current_state)

#         # Movimentos possíveis: cima, baixo, esquerda, direita
#         moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#         for move in moves:
#             new_row, new_col = zero_row + move[0], zero_col + move[1]

#             if 0 <= new_row < len(current_state) and 0 <= new_col < len(current_state[0]):
#                 new_state = copy.deepcopy(current_state)
#                 new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

#                 if tuple(map(tuple, new_state)) not in explored and new_state not in frontier:
#                     frontier.append(new_state)

#                 # Atualiza a tela a cada iteração
#                 update_display(screen, new_state)

#     return None

# # Algoritmo A*
# def astar_search(initial_state, goal_state, screen):
#     frontier = [(heuristic(initial_state, goal_state), 0, initial_state)]
#     heapq.heapify(frontier)
#     explored = set()

#     while frontier:
#         _, cost, current_state = heapq.heappop(frontier)
#         explored.add(tuple(map(tuple, current_state)))

#         if current_state == goal_state:
#             return current_state

#         zero_row, zero_col = find_zero(current_state)

#         # Movimentos possíveis: cima, baixo, esquerda, direita
#         moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#         for move in moves:
#             new_row, new_col = zero_row + move[0], zero_col + move[1]

#             if 0 <= new_row < len(current_state) and 0 <= new_col < len(current_state[0]):
#                 new_state = copy.deepcopy(current_state)
#                 new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

#                 if tuple(map(tuple, new_state)) not in explored:
#                     heapq.heappush(frontier, (cost + heuristic(new_state, goal_state), cost + 1, new_state))

#                 # Atualiza a tela a cada iteração
#                 update_display(screen, new_state)

#     return None

# # Função de heurística (distância de Manhattan)
# def heuristic(state, goal_state):
#     distance = 0

#     for i in range(len(state)):
#         for j in range(len(state[i])):
#             value = state[i][j]
#             if value != 0:
#                 goal_row, goal_col = find_position(goal_state, value)
#                 distance += abs(i - goal_row) + abs(j - goal_col)

#     return distance

# # Função para desenhar o grid na tela
# def draw_grid(screen, state):
#     for i in range(len(state)):
#         for j in range(len(state[i])):
#             pygame.draw.rect(screen, WHITE, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))
#             pygame.draw.rect(screen, BLACK, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
#             if state[i][j] != 0:
#                 font = pygame.font.Font(None, 36)
#                 text = font.render(str(state[i][j]), True, BLACK)
#                 text_rect = text.get_rect(center=(j * GRID_SIZE + GRID_SIZE // 2, i * GRID_SIZE + GRID_SIZE // 2))
#                 screen.blit(text, text_rect)

# # Função principal
# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((WIDTH, HEIGHT))
#     pygame.display.set_caption("Sliding Puzzle")
#     clock = pygame.time.Clock()

#     initial_state = [
#         [1, 2, 3],
#         [4, 0, 6],
#         [7, 5, 8]
#     ]

#     goal_state = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 0]
#     ]

#     solving = True
#     start_time = time.time()

#     while solving:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 solving = False

#         # Atualiza a tela inicial
#         update_display(screen, initial_state)

#         # Resolve o quebra-cabeça usando os algoritmos
#         solution_bfs = breadth_first_search(copy.deepcopy(initial_state), goal_state, screen)
#         solution_astar = astar_search(copy.deepcopy(initial_state), goal_state, screen)

#         # Verifica se a solução foi encontrada
#         if solution_bfs or solution_astar:
#             solving = False

#     end_time = time.time()
#     pygame.quit()

#     print(f"Tempo total: {end_time - start_time} segundos")

# if __name__ == "__main__":
#     main()


import pygame
import copy
import heapq
import time

# Configurações
WIDTH, HEIGHT = 300, 300
GRID_SIZE = WIDTH // 3
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Função para imprimir o estado do puzzle
def print_state(state):
    for row in state:
        print(row)
    print()

# Função para encontrar a posição do zero no estado do puzzle
def find_zero(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

# Função para encontrar a posição de um valor no estado do puzzle
def find_position(state, value):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == value:
                return i, j

# Função para atualizar a tela
def update_display(screen, state):
    screen.fill(WHITE)
    draw_grid(screen, state)
    pygame.display.flip()
    pygame.time.delay(1000)  # Adiciona um pequeno atraso para visualização

# Algoritmo de busca por largura
def breadth_first_search(initial_state, goal_state, screen):
    frontier = [initial_state]
    explored = set()

    while frontier:
        current_state = frontier.pop(0)
        explored.add(tuple(map(tuple, current_state)))

        if current_state == goal_state:
            return current_state

        zero_row, zero_col = find_zero(current_state)

        # Movimentos possíveis: cima, baixo, esquerda, direita
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < len(current_state) and 0 <= new_col < len(current_state[0]):
                new_state = copy.deepcopy(current_state)
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in explored and new_state not in frontier:
                    frontier.append(new_state)

                # Atualiza a tela a cada iteração
                update_display(screen, new_state)

    return None

# Algoritmo A*
def astar_search(initial_state, goal_state, screen):
    frontier = [(heuristic(initial_state, goal_state), 0, initial_state)]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        _, cost, current_state = heapq.heappop(frontier)
        explored.add(tuple(map(tuple, current_state)))

        if current_state == goal_state:
            return current_state

        zero_row, zero_col = find_zero(current_state)

        # Movimentos possíveis: cima, baixo, esquerda, direita
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < len(current_state) and 0 <= new_col < len(current_state[0]):
                new_state = copy.deepcopy(current_state)
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in explored:
                    heapq.heappush(frontier, (cost + heuristic(new_state, goal_state), cost + 1, new_state))

                # Atualiza a tela a cada iteração
                update_display(screen, new_state)

    return None

# Função de heurística (distância de Manhattan)
def heuristic(state, goal_state):
    distance = 0

    for i in range(len(state)):
        for j in range(len(state[i])):
            value = state[i][j]
            if value != 0:
                goal_row, goal_col = find_position(goal_state, value)
                distance += abs(i - goal_row) + abs(j - goal_col)

    return distance

# Função para desenhar o grid na tela
def draw_grid(screen, state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            pygame.draw.rect(screen, WHITE, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BLACK, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
            if state[i][j] != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(state[i][j]), True, BLACK)
                text_rect = text.get_rect(center=(j * GRID_SIZE + GRID_SIZE // 2, i * GRID_SIZE + GRID_SIZE // 2))
                screen.blit(text, text_rect)

# Função principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sliding Puzzle")
    clock = pygame.time.Clock()

    initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    # Executa busca em largura
    solving_bfs = True
    start_time_bfs = time.time()

    while solving_bfs:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                solving_bfs = False

        # Atualiza a tela inicial
        update_display(screen, initial_state)

        # Resolve o quebra-cabeça usando busca em largura
        solution_bfs = breadth_first_search(copy.deepcopy(initial_state), goal_state, screen)

        # Verifica se a solução foi encontrada
        if solution_bfs:
            solving_bfs = False

    end_time_bfs = time.time()

    # Executa A*
    solving_astar = True
    start_time_astar = time.time()

    while solving_astar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                solving_astar = False

        # Atualiza a tela inicial
        update_display(screen, initial_state)

        # Resolve o quebra-cabeça usando A*
        solution_astar = astar_search(copy.deepcopy(initial_state), goal_state, screen)

        # Verifica se a solução foi encontrada
        if solution_astar:
            solving_astar = False

    end_time_astar = time.time()

    pygame.quit()

    print(f"Tempo total (Busca em Largura): {end_time_bfs - start_time_bfs} segundos")
    print(f"Tempo total (A*): {end_time_astar - start_time_astar} segundos")

if __name__ == "__main__":
    main()
