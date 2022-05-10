import chess
board = chess.Board()
print(board)
# get position of King in board
print(list(board.pieces(chess.ROOK, chess.WHITE)))
PAWNSCORE = [0,  0,  0,  0,  0,  0,  0,  0,
50, 50, 50, 50, 50, 50, 50, 50,
10, 10, 20, 30, 30, 20, 10, 10,
 5,  5, 10, 25, 25, 10,  5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5, -5,-10,  0,  0,-10, -5,  5,
 5, 10, 10,-20,-20, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0]

#GET SUM OF PAWN SCORE
def get_pawn_score(piece_name, piece_color):
    score = 0
    for v in list(board.pieces(chess.PAWN, chess.WHITE)):
        score += PAWNSCORE[v]
    return score

print(get_pawn_score(board))