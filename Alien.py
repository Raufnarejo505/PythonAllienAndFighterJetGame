from tkinter import *
import math
import time, random

class Alien:
    ### to complete
    def __init__(self,canvas,speed=4,color='yellow',width=50,height=50):
        self.canvas = canvas
        self.speed = speed
        self.color=color
        self.width = width
        self.height=height
        
        self.__active = False

    def activate(self,x=None,y=None):
        if not x:
            self.x = random.randint(1,self.canvas.winfo_width())
        else:
            self.x = x
        if not y:
            self.y = 0
        else:
            self.y=y
        self.alien = self.canvas.create_rectangle(self.x,self.y-self.height,self.x+self.width,self.y+self.height,fill=self.color)
        self.__active=True
    def is_active(self):
        return self.__active

    def is_shot(self,x,y):
        rect = self.canvas.coords(self.alien)
       
        if not rect:return
        if int(x) in range(int(rect[0])-int(self.width/2),int(rect[0])+int(self.width/2)+1) and int(y) in range(int(rect[1]-int(self.height/2)),int(rect[1])+int(self.height/2)+1):
            return True
        else:
            return False

    def deactivate(self):
        self.__active = False
        self.canvas.delete(self.alien)

    def set_active(self,val):
        self.__active=val

    def next(self):
        self.y += self.speed
        self.canvas.move(self.alien,0,self.speed)
        if self.y > self.canvas.winfo_height():
            self.deactivate()

    def add_alien(canvas,aliens):
        a = random.choice(['r','g','b'])
        if a == 'r':
            alien = Alien_red(canvas)
        elif a == 'g':
            alien = Alien_green(canvas)
        elif a == 'b':
            alien = Alien_blue(canvas)
        
        alien.activate()
        aliens.append(alien)
        
################################################################
################################################################

class Alien_red(Alien):
    def __init__(self,canvas,speed=4,color='red',point=2):
        
        self.image=PhotoImage(file="alien_red.png")  # keep a reference (avoid garbage collector)
        width=self.image.width()
        height=self.image.height()
        # contstructor to complete
        self.canvas = canvas
        self.speed = speed
        self.color = color
        self.width = width
        self.height = height
        self.point = point
        self.__active=False
        super().__init__(self.canvas)

    

        
    # to complete
    def activate(self,x=None,y=None):
        if not x:
            self.x = random.randint(1,self.canvas.winfo_width())
        else:
            self.x = x
        if not y:
            self.y = 10
        else:
            self.y=y
        self.alien = self.canvas.create_image(self.x,self.y,anchor=CENTER,image=self.image)
        self.__active = True
        print(self.y)
        return super().set_active(True)

    def next(self):
        self.y += self.speed
        self.canvas.move(self.alien,0,self.speed)
        if self.y > self.canvas.winfo_height():
            self.deactivate()
        


###############################################################
###############################################################

class Alien_green(Alien_red):
    def __init__(self,canvas,speed=4,color='green',point=4):
        self.image=PhotoImage(file="alien_green.png")  # keep a reference (avoid garbage collector)
        width=self.image.width()
        height=self.image.height()
        # contstructor to complete
        Alien.__init__(self,canvas)
        self.canvas = canvas
        self.speed = speed
        self.color = color
        self.width = width
        self.height = height
        self.point = point
        
    # to complete
    
      
        
    def next(self):
        self.y += self.speed
        self.canvas.move(self.alien,random.randint(-5,5),self.speed)
        if self.y > self.canvas.winfo_height():
            self.deactivate()


###############################################################
###############################################################
 

class Alien_blue(Alien_red):

    # to complete
    def __init__(self,canvas,speed=4,color='blue',point=3):
        self.image=PhotoImage(file="alien_blue.png")  # keep a reference (avoid garbage collector)
        width=self.image.width()
        height=self.image.height()
        # contstructor to complete
        Alien.__init__(self,canvas)
        self.canvas = canvas
        self.color = color
        self.width = width
        self.height = height
        self.point = point
        self.angle = -20
        self.speed = [6,4]
       
    # to complete
    
        
    def next(self):
        if self.hit_left_wall(self.canvas, self.alien) or self.hit_right_wall(self.canvas, self.alien):
            self.speed[0] *= -1
        if self.hit_top_wall(self.canvas, self.alien) or self.hit_bottom_wall(self.canvas, self.alien):
            self.speed[1] *= -1
        self.y += self.speed[1]
        self.x += self.speed[0]
        self.canvas.move(self.alien,self.speed[0],self.speed[1])
        
    def hit_left_wall(self,canvas, object):
        return self.x <= 0

    def hit_top_wall(self,canvas, object):
        return self.y <= 0

    def hit_right_wall(self,canvas, object):
        print(self.x + self.width >= int(canvas.cget('width')))
        print(self.y+self.height,int(canvas.cget('height')))
        return self.x + self.width >= int(canvas.cget('width'))

    def hit_bottom_wall(self,canvas, object):
        return self.y + self.height >= int(canvas.cget('height'))


    ######## These helper methods use "lists" ###########
    ### Which is a concept you will learn Monday ###########



class Alien_mine(Alien_red):
    def __init__(self,canvas,speed=4,color='blue',point=3):
        self.image=PhotoImage(file="enemy.gif")  # keep a reference (avoid garbage collector)
        width=self.image.width()
        height=self.image.height()
        # contstructor to complete
        self.canvas = canvas
        self.canvas = canvas
        self.speed = speed
        self.color = color
        self.width = width
        self.height = height
        self.point = point
        self.angle = -20
        Alien.__init__(self,self.canvas)
    # to complete
    
        
    def next(self):
        self.y += self.speed
        self.canvas.move(self.alien,random.randint(-5,5),self.speed)
        if self.y > self.canvas.winfo_height():
            self.deactivate()

###############################################################
################################################################
def shoot(alien,x,y):
    if alien.is_shot(x,y):
        result="hit!"
    else:
        result="miss!"
   



    
def main(): 
        
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="space2.png")

        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height

        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (neede to capture w and h for canvas)
        

        #Initialize alien
        #alien=Alien(canvas)
        alien=Alien_mine(canvas)
        #alien=Alien_green(canvas)
        alien=Alien_blue(canvas)

        alien.activate()
        

        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(alien,e.x,e.y))

        
        ############################################
        ####### start simulation
        ############################################
        #t=0               # time clock
        while True:

            if (not alien.is_active()):
                alien.activate()
            #print(alien.is_active())
              
            alien.next() # next time step
                    
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second (simulation
           
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

