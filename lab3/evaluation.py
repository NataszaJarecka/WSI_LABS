from two_player_games.games.connect_four import ConnectFourState, ConnectFourMove
from two_player_games.player import Player


def evaluate_move(state: ConnectFourState, max_player: Player, min_player: Player) -> int:
    winner = state.get_winner()

    if winner is not None:
        if winner.char == max_player.char:
            return 1
        elif winner.char == min_player.char:
            return -1
    return 0
