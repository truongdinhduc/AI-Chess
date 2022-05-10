import chess
board = chess.Board()
print(board)
# get position of King in board
king = board.rooks(board.turn)
print(king)
