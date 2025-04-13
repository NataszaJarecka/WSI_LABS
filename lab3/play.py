from evaluation import evaluate_move
from minimax import minimax
from two_player_games.player import Player
from two_player_games.games.connect_four import ConnectFourMove, ConnectFour, ConnectFourState

def play(depth1, depth2, max_first):

    player1 = Player("1")
    player2 = Player("2")
    game = ConnectFour((7,6), player1, player2)

    if max_first == True:
        max_player = player1
        min_player = player2

    else:
        max_player = player2
        min_player = player1




    while not game.is_finished():
        if game.get_current_player() == max_player:
            max_move = True
            depth = depth1
        else:
            max_move = False
            depth = depth2

        _, move = minimax(evaluate_move, depth, game, max_move, max_player, min_player, float('-inf'), float("inf"))

        game.make_move(move)
        #print(game.state)

    winner = game.get_winner()
    if winner:
        return winner



