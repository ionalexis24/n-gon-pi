r=400
n=2

def gon(n,R):
    a=TWO_PI/n
    beginShape()
    for j in range(n+1):
        stroke(200)
        strokeWeight(4)
        vertex(cos(j*a)*R,sin(j*a)*R)
    endShape()        

def setup():
    size(2*r+100,2*r+100)
    background(0)
    translate(width/2, height/2)

def draw():
    global n
    background(0)
    translate(width/2, height/2)
    stroke(225)
    strokeWeight(3)
    point(0,0)
    noFill()
    strokeWeight(1)
    circle(0,0,2*r)
    gon(n,r)
    stroke(0,0,255)
    line(r,0,r*cos(TWO_PI/n),r*sin(TWO_PI/n))
    amic=dist(r,0,r*cos(TWO_PI/n),r*sin(TWO_PI/n))
    Per=n*amic
    print(Per/(2*r),TWO_PI*r,Per,amic) 
    delay(300)    
    if n<100:
       n=n+1
