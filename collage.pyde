#Setup: Window Size and Background Color
size(700,600)
background(255,127,80)

#Border
for x in range(0,20,10):
    for y in range(0,height,10):
        rect(x,y,10,10)
        fill(255,random(0,255),random(0,255))
for x1 in range(0,width,10):
    for y1 in range(0,20,10):
        rect(x1,y1,10,10)
        fill(255,random(0,255),random(0,255))
for x2 in range(width-20,width,10):
    for y2 in range(0,height,10):
        rect(x2,y2,10,10)
        fill(255,random(0,255),random(0,255))
for x3 in range(0,width,10):
    for y3 in range(height-20,height,10):
        rect(x3,y3,10,10)
        fill(255,random(0,255),random(0,255))
        
#User Defined functions for chaning Pictures
def negGray(Picture): #Negative Grayscale 
    img = loadImage(str(Picture))
    
    loadPixels()
    for i in range(0,len(img.pixels)):
        r = 255 - red(img.pixels[i])
        g = 255 - green(img.pixels[i])
        b = 255 - blue(img.pixels[i])
        a = alpha(img.pixels[i])
        gray = (r+g+b)/3
        img.pixels[i] = color(gray,a)
    image(img,250,150)

def makeNegative(Picture): #Negative 
    img = loadImage(str(Picture))
      
    loadPixels()
    for i in range(0,len(img.pixels)):
        r = 255 - red(img.pixels[i])
        g = 255 - green(img.pixels[i])
        b = 255 - blue(img.pixels[i])
        a = alpha(img.pixels[i])
        img.pixels[i] = color(r,g,b,a)
    image(img,90,-50)

def reduceBlue(Picture,x): #use decimals
    img = loadImage(str(Picture))

    x = float(x)
    loadPixels()
    for i in range(0,len(img.pixels)):
        r = red(img.pixels[i])
        g = green(img.pixels[i])
        b = x*blue(img.pixels[i])
        img.pixels[i] = color(r,g,b)
    image(img,450,20)    

def makeRed(Picture):
    img = loadImage(str(Picture))
    
    loadPixels()
    for i in range(0,len(img.pixels)):
        r = red(img.pixels[i]) 
        g = 0
        b = 0
        img.pixels[i] = color(r,g,b)
    image(img,20,200)

def clearBlue(Picture):
    img = loadImage(str(Picture))
    
    loadPixels()
    for i in range(0,len(img.pixels)):
        r = red(img.pixels[i]) 
        g = green(img.pixels[i])
        b = 0
        img.pixels[i] = color(r,g,b)
    image(img,375,200)

def reduceRed(Picture,x): #use decimals
    img = loadImage(str(Picture))

    x = float(x)
    loadPixels()
    for i in range(0,len(img.pixels)):
        r = x*red(img.pixels[i])
        g = green(img.pixels[i])
        b = blue(img.pixels[i])
        img.pixels[i] = color(r,g,b)
    image(img,20,425)

def makeBlue(Picture):
    img = loadImage(str(Picture))
    
    loadPixels()
    for i in range(0,len(img.pixels)):
        r = 0 
        g = 0
        b = blue(img.pixels[i])
        a = alpha(img.pixels[i])
        img.pixels[i] = color(r,g,b,a)
    image(img,100,0)


def clearRed(Picture):
    img = loadImage(str(Picture))
    
    loadPixels()
    for i in range(0,len(img.pixels)):
        r = 0 
        g = green(img.pixels[i])
        b = blue(img.pixels[i])
        img.pixels[i] = color(r,g,b)
    image(img,360,425)

def makeGray(Picture):
    img = loadImage(str(Picture))
    
    loadPixels()
    for i in range(0,len(img.pixels)):
        r = red(img.pixels[i])
        g = green(img.pixels[i])
        b = blue(img.pixels[i])
        a = alpha(img.pixels[i])
        gray =(r+g+b)/3
        img.pixels[i] = color(gray,a)
    image(img,575,425)

def makeGreen(Picture):
    img = loadImage(str(Picture))
    
    loadPixels()
    for i in range(0,len(img.pixels)):
        r = 0 
        g = green(img.pixels[i])
        b = 0
        img.pixels[i] = color(r,g,b)
    image(img,250,325)

def clearGreen(Picture):
    img = loadImage(str(Picture))

    loadPixels()
    for i in range(0,len(img.pixels)):
        r = red(img.pixels[i]) 
        g = 0 
        b = blue(img.pixels[i])
        img.pixels[i] = color(r,g,b)
    image(img,250,425)

def reduceGreen(Picture,x): #use decimals
    img = loadImage(str(Picture))
    
    x = float(x)
    loadPixels()
    for i in range(0,len(img.pixels)):
        r = red(img.pixels[i])
        g = x*green(img.pixels[i])
        b = blue(img.pixels[i])
        a = alpha(img.pixels[i])
        img.pixels[i] = color(r,g,b,a)
    image(img,275,-50)   

#Saying
textSize(32)
fill(0)
text("It's My Life...", 40, 50)
text("-Billy Joel",400,400)

#Pitures
reduceBlue('computers.jpg',.5)
makeRed('xbox.gif')
clearBlue('last.jpg')

reduceRed('track.jpg',.25)
clearRed('coding.jpg')

makeGreen('chicago.jpg')
clearGreen('fallout.jpg')

#Transparent Background 
rotate(0.1)
negGray('tux.png')

rotate(-.125)
makeGray('Baseball.png')

rotate(.3)
reduceGreen('devon.png',.25)

rotate(.8)
makeNegative('basketball.png')

rotate(-.8)
makeBlue('sixf.png')
