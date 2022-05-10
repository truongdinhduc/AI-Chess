import chess
board = chess.Board()
print(board)
# get position of King in board
print(list(board.pieces(chess.PAWN, chess.WHITE)))
for v in list(board.pieces(chess.PAWN, chess.WHITE)):
    col = v % 8
    row = v // 8
