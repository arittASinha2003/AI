import heapq

# Define the goal state for the 8-puzzle
goal_state = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)  # 0 represents the empty tile
)

# Define the possible moves (up, down, left, right)
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Define a heuristic function (Manhattan distance)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x1, y1 = i, j
                x2, y2 = divmod(state[i][j] - 1, 3)
                distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Define the A* search algorithm
def solve_puzzle(initial_state):
    open_set = [(heuristic(initial_state), 0, initial_state)]
    closed_set = set()
    parent = {}
    
    while open_set:
        _, cost, current_state = heapq.heappop(open_set)
        
        if current_state == goal_state:
            # Reconstruct the path
            path = []
            while current_state != initial_state:
                path.append(current_state)
                current_state = parent[current_state]
            path.append(initial_state)
            return path[::-1]
        
        if current_state in closed_set:
            continue
        
        closed_set.add(current_state)
        empty_tile_i, empty_tile_j = [(i, j) for i in range(3) for j in range(3) if current_state[i][j] == 0][0]
        
        for dx, dy in moves:
            new_i, new_j = empty_tile_i + dx, empty_tile_j + dy
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = list(list(row) for row in current_state)
                new_state[empty_tile_i][empty_tile_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_tile_i][empty_tile_j]
                new_state = tuple(tuple(row) for row in new_state)
                
                if new_state not in closed_set:
                    parent[new_state] = current_state
                    heapq.heappush(open_set, (cost + 1 + heuristic(new_state), cost + 1, new_state))
    
    return None

# Example initial state as a 2D matrix (change this to your desired initial state)
initial_state_2d = (
    (1, 2, 3),
    (4, 0, 5),
    (7, 8, 6)
)

# Solve the 8-puzzle problem
solution = solve_puzzle(initial_state_2d)

# Print the sequence of steps
if solution:
    print("Sequence of Steps:")
    for step, state in enumerate(solution):
        print(f"Step {step + 1}:")
        for row in state:
            print(*row)
        print()
else:
    print("No solution found.")
