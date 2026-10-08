def minimax(board, depth, isMax):
    winner = check_winner(board)
    if winner == 'X':
        return 10 - depth
    if winner == 'O':
        return depth - 10
    if ' ' not in board:
        return 0
    if isMax:
        best = -1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best = max(best, score)
        return best
    else:
        best = 1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best = min(best, score)
        return best
def check_winner(board):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return None
def best_move(board):
    best_score = -1000
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move
board = [
    'X', 'O', 'X',
    ' ', 'O', ' ',
    ' ', ' ', ' '
]
print("Current Board:")
for i in range(0, 9, 3):
    print(board[i], "|", board[i+1], "|", board[i+2])
move = best_move(board)
print("\nBest Move for X:", move + 1)
