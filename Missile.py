from tkinter import *
import time,random

class Missile:
    def __init__(self,parent,c_height = 0,speed=5,color='orange',width=8,height=25):
        self.__active=False
        self.parent=parent
        self.c_height=c_height
        self.speed = speed
        self.color=color
        self.width=width
        self.height=height

    def add_missile(parent,m,x,y,height=0,speed = 5,color = 'orange'):
        new = Missile(parent,height,speed=speed,color=color)
        new.activate(x,y)
        m.append(new)

    def activate(self,x,y):
        self.x = x
        self.y = y
        self.__active=True
        self.missile = self.parent.create_rectangle(x,y-self.height,x+self.width,y+self.height,fill=self.color)

    def deactivate(self):
        self.parent.delete(self.missile)
        self.__active = False

    def is_active(self):
        return self.__active

    def next(self):
        self.y -= self.speed
        if self.is_active():
            self.parent.move(self.missile,0,-self.speed)
        if self.y <self.c_height:
            self.deactivate()




###################################################
###################################################

        
def main(): 
       
        ##### create a window, canvas and ball object
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
        
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)

        #Initialize list of Missiles
        missiles=[]
        
        
        ############################################
        ####### start simulation
        ############################################
        t=0                # initialize time clock     
        t = time.time()
        while True:

            ##### To complete
            x = random.randint(1,1000)
            color = random.choice(['blue', 'yellow', 'green', 'purple', 'red', 'orange'])
            speed = random.choice([3,4,5,6])
            if t-time.time()  >= 30:
                Missile.add_missile(canvas,missiles,x,500,height=0,speed = 5,color = color)
                t = time.time()
            for m in missiles:
                m.next()
            to_del = []
            for m in missiles:
                if not m.is_active():
                    to_del.append(m)
            for item in to_del:
                missiles.remove(item)

            # check active status of list of booms (for debugging)
            for m in missiles:
                print(m.is_active(),end=" ")
            print()
            
            # update the graphic and wait time        
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second  
            t=t+1      # increment time
       
        root.mainloop() # wait until the window is closed
        
if __name__=="__main__":
    main()

