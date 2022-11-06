# LAB2 - Set covering with Genetic Algorithm

I tried to solve the problem using 2 values of fitness (in order of importance):
- first one is the number of uncovered elements in the current solution
- second one is the actual weight, as the sum of lenght of the subsets considered in the solution

I've chosen to work with a binary rappresentation, as I though it would have been easy to work with.

In the table below you can see some of the results I got using it.

## Strategies

For the crossover I implemented 2 functions: the first one is a singole one-point crossover, with rundomized cut point.
The second one is a duble-point crossover: 2 individuals are created, the first has part 1 and 3 of the first parent and part 2 of the second parent. The second individual has part 1 and 3 of the second parent and part 2 of the first parent.

For the mutation, there is a 20% probability of performin mutations. Within this probability, for each solution there is a 10% probability to be mutated. If a solution is selected to be mutated, then we perform up to 5 mutation (the number of mutations is randomized).
Did I already say the word... mutation? lol

## Some results
| N  | weight | time |
|:----:|:--------:|------|
| 5  |    5    |   8.8s   |
| 10 |   10     |   18.6s   |
| 20 |    23    |   23.5s   |
| 50 |    70    |   1m 4s   |
| 100 |   192     |   4min 6.2s   |
| 200 |   1554     |   11min 27.5s   |

Parameters changes for every run, but in general are:
- population: 10 * N
- max useless generations: 1000

## A little auto review
The algorithm works fine, but it doesn't scale really well. I left the program running for an hour with N = 500, population 5000 and a useless generations cap at 1000, and still no result was provided.

Possible problems could be:
- the number of mutations: I randomize a number of mutations (up to 5) for each possible solutions. I got this idea from a youtube video (link is below) and it leads to better solutions in generale, but that could be one of the reason why it takes so long.
- probably the fitness function of counting the number of uncovered elements is not so scalable.

## Resources used
[Micah Burkhardt youtube video](https://www.youtube.com/watch?v=gsq_Rp0u4V4&t=1036s)