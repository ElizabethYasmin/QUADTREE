import pygame
from pygame.locals import *
import random

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

lines = []


class Node():
	def __init__(self, x0, y0, x1, y1):
		self.x0 = x0
		self.y0 = y0
		self.x1 = x1
		self.y1 = y1
		self.nodes = []
		self.lines = [(x0,y0, (x1-x0), 1), (x0,y0, 1,(x1-x0)), (x0, (y1+y0)/2,  (y1-y0), 1), ((x1+x0)/2,y0,1,(y1-y0))]
		self.sub = []
		for i in range(4):
			self.sub.append(None)

	def divide(self, pnt):



		for point in self.nodes:

			if point.x >= self.x0 and point.x < self.x1/2+self.x0/2 and point.y >= self.y0 and point.y < self.y1/2+self.y0/2:
				if self.sub[0] == None:
					self.sub[0] = Node(self.x0, self.y0, self.x1/2+self.x0/2, self.y1/2+self.y0/2)
					self.sub[0].insert(point, "cuadrante 1")
					print("aqui")
				else:
					self.sub[0].insert(point, "cuadrante 1")

			elif point.x >= self.x1/2+self.x0/2 and point.x < self.x1 and point.y >= self.y0 and point.y < self.y1/2+self.y0/2:
				if self.sub[1] == None:
					self.sub[1] = Node(self.x1/2+self.x0/2, self.y0, self.x1, self.y1/2+self.y0/2)
					self.sub[1].insert(point, "cuadrante 2")
					print("aqui")
				else:
					self.sub[1].insert(point, "cuadrante 2")

			elif point.x >= self.x0 and point.x < self.x1/2+self.x0/2 and point.y >= self.y1/2+self.y0/2 and point.y < self.y1:
				if self.sub[2] == None:
					self.sub[2] = Node(self.x0, self.y1/2+self.y0/2, self.x1/2+self.x0/2, self.y1)
					self.sub[2].insert(point, "cuadrante 3")
					print("aqui")
				else:
					self.sub[2].insert(point, "cuadrante 3")

			elif point.x >= self.x1/2+self.x0/2 and point.x < self.x1 and point.y >= self.y1/2+self.y0/2 and point.y < self.y1:
				if self.sub[3] == None:
					self.sub[3] = Node(self.x1/2+self.x0/2, self.y1/2+self.y0/2, self.x1, self.y1)
					self.sub[3].insert(point, "cuadrante 4")
					print("aqui")
				else:
					self.sub[3].insert(point, "cuadrante 4")


		if pnt.x >= self.x0 and pnt.x < self.x1/2+self.x0/2 and pnt.y >= self.y0 and pnt.y < self.y1/2+self.y0/2:
			if self.sub[0] == None:
				self.sub[0] = Node(self.x0, self.y0, self.x1/2+self.x0/2, self.y1/2+self.y0/2)
				self.sub[0].insert(pnt, "cuadrante 1")
				print("aqui")
			else:
				self.sub[0].insert(pnt, "cuadrante 1")

		elif pnt.x >= self.x1/2+self.x0/2 and pnt.x < self.x1 and pnt.y >= self.y0 and pnt.y < self.y1/2+self.y0/2:
			if self.sub[1] == None:
				self.sub[1] = Node(self.x1/2+self.x0/2, self.y0, self.x1, self.y1/2+self.y0/2)
				self.sub[1].insert(pnt, "cuadrante 2")
				print("aqui")
			else:
				self.sub[1].insert(pnt, "cuadrante 2")

		elif pnt.x >= self.x0 and pnt.x < self.x1/2+self.x0/2 and pnt.y >= self.y1/2+self.y0/2 and pnt.y < self.y1:
			if self.sub[2] == None:
				self.sub[2] = Node(self.x0, self.y1/2+self.y0/2, self.x1/2+self.x0/2, self.y1)
				self.sub[2].insert(pnt, "cuadrante 3")
				print("aqui")
			else:
				self.sub[2].insert(pnt, "cuadrante 3")

		elif pnt.x >= self.x1/2+self.x0/2 and pnt.x < self.x1 and pnt.y >= self.y1/2+self.y0/2 and pnt.y < self.y1:
			if self.sub[3] == None:
				self.sub[3] = Node(self.x1/2+self.x0/2, self.y1/2+self.y0/2, self.x1, self.y1)
				self.sub[3].insert(pnt, "cuadrante 4")
				print("aqui")
			else:
				self.sub[3].insert(pnt, "cuadrante 4")



		"""
		self.sub.append(Node(self.x0, self.y0, self.x1/2+self.x0/2, self.y1/2+self.y0/2))   #CUADRANTE 0	
		self.sub.append(Node(self.x1/2+self.x0/2, self.y0, self.x1, self.y1/2+self.y0/2))	#CUADRANTE 1
	
		self.sub.append(Node(self.x0, self.y1/2+self.y0/2, self.x1/2+self.x0/2, self.y1))   #CUADRANTE 2
		self.sub.append(Node(self.x1/2+self.x0/2, self.y1/2+self.y0/2, self.x1, self.y1))	#CUADRANTE 3
		"""


		

	def insert(self, point, cuadrante):

		#if len(self.sub) ==0:
		if not point in self.nodes:
			if point.x >= self.x0 and point.x < self.x1 and point.y >= self.y0 and point.y < self.y1:
				if len(self.nodes) < 4:
					self.nodes.append(point)
				#print(cuadrante)
				else:
					self.divide(point)
				return
		"""
		j = 0
		for i in self.sub:
			i.insert(point, "cuadrante" + str(j))
			j+=1
		"""

	def get(self,lines):
		if len(self.nodes) >=4:
			for i in range(4):
				lines.append(self.lines[i])

		for i in range(4):
			if self.sub[i] != None:
				self.sub[i].get(lines)


	def get_lines(self):
		lines = []

		self.get(lines)

		return lines

	def getintersect(self, x1,x2,y1,y2):
		points = []

		for i in range(len(self.nodes)):
			if self.nodes[i] != None:
				print(self.nodes[i].x, self.nodes[i].y)
				#print("aqui")
				if self.nodes[i].x < x2 and self.nodes[i].x > x1 and self.nodes[i].y < y2 and self.nodes[i].y > y1:
					print("aqui")
					points.append(self.nodes[i])
		
		return points

def conc(arr, arr2):
	for i in range(len(arr2)):
		if not arr2[i] in arr: 
			arr.append(arr2[i])

def getpoints(root, x1,x2,y1,y2):

	points = []

	a = root.getintersect(x1,x2,y1,y2)

	for i in range(len(a)):
		points.append(a[i])

	print(points)



	if root.sub[0] != None:
		conc(points, getpoints(root.sub[0], x1,x2,y1,y2))
	if root.sub[1] != None:
		conc(points, getpoints(root.sub[1], x1,x2,y1,y2))
	if root.sub[2] != None:
		conc(points, getpoints(root.sub[2], x1,x2,y1,y2))
	if root.sub[3] != None:
		conc(points, getpoints(root.sub[3], x1,x2,y1,y2))

	return points



	"""
	def get(self, x_min, y_min, y_max, x_max, lines):
		if len(self.sub) == 0:
			return

		lines.append((x_min, (y_max+y_min)/2, x_max-x_min, 1))
		lines.append(((x_max+x_min)/2, y_min, 1, y_max-y_min))

		
		self.sub[0].get(x_min, y_min, y_max/2+y_min/2, x_max/2+x_min/2, lines)
		self.sub[1].get(x_max/2+x_min/2, y_min, y_max/2+y_min/2, x_max, lines)
		self.sub[2].get(x_min,y_max/2+y_min/2, y_max, x_max/2+x_min/2, lines)
		self.sub[3].get(x_max/2+x_min/2, y_max/2+y_min/2, y_max, x_max, lines)

	def get_lines(self,x_min, y_min, y_max, x_max):

		lines = []
		self.get(x_min, y_min, y_max, x_max, lines)

		return lines
	def prin(self):
		if len(self.sub) == 0:
			print("[]")
		else:
			for i in self.sub:
				i.prin()
	"""

WIDTH = 1000
HEIGHT = 1000
BLACK = (0,0,0)

Qtree = Node(0,0,700,700)


points = []

pygame.init()

screen = pygame.display.set_mode((700,700))

for i in range(200):
	p = Point(int(round(random.uniform(0,10), 2)*70),int(round(random.uniform(0,10), 2)*70))
	points.append(p)

count = 0

listade_sprites_activas = pygame.sprite.Group()

reloj = pygame.time.Clock()

rect = []

#print(points)

for i in range(len(points)):
	print(points[i].x, points[i].y)

a = Rect((0,0,0,0))

aux = 0
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			break


	if count <= 50:
		aux = count
		Qtree.insert(points[count], "root")

	else:
		x1 = int(input("inserte x1"))
		x2 = int(input("inserte x2"))
		y1 = int(input("inserte y1"))
		y2 = int(input("inserte y2"))

		a = Rect((x1,y1,x2-x1,y2-y1))
		
		l = getpoints(Qtree,x1,x2,y1,y2)

		for i in range(len(l)):
			print(l[i].x, l[i].y)
		print(len(l))
		#print(l)


	lines = Qtree.get_lines()

	#print(lines)

	screen.fill(BLACK)

	pygame.draw.rect(screen, (0,0,255), a)

	for i in lines:
		rect.append(Rect(i))
	for i in range(len(rect)):
		pygame.draw.rect(screen, (255,255,255), rect[i])

	
	for i in range(0, aux+1):
		#print(int(points[i].x*50), 500-int(points[i].y*50))
		pygame.draw.circle(screen, (255,0,0), (points[i].x, points[i].y), 5)


	reloj.tick(10)

	pygame.display.flip()

	count+=1
	#Qtree.prin()


pygame.quit()


