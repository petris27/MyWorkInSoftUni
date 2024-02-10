def draw_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(board, symbol):
    # Проверка за победител по редове, колони и диагонали
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def is_board_full(board):
    # Проверка за пълно игрално поле
    return all(all(cell != ' ' for cell in row) for row in board)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_symbol = 'X'

    while True:
        draw_board(board)
        row = int(input(f"Изберете ред (0, 1, 2) за {current_symbol}: "))
        col = int(input(f"Изберете колона (0, 1, 2) за {current_symbol}: "))

        if board[row][col] == ' ':
            board[row][col] = current_symbol

            if is_winner(board, current_symbol):
                draw_board(board)
                print(f"{current_symbol} печели!")
                break
            elif is_board_full(board):
                draw_board(board)
                print("Играта завършва без победител!")
                break

            # Променяне на текущия символ за следващия вход
            current_symbol = 'O' if current_symbol == 'X' else 'X'
        else:
            print("Това място е вече заето. Изберете друго.")

if __name__ == "__main__":
    tic_tac_toe()