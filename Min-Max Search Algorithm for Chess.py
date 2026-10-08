def minimax(depth, node, maximizingPlayer):
    if depth == 0:
        return node
    if maximizingPlayer:
        best = -9999
        for value in node:
            best = max(best, value)
        return best
    else:
        best = 9999
        for value in node:
            best = min(best, value)
        return best
moves = [
    [3, 5],
    [2, 9],
    [1, 4],
    [6, 8]
]
print("Chess Board Evaluation:")
print(moves)
best_move = -9999
move_number = 1
for move in moves:
    value = minimax(1, move, True)
    print("Move", move_number, "Evaluation:", value)
    if value > best_move:
        best_move = value
        best_move_number = move_number
    move_number += 1
print("\nBest Move:", best_move_number)
print("Best Evaluation:", best_move)
