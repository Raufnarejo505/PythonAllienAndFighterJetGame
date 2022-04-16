from tkinter import *
import time
from Alien import *
from Explosion import Explosion
from SpaceShip import SpaceShip
from Counter import Counter
from Missile import Missile


        
########## global variable
game_over=False

######### Function
def stop_game():
    global game_over
    game_over=True
    

    
def main():
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    #my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png")
    
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
   
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)





    #### to complete
    #Initialize list of Explosions
    booms=[]
    #Initialize list of Aliens
    aliens=[]
    #Initialize counter ammunition
    amunition=Counter(canvas,0)
    #Initialize list of Missiles
    missiles=[]

    ####### Tkinter binding mouse actions
    #Initialize the ship
    ship=SpaceShip(canvas)
    ship.activate()
    amunition.add_life()
    
    
    ####### Tkinter binding mouse actions
    root.bind("<Left>",lambda e:ship.shift_left())
    root.bind("<Right>",lambda e:ship.shift_right())
    root.bind("<Escape>",lambda e:stop_game())
    life = 4
    t = time.time()
    xt = time.time()
    while not game_over:
        to_del = []
        x = ship.x+ship.my_image.width()/2
        if  time.time() -t >= 1 :
            Alien.add_alien(canvas,aliens)
            t = time.time()
        if  time.time() -xt >= .5 :
            SpaceShip.add_missile(canvas,missiles,x,ship.y,height=0,speed = 5,color = 'red')
            xt = time.time()
        for item in aliens:
            item.next() # next time step

        for m in missiles:
            m.next()
        for item in booms:
            item.next()
        
        for item in missiles:
            if item.is_active():
                for enemy in aliens:
                    if enemy.is_active() and enemy.is_shot(item.x,item.y):
                        amunition.increment(enemy.point)
                        item.deactivate()
                        enemy.deactivate()
                        to_del.append(item)
                        to_del.append(enemy)
                        Explosion.add_explosion(canvas,booms,enemy.x,enemy.y,radius = 30,color='red')
                        break
        for item in aliens:
            if item.is_active() and item.is_shot(ship.x,ship.y) or item.is_active() and item.is_shot(ship.x+ship.width,ship.y):
                to_del.append(item)
                item.deactivate()
                to_del.append(item)
                amunition.hit()
        for item in to_del:
            canvas.delete(item)
        if amunition.life==0:
            canvas.create_text(w-w/2,h-h/2,text='Game Over',fill='red',font=('Courier 30 bold'))
                
            stop_game()
        root.update()   # update the graphic (redraw)
        time.sleep(0.01)  # wait 0.01 second (simulation
      
       
    root.mainloop() # wait until the window is closed
    








if __name__=="__main__":
    main()

