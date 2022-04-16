########################
## Team Members
## Name1:         
## Name2:
#########################

from tkinter import *
import random


class Dot:
    def __init__(self,parent,x,y,color,display=False):
        # incase no direct color name select randomly
        if color == 'rainbow':
            col = random.choice(['white','green','red','yellow','blue','orange','purple'])
        # else use the given color
        else:
            col = color
        # add a oval the parent window as dot to display
        self.dot = parent.create_oval(x-1,y-1,x+2,y+2,fill=col)

        # display information incase needed
        if display:
            print(x,y,col)
        
#################################################################
#################################################################
    
def main(): 

        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        canvas = Canvas(root,width=800,height=1000,bg="black") # create a canvas width*height
        canvas.pack()
        root.update()   # update the graphic
        
        
        # Tkinter binding action (mouse click)
        root.bind("<Button-1>",lambda e:Dot(canvas,e.x,e.y,"rainbow",True))
        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

