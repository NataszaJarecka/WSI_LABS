import random
import copy



def minimax(evaluation, depth, game, move_max, max_player, min_player, alpha, beta):
    if game.is_finished() or depth == 0:
        return evaluation(game.state, max_player, min_player), None

    possible_moves = game.get_moves()
    best_moves = []


    if move_max:

        max_eval = -float('inf')
        for move in sorted(possible_moves, key=lambda m: abs(m.column - 3)):

            game_copy = copy.deepcopy(game)
            game_copy.make_move(move)

            eval_value, _ = minimax(evaluation, depth - 1, game_copy, not move_max, max_player, min_player, alpha, beta)
            if eval_value > max_eval:
                best_moves.clear()
                max_eval = eval_value
                best_moves = [move]
            elif eval_value == max_eval:
                best_moves.append(move)
            alpha = max(alpha, eval_value)
            if alpha >= beta:
                break
        best_move = random.choice(best_moves) if best_moves else None
        return max_eval, best_move

    else:
        min_eval = float('inf')
        for move in sorted(possible_moves, key=lambda m: abs(m.column - 3)):


            game_copy = copy.deepcopy(game)
            game_copy.make_move(move)

            eval_value, _ = minimax(evaluation, depth - 1, game_copy, not move_max, max_player, min_player, alpha, beta)
            if eval_value < min_eval:
                best_moves.clear()
                min_eval = eval_value
                best_moves = [move]
            elif eval_value == min_eval:
                best_moves.append(move)
            beta = min(beta, eval_value)
            if alpha >= beta:
                break
        best_move = random.choice(best_moves) if best_moves else None
        return min_eval, best_move
