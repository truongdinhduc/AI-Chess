import chess
import minimax_agent
import random_agent

PLAYER = True
board = chess.Board()

player1 = minimax_agent.MinimaxPlayer(True)
player2 = random_agent.RandomPlayer()

while not board.is_game_over():
    if board.turn == player1.player:
        move = player1.get_move(board, 3)
        board.push(move)
    else:
        move = player2.get_move(board)
        board.push(move)
    print(board)
    print('-----------------------')

print(board.result())
