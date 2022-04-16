from tkinter import *
from Missile import Missile
class SpaceShip:
    def __init__(self,parent,speed = 10):
        # incase no direct color name select randomly
        self.my_image=PhotoImage(file="ship.png")
        self.parent = parent
        self._activ = False
        self.speed = speed
        self.x = 0
        self.y = 0
        self.width = self.my_image.width()
        self.height=self.my_image.height()

    
    def activate(self):
        self.x = self.parent.winfo_width()/2
        self.y = 3*self.parent.winfo_height()/4
        self.ship = self.parent.create_image(self.x,self.y,anchor=NW,image=self.my_image)
        self.__active = False
    def deactivate(self):
        self.parent.delete(self.ship)
        self.__active = False

    def is_active(self):
        return self.__active
    def shift_left(self):
        self.x -= self.speed
        self.parent.move(self.ship,-self.speed,0)

    def shift_right(self):
        self.x += self.speed
        self.parent.move(self.ship,self.speed,0)

    def add_missile(parent,m,x,y,height=0,speed = 5,color = 'orange'):
        new = Missile(parent,height,speed=speed,color=color)
        new.activate(x,y)
        m.append(new)



    
def main():
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    #my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png")
    
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h) # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
   
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)


    #Initialize the ship
    ship=SpaceShip(canvas)
    ship.activate()
    
    
    ####### Tkinter binding mouse actions
    root.bind("<Left>",lambda e:ship.shift_left())
    root.bind("<Right>",lambda e:ship.shift_right())

    root.mainloop() # wait until the window is closed
    

if __name__=="__main__":
    main()

