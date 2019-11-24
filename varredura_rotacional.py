from cg import CG
import tkinter as tk
import numpy as np
class App:
	
	def __init__(self, root):
		#SETUP INCIAL
		self.z_buffer = np.full((1366, 768), -100000)
		self.color_buffer = np.empty((1366, 768), dtype=object)


		self.l = []
		self.points = []
		self.master = root
		self.center_x = (root.winfo_screenwidth()/2)
		self.center_y = (root.winfo_screenheight()/2)
		
		self.menu = tk.Menu(self.master)
		self.reset = tk.Menu(self.menu)
		self.reset.add_command(label='Reset desenho', command=self.reset_draw)
		self.menu.add_cascade(label='Reset desenho', menu=self.reset)
		self.master.config(menu=self.menu)

		self.canvas = tk.Canvas(self.master, width=self.center_x*2,
		height=self.center_y*2, background='#ffffff')
		self.canvas.grid(row=0, column=0)
		CG.line_breasenham(self.center_x, 0, self.center_x,
		int(self.center_y*2), self.canvas)
		self.canvas.bind('<B1-Motion>', self.mouse_motion)
		self.canvas.bind('<ButtonRelease-1>',self.mouse_release)
		self.fill_buffer()


	def fill_buffer(self):
		for i in range(0, 1366):
			for j in range(0, 768):
				self.color_buffer[i][j] = '#ffffff'

	def reset_draw(self):
		if self.canvas:
			self.canvas.delete('all')
			self.canvas = None
		self.canvas = tk.Canvas(self.master, width=self.center_x*2,
		height=self.center_y*2, background='#ffffff')
		self.canvas.grid(row=0, column=0)
		CG.line_breasenham(self.center_x, 0, self.center_x,
		int(self.center_y*2), self.canvas)
		self.canvas.bind('<B1-Motion>', self.mouse_motion)
		self.canvas.bind('<ButtonRelease-1>',self.mouse_release)
		self.l = []
		self.points = []
		self.z_buffer = np.full((1366, 768), -100000)
		self.color_buffer = np.empty((1366, 768), dtype=object)
		self.fill_buffer()

	#METODOS PARA PEGAR O TRAÇADO DO MOUSE E DESENHAR
	def mouse_motion(self, event):
		print(f'Posição do Mouse: {event.x} {event.y}')
		self.x1 = event.x
		self.y1 = event.y
		self.points.append((event.x-self.center_x, 0, event.y))
		CG.line_breasenham(event.x, event.y, event.x+1, event.y+1, self.canvas)


	def mouse_release(self, event):
		print(f'Posição do Mouse: {event.x} {event.y}')
		self.x1 = event.x
		self.y1 = event.y

		self.points.append((event.x-self.center_x, 0, event.y))
		CG.line_breasenham(event.x, event.y, event.x+1, event.y+1, self.canvas)

		#CHAMADA 
		for points in self.points:
			# print(points)
			# input()
			self.circunferencia(self.center_x, points[1],
			points[0], points[2], self.canvas)


		for pontos in self.l:
			if self.z_buffer[int(pontos[0])][int(pontos[1])] < pontos[2]:
				self.color_buffer[int(pontos[0])][int(pontos[1])] = '#000000'
				# self.canvas.create_line(pontos[0],pontos[1], pontos[0]+1,pontos[1], fill='#000000')
		self.draw_color_buffer()

	def draw_color_buffer(self):
		if self.canvas:
			self.canvas.delete('all')
			self.canvas = None

		self.canvas = tk.Canvas(self.master, height=768, width=1366, 
		background="#ffffff")        
		self.canvas.grid(row=0, column=0)

		for line in range(len(self.color_buffer)):
			for column in range(len(self.color_buffer[line])):
				# print(self.rgb2hex(self.color_buffer[line][column]))
				# print(f'{line}, {column} ')
				if self.color_buffer[line][column]!='#ffffff':
					self.canvas.create_line(line, column, line+1,column,
					fill=self.color_buffer[line][column])




	
	def cavaleira(self, x, y, z):
		
		Mc = np.array([[1, 0, 0, 0],
						[0, 1, 0, 0],
						[((2)**(1/2))/2, ((2)**(1/2))/2, 0, 0],
						[0, 0, 0, 1]])
        
		return np.dot(np.array([x, y, z, 1]), Mc)
    

	def circunferencia(self, xc, yc, r, z, canvas):
		# print(r)
		# input()
		print('entrou circunferencia')
		x = 0
		y = r
		d = 3 - 2*r
		self.draw_circle(xc, yc, x, y, z,  canvas)
		print(f'xc: {xc}, yc: {yc}, x: {x}, y: {y}, r: {r}, d: {d}')
		while y >= x:
			x += 1
			if d > 0:
				print(y)
				y -=1
				d += 4*(x-y) + 10
			else:
				d+=4*(x) + 6
			self.draw_circle(xc, yc, x, y, z, canvas)
			print(f'xc: {xc}, yc: {yc}, x: {x}, y: {y}, r: {r}, d: {d}')


	def draw_circle(self, xc, yc, x, y, z, canvas):

		

		self.l.append(self.cavaleira(xc+x, yc+y, z))
		self.l.append(self.cavaleira(xc-x, yc+y, z))
		self.l.append(self.cavaleira(xc+x, yc-y, z))
		self.l.append(self.cavaleira(xc-x, yc-y, z))
		self.l.append(self.cavaleira(xc+y, yc+x, z))
		self.l.append(self.cavaleira(xc-y, yc+x, z))
		self.l.append(self.cavaleira(xc+y, yc-x, z))
		self.l.append(self.cavaleira(xc-y, yc-x, z))
		
		






if __name__ == '__main__':
	root = tk.Tk()
	app  = App(root)
	root.mainloop()