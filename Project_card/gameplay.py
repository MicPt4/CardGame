import pgzrun
import random 
import time

WIDTH = 800
HEIGHT = 600

#object 
back_card = Actor('behind',(50,50))
back_card.topleft = (0,0)
card01 = Actor('demon01',(50,50))
card01.topleft = (0,0)


# all of values 
Col = 2
Row = 2
Imsize = 200
Status =[]
Ignore = []

START_IMAGES= [ "im"+str(i+1) for i in range(Col*Row//2)]*2
random.shuffle(START_IMAGES)

Status =[]
board = []
for row in range (Row):
    new_row = []
    for col in range (col):
        image_name = START_IMAGES.pop()
        temp = Actor(image_name,(col*Imsize, row*Imsize))
        temp.image_name = image_name
        temp.topleft = (col*Imsize,row*Imsize)
        new_row.append(temp)
board.append(new_row)

def draw ():
    screen.clear()
    for row in range (Row):
        for col in range (col):
            if (row,col) in Ignore:
                back_card.topleft =  Imsize*col , Imsize*row 
                back_card.draw()
            elif (row,col) in Status :
                board[row][col].draw()
            else:
              card01.topleft =  Imsize*col , Imsize*row 
              card01.draw()


def findTile(pos):
    y,x = pos 
    result = x // Imsize , y // Imsize
    return result

def showTile():
    pass


def on_mouse_down(pos,button):
    if len(Status) == 2:
        return
    if pos in Ignore:
        return 
    if button == mouse.LEFT and (pos):
        coords = findTile(pos)
        if coords not in Status:
            Status.append(coords)
            if len(Status) == 1:
                pass
            elif len(Status) == 2:
                (x1, y1), (x2, y2) = Status
                if board[x1][y1].image_name == board[x2][y2].image_name:
                    print("Success sound")
                    for pos in Status:
                        Ignore.append(pos)    
                else:
                    print("Failure sound")
                clock.schedule_unique(next_turn, 60.0)
def next_turn():
    del STATUS[:]
