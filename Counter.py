from tkinter import *

class Counter:


    # to complete
    def __init__(self,parent,val):
    	self.parent = parent
    	self.value = val
    	self.life = 4
    	self.counter = parent.create_text(int(self.parent.cget('width'))-70,20,text=str(self.value),fill='orange',font=('Courier 25'))
    	self.image1 = PhotoImage(file="player.gif").subsample(2, 2) 
    	self.image2 = PhotoImage(file="player.gif").subsample(3,3) 
    	self.image3 = PhotoImage(file="player.gif").subsample(5, 5) 
    	self.image4 = PhotoImage(file="player.gif").subsample(5, 5) 
    	
    def add_life(self):
        self.life1 = self.parent.create_image(10,20,image=self.image1)
        self.life2 = self.parent.create_image(30,20,image=self.image1)
        self.life3 = self.parent.create_image(50,20,image=self.image1)
        self.life4 = self.parent.create_image(70,20,image=self.image1)
        self.all_life = [self.life1,self.life2,self.life3,self.life4]
    def hit(self):
    	self.life -= 1
    	self.parent.delete(self.all_life[-1])
    	self.all_life.pop(-1)
    	
    def increment(self,val):
    	self.value += val
    	self.parent.itemconfig(self.counter,text=str(self.value))

        
        
#########################




def main(): 

    # to complete
	root = Tk() # instantiate a tkinter window
	my_image=PhotoImage(file="space2.png")

	w=my_image.width()
	h=my_image.height()
	canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height

	canvas.create_image(0,0,anchor=NW,image=my_image)
	    
	canvas.pack()
	counter = Counter(canvas,val = 10)
	root.bind("<Left>",lambda e:counter.increment(-1))
	root.bind("<Right>",lambda e:counter.increment(1))
	mainloop()
	root.update()   # update the graphic (neede to capture w and h for canvas)






if __name__=="__main__":
    main()
  



        
