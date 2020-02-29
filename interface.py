from tkinter import *
from tkinter.filedialog import *
import matplotlib.image as mpimg
from analyse import *


palette = "simple.png"

class Win(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master.title("Titre")
		self.pack()
		self.filepath = "image_load/resultat 0.0.png"
		self.create()
		self.color = (255,0,0)

	def create(self):
		self.t = 0
		self.pan1 = PanedWindow(self,orient=VERTICAL)
		
		self.value = DoubleVar()
		self.scale = Scale(self.pan1,orient='horizontal', from_=0, to=1, variable=self.value,resolution=0.1,command = self.majimage)
		self.pan1.add(self.scale)
			
	
		self.photo = PhotoImage(file=self.filepath)
		self.resultat = Label(self,image = self.photo,anchor="nw",height = 350)
		self.resultat.bind("<Button-1>", self.pipette)		
		self.majimage(0)

				
		self.nbcellule = Label(self,text="yo")
		self.pan1.add(self.nbcellule)
		self.pan1.add(self.resultat)	
		self.pan1.grid(column=0,row=0)
		
		
		
		self.pan2 = PanedWindow(self,orient=VERTICAL)
		
		self.color_select = Label(self,bg="#ff0000")
		self.pan2.add(self.color_select)
		
		self.photo2 = PhotoImage(file=palette)
		self.pan2.add(Button(image=self.photo2,command =self.change_color))
		
		self.loadbutton = Button(self.pan2,command=self.load,text = "Load")
		self.pan2.add(self.loadbutton)		

		self.calculbutton = Button(self.pan2,command=self.calcul,text = "Calcul")
		self.pan2.add(self.calculbutton)	
			
		self.exportbutton = Button(self.pan2,text = "Exporter",command=self.export)
		self.pan2.add(self.exportbutton)	
		
			
		self.pan2.grid(column=1,row = 0)
	def pipette(self,event):
		self.x,self.y =event.x,event.y
		print(self.x,self.y)
		self.color = list(get_rgb(self.img,self.x,self.y))[:3]
		print(self.color)
		self.color_hex = rgb_to_hex(tuple(self.color))
		self.color_select.configure(bg = self.color_hex )		
	
	
	def pointeur(self,event):
		
		self.x,self.y =event.x,event.y
		print(self.x,self.y)
		self.color = list(get_rgb(palette,self.x,self.y))[:3]
		self.color_hex = rgb_to_hex(tuple(self.color))
		self.color_select.configure(bg = self.color_hex )
		
		print(self.color)
		
	def majimage(self,_):
		try: 
			self.dataimage
			self.t = self.scale.get()
			self.img = Image.open("image_load/resultat {}.png".format(self.t))
			self.nbcellule.configure(text="il y a {} cellule(s)".format(self.dataimage[self.t][1]))
		except AttributeError:
			self.img = Image.open("{}".format(self.filepath))
		w,h = self.img.size

		r = 500/w

		self.img = self.img.resize((int(w*r),int(h*r)),Image.ANTIALIAS)
		self.photo =  ImageTk.PhotoImage(self.img)
		
		self.resultat.configure(image=self.photo)
		self.resultat.image = self.photo

	def change_color(self):
		self.t = Toplevel(self)
		self.t.grab_set() 
		self.img = PhotoImage(file=palette)
		cadre = Label(self.t,image=self.img)
		cadre.bind("<Button-1>", self.pointeur)
		cadre.pack()
		
			
			
	def load(self):
		self.filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
		self.majimage(0)
		try :
			del self.dataimage
		except:
			pass
		
		
	def calcul(self):
		print (self.filepath)
		if not self.filepath:
			return False

		self.dataimage = {}
		
		for t0 in range(0,11):
			t = t0/10
			print (t0)
			self.dataimage[t] = image_load(t,self.filepath,self.color)
			img,n = self.dataimage[t]	
			imgpil = Image.fromarray(img)
			imgpil.save("image_load/resultat {}.png".format(t))
			
		self.majimage(0)

	def export(self):
		self.e = Toplevel()
		self.e.grab_set()
		self.te  =Label(self.e,text= "entrer le chemin")
		self.te.pack()
		
		self.w = Text(self.e,height=1,width=50)
		self.w.pack()
		
		self.bu = Button(self.e, text="exporter",command=self.dl)
		self.bu.pack()
		
	def dl(self):
		chemin = self.w.get("1.0",END)
		img,n = self.dataimage[self.t]
		imgpil = Image.fromarray(img)
		imgpil.save("{}/resultat {}.png".format(chemin[:-1],self.t))		
		
		
		print (chemin)
fenetre = Win()
fenetre.mainloop()


