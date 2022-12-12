# 3.4: Reinforcment Learning

The implementation of this algorightm is heavily based on the code that was provided to us during lessons.
I added in the Nim class the information about the current player, which now switch after a nimmin action has been done.

The reward to the algorithm is:
- if I'm in a ongoing position: -1
- if I'm in a end position: 0

The problem is that the algorithm does not perform well. 
The main problem in my opinion is that the state is not associated to the move, hence the information about the player turn is lost, with a probability to associate a state to a good reward but in reality it is good for the opponent.
I don't have time to implement it (this lab took me so long 😓) but I think that could be one of the problem.

Looking forward to the peer review to get what I'm missing!
