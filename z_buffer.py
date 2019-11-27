import tkinter as tk
import numpy as np
import math

class App:
	def __init__(self, root):
		self.master = root
		self.z_buffer = np.full((1366, 768), -100000)
		self.color_buffer = np.empty((1366, 768), dtype=object)
		self.fill_buffer()
		self.canvas = tk.Canvas(self.master, height=768, width=1366)
		self.canvas.grid(row=0, column=0)

		self.center_x = int(1366/2)
		self.center_y = int(768/2)

		self.fill_buffer()
		self.draw_obj_1()
		self.draw_obj_2()
		self.draw_obj_3()
		self.draw_obj_4()
		self.draw_obj_5()
		self.draw_color_buffer()

	def fill_buffer(self):
		for i in range(0, 1366):
			for j in range(0, 768):
				self.color_buffer[i][j] = '#000000'



	def draw_color_buffer(self):
		if self.canvas:
			self.canvas.delete('all')
			self.canvas = None

		self.canvas = tk.Canvas(self.master, height=768, width=1366, 
		background="#000000")        
		self.canvas.grid(row=0, column=0)

		for line in range(len(self.color_buffer)):
			for column in range(len(self.color_buffer[line])):
				
				# print(f'{line}, {column} ')
				if self.color_buffer[line][column]!='#000000':
					self.canvas.create_line(line, column, line+1,column,
					fill=self.color_buffer[line][column])


	def draw_obj_1(self):
		x_points = [i for i in range(int(self.center_x)+10, int(self.center_x)+31)]
		y_points = [i for i in range(int(self.center_y)+20, int(self.center_y)+41)]
		color = '#0000ff'
		for x in x_points:
			for y in y_points:
				z = x*x + y
				if self.z_buffer[x][y] < z:
					# print(f'x: {x} y:{y}')
					self.z_buffer[x][y] = z
					self.color_buffer[x][y] = color



	def draw_obj_2(self):
		x_points = [i for i in range(int(self.center_x)+50, int(self.center_x)+101)]
		y_points = [i for i in range(int(self.center_y)+30, int(self.center_y)+81)]
		color = '#ff0000'
		
		for x in x_points:
			for y in y_points:
				z = 3*x + 2*y + 5
				if self.z_buffer[x][y] < z:
					self.z_buffer[x][y] = z
					self.color_buffer[x][y] = color



	def draw_obj_3(self):
		color = '#ffff00'
		for t in range(0, 51):
			for alpha in np.arange(0, 2*math.pi, 0.01):
				# print(alpha)
				z = 10+t
				x = int(30 + t * math.cos(alpha))
				y = int(50 + t*math.sin(alpha))
				# print(f'x: {x}, y:{y}')
				# 	print(f'x:{self.center_x}, y:{self.center_y}')
				
				if self.z_buffer[x+self.center_x][y+self.center_y] < z:
					self.z_buffer[x+self.center_x][y+self.center_y] = z
					self.color_buffer[x+self.center_x][y+self.center_y] = color


	def draw_obj_4(self):
		color = '#00ff00'
		for alpha in np.arange(0, 2*math.pi, .01):
			for beta in np.arange(0, 2*math.pi, .01):
				z = 20+30*math.sin(alpha)
				x = int(100+30*math.cos(alpha)*math.cos(beta))
				y = int(50+30*math.cos(alpha)*math.sin(beta))
				
				if (self.z_buffer[self.center_x+x][self.center_y+y] < z):
					self.z_buffer[x+self.center_x][y+self.center_y] = z
					self.color_buffer[x+self.center_x][y+self.center_y] = color				



	def draw_obj_5(self):
		color = '#ffffff'
		for x in range(0,41):
			for y in range(0, 41):
				for z in range(0, 41):
					if(self.z_buffer[x+self.center_x][self.center_y+y] < z):
						self.z_buffer[self.center_x+x][self.center_y+y] = z
						self.color_buffer[self.center_x+x][self.center_y+y] = color				


		

if __name__ == '__main__':
	root = tk.Tk()
	app = App(root)
	root.mainloop()