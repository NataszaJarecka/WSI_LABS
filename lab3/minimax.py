import random

def minimax(evaluation, depth, state, move_max, max_player, min_player, alpha, beta):
    if state.is_finished() or depth == 0:
        return evaluation(state, max_player, min_player), None

    possible_moves = state.get_moves()
    random.shuffle(possible_moves)

    if move_max:

        max_eval = -float('inf')
        for move in possible_moves:

            new_state = state.make_move(move)

            eval_value, _ = minimax(evaluation, depth - 1, new_state, not move_max, max_player, min_player, alpha, beta)
            if eval_value > max_eval:

                max_eval = eval_value
                best_move = move


            alpha = max(alpha, eval_value)
            if alpha >= beta:
                break

        return max_eval, best_move

    else:
        min_eval = float('inf')
        for move in possible_moves:


            new_state = state.make_move(move)

            eval_value, _ = minimax(evaluation, depth - 1, new_state, not move_max, max_player, min_player, alpha, beta)
            if eval_value < min_eval:

                min_eval = eval_value
                best_move = move

            beta = min(beta, eval_value)
            if alpha >= beta:
                break

        return min_eval, best_move
