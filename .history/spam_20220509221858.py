import chess
board = chess.Board()
print(board)
# get position of Rooks
rook_pos = board.piece_map(chess.WHITE)
print(rook_pos)
