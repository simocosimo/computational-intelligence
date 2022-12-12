# 3.2: Minmax
The approach I used is a really standard minmax algorithm with alpha-beta pruning and the use of cache and depth limit to speed up the computation a little bit.

## Cache
I think I would explain my use of the cache since it was the major problematic component for me, developing this algorithm. 
The way I implemented the cache is the following:
- The cache is indexed by the tuple (configuration, player). The player is needed because we don't want to use the evaluation done as a another player.
- I add an evaluation to cache only if the subtree I'm considering was completely explored. If I evaluate a subtree partially (maybe because I reach depth limit) I don't want to add it to cache because there's the risk that, in the future, I might use that incomplete computation to make a choice, instead of exploring the subtree completely.

## Possible improvements
I think there's some ground for improvements in the evaluation function.
When I compare the eval with the maxEval/minEval, I just do it by the evaluation function, so if 2 moves generate a configuration with the same evaluation, the first one that was computed is taken.

But sometimes a later-evaluated move would be better. In order to fix this I think we pretty much have to use the nim-sum formula, but that would against the scope of the project obviusly.
Another way that comes to my mind to try to get better result is to randomly shuffle the list of possible moves, so that no particular move is more important than others.

## Results
I can win consistently against pure_random with this strategy. No luck winning against nim-sum though :(
