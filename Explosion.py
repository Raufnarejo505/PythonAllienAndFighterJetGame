from tkinter import *
import math,time,random
from Dot import Dot


class Explosion:
    def __init__(self,parent,max_radius = 80,color = 'rainbow'):
        self.num_dots = 15
        self.dots = []
        self.__active = False
        self.max_radius = max_radius
        self.color = color
        self.parent = parent

    def activate(self,x,y):
        self.x = x
        self.y = y
        self.r = 0
        self.__active = True

    def deactivate(self):
        for item in self.dots:
            self.parent.delete(item.dot)
        self.__active = False
            
    def is_active(self):
        return self.__active
    def next(self):

        self.r += 3
        # if max radius is recieved remove the explosion
        if self.r > self.max_radius:
            self.deactivate()
            return
        
        for i in range(self.num_dots):
            # generate random angle
            a = random.random()* 2*math.pi
            newx = self.r*math.cos(a) + self.x
            newy = self.r*math.sin(a) + self.y
            if self.color == 'rainbow':
                col = random.choice(['white','green','red','yellow','blue','orange','purple'])
            else:
                col = self.color
            self.dots.append(Dot(self.parent,newx,newy,color=col))



    def add_explosion(canvas,booms,x,y,radius=80,color='rainbow'):

        ex = Explosion(canvas,radius,color)
        ex.activate(x,y)
        booms.append(ex)
        













        
#################################################################
#################################################################
    
def main(): 

        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root,width=w,height=h,bg="black") # create a canvas width*height
        canvas.pack()
        root.update()   # update the graphic
        
        #Initialize list of Explosions
        booms=[]
        
        # Tkinter binding action (mouse click)
        root.bind("<Button-1>",lambda e:Explosion.add_explosion(canvas,booms,e.x,e.y) )
        
        ############################################
        ####### start simulation
        ############################################
        
        while True:
            # scan booms list and execute next time step
            for boom in booms:
                boom.next()
                
            # check active status of list of booms (for debugging)
            for b in booms:
                print(b.is_active(),end=" ")
            for b in booms:
                if not b.is_active():
                    booms.remove(b)
                    break
            print()

            # update the graphic and wait time
            root.update()    #redraw
            time.sleep(0.03) #pause

        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

