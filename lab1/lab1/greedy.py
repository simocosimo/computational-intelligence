import random

def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]

# This is the solution I implemented once I started questioning the criteria to
# use to select the best candidate to insert into the solution
def greedy_solution_ratio(N: int, subsets: dict):
    set_subsets = set(e for s in subsets.keys() for e in subsets[s])
    u = set(range(N))
    if set_subsets != u:
        return None

    partial_solution = set()
    index_solution = []

    while partial_solution != u:
        min_ratio = float("inf")
        min_key = None

        # I took inspiration from the below link for this decision function
        # in this greedy implementation
        # https://high-python-ext-3-algorithms.readthedocs.io/ko/latest/chapter18.html#set-covering
        for s, l in subsets.items():
            len_info = len(l - partial_solution)
            if len_info != 0:
                ratio = len(l) / len_info
                if ratio < min_ratio:
                    min_ratio = ratio
                    min_key = s
        index_solution.append(min_key)
        partial_solution = set.union(partial_solution, subsets[min_key])
    return index_solution

# This was the solution I came up with initially
def greedy_solution_len(N: int, subsets: dict):
    set_subsets = set(e for s in subsets.keys() for e in subsets[s])
    u = set(range(N))
    if set_subsets != u:
        return None

    partial_solution = set()
    index_solution = []

    while partial_solution != u:
        vals = list(subsets.values())
        choosen_set = max(vals, key=lambda s: len(s - partial_solution))
        min_key = list(subsets.keys())[vals.index(choosen_set)]

        index_solution.append(min_key)
        partial_solution = set.union(partial_solution, choosen_set)
    return index_solution

# Solution based on powersets
def powerset_solution():
    # TODO
    return

def main(N, alg='ratio'):
    choices = problem(N, 42)
    gen = {'S'+str(key):set(value) for key, value in enumerate(choices) }

    if alg == 'ratio':
        # Executing greedy alg with ratio decision function
        index_sol = greedy_solution_ratio(N, gen)
        w = sum(len(gen[n]) for n in index_sol)
        if index_sol is None:
            print("Cannot find solution")
            return
        # for n in index_sol: print(n, gen[n])
        print(f"- Solution with ratio function (greedy): {w}")
    else:
        # Executing greedy alg with len decision function
        index_sol = greedy_solution_len(N, gen)
        w = sum(len(gen[n]) for n in index_sol)
        if index_sol is None:
            print("Cannot find solution")
            return
        # for n in index_sol: print(n, gen[n])
        print(f"- Solution with len function (greedy): {w}")

if __name__ == "__main__":
    for i in [5, 10, 20, 100, 500, 1000]:
        print(f"With N = {i}")
        main(i, 'ratio')
        main(i, 'len')
