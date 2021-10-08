import pgzrun

#Object
card01 = Actor ('demon01')
card01.pos =  100 ,100 


WIDTH = 800
HEIGHT = 600




def  draw():
    screen.clear()
    card01.draw()
    card02.draw()
    card03.draw()
    card04.draw()
    card05.draw()





def on_mouse_down(pos,):
    if card01.collidepiont(pos,card01):
        print('Great')
    else:
      print('Miss')  


pgzrun.go()