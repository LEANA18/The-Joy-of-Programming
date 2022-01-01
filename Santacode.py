c = circle(r=100,fill="#A30000",stroke="none")
r=rectangle(x=0,y=105,w=25,h=15,fill="#C0C0C0",stroke="none")
x1,y1=0,111
x2,y2=0,200
l=line(x1,y1,x2,y2,stroke="#000000",stroke_width=2)
shape=circle(x=50,y=0,r=50,stroke="#FFFFFF",stroke_width=2)|repeat(6,rotate(60))
show(c,r,l)
show(shape)

          
