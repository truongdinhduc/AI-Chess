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
KNIGHTSCORE = [-50, -40, -30, -30, -30, -30, -40, -50,
                -40, -20, 0, 0, 0, 0, -20, -40,
                -30, 0, 10, 15, 15, 10, 0, -30,
                -30, 5, 15, 20, 20, 15, 5, -30,
                -30, 0, 15, 20, 20, 15, 0, -30,
                -30, 5, 10, 15, 15, 10, 5, -30,
                -40, -20, 0, 5, 5, 0, -20, -40,
# GET SUM OF PAWN SCORE
# quan trang la chu hoa
# quan den chu thuong
# pawnscore dang danh cho quan trang
# pawn  = 1, knight  = 2, bishop = 3, rook = 4, queen = 5, king = 6
dict = {'1': PAWNSCORE, '2': KNIGHTSCORE, '3': 3, '4': 4, '5': 5, '6': 6}
def get_position_score(piece_name, piece_color):
    score = 0
    for v in list(board.pieces(piece_name, piece_color)):
        score += PAWNSCORE[v]
    return score


print(str(chess.ROOK))
print(get_position_score(chess.PAWN, chess.WHITE))
