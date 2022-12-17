# Free for personal or classroom use; see 'LICENSE.md' for details.
# https://github.com/squillero/computational-intelligence

import logging
import argparse
import random
import quarto
from RLAgent import RLAgent, quarto_to_tuple
import copy
import numpy as np

class RandomPlayer(quarto.Player):
    """Random player"""

    def __init__(self, quarto: quarto.Quarto) -> None:
        super().__init__(quarto)

    def choose_piece(self) -> int:
        return random.randint(0, 15)

    def place_piece(self) -> tuple[int, int]:
        return random.randint(0, 3), random.randint(0, 3)

def learning_phase():
    EPISODES = 25000
    SHOW_EVERY = 3000
    wincount = 0

    for episode in range(EPISODES):
        game = quarto.Quarto()
        agent = RLAgent(game)
        game.set_players((RandomPlayer(game), agent))
        
        winner = -1
        while winner < 0 and not game.check_finished():
            if episode % SHOW_EVERY == 0: game.print()
            piece_ok = False
            while not piece_ok:
                piece_ok = game.select(game.get_current_player().choose_piece())
            piece_ok = False
            game.set_current_player((game.get_current_player_id() + 1) % game.MAX_PLAYERS)
            if episode % SHOW_EVERY == 0: game.print()
            prev_tuple_state = quarto_to_tuple(game)
            while not piece_ok:
                x, y = game.get_current_player().place_piece()
                piece_ok = game.place(x, y)
            
            # here the piece is placed, so new state
            new_tuple_state = quarto_to_tuple(game)
            winner = game.check_winner()
            reward = -2
            if new_tuple_state not in agent._q_table:
                agent._q_table[new_tuple_state] = np.random.uniform(low=-2, high=0, size=(16, 16))

            if winner < 0:  # if not in a final state
                # Maximum possible Q value in next step (for new state)
                max_future_q = np.max(agent._q_table[new_tuple_state])  #TODO check this thing
                # Current Q value (for current state and performed action)
                current_q = agent._q_table[prev_tuple_state][game.get_selected_piece()][y * 4 + x]
                # And here's our equation for a new Q value for current state and action
                new_q = (1 - agent._learning_rate) * current_q + agent._learning_rate * (reward + agent._discount * max_future_q)
                # Update Q table with new Q value
                agent._q_table[prev_tuple_state][game.get_selected_piece()][y * 4 + x] = new_q
            else:   # if in a file state
                agent._q_table[prev_tuple_state][game.get_selected_piece()][y * 4 + x] = 0
    
        if winner == 1: wincount += 1
        if episode % SHOW_EVERY == 0:
            print(f"Episode {episode} - winrate: {wincount/SHOW_EVERY*100:.2f}%")
            wincount = 0
        print(f"finished episode {episode}")


def main():
    game = quarto.Quarto()
    game.set_players((RandomPlayer(game), RandomPlayer(game)))
    winner = game.run()
    logging.warning(f"main: Winner: player {winner}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', default=0, help='increase log verbosity')
    parser.add_argument('-d',
                        '--debug',
                        action='store_const',
                        dest='verbose',
                        const=2,
                        help='log debug messages (same as -vv)')
    args = parser.parse_args()

    if args.verbose == 0:
        logging.getLogger().setLevel(level=logging.WARNING)
    elif args.verbose == 1:
        logging.getLogger().setLevel(level=logging.INFO)
    elif args.verbose == 2:
        logging.getLogger().setLevel(level=logging.DEBUG)

    #main()
    learning_phase()