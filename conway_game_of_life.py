import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter  

import os, time, random, sys
import argparse

def main():
	parser = argparse.ArgumentParser(description="Dimension of the Board")
	parser.add_argument('-weight', type=int, default=150, help='The width of the game board')
	parser.add_argument('-height', type=int, default=150, help='The height of the game board')
	args = parser.parse_args()
	game = Board(args.weight,args.height)
	ani = game.animation()
	writer = PillowWriter(fps=60)  
	ani.save("game_of_life.gif", writer=writer)  
	plt.show()
	
	
class Board:
	def __init__(self,w,h):
		self.w = w
		self.h = h
		self.state = {}
		for y in range(self.h):
			for x in range(self.w):
				self.state[x,y] = 1 if random.uniform(0, 1) <0.1 else 0
		self.fig1 = plt.figure()		
	def initialState(self):
		max_x, max_y = map(max, zip(*self.state))
		self.grid = [[self.state.get((i,j),0) for i in range(max_x+1)] for j in range(max_y+1)]
		self.im = plt.imshow(self.grid, cmap='binary', origin='lower', interpolation='nearest')	
		return self.im,
		
	def evaluateState(self,x,y):
		count = 0
		for x_neighbor in range(x-1,x+2):
			for y_neighbor in range(y-1,y+2):
				if (x_neighbor,y_neighbor) in self.state and not (x_neighbor == x and y_neighbor == y):
					count += self.state[x_neighbor,y_neighbor]
		return count
		
	def refreshState(self, gen):
		print(f'Running iteration #{gen+1}...')
		new_state = {}
		for x in range(self.w):
			for y in range(self.h):
				neighbors_count = self.evaluateState(x,y)
				#Birth rule: An empty, or “dead,” cell with precisely three “live” neighbors (full cells) becomes live.
				if self.state[x,y]==0 and neighbors_count==3:
					new_state[x,y] = 1
				else:
					new_state[x,y] = 0
				#Death rule: A live cell with zero or one neighbors dies of isolation; a live cell with four or more neighbors dies of overcrowding.
				if self.state[x,y]==1 and neighbors_count<2:
					new_state[x,y] = 0
				if self.state[x,y]==1 and neighbors_count>3:
					new_state[x,y] = 0
				#Survival rule: A live cell with two or three neighbors remains alive.
				if self.state[x,y]==1 and neighbors_count in [2,3]:
					new_state[x,y] = 1
		self.state = new_state
		temp_x, temp_y = map(max, zip(*self.state))
		new_grid = [[self.state.get((i,j),0) for i in range(temp_x+1)] for j in range(temp_y+1)]
		self.im.set_array(new_grid)
		self.grid = new_grid
		return [self.im]
	def animation(self):
		return FuncAnimation(self.fig1, self.refreshState , frames=500,init_func=self.initialState, interval=5, blit=True, repeat=False)
		
		
		
		
if __name__ == '__main__':
    main()