# John Conway's Game of Life

> You know, people think that mathematics is complicated. Mathematics is the simple bit. It's the stuff we can understand. It's cats that are complicated. I mean, what is it in those little molecules and stuff that make one cat behave differently to another? Or that make a cat? How do you define a cat? I have no idea." - John Horton Conway 

John Horton Conway, pioneering Mathematician and creator of the Game of Life, was sadly lost to covid-19 in April.

As a tribute, this is my take on the famous John Conway's [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). The board is initiated with a random number generator between 0 and 1 drawing samples from a uniform distribution; any cell with a number samller than 0.1 will be initiated with an alive-cell. The game will run for 500 generations and the process is animated with *matplotlib.animation.FuncAnimation*. By default, the board will have a dimension of 150x150. 

The Game of Life, also known simply as Life, is a cellular automaton was invented in 1970. With only 3 basic rules, unpredictable and complex patterns seemingly evolve into creatures. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.

The rules of John Conway's Game of Life are as followed:
* Any live cell with two or three live neighbours survives.
* Any dead cell with three live neighbours becomes a live cell.
* All other live cells die in the next generation. Similarly, all other dead cells stay dead.

The following is a sample outcome:

![](game_of_life.gif)

Simply run the script as followed:

```python game_of_life.py -weight 200 -height 200```
