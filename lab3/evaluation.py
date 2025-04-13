from two_player_games.games.connect_four import ConnectFourState, ConnectFourMove
from two_player_games.player import Player


def count_all_alignments(state: ConnectFourState, player: Player) -> dict:
    counts = {2: 0, 3: 0, 4: 0, 'split_3': 0}
    cols = len(state.fields)
    rows = len(state.fields[0])
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

    def in_bounds(c, r):
        return 0 <= c < cols and 0 <= r < rows

    for c in range(cols):
        for r in range(rows):
            for dc, dr in directions:

                prev_c, prev_r = c - dc, r - dr
                if in_bounds(prev_c, prev_r) and state.fields[prev_c][prev_r] == player:
                    continue


                if not in_bounds(c + dc * 3, r + dr * 3):
                    continue


                alignment = [state.fields[c + dc * i][r + dr * i] for i in range(4)]
                player_count = alignment.count(player)
                empty_count = alignment.count(None)


                if player_count + empty_count == 4 and player_count > 1:
                    counts[player_count] += 1


                if player_count == 3 and empty_count == 1:
                    if (
                        alignment[0] == player and alignment[2] == player and alignment[3] == player and alignment[1] is None or
                        alignment[0] == player and alignment[1] == player and alignment[3] == player and alignment[2] is None
                    ):
                        counts['split_3'] += 1

    return counts


def evaluate_move(state: ConnectFourState, max_player: Player, min_player: Player) -> int:
    winner = state.get_winner()

    if winner is not None:
        if winner.char == max_player.char:
            return 100000
        elif winner.char == min_player.char:
            return -100000

    max_counts = count_all_alignments(state, max_player)
    min_counts = count_all_alignments(state, min_player)

    score = 0


    total_cells = len(state.fields) * len(state.fields[0])
    empty_cells = sum(col.count(None) for col in state.fields)
    game_progress = 1 - (empty_cells / total_cells)


    score += max_counts[4] * 100000
    score += max_counts[3] * int(500 + 200 * game_progress)
    score += max_counts[2] * 100
    score += max_counts['split_3'] * 300


    score -= min_counts[4] * 100000
    score -= min_counts[3] * int(600 + 300 * game_progress)
    score -= min_counts[2] * 100
    score -= min_counts['split_3'] * 350


    center_col = len(state.fields) // 2
    for col in range(len(state.fields)):
        center_weight = (len(state.fields) - abs(center_col - col))
        for row in range(len(state.fields[col])):
            cell = state.fields[col][row]
            if cell == max_player:
                score += center_weight * 2
            elif cell == min_player:
                score -= center_weight * 2

    return score
