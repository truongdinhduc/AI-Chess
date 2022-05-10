import chess
board = chess.Board()
print(board)
# get position of King in board
print(len(board.pieces(chess.ROOK, chess.WHITE)))
print(len(board.pieces(chess.ROOK, chess.BLACK)))
print(list(board.pieces(chess.ROOK, True)))
print(list(board.rooks(chess.)))