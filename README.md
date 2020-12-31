# Conway_Game_of_Life
This is my take on the famous John Conway's [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). The board is initiated with a random number generator between 0 and 1 drawing samples from a uniform distribution; any cell with a number samller than 0.1 will be initiated with an alive-cell. The game will run for 500 generations and the process is animated with *matplotlib.animation.FuncAnimation*. By default, the board will have a dimension of 150x150. 

The rules of John Conway's Game of Life are as followed:
* Any live cell with two or three live neighbours survives.
* Any dead cell with three live neighbours becomes a live cell.
* All other live cells die in the next generation. Similarly, all other dead cells stay dead.

The following is a sample result:

![](game_of_life.gif)

Simply run the script as followed:

```python game_of_life.py -weight 200 -height 200```
