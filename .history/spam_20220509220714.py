import chess
board = chess.Board()
print(board)
# get position of Rooks
rook_pos = board.pieces(chess.ROOK, chess.WHITE)
print(board.rooks(chess.BLACK))
