import chess
board = chess.Board()
print(board)
king_square_index = board.king(chess.WHITE)
# get the current square name of the white king
king_square_name = chess.square_name(king_square_index)
print()
