# 변수

# 하이퍼 파라미터
Test_Depth = 7
Score = {
    "X" : -1,
    "O" : 1,
    "D" : 0
}

# 기타
Board_Size = 3
Board = [" " for _ in range(Board_Size**2)]
"""
공백: " "
인간: "X"
AI: "O"
"""
######################################################################
# 함수
def print_board():
    print()
    for i in range(0, Board_Size**2, Board_Size):
        print("".join([f" {Board[i+k]} |" for k in range(Board_Size-1)]), end=f" {Board[i+Board_Size-1]}\n")
        if i < Board_Size*(Board_Size-1):
            print("---+" * (Board_Size-1), end = "---\n")
    print()

check = []
check.extend([[i*Board_Size+k for k in range(Board_Size)] for i in range(Board_Size)])
check.extend([[i+k*Board_Size for k in range(Board_Size)] for i in range(Board_Size)])
check.append([i*Board_Size+i for i in range(Board_Size)])
check.append([i*Board_Size+(Board_Size-i-1) for i in range(Board_Size)])
def check_winner(board):
    if " " not in board: return "D"

    for i in check:
        temp = board[i[0]]
        if temp == " ": continue
        for k in i[1:]:
            if temp != board[k]:
                temp = " "
                break
        if temp != " ": return temp

    return " "

def Search(board, depth, turn):
    s = check_winner(board)
    if s != " ": return Score[s]

    if turn:
        max_score = -float("inf")
        for i in range(Board_Size**2):
            if board[i] == " ":
                board[i] = "O"
                score = Search(board, depth+1, False)
                board[i] = " "
                max_score = max(max_score, score)
        return max_score
    else:
        min_score = float("inf")
        for i in range(Board_Size**2):
            if board[i] == " ":
                board[i] = "X"
                score = Search(board, depth+1, True)
                board[i] = " "
                min_score = min(min_score, score)
        return min_score

def minmax():
    max_score = -float("inf")
    move = -1
    for i in range(Board_Size**2):
        if Board[i] == " ":
            Board[i] = "O"
            score = Search(Board, 0, False)
            Board[i] = " "
            if score > max_score:
                max_score = score
                move = i
    return move

def human_move():
    while True:
        try:
            pos = int(input("(종료:-1)위치 입력: "))
            if pos < -1 or pos >= Board_Size**2 or Board[pos] != " ":
                continue
            if pos == -1: exit()
            return pos
        except ValueError:
            pass
######################################################################
# 게임
if input("선공(y/n): ") == "n":
    Board[minmax()] = "O"
print_board()
while True:
    Board[human_move()] = "X"
    if check_winner(Board) == "X":
        print("인간 승")
        break

    Board[minmax()] = "O"
    print_board()

    if (s := check_winner(Board)) == "O":
        print("AI 승")
        break
    elif s == "D":
        print("무승부")
        break