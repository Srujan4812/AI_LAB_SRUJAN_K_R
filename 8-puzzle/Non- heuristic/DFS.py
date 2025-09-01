def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def is_goal(state):
    return state == "123804765"

def get_neighbors(state):
    neighbors = []
    moves = {'Up': -3, 'Down': 3, 'Left': -1, 'Right': 1}
    zero_index = state.index('0')

    for move, pos_change in moves.items():
        new_index = zero_index + pos_change

        # Boundary checks
        if move == 'Left' and zero_index % 3 == 0:
            continue
        if move == 'Right' and zero_index % 3 == 2:
            continue
        if move == 'Up' and zero_index < 3:
            continue
        if move == 'Down' and zero_index > 5:
            continue

        state_list = list(state)
        state_list[zero_index], state_list[new_index] = state_list[new_index], state_list[zero_index]
        neighbors.append(("".join(state_list), move))

    return neighbors

def depth_limited_search(state, limit, visited, path, moves):
    if is_goal(state):
        return path + [state], moves

    if limit <= 0:
        return None

    visited.add(state)

    for neighbor, move in get_neighbors(state):
        if neighbor not in visited:
            result = depth_limited_search(neighbor, limit - 1, visited, path + [state], moves + [move])
            if result is not None:
                return result

    visited.remove(state)  # allow other paths to explore this state later
    return None

def dls(start_state, max_depth):
    visited = set()
    result = depth_limited_search(start_state, max_depth, visited, [], [])
    if result:
        path, moves = result
        print("\n🎯 Goal reached (Depth-Limited Search)!\n")
        for i, step in enumerate(path):
            print(f"Step {i}:")
            print_state(step)
        print("🧭 Moves:", " -> ".join(moves))
        print("📌 Total steps to goal:", len(path) - 1)
        print("📊 Total unique states visited:", len(visited))
    else:
        print(f"❌ No solution found within depth limit {max_depth}.")

if __name__ == "__main__":
    start = "283164705"
    max_depth = 20  # You can adjust this limit based on problem complexity
    dls(start, max_depth)

