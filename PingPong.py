import turtle
from turtle import*
#window setup for ping pong
wd=turtle.Screen()
wd.setup(800,420)
wd.bgcolor("Black")
wd.tracer(False)
score1,score2=0,0
#Turtles used in program
playerA=turtle.Turtle()
playerB=turtle.Turtle()
Ball=turtle.Turtle()
score=turtle.Turtle()
#initial score(0:0)
score.hideturtle()
hideturtle()
penup()
pencolor("white")
goto(-25,190)
pendown()
write("0",align='center',font=15)
penup()
goto(25,190)
pendown()
write("0",align='center',font=15)

#PlayerA movement upwards
def playerA_moveup():
 y=playerA.ycor()
 
 if y in range(-180,180):
  y+=20
  
  playerA.sety(y)

#PlayerA movement downwards
def playerA_movedown():
 y=playerA.ycor()
 
 if y in range(-160,200):
  y-=20
  
  playerA.sety(y)    

#PlayerB movement upwards
def playerB_moveup():
 y=playerB.ycor()
 
 if y in range(-180,180):
  y+=20
  
  playerB.sety(y)

#PlayerB movement downwards
def playerB_movedown():
 y=playerB.ycor()
 
 if y in range(-160,200):
  y-=20
  
  playerB.sety(y)

#PlayerA Looks
playerA.penup()
playerA.goto(-380,0)
playerA.color("White")
playerA.shape("square")
playerA.shapesize(3,1)

#PlayerA binding keys
wd.onkeypress(playerA_movedown,"s")
wd.listen()
wd.onkeypress(playerA_moveup,"w")
wd.listen()

#PlayerB Looks
playerB.penup()
playerB.goto(370,0)
playerB.color("White")
playerB.shape("square")
playerB.shapesize(3,1)
 
#PlayerB binding keys
wd.onkeypress(playerB_movedown,"Down")
wd.listen() 
wd.onkeypress(playerB_moveup,"Up")
wd.listen()


#Ball Attributes
Ball.speed(1)
Ball.penup()
Ball.goto(0,0)
Ball.color("White")
Ball.shape("circle")
Ball.x1=1
Ball.y1=1


#FPS
while True:
   wd.update()
   #Ball bouncing off the wall condition
   Ball.speed(1)
   Ball.setx(Ball.xcor()+Ball.x1)
   Ball.sety(Ball.ycor()+Ball.y1)
   if Ball.ycor()>=200:
     Ball.y1*=-1

  

   if Ball.ycor()<=-200:
     Ball.y1*=-1

   
   
   score.hideturtle()

   #Score increment after left player scores
   if Ball.xcor()>=390:
    Ball.speed(1)
    score.undo()
    score1+=1
    Ball.goto(0,0)
    
    #Erases previous score and dispays new one
    penup()
    goto(-30,210)
    pendown()
    begin_fill()
    forward(20)
    right(90)
    forward(20)
    right(90)
    forward(20)
    right(90)
    forward(20)
    right(90)
    end_fill()
    score.penup()
    score.goto(-20,190)
    score.pendown()
       
    score.pencolor("white")
    score.write(score1,align='center',font=15)
    



    
   #Score increment after right player scores
   if Ball.xcor()<=-390:
       Ball.speed(1)
       score.undo()
       score2+=1
       Ball.goto(0,0)
       
       #Erases previous score and dispays new one
       penup()
       goto(10,210)
       pendown()
       begin_fill()
       forward(20)
       right(90)
       forward(20)
       right(90)
       forward(20)
       right(90)
       forward(20)
       right(90)
       end_fill()
       score.penup()
       score.goto(20,190)
       score.pendown()
       score.pencolor("white")
       score.write(score2,align='center',font=15)
       
   #Condition for ball to bounce off playerB
   if Ball.xcor()==(playerB.xcor()-20) and (Ball.ycor() in range(playerB.ycor()-60,playerB.ycor()+60)):
     Ball.x1*=-1
     Ball.y1*=-1

   #Condition for ball to bounce off playerA
   if Ball.xcor()==(playerA.xcor()+20) and (Ball.ycor() in range(playerA.ycor()-60,playerA.ycor()+60)):
     
     Ball.x1*=-1
     Ball.y1*=-1
