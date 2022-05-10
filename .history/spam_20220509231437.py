# GET SUM OF PAWN SCORE
# quan trang la chu hoa
# quan den chu thuong
# pawnscore dang danh cho quan trang
# pawn  = 1, knight  = 2, bishop = 3, rook = 4, queen = 5, king = 6
import chess
board = chess.Board()
print(board)
# get position of King in board
print(list(board.pieces(chess.ROOK, chess.BLACK)))
PAWNSCORE = [0,   0,   0,   0,   0,   0,  0,   0,
             98, 134,  61,  95,  68, 126, 34, -11,
             -6,   7,  26,  31,  65,  56, 25, -20,
             -14,  13,   6,  21,  23,  12, 17, -23,
             -27,  -2,  -5,  12,  17,   6, 10, -25,
             -26,  -4,  -4, -10,   3,   3, 33, -12,
             -35,  -1, -20, -23, -15,  24, 38, -22,
             0,   0,   0,   0,   0,   0,  0,   0]
KNIGHTSCORE = [-50, -40, -30, -30, -30, -30, -40, -50,
               -40, -20, 0, 0, 0, 0, -20, -40,
               -30, 0, 10, 15, 15, 10, 0, -30,
               -30, 5, 15, 20, 20, 15, 5, -30,
               -30, 0, 15, 20, 20, 15, 0, -30,
               -30, 5, 10, 15, 15, 10, 5, -30,
               -40, -20, 0, 5, 5, 0, -20, -40,
               -50, -40, -30, -30, -30, -30, -40, -50]
BISHOPSCORE = [-20, -10, -10, -10, -10, -10, -10, -20,
               -10, 0, 0, 0, 0, 0, 0, -10,
               -10, 0, 5, 10, 10, 5, 0, -10,
               -10, 5, 5, 10, 10, 5, 5, -10,
               -10, 0, 10, 10, 10, 10, 0, -10,
               -10, 10, 10, 10, 10, 10, 10, -10,
               -10, 5, 0, 0, 0, 0, 5, -10,
               -20, -10, -10, -10, -10, -10, -10, -20]
ROOKSCORE = [0, 0, 0, 0, 0, 0, 0, 0,
             5, 10, 10, 10, 10, 10, 10, 5,
             -5, 0, 0, 0, 0, 0, 0, -5,
             -5, 0, 0, 0, 0, 0, 0, -5,
             -5, 0, 0, 0, 0, 0, 0, -5,
             -5, 0, 0, 0, 0, 0, 0, -5,
             -5, 0, 0, 0, 0, 0, 0, -5,
             0, 0, 0, 5, 5, 0, 0, 0]
QUEENSCORE = [-20, -10, -10, -5, -5, -10, -10, -20,
              -10, 0, 0, 0, 0, 0, 0, -10,
              -10, 0, 5, 5, 5, 5, 0, -10,
              -5, 0, 5, 5, 5, 5, 0, -5,
              0, 0, 5, 5, 5, 5, 0, -5,
              -10, 5, 5, 5, 5, 5, 0, -10,
              -10, 0, 5, 0, 0, 0, 0, -10,
              -20, -10, -10, -5, -5, -10, -10, -20]
KINGSCORE = [-30, -40, -40, -50, -50, -40, -40, -30,
             -30, -40, -40, -50, -50, -40, -40, -30,
             -30, -40, -40, -50, -50, -40, -40, -30,
             -30, -40, -40, -50, -50, -40, -40, -30,
             -20, -30, -30, -40, -40, -30, -30, -20,
             -10, -20, -20, -20, -20, -20, -20, -10,
             20, 20, 0, 0, 0, 0, 20, 20,
             20, 30, 10, 0, 0, 10, 30, 20]

dict = {'1': PAWNSCORE, '2': KNIGHTSCORE, '3': BISHOPSCORE,
        '4': ROOKSCORE, '5': QUEENSCORE, '6': KINGSCORE}


def get_position_score(piece_name, piece_color):
    score = 0
    for v in list(board.pieces(piece_name, piece_color)):
        score += dict[str(piece_name)][v]
    return score
