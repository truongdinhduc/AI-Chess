import chess
board = chess.Board()
print(board)
king_square_index = board.qu(chess.WHITE)
# get the current square name of the white king
king_square_name = chess.square_name(0)

print(king_square_name)
