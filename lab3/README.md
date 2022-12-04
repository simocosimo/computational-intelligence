# Lab3 - Nim

## 3.1: nim-sum
Implementation of nim-sum was already done during lecture. It wasn't clear what was requested for this point to be honest.

## 3.1: evolving rules
I really tried my best to understand what was the meaning of "evolving fixed rules" since rules are... fixed. And I also couldn't understand defining a parameter and evolving it, since no metter what, the rules would be always the same ones.

So I tried to implement an evolving strategy with some concepts that I got from here.
The solution is based on building random functions that evaluate the nim configurations.

The result of these functions represent the current state of the game:
- P-position: if result is 0. This means that the position is an advantage for the player that just moved
- N-position: if result is not 0. This means that the position is an advanget for the player that is about to move

With this concept in mind, we can check if some mathematical theormes are satisfied:
- After a move, every P-position generate configurations which are all N-positions
- After a move, every N-position generate at least one P-Position configuration
- The winnin state is always a P-position

### Chromosome
It is composed by genomes that represents:
- terminal symbols: indices that point to a value in the nim configuration
- function symbols: math functions that operate on terminal symbols

Example:
- [0] = 2
- [1] = 5
- [2] = - 1, 0
- [3] = 4
- [4] = 9
- [5] = * 0, 2

Which translates into 
```
2 * (5 - 2)
```
Remember that the number you see here are indices into a nim configuration, so if nim config is `(1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21)` it will be translated into
```
5 * (11 - 5)
```

### Fitness
Here comes the trouble lol
So originally the fitness function takes a chromosome and evalutes the whole game tree starting from the initial nim configuration. The result of the fintess function is a value that represnts the times that the chromosome didn't respect the rules specified before.

But this is so slow that if I do it I might miss Christmas. 

I think there is also no way to prune the game tree because the evaluation should be done with different chromosomes each time, so no way to skip some already-done computation, since there will be none (correct me if I'm wrong, though).
I made an attempt to code this, I correctly built the game tree and evaluated the first rule. No luck on the other ones, since I should do multiple 

So my fitness works this way: 50 games against `pure_random`. The fitness value is the loss rate, so I need to minimize that.

### Genetic strategies
I defined 2 crossover functions (single and double point), but the single point one seems to be the best.

Binary tournament selects two candidates, with a starting probability of 0.8, they are crossovered. They generate an offspring of size 2. This 2 new individual have an opportunity to be mutated twice, instantly.
If they are not crossovered, they are mutated, twice.

Then I add the best one in the offspring to the population and remove the new worst one.

Mutation is simple, just select a random symbol (both terminal or function) with the exeption of the first gene in the chromosome, which always need to be terminal.

## Results

For the genetic approach: the best I could get was a chromosome that was able to win against a random strategy 72% of the times. This was a best result, the more common case was around 64%.