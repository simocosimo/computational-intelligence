from gx_utils import *
import random

import logging
from typing import Callable

logging.basicConfig(format="%(message)s", level=logging.INFO)

def problem(N, seed=None):
    random.seed(seed)
    return [
        set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2)))
        for n in range(random.randint(N, N * 5))
    ]

class State:
    def __init__(self, data: set, name: str):
        self._data = data.copy()
        self._name = name

    def __hash__(self):
        return hash(bytes(self._data))

    def __eq__(self, other):
        return bytes(self._data) == bytes(other._data)

    def __lt__(self, other):
        return bytes(self._data) < bytes(other._data)

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return repr(self.name + " " + str(self._data))

    @property
    def data(self):
        return self._data

    @property
    def name(self):
        return self._name

    def copy_data(self):
        return self._data.copy()

    def combine_data(self, s: set):
        self._data |= s

    def combine_name(self, s: str):
        self._data |= set(s)

def search(
    initial_state: State,
    goal_test: Callable,
    parent_state: dict,
    state_cost: dict,
    priority_function: Callable,
    unit_cost: Callable,
    N: int,
    gen: dict
):
    frontier = PriorityQueue()
    parent_state.clear()
    state_cost.clear()

    state = initial_state
    name_state = State(set(), "name_state")
    parent_state[state] = None
    state_cost[state] = 0

    while state is not None and not goal_test(N, state):
        for label, a in possible_actions(gen, name_state).items():
            new_state = result(state, name_state, a, label)
            #print(new_state)
            cost = unit_cost(a)
            if new_state not in state_cost and new_state not in frontier:
                parent_state[new_state] = state
                state_cost[new_state] = state_cost[state] + cost
                frontier.push(new_state, p=priority_function(N, new_state))
                logging.debug(f"Added new node to frontier (cost={state_cost[new_state]})")
            elif new_state in frontier and state_cost[new_state] > state_cost[state] + cost:
                old_cost = state_cost[new_state]
                parent_state[new_state] = state
                state_cost[new_state] = state_cost[state] + cost
                logging.debug(f"Updated node cost in frontier: {old_cost} -> {state_cost[new_state]}")
        if frontier:
            state = frontier.pop()
        else:
            state = None

    path = list()
    s = state
    while s:
        path.append(s)
        s = parent_state[s]

    logging.info(f"Found a solution in {len(path):,} steps; visited {len(state_cost):,} states")
    return list(reversed(path))

def h(N: int, state: State):
    return int(N / (N + 1 - len(state.data)))

def result(state: State, name_state: State, s: set, label: str):
    name_state.combine_name(label)
    new_data = set.union(state.copy_data(), s)
    return State(new_data, state.name + label + '-')

def goal_test(N: int, state: State):
    return set(range(N)) == state.data

def possible_actions(gen: dict, name_state: State):
    return {k:s for k, s in gen.items() if k not in name_state.data}

def main():
    parent_state = dict()
    state_cost = dict()

    # Better take some days(months?) off when it starts computing with N >= 100 lol
    #for N in [5, 10, 20, 100, 500, 1000]:
    for N in [5, 10, 20]:
        gen = {'S'+str(key):set(value) for key, value in enumerate(problem(N, 42)) }
        final = search(
            State(set(), ""),
            goal_test=goal_test,
            parent_state=parent_state,
            state_cost=state_cost,
            priority_function=lambda n, s: state_cost[s] + h(n, s),
            unit_cost=lambda a: len(a),
            N=N,
            gen=gen
        )
        
        chosen_lists = final[-1].name.split('-')[:-1]
        w = sum(len(gen[l]) for l in chosen_lists)
        print(f"Solution weight is {w}")
        print(final)

if __name__ == "__main__":
    main()