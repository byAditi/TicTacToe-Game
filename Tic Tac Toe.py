import random

# Initialize the board and score counters
def reset_board():
    return [" "] * 9

x_wins = 0
o_wins = 0
draws = 0

# Display the board
def print_board(board):
    print()
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
    print()

# Check for win
def check_win(board, player):
    win_cond = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in cond) for cond in win_cond)

# Check for draw
def check_draw(board):
    return " " not in board

# Get player move
def get_player_move(board):
    while True:
        try:
            move = int(input("Choose your move (1-9): ")) - 1
            if board[move] != " ":
                print("❌ That spot is already taken.")
            else:
                return move
        except:
            print("⚠️ Invalid input. Enter a number between 1 and 9.")

# AI move (random)
def get_ai_move(board):
    available = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(available)

# Play one game
def play_game(mode):
    global x_wins, o_wins, draws
    board = reset_board()
    current = "X"

    while True:
        print_board(board)
        if mode == "1" and current == "O":
            print("🤖 Computer is making a move...")
            move = get_ai_move(board)
        else:
            print(f"🎯 Player {current}'s turn")
            move = get_player_move(board)

        board[move] = current

        if check_win(board, current):
            print_board(board)
            if mode == "1" and current == "O":
                print("🎉 Computer (O) wins!")
            else:
                print(f"🎉 Player {current} wins!")
            if current == "X":
                x_wins += 1
            else:
                o_wins += 1
            break
        elif check_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            draws += 1
            break

        current = "O" if current == "X" else "X"

# Game entry point
def main():
    print("🎮 Welcome to Python Tic Tac Toe!")
    while True:
        print("\nSelect Game Mode:")
        print("1. Single Player (You vs Computer 🤖)")
        print("2. Two Player (Player X vs Player O)")
        mode = input("Enter 1 or 2: ").strip()
        if mode not in ["1", "2"]:
            print("⚠️ Invalid mode. Try again.")
            continue

        play_game(mode)

        # Show Scoreboard
        print("\n📊 Scoreboard:")
        print(f"Player X Wins: {x_wins}")
        print(f"{'Computer (O)' if mode == '1' else 'Player O'} Wins: {o_wins}")
        print(f"Draws: {draws}")

        again = input("\n🔁 Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("\n👋 Thanks for playing! Bye!")
            break

# Run the game
main()
