import pygame
import copy
import heapq
import time

# configura a interface
WIDTH, HEIGHT = 300, 300
GRID_SIZE = WIDTH // 3
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# imprimir o puzzle
def print_state(state):
    for row in state:
        print(row)
    print()

# encontra pos(0)
def find_zero(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

# encontrar qualquer pos
def find_position(state, value):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == value:
                return i, j

# atualizar a tela, na medida que vai passando os num
def update_display(screen, state):
    screen.fill(WHITE)
    draw_grid(screen, state)
    pygame.display.flip()
    pygame.time.delay(500)  # delay para ver os numeros se mov

#  busca por largura
def breadth_first_search(initial_state, goal_state, screen):
    frontier = [initial_state]
    explored = set()

    while frontier:
        current_state = frontier.pop(0)
        explored.add(tuple(map(tuple, current_state)))

        if current_state == goal_state:
            return current_state, explored

        zero_row, zero_col = find_zero(current_state)

        # mov > Up, Down, Left, Right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < len(current_state) and 0 <= new_col < len(current_state[0]):
                new_state = copy.deepcopy(current_state)
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in explored and new_state not in frontier:
                    frontier.append(new_state)

                # atualiza a tela a cada iteracao
                update_display(screen, new_state)

    return None, None

# Algoritmo A*
def astar_search(initial_state, goal_state, screen):
    frontier = [(heuristic(initial_state, goal_state), 0, initial_state)]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        _, cost, current_state = heapq.heappop(frontier)
        explored.add(tuple(map(tuple, current_state)))

        if current_state == goal_state:
            return current_state, explored

        zero_row, zero_col = find_zero(current_state)

        #  mov > Up, Down, Left, Right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < len(current_state) and 0 <= new_col < len(current_state[0]):
                new_state = copy.deepcopy(current_state)
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in explored:
                    heapq.heappush(frontier, (cost + heuristic(new_state, goal_state), cost + 1, new_state))

                # atualiza novamente
                update_display(screen, new_state)

    return None, None
# Custo Uniforme
def uniform_cost_search(initial_state, goal_state, screen):
    frontier = [(0, initial_state)]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        cost, current_state = heapq.heappop(frontier)
        explored.add(tuple(map(tuple, current_state)))

        if current_state == goal_state:
            return current_state, explored

        zero_row, zero_col = find_zero(current_state)

        # mov > Up, Down, Left, Right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < len(current_state) and 0 <= new_col < len(current_state[0]):
                new_state = copy.deepcopy(current_state)
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in explored:
                    heapq.heappush(frontier, (cost + 1, new_state))

                # atualiza a tela a cada iteração
                update_display(screen, new_state)

    return None, None

    # gulosa
def greedy_search(initial_state, goal_state, screen):
    frontier = [(heuristic(initial_state, goal_state), initial_state)]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        _, current_state = heapq.heappop(frontier)
        explored.add(tuple(map(tuple, current_state)))

        if current_state == goal_state:
            return current_state, explored

        zero_row, zero_col = find_zero(current_state)

        #  mov > Up, Down, Left, Right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < len(current_state) and 0 <= new_col < len(current_state[0]):
                new_state = copy.deepcopy(current_state)
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in explored:
                    heapq.heappush(frontier, (heuristic(new_state, goal_state), new_state))

                # atualiza novamente (comente ou remova esta linha para acelerar)
                # update_display(screen, new_state)

    return None, None

# func heuristica (distancia de Manhattan)
def heuristic(state, goal_state):
    distance = 0

    for i in range(len(state)):
        for j in range(len(state[i])):
            value = state[i][j]
            if value != 0:
                goal_row, goal_col = find_position(goal_state, value)
                distance += abs(i - goal_row) + abs(j - goal_col)

    return distance

# desenhar grid na tela
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

    solution_bfs, explored_bfs = breadth_first_search(copy.deepcopy(initial_state), goal_state, screen)

    end_time_bfs = time.time()

    # nos explorados (Largura)
    with open("busca_Largura.txt", "w") as file:
        for node in explored_bfs:
            file.write(str(node) + "\n")

    # Executa A*
    solving_astar = True
    start_time_astar = time.time()

    solution_astar, explored_astar = astar_search(copy.deepcopy(initial_state), goal_state, screen)

    end_time_astar = time.time()

    # nos explorados (Largura)
    with open("A_Estrela", "w") as file:
        for node in explored_astar:
            file.write(str(node) + "\n")
            
    solving_ucs = True      
    start_time_ucs = time.time()

    solution_ucs, explored_ucs = uniform_cost_search(copy.deepcopy(initial_state), goal_state, screen)

    end_time_ucs = time.time()

    # nós explorados (UCS)
    with open("busca_uniforme.txt", "w") as file:
        for node in explored_ucs:
            file.write(str(node) + "\n")

    # Executa Busca Gulosa
    solving_greedy = True      
    start_time_greedy = time.time()

    solution_greedy, explored_greedy = greedy_search(copy.deepcopy(initial_state), goal_state, screen)

    end_time_greedy = time.time()

    # nós explorados (Gulosa)
    with open("busca_gulosa.txt", "w") as file:
        for node in explored_greedy:
            file.write(str(node) + "\n")

    pygame.quit()

    print(f"Tempo total (Busca em Largura): {end_time_bfs - start_time_bfs} segundos")
    print(f"Tempo total (A*): {end_time_astar - start_time_astar} segundos")
    print(f"Tempo total (Busca Uniforme): {end_time_ucs - start_time_ucs} segundos")
    print(f"Tempo total (Busca Gulosa): {end_time_greedy - start_time_greedy} segundos")


if __name__ == "__main__":
    main()
