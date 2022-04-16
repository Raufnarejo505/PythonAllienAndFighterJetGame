from tkinter import *
import time
from Explosion import Explosion
from Counter import Counter
from Alien import *
from itertools import cycle

 

########## global variable
game_over=False




######### Functions


def stop_game():
    global game_over
    game_over=True
    
def shoot(canvas,aliens,booms,amunition,x,y):
    to_del = []
    for item in aliens:
        if item.is_shot(x,y):
            Explosion.add_explosion(canvas,booms,x,y,radius=30,color=item.color)
            item.deactivate()
            to_del.append(item)
            amunition.increment(item.point)
    # miss
    if not to_del:
        Explosion.add_explosion(canvas,booms,x,y,radius=30,color='white')
        amunition.increment(-3)
    for item in to_del:
        aliens.remove(item)



    

    ####### to complete




################
    
def main(): 
       
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="space1.png")
        #my_image=PhotoImage(file="space2.png")

        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height

        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas)
        
        
        #Initialize list of Explosions
        booms=[]
        #Initialize list of Aliens
        aliens=[]
        #Initialize counter ammunition
        amunition=Counter(canvas,10)

        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(canvas,aliens,booms,amunition,e.x,e.y))
        root.bind("<Escape>",lambda e:stop_game())

        
        ############################################
        ####### start simulation
        ############################################



        #To complete (time sleep is 0.01s)
        
        t = time.time()
        while not game_over:
            
            if  time.time() -t >= 1 :
                Alien.add_alien(canvas,aliens)
                t = time.time()
        
            for item in aliens:
                item.next() # next time step

            for item in booms:
                item.next()
            
            # check game over
            if amunition.value <= 0:
                canvas.create_text(w-w/2,h-h/2,text='Game Over',fill='red',font=('Courier 30 bold'))
                stop_game()
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second (simulation
          
           
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

