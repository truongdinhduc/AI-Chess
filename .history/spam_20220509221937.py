import chess
board = chess.Board()
print(board)
# get position of King in board
king = board.king(board.turn)
print(king)
