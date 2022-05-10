import chess
board = chess.Board()
print(board)
# get the current square index of the white king
king_square_index = board.king(chess.WHITE)
# get the current square name of the white king
king_square_name = chess.square_name(king_square_index)
print(king_square_name)  # e1
# Move white pawn to e4
board.push_san("e4")
# Move black pawn to e5
board.push_san("e5")
# Move white king to e2
board.push_san("Ke2")
# get the current square index of the white king
king_square_index = board.king(chess.WHITE)
# get the current square name of the white king
king_square_name = chess.square_name(king_square_index)
print(king_square_name)  # e2
