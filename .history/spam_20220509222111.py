import chess
board = chess.Board()
print(board)
# get position of King in board
print(len(board.pieces(chess.ROOK, chess.WHITE)))
