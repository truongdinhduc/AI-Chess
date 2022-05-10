import chess
board = chess.Board()
print(board)
# get position of King in board
print(list(board.pieces(chess.ROOK, chess.BLACK)))
PAWNSCORE = [0,  0,  0,  0,  0,  0,  0,  0,
             50, 50, 50, 50, 50, 50, 50, 50,
             10, 10, 20, 30, 30, 20, 10, 10,
             5,  5, 10, 25, 25, 10,  5,  5,
             0,  0,  0, 20, 20,  0,  0,  0,
             5, -5, -10,  0,  0, -10, -5,  5,
             5, 10, 10, -20, -20, 10, 10,  5,
             0,  0,  0,  0,  0,  0,  0,  0]

# GET SUM OF PAWN SCORE
# quan trang la chu hoa
# quan den chu thuong
# pawnscore dang danh cho quan trang
# pawn  = 1, knight  = 2, bishop = 3, rook = 4, queen = 5, king = 6
dict = {}
def get_position_score(piece_name, piece_color):
    score = 0
    for v in list(board.pieces(piece_name, piece_color)):
        score += PAWNSCORE[v]
    return score


print(str(chess.ROOK))
print(get_position_score(chess.PAWN, chess.WHITE))
