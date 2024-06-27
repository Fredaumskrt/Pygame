import pygame
import copy
import heapq
import time
import math

# Configuração da interface
WIDTH, HEIGHT = 600, 600
GRID_SIZE = WIDTH // 3
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEXT_COLOR = (255, 0, 0)

# Funções auxiliares
def print_state(state):
    for row in state:
        print(row)
    print()

def find_zero(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

def find_position(state, value):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == value:
                return i, j

def update_display(screen, state):
    screen.fill(WHITE)
    draw_grid(screen, state)
    pygame.display.flip()
    pygame.time.delay(500)  # Delay para ver os números se movendo

# Heurística de distância de Manhattan
def manhattan_heuristic(state, goal_state):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            value = state[i][j]
            if value != 0:
                goal_row, goal_col = find_position(goal_state, value)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

# Heurística de distância Euclidiana
def euclidean_heuristic(state, goal_state):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            value = state[i][j]
            if value != 0:
                goal_row, goal_col = find_position(goal_state, value)
                distance += math.sqrt((i - goal_row) ** 2 + (j - goal_col) ** 2)
    return distance

# Algoritmo A*
def astar_search(initial_state, goal_state, screen, heuristic):
    frontier = [(heuristic(initial_state, goal_state), 0, initial_state)]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        _, cost, current_state = heapq.heappop(frontier)
        explored.add(tuple(map(tuple, current_state)))

        if current_state == goal_state:
            return current_state, explored

        zero_row, zero_col = find_zero(current_state)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < len(current_state) and 0 <= new_col < len(current_state[0]):
                new_state = copy.deepcopy(current_state)
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in explored:
                    heapq.heappush(frontier, (cost + heuristic(new_state, goal_state), cost + 1, new_state))

                update_display(screen, new_state)

    return None, None

# Busca Gulosa
def greedy_search(initial_state, goal_state, screen, heuristic):
    frontier = [(heuristic(initial_state, goal_state), initial_state)]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        _, current_state = heapq.heappop(frontier)
        explored.add(tuple(map(tuple, current_state)))

        if current_state == goal_state:
            return current_state, explored

        zero_row, zero_col = find_zero(current_state)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < len(current_state) and 0 <= new_col < len(current_state[0]):
                new_state = copy.deepcopy(current_state)
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in explored:
                    heapq.heappush(frontier, (heuristic(new_state, goal_state), new_state))

                update_display(screen, new_state)

    return None, None

# Busca em Largura
def breadth_first_search(initial_state, goal_state, screen):
    frontier = [initial_state]
    explored = set()

    while frontier:
        current_state = frontier.pop(0)
        explored.add(tuple(map(tuple, current_state)))

        if current_state == goal_state:
            return current_state, explored

        zero_row, zero_col = find_zero(current_state)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < len(current_state) and 0 <= new_col < len(current_state[0]):
                new_state = copy.deepcopy(current_state)
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in explored and new_state not in frontier:
                    frontier.append(new_state)

                update_display(screen, new_state)

    return None, None

# Busca em Profundidade
def depth_first_search(initial_state, goal_state, screen):
    frontier = [initial_state]
    explored = set()

    while frontier:
        current_state = frontier.pop()
        explored.add(tuple(map(tuple, current_state)))

        if current_state == goal_state:
            return current_state, explored

        zero_row, zero_col = find_zero(current_state)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < len(current_state) and 0 <= new_col < len(current_state[0]):
                new_state = copy.deepcopy(current_state)
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in explored and new_state not in frontier:
                    frontier.append(new_state)

                update_display(screen, new_state)

    return None, None

# Busca Uniforme
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

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < len(current_state) and 0 <= new_col < len(current_state[0]):
                new_state = copy.deepcopy(current_state)
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in explored:
                    heapq.heappush(frontier, (cost + 1, new_state))

                update_display(screen, new_state)

    return None, None

# Função para desenhar a grade
def draw_grid(screen, state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            pygame.draw.rect(screen, WHITE, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BLACK, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
            if state[i][j] != 0:
                font = pygame.font.Font(None, 72)
                text = font.render(str(state[i][j]), True, TEXT_COLOR)
                text_rect = text.get_rect(center=(j * GRID_SIZE + GRID_SIZE // 2, i * GRID_SIZE + GRID_SIZE // 2))
                screen.blit(text, text_rect)

# Menu principal
def main_menu(screen):
    font = pygame.font.Font(None, 36)
    options = ["A* (Manhattan)", "A* (Euclidiana)", "Busca Gulosa (Manhattan)", "Busca Gulosa (Euclidiana)", "Busca em Largura", "Busca em Profundidade", "Busca Uniforme"]
    selected_option = 0

    while True:
        screen.fill(WHITE)
        
        for i, option in enumerate(options):
            color = BLACK
            if i == selected_option:
                color = (0, 255, 0)
            text = font.render(option, True, color)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 40))
            screen.blit(text, text_rect)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return selected_option

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sliding Puzzle")
    clock = pygame.time.Clock()

    options = ["A* (Manhattan)", "A* (Euclidiana)", "Busca Gulosa (Manhattan)", "Busca Gulosa (Euclidiana)", "Busca em Largura", "Busca em Profundidade", "Busca Uniforme"]
    selected_option = main_menu(screen)
    if selected_option is None:
        return

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

    start_time = time.time()

    if selected_option == 0:
        solution, explored = astar_search(copy.deepcopy(initial_state), goal_state, screen, manhattan_heuristic)
        filename = "A_Estrela_Manhattan.txt"
    elif selected_option == 1:
        solution, explored = astar_search(copy.deepcopy(initial_state), goal_state, screen, euclidean_heuristic)
        filename = "A_Estrela_Euclidiana.txt"
    elif selected_option == 2:
        solution, explored = greedy_search(copy.deepcopy(initial_state), goal_state, screen, manhattan_heuristic)
        filename = "busca_gulosa_manhattan.txt"
    elif selected_option == 3:
        solution, explored = greedy_search(copy.deepcopy(initial_state), goal_state, screen, euclidean_heuristic)
        filename = "busca_gulosa_euclidiana.txt"
    elif selected_option == 4:
        solution, explored = breadth_first_search(copy.deepcopy(initial_state), goal_state, screen)
        filename = "busca_em_largura.txt"
    elif selected_option == 5:
        solution, explored = depth_first_search(copy.deepcopy(initial_state), goal_state, screen)
        filename = "busca_em_profundidade.txt"
    elif selected_option == 6:
        solution, explored = uniform_cost_search(copy.deepcopy(initial_state), goal_state, screen)
        filename = "busca_uniforme.txt"

    end_time = time.time()

    with open(filename, "w") as file:
        for node in explored:
            file.write(str(node) + "\n")

    pygame.quit()

    print(f"Tempo total ({options[selected_option]}): {end_time - start_time} segundos")

if __name__ == "__main__":
    main()
