import chess
board = chess.Board()
print(board)
# get position of King in board
print(list(board.pieces(chess.P, chess.WHITE)))
