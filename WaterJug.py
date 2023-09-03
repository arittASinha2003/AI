from collections import deque

def water_jug_problem(capacity_a, capacity_b, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        current_state = queue.popleft()
        if current_state == target:
            return True
        
        a, b = current_state

        if (capacity_a, b) not in visited:
            visited.add((capacity_a, b))
            queue.append((capacity_a, b))

        if (a, capacity_b) not in visited:
            visited.add((a, capacity_b))
            queue.append((a, capacity_b))

        if (0, b) not in visited:
            visited.add((0, b))
            queue.append((0, b))

        if (a, 0) not in visited:
            visited.add((a, 0))
            queue.append((a, 0))

        pour_amount = min(a, capacity_b - b)
        if (a - pour_amount, b + pour_amount) not in visited:
            visited.add((a - pour_amount, b + pour_amount))
            queue.append((a - pour_amount, b + pour_amount))

        pour_amount = min(b, capacity_a - a)
        if (a + pour_amount, b - pour_amount) not in visited:
            visited.add((a + pour_amount, b - pour_amount))
            queue.append((a + pour_amount, b - pour_amount))

    return False

capacity_a = int(input("Enter the capacity of jug A: "))
capacity_b = int(input("Enter the capacity of jug B: "))
target_capacity = int(input("Enter the target capacity: "))

target = (0, target_capacity)  # Target state

if water_jug_problem(capacity_a, capacity_b, target):
    print("Yes, it's possible to reach the target state.")
else:
    print("No, it's not possible to reach the target state.")
