import chess
board = chess.Board()
print(board)
# get position of King in board
king = board.rook(board.turn)
print(king)
