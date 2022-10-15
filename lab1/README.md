# LAB1 SOLUTIONS

## Greedy solutions
So, I started approaching the problem with a greedy solution and I managed to solve for all the possible values of N.
In the greedy.py file you can see how I solved it, it's really nothing special:
- The first greedy algorithm (that I call `len`) simply iterates until the partial_solution set is equal to the set of the whole numbers (`N=5 {0, 1, 2, 3, 4}`). In each iteration a list is chosen to be added to the partial_solution: the choice is done my selecting the list with the max len difference from the present partial_solution. This is the first approach I thought about and it looks like it works.

- The second greedy algorithm (that I call `ratio`) is very similar to the firts one, but it differs in the way I choose the list to be added to the partial_solution var. In this case, after browsing a little bit and discovering [this site](https://high-python-ext-3-algorithms.readthedocs.io/ko/latest/chapter18.html#set-covering), I noticed that there is a better function that leads to better final weights: the selected list is the one with the minimum `element_added/cost` ratio.

## A* solution
Thanks to the hint from the professor I started working on a A* solution, starting from the examples showed during lessons. I modified the State class a little: the data is now a `set` and each State has a `name`. The `name` does a multiple job:
- the state needed for the computation uses the name to keep track of the used list to arrive to the result (so I can retrieve it at the end and calculate the wieght)
- a blank state is created just to keep track of the pickable list, used in the `possible_actions` function (this could easly be a list, auto peer review :))

The h(.) function that I used is a slightly modified version of the 'ratio' strategy I used in the second greedy algorithm. It's the ratio between `N` and `(N - len(partial_solution) + 1)`.
The `+1` is to make sure I don't overestimate the heuristic cost and to avoid division by zero.

Quick note: the A* solution works well with N <= 20, starting from N = 100 it is incredibly slow. Greedy algorithms work fast with evey N value but they tend to not always yield the best weights values.

That's all, hope to hear some feedback!