from time import sleep
import pygame as p
from zmq import DEALER
import minimax_agent
import random_agent
import chess
import array

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 60
IMAGES = {}


def loadImage():
    pieces = ['wp', 'bp', 'wn', 'bn', 'wr',
              'br', 'wb', 'bb', 'wq', 'bq', 'wk', 'bk']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(
            "images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def drawboard(screen):
    color = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            p.draw.rect(screen, color[(r + c) % 2],
                        (c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawpiece(screen, board):
    color = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            p.draw.rect(screen, color[(r + c) % 2],
                        (c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            if piece != '--':
                screen.blit(IMAGES[piece], (c * SQ_SIZE, r * SQ_SIZE))


def convert_to_int(board):
    dict = {
        '♚': 'bk',
        '♛': 'bq',
        '♜': 'br',
        '♝': 'bb',
        '♞': 'bn',
        '♟': 'bp',
        '⭘': '--',
        '♙': 'wp',
        '♘': 'wn',
        '♗': 'wb',
        '♖': 'wr',
        '♕': 'wq',
        '♔': 'wk'
    }
    unicode = board.unicode()
    newboard = [
        [dict[c] for c in row.split()]
        for row in unicode.split('\n')
    ]
    return newboard


def main():
    p.init()
    PLAYER = True
    screen = p.display.set_mode((WIDTH, HEIGHT))
    board = chess.Board()
    player1 = minimax_agent.MinimaxPlayer(PLAYER)
    player2 = minimax_agent.MinimaxPlayer(False)
    drawboard(screen)
    loadImage()
    while not board.is_game_over():
        if board.turn == player1.player:
            move = player1.get_move(board, 3)
            board.push(move)
        else:
            move = player2.get_move(board, 3)
            board.push(move)
        drawpiece(screen, convert_to_int(board))
        p.display.flip()
        sleep(0.5)
    print(board.result())


main()
