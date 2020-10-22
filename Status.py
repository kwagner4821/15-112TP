import math

def status0(canvas,data):
    canvas.create_rectangle\
    (0,0,data.width,data.height,fill = "red",outline="")
    canvas.create_rectangle\
    (data.width//2-150,data.height//3-25,data.width//2+150,data.height//3+25,outline = "")
    canvas.create_rectangle\
    (data.width//2-75,data.height//3+40,data.width//2+75,data.height//3+75,outline = "")
    canvas.create_rectangle\
    (data.width//2-40,data.height//3+80,data.width//2+40,data.height//3+105,outline = "")
    canvas.create_text\
    (data.width//2,data.height//3, text = "Welcome to PyShooter",font = "Times 30 italic bold")
    canvas.create_text\
    (data.width//2,data.height//3 + 60, text = "Click to Play", font = "Times 20 italic bold")
    canvas.create_text\
    (data.width//2,data.height//3 + 90, text = "About", font = "Times 20 italic bold")
    canvas.create_text\
    (data.width//2,data.height//3 + 120, text = "A Kyle Wagner Game", font = "Times 15 italic bold")

def status1(canvas,data):
    canvas.create_rectangle\
    (0,data.height//2,data.width,data.height, fill = "grey21", outline = "")
    canvas.create_rectangle\
    (0,0,data.width,data.height//2, fill = "grey67", outline = "")
    # draw in canvas
    for i in range(8):
        canvas.create_line(i * data.height//8,0,i*data.height//8,data.height)
    for i in range(8):
        canvas.create_line(0,i*data.height//8,data.height,i * data.height//8)
    for angle in range(data.angle-45,data.angle+46):
        if angle > 360:
            angle = angle % 360
        elif angle < 0:
            angle = 360 + angle
        if angle in data.hitsy:
            x,y = data.hitsy[angle]
            canvas.create_line(data.cxS,data.cyS,x,y)
    for angle in range(data.angle-45,data.angle+46):
        if angle > 360:
            angle = angle % 360
        elif angle < 0:
            angle = 360 + angle
        if angle in data.hitsx:
            x,y = data.hitsx[angle]
            canvas.create_line(data.cxS,data.cyS,x,y)
    size = 10
    angle = math.radians(data.angle)
    angleChange = 2*math.pi/3
    numPoints = 3
    points = []
    for point in range(numPoints):
        points.append
        ((data.cxS + size*math.cos(angle + point*angleChange),
        data.cyS - size*math.sin(angle + point*angleChange)))
    points.insert(numPoints-1, (data.cxS, data.cyS))
    canvas.create_polygon(points,fill="black")    
    canvas.create_oval(data.miniX - 5, data.miniY -5, data.miniX + 5, data.miniY + 5)
    #loop to check if line hits side
    '''
    canvas.create_line(data.cxS,data.cyS,data.cxS + 800 * \
    math.cos(math.radians(data.angle + 45)),data.cyS - 800 * math.sin(math.radians(data.angle + 45)))
    canvas.create_line(data.cxS,data.cyS,data.cxS + 800 * \
    math.cos(math.radians(data.angle - 45)),data.cyS - 800 * math.sin(math.radians(data.angle - 45)))
    '''
    for i in range(len(data.room)):
        for j in range(8):
            if data.room[i][j] == 1:
                canvas.create_rectangle\
                (data.blocksize * j, data.blocksize * i, data.blocksize * (j+1), \
                data.blocksize * (i+1),fill = "black",outline = "white")
    counter = 0
    sliceWidth = 800/90 
    for angle in range(abs(data.angle % 360) - 45, abs(data.angle % 360) + 46):#calculating distance
        if angle < 0:
            angle = 360 + angle
        elif angle > 360:
            angle = angle % 360 
        if angle not in data.hitsF:
            None
        elif angle in data.hitsF:
            #800/90
            #height = constant/p, constaant = 150,000 
            #unpack
            distance = data.hitsF[angle]
            #make distance based off angle, should be range of 0,90
            if counter == 0:
                refAngle = angle
                counter += 1
            scaleAngle = angle - refAngle
            if distance == 0:
                None
            else:
                height = abs(130000/distance)
                canvas.create_rectangle(abs(scaleAngle*sliceWidth),data.height//2 + abs(height/2),abs(scaleAngle * (sliceWidth + 1)),data.height//2 - abs(height/2),fill = "red")
    
    