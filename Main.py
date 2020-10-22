# Updated Animation Starter Code

import Status
import math
from tkinter import *

#Welcome to PyShooter, a game by Kyle Wagner
#This code utilizes the updated 2d timer fired animation framework.

####################################
# customize these functions
####################################
    
#Lines 29 through 86 were inspired by this website. Citation: https://lodev.org/cgtutor/raycasting.html
def rayCast(canvas,data):
    for x in range(data.width):
        cameraX = 2 * x / (data.width) - 1
        rayDirX = data.dirX + data.planeX * cameraX
        rayDirY = data.dirY + data.planeY * cameraX + .00000001
        
        mapX = int(data.posX)
        mapY = int(data.posY)
        
        deltaDistX = abs(1/rayDirX)
        deltaDistY = abs(1/rayDirY)
        
        if rayDirX < 0:
            stepX = -1
            sideDistX = (data.posX - mapX) * deltaDistX
        else:
            stepX = 1
            sideDistX = (mapX + 1.0 - data.posX) * deltaDistX
        
        if rayDirY < 0:
            stepY = -1
            sideDistY = (data.posY - mapY) * deltaDistY
        else:
            stepY = 1
            sideDistY = (mapY + 1.0 - data.posY) * deltaDistY
        hit = 0
        while hit == 0:
            if sideDistX < sideDistY:
                sideDistX += deltaDistX
                mapX += stepX
                side = 0
            else:
                sideDistY += deltaDistY
                mapY += stepY
                side = 1
            
            if data.worldMap[mapX][mapY] > 0:
                hit = 1
        if side == 0:
            perpWallDist = (mapX - data.posX + (1- stepX) / 2) / rayDirX
        else:
            perpWallDist = (mapY - data.posY + (1 - stepY) / 2) / rayDirY
        ZBuffer = []
        ZBuffer.append(perpWallDist)
        lineHeight = 2 * int(data.height / (perpWallDist + .0000001))
        drawStart = -lineHeight / 2 + data.height / 2
        if (drawStart < 0):
            drawStart = 0
        drawEnd = lineHeight / 2 + data.height / 2
        if drawEnd >= data.height:
            drawEnd = data.height - 1
        #Choosing wall color
        blockValue = data.worldMap[mapX][mapY]
        colorValues = ["white","red","green","blue","yellow","orange"]
        color = colorValues[blockValue]
        #print(x,drawStart,x,drawEnd)
        canvas.create_line(x,drawStart,x,drawEnd,fill = color)
    for i in range(len(data.zombies)):
        y = data.zombies[i][0]
        x = data.zombies[i][1]
        zombieVector = (y - data.posY, x - data.posX)
        dirVector = (data.dirY, data.dirX)
        zombieVectorMag = (zombieVector[0]**2 + zombieVector[1]**2)**0.5
        dotProduct = dirVector[0] * zombieVector[0] + dirVector[1] * zombieVector[1]
        dirVectorMag = (data.dirX**2 + data.dirY**2)**0.5
        angle = (math.acos(dotProduct/(dirVectorMag*zombieVectorMag)))
        #enemy is 50 wide and 75 tall
        #find intersection point, increment 
        if angle <= 30:
            #find endpoints
            #endpoint 1
            planeMag = (data.planeX**2 + data.planeY**2)**0.5
            relativeL = (.25*data.planeX/planeMag,.25*data.planeY/planeMag)
            endpoint1 = (y+relativeL[1],x+relativeL[0])
            #endpoint 2
            endpoint2 = (y-relativeL[1],x-relativeL[0])
            #realistic endpoints
            maxRayDirX = data.dirX + data.planeX * 1
            minRayDirX = data.dirX + data.planeX * -1
            maxRayDirY = data.dirY + data.planeY * 1
            minRayDirY = data.dirY + data.planeY * -1
            realEnd1 = (maxRayDirY+data.posY,maxRayDirX+data.posX)
            realEnd2 = (minRayDirY+data.posY,minRayDirX+data.posX)
            
    #Labels
    canvas.create_rectangle(20,10,140,140,fill = "grey67",outline = "")
    canvas.create_text(60,25,text = "Menu",font = "Times 20 italic bold")
    canvas.create_text(65,55,text = "Lives: %d" % data.lives,font = "Times 20 italic bold")
    canvas.create_text(63,85,text = "Health",font = "Times 20 italic bold")
    canvas.create_rectangle(32,100,132,132,fill = "white",outline = "")
    canvas.create_rectangle(32,100,32+data.health,132,fill = "red", outline = "")
    canvas.create_text(50,116,text = "%d" % data.health,font = "Times 20 italic bold")
    canvas.create_rectangle(data.width/2-350,data.height-100,data.width/2+350,data.height,fill="blue")
    canvas.create_rectangle(data.width/2-1,data.height/2-25,data.width/2+1,data.height/2+25,fill = "white",outline = "")
    canvas.create_rectangle(data.width/2-25,data.height/2-1,data.width/2+25,data.height/2+1,fill = "white",outline = "")
    canvas.create_rectangle(data.width/2-340,data.height-90,data.width/2-116.7,data.height-10,fill= "blue4",outline = "white")
    canvas.create_rectangle(data.width/2-96.7,data.height-90,data.width/2+116.3,data.height-10,fill= "blue4",outline = "white")
    canvas.create_rectangle(data.width/2+136.7,data.height-90,data.width/2+340,data.height-10,fill= "blue4",outline = "white")
    canvas.create_text(data.width/2-225,data.height-75,text = "Ammo",font = "Times 20 italic bold",fill="SteelBlue3")
    canvas.create_text(data.width/2-225,data.height-40,text = "%d" % data.ammo,font = "Times 30 italic bold",fill="white")
    canvas.create_text(data.width/2,data.height-75,text = "Score",font = "Times 20 italic bold",fill="SteelBlue3")
    canvas.create_text(data.width/2,data.height-40,text = "%d" % data.score ,font = "Times 30 italic bold",fill="white")
    #canvas.create_image(data.width/2+125,data.height,anchor= SW,image = data.myImage)
    canvas.create_text(50,150,text = "Time: %.1f" % (data.timer/10))
def init(data):
    # load data.xyz as appropriate
    data.mapWidth = 24
    data.mapHeight = 24
    data.texWidth = 64
    data.texHeight = 64
    data.worldMap=[
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,2,2,2,2,2,0,0,0,0,3,0,3,0,3,0,0,0,1],
  [1,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,2,0,0,0,2,0,0,0,0,3,0,0,0,3,0,0,0,1],
  [1,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,2,2,0,2,2,0,0,0,0,3,0,3,0,3,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,4,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,0,0,0,5,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,4,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]];
    data.posX = 22
    data.posY = 12
    data.dirX = -1
    data.dirY = -0
    data.planeX = 0
    data.planeY = .66
    data.width = 1440
    data.height = 800
    data.movSpeed = 1
    data.rotSpeed = .2
    data.status = 0
    data.zombies = []
    data.timer = 0
    data.lives = 3
    data.health = 100
    data.score = 0
    #data.myImage = PhotoImage(file = '/Users/kwagner/Desktop/untitled/folder/2/Gun.gif')
    data.ammo = 100
    data.spawn= [[],[1,22],[1,1],[18,9],[22,22]]
    data.zombiesSimp = []

def mousePressed(event, data):
    # use event.x and event.y      
    if data.status == 0:
        #first button
        if event.x < data.width//2 + 75 and event.x > data.width//2 - 75\
        and event.y < data.height//3 + 75 and event.y > data.height//3 + 40:
            data.status = 1
        if event.x < data.width//2 + 40 and event.x > data.width//2 - 40\
        and event.y < data.height//3 + 105 and event.y > data.height//3 + 75:
            data.status = 2
        #second button
        #third button
    elif data.status == 1:
        if event.x <= 90 and event.x >= 30\
        and event.y <= 35 and event.y >= 15:
            data.status = 3
    elif data.status == 2:
        if event.x <= 815 and event.x >= 625\
        and event.y <= 385 and event.y >= 370:
            data.status = 0
    elif data.status == 3:
        if event.y >= 183 and event.y <= 198\
        and event.x <= 730 and event.x >= 540:
            data.status = 0
        elif event.y >= 214 and event.y <= 228\
        and event.x <= 730 and event.x > 540:
            data.status = 1
    elif data.status == 4:
        if event.y >= 183 and event.y <= 198\
        and event.x <= 730 and event.x >= 540:
            data.status = 0
        elif event.y >= 214 and event.y <= 228\
        and event.x <= 730 and event.x > 540:
            data.lives -= 1
            data.status = 1
    elif data.status == 5:
        if event.y >= 183 and event.y <= 198\
        and event.x <= 730 and event.x >= 540:
            init(data)
            data.status = 0
        
def keyPressed(event, data):
    # use event.char and event.keysym
    if data.status == 1:
        if event.keysym == "Left":
            oldDirX = data.dirX
            data.dirX = data.dirX * math.cos(data.rotSpeed) - data.dirY *math.sin(data.rotSpeed)
            data.dirY = oldDirX * math.sin(data.rotSpeed) + data.dirY *math.cos(data.rotSpeed)
            oldPlaneX = data.planeX
            data.planeX = data.planeX * math.cos(data.rotSpeed) - data.planeY * math.sin(data.rotSpeed)
            data.planeY = oldPlaneX * math.sin(data.rotSpeed) + data.planeY * math.cos(data.rotSpeed)
        elif event.keysym == "Right":
            oldDirX = data.dirX
            data.dirX = data.dirX * math.cos(-1*data.rotSpeed) - data.dirY *math.sin(-1*data.rotSpeed)
            data.dirY = oldDirX * math.sin(-1*data.rotSpeed) + data.dirY *math.cos(-1*data.rotSpeed)
            oldPlaneX = data.planeX
            data.planeX = data.planeX * math.cos(-1*data.rotSpeed) - data.planeY * math.sin(-1*data.rotSpeed)
            data.planeY = oldPlaneX * math.sin(-1*data.rotSpeed) + data.planeY * math.cos(-1*data.rotSpeed)
        elif event.keysym == "Up":
            if data.worldMap[int(data.posX + data.dirX * data.movSpeed)][int(data.posY)] == False:
                data.posX += data.dirX * data.movSpeed
            if data.worldMap[int(data.posX)][int(data.posY + data.dirY * data.movSpeed)] == False:
                data.posY += data.dirY * data.movSpeed
        elif event.keysym == "Down":
            if data.worldMap[int(data.posX - data.dirX * data.movSpeed)][int(data.posY)] == False:
                data.posX -= data.dirX * data.movSpeed
            if data.worldMap[int(data.posX)][int(data.posY - data.dirY * data.movSpeed)] == False:
                data.posY -=  data.dirY * data.movSpeed
        elif event.keysym == "Escape":
            print(data.zombies)

def timerFired(data):
    if data.status == 1:
        data.timer += 1
        if data.health <= 0:
            if data.lives > 0:
                data.health = 100
                data.status = 4
            elif data.lives == 0:
                data.status = 5
        if data.timer % 50 == 0:
        #Determine which quadrant
            if data.posX > 12:
                if data.posY < 12:
                    quad = 1
                else:
                    quad = 4
            else:
                if data.posY < 12:
                    quad = 2
                else:
                    quad = 3
            data.zombies.append(data.spawn[quad])
        for zombie in data.zombies:
            y,x = zombie
            chaseVector = (data.posY - y,data.posX - x)
            magnitude = (chaseVector[0] ** 2 + chaseVector[1] ** 2)**0.5
            movVector0 = .3*chaseVector[0]/magnitude
            movVector1 = .3*chaseVector[1]/magnitude
            #zombie[0] += movVector0
            #zombie[1] += movVector1
            #dist = ((zombie[0] - data.posY)**2 + (zombie[1] - data.posX)**2)**0.5
            #if zombie in data.zombies and dist < .5:
            #    if data.timer % 50 == 0:
            #        data.health -= 10
            #data.zombiesSimp.append([int(zombie[0]),int(zombie[1])])

def redrawAll(canvas, data):
    if data.status == 0:
        Status.status0(canvas,data)
    elif data.status == 1:
        rayCast(canvas,data)
    elif data.status == 2:
        canvas.create_rectangle\
        (0,0,data.width,data.height,fill = "red",outline="")
        canvas.create_text\
        (data.width/2,data.height/3, text ="This Project is named, PyAmnesia, which will implement the python version of the game Amnesia. \nAmnesia is a 1st person interactive horror game, in which the user must solve tasks to avoid dying to a monster. \nMy version will utilize pygame, and will play music in the background which will heighten the scariness of the game",font = "Times 20 italic bold")
        canvas.create_text(data.width/2,data.height/3 + 75,text = "Return to Main Screen",font = "Times 20 italic bold")
    elif data.status == 3:
        rayCast(canvas,data)
        canvas.create_rectangle(data.width/2-200,data.height/2-300,data.width/2+200,data.height/2+300, fill = "grey21",outline = "")
        canvas.create_rectangle(data.width/2-190,data.height/2-290,data.width/2+190,data.height/2+290, fill = "grey67",outline = "")
        canvas.create_text(data.width/2,data.height/2-280,text = "Main Menu", font = "Times 20 italic bold")
        canvas.create_text(data.width/2-150,data.height/2-240,text = "Options",font = "Times 20 italic bold")
        canvas.create_text(data.width/2-85,data.height/2-210,text = "Return to Main Screen",font = "Times 20 italic bold")
        canvas.create_text(data.width/2-83,data.height/2-180,text = "Return to Game Screen",font = "Times 20 italic bold")
    elif data.status == 4:
        rayCast(canvas,data)
        canvas.create_rectangle(data.width/2-200,data.height/2-300,data.width/2+200,data.height/2+300, fill = "grey21",outline = "")
        canvas.create_rectangle(data.width/2-190,data.height/2-290,data.width/2+190,data.height/2+290, fill = "grey67",outline = "")
        canvas.create_text(data.width/2,data.height/2-280,text = "Main Menu", font = "Times 20 italic bold")
        canvas.create_text(data.width/2-150,data.height/2-240,text = "Options",font = "Times 20 italic bold")
        canvas.create_text(data.width/2-85,data.height/2-210,text = "Return to Main Screen",font = "Times 20 italic bold")
        canvas.create_text(data.width/2-20,data.height/2-180,text = "Return to Game Screen with a New Life",font = "Times 20 italic bold")
    elif data.status == 5:
        rayCast(canvas,data)
        canvas.create_rectangle(data.width/2-200,data.height/2-300,data.width/2+200,data.height/2+300, fill = "grey21",outline = "")
        canvas.create_rectangle(data.width/2-190,data.height/2-290,data.width/2+190,data.height/2+290, fill = "grey67",outline = "")
        canvas.create_text(data.width/2,data.height/2-280,text = "Main Menu", font = "Times 20 italic bold")
        canvas.create_text(data.width/2-150,data.height/2-240,text = "Options",font = "Times 20 italic bold")
        canvas.create_text(data.width/2-85,data.height/2-210,text = "New Game",font = "Times 20 italic bold")
####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, data.height//2, data.width, data.height,
                                fill='black', width=0)
        canvas.create_rectangle(0,0,data.width,data.height//2,fill="grey",width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1440, 800)