# Day 04

## Instructions

From inside this folder, run the following (where x is replaced with 1 or 2):

`python3 day04.x.py`

You may optionally run either program with a specified source file:

`python3 day04.x.py example.txt`

## Thoughts

I was initially caught off guard by the challenge of parsing the text. I wrestled with whether or not it was worth composing the data into nested lists to simulate bingo grids, but ultimately I decided it was worth it because it would make the processing of the data more coherent later on. In theory I could have just stored every bingo table in a flat list because the size of each bingo board is constant, but it would have required so many modulus operators to make sense of that even Carl Gauss's head would spin.

After writing the first challenge, I realized that most of the logic could be reused in the second challenge so I created a `bingo.py` module. I also thought it would be fun to allow an argument to be passed for the desired txt file, so this is implemented as well.
