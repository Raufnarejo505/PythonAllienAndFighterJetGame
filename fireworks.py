from tkinter import *
import time,random
from Explosion import Explosion
from Missile import Missile

        
       
def main(): 
       
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        
        my_image=PhotoImage(file="umass_campus.png")
        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h) # create a canvas width*height

        i = canvas.create_image(10,10,anchor=NW,image=my_image)
        
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)

        #Initialize list of Explosions
        booms=[]
        #Initialize list of Missiles
        missiles=[]
        

        
        ############################################
        ####### start simulation
        ############################################
      






        ### To complete
        t = time.time()
        while True:
            
            if  time.time() -t >= 3 :
                c_h = random.randint(int(h/4),int(3*h/4))
                x = random.randint(1,w)
                color = random.choice(['blue', 'yellow', 'green', 'purple', 'red', 'orange'])
                speed = random.choice([3,4,5,6])
                Missile.add_missile(canvas,missiles,x,h,height=c_h,speed = 5,color = color)
                t = time.time()

            del_m = []
            for m in missiles:
                if m.is_active():
                    m.next()
                else:
                    color = random.choice(['blue', 'yellow','rainbow', 'green','rainbow', 'purple', 'red', 'orange','rainbow'])
                    radius = random.randint(100,300)
                    Explosion.add_explosion(canvas,booms,m.x,m.c_height,radius = radius,color=color)
                    del_m.append(m)
            for item in del_m:
                missiles.remove(item)
                    
            
            to_r = []
            for boom in booms:
                if boom.is_active():
                    boom.next()  
                else:
                    to_r.append(booms)
            for item in to_r:
                try:
                    booms.remove(item)
                except:pass
                    
            print(len(booms),len(missiles))
            # update the graphic and wait time        
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second  
                


if __name__=="__main__":
    main()

