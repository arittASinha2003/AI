from queue import PriorityQueue

def uniform_cost_search(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start, []))

    while not queue.empty():
        (cost, node, path) = queue.get()

        if node not in visited:
            visited.add(node)
            path = path + [node]

            if node == goal:
                return cost, path

            for neighbour, neighbour_cost in graph[node]:
                if neighbour not in visited:
                    total_cost = cost + neighbour_cost
                    queue.put((total_cost, neighbour, path))

    return None

graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('S', 1), ('C', 3), ('D', 2)],
    'B': [('S', 4), ('G1', 5)],
    'C': [('A', 3), ('E', 5)],
    'D': [('A', 2), ('F', 1), ('G2', 3)],
    'G1': [('B', 5)],
    'E': [('C', 5), ('G3', 5)],
    'F': [('D', 1)],
    'G2': [('D', 3)],
    'G3': [('E', 5)]
}

start = input("Enter the start state: ")
goal = input("Enter the goal state: ")

result = uniform_cost_search(graph, start, goal)

if result:
    print(f"Shortest path cost from {start} to {goal}: {result[0]}")
    print(f"Shortest path chosen: {' -> '.join(result[1])}")
else:
    print("No path found.")