from PIL import Image,ImageTk
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import tkinter as tk

vect = {(0,1),(1,0),(0,-1),(-1,0),(-1,1),(1,-1),(1,1),(-1,-1)}

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def distance3d(a,b):
	return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)


def iscolor(rgb,c,t):
	if t*400>distance3d(rgb,c):
		return True
		
		
def first(m):
	tx,ty = len(m[0]),len(m)
	for y in range(1,ty-1):
		for x in range(1,tx-1):
			if m[y][x] == "c":
				return (x,y)

def get_rgb(filepath,x,y):
	if type(filepath) == str:
		imgpil = Image.open(filepath)
	else:
		imgpil = filepath
	img = np.array(imgpil)	
	return img[y][x]
	


def image_load(t,filepath,couleur):

	imgpil = Image.open(filepath)
	img = np.array(imgpil)
	
	ty,tx,_ = img.shape
	matrice = [["." for k in range(tx)] for _ in range(ty)]
	voisin = [["." for k in range(tx)] for _ in range(ty)]
	
	r = 0
	for x in range(tx):
		for y in range(ty):
			pixel = list(img[y,x])

			if iscolor(pixel,couleur,t):
				matrice[y][x] = "c"
				r +=1
				try:
					img[y,x] = (255,255,255,0)
				except: 
					img[y,x] = (255,255,255)
		numcel = 0

	while first(matrice):
		x,y = first(matrice)
		matrice[y][x] = numcel
		for k in vect:
			vx,vy = k
			voisin[y+vy][x+vx] = 1	
			
		new = True
		while new:
			new = False
			for y in range(ty-1):
				for x in range(tx-1):

					if voisin[y][x] == 1 and matrice[y][x]=="c":
						new = True
						matrice[y][x] = numcel
						for k in vect:
							vx,vy = k
							voisin[y+vy][x+vx] = 1
	
		numcel+= 1


	return (img,numcel)
	#plt.imshow(img)
	#plt.show()	

if "__main__" == __file__:
	image_load(1,img,(255,0,0))
 #print(image_load(0.5,"C:/Users/PC/Desktop/machin kecture d image/cellule.png",(255,0,0)))


