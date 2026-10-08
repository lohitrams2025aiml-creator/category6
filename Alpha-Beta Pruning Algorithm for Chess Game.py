def alphabeta(depth, node, alpha, beta, maximizingPlayer):
    if depth == 0:
        return node
    if maximizingPlayer:
        best = -9999
        for value in node:
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                print("Branch Pruned")
                break
        return best
    else:
        best = 9999
        for value in node:
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                print("Branch Pruned")
                break
        return best
moves = [
    [3, 5],
    [2, 9],
    [1, 4],
    [6, 8]
]
print("Chess Move Evaluations:")
print(moves)
best_move = -9999
for i, move in enumerate(moves):
    value = alphabeta(1, move, -9999, 9999, True)
    print("Move", i + 1, "Evaluation:", value)
    if value > best_move:
        best_move = value
        best_move_number = i + 1
print("\nBest Move:", best_move_number)
print("Best Evaluation:", best_move)
