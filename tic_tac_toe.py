import math

HUMAN = "X"
AI = "O"
EMPTY = " "

def print_board(board):
    print()
    for row in range(3):
        print(" " + " | ".join(board[row * 3:(row + 1) * 3]))
        if row < 2:
            print("---+---+---")
    print()

def check_winner(board, player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(all(board[i] == player for i in line) for line in wins)

def is_draw(board):
    return EMPTY not in board and not check_winner(board, HUMAN) and not check_winner(board, AI)

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, AI):
        return 10 - depth
    if check_winner(board, HUMAN):
        return depth - 10
    if EMPTY not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score

    best_score = math.inf
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = HUMAN
            score = minimax(board, depth + 1, True, alpha, beta)
            board[i] = EMPTY
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
    return best_score

def get_ai_move(board):
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = EMPTY

            if score > best_score:
                best_score = score
                best_move = i

    return best_move

def get_human_move(board):
    while True:
        choice = input("Choose a square (1-9): ").strip()

        if not choice.isdigit() or not 1 <= int(choice) <= 9:
            print("Please enter a number from 1 to 9.")
            continue

        index = int(choice) - 1
        if board[index] != EMPTY:
            print("That square is already occupied. Try again.")
            continue

        return index

def play_game():
    board = [str(i + 1) for i in range(9)]
    print("=" * 38)
    print("TIC-TAC-TOE: HUMAN vs AI")
    print("You are X. The AI is O.")
    print("The AI uses Minimax with Alpha-Beta Pruning.")
    print("=" * 38)

    board = [EMPTY] * 9
    print("Square positions:")
    print_board([str(i + 1) for i in range(9)])

    while True:
        print_board(board)
        move = get_human_move(board)
        board[move] = HUMAN

        if check_winner(board, HUMAN):
            print_board(board)
            print("Congratulations! You won.")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_move = get_ai_move(board)
        board[ai_move] = AI
        print(f"AI chooses square {ai_move + 1}.")

        if check_winner(board, AI):
            print_board(board)
            print("AI wins! Better luck next time.")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

    if input("Play again? (y/n): ").strip().lower() == "y":
        play_game()

if __name__ == "__main__":
    play_game()
