
def minimax(evaluation, state, depth, game, move_max, alpha, beta):
    if game.is_finished() or depth == 0:
        return evaluation(state)

    possible_moves = game.get_moves()

    if move_max:
        for move in possible_moves:
            alpha = max(alpha, minimax(move, depth - 1, not move_max, alpha, beta))
            if alpha >= beta: return alpha
        return alpha

    else:
        for move in possible_moves:
            beta = min(beta, minimax(move, depth - 1, not move_max, alpha, beta))
            if alpha >= beta: return beta
        return beta




