# Clue
Clue guessing bot


First problem the upperbound on a 3 player game is managable as already shown but the worst case is a 6 player game.
Less cards are certain from the onset
6 choose 1 * 3 * 15 choose 3 * 12 choose 3 * 9 choose 3 * 6 choose 3 = 3027024000 this might be unmanagable but even in the worst case it drops quickly
Making this a generator would shink ram consumption drastically.
It's technically a csp, look for libs that can construct sets based on csp?
