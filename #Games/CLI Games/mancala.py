board = [0, 4,4,4,4,4,4, 0, 4,4,4,4,4,4]
def move(player:bool, number:int, board:list):
    return board
def printBoard() -> str :
    return f"""
+----------------+
| |{board[1]}|{board[2]}|{board[3]}|{board[4]}|{board[5]}|{board[6]}| |
|{board[0]}|           |{board[7]}|
| |{board[13]}|{board[12]}|{board[11]}|{board[10]}|{board[9]}|{board[8]}| |
+----------------+
"""

print(printBoard())