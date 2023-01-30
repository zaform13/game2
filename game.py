import turtle

#okno
w = turtle.Screen() #defniuje zmieną "wn" która pojawia okno
w.title("Pong") #nazywa okno "Pong"
w.bgcolor("black") #ustawia tło na czarno
w.setup(width=800, height=600) #ustawia szerokość i wysokość okna
w.tracer(0) #wyłącza animacje żółwia

# punkty
score_a = 0  #tworzy zmienną punktów paletki a
score_b = 0  #tworzy zmienną punktów paletki b

# paletka czerwona
pad_a = turtle.Turtle() #tworzy nowego żółwia
pad_a.speed(0) #ustawia prędkość żółwia na 0
pad_a.shape("square") #ustawia kształt żówia na kwadrat
pad_a.color("red") #ustawia kolor żółwia na czerwony
pad_a.shapesize(stretch_wid=5.1,stretch_len=0.8) #ustawia szerokość i wysokość żówia
pad_a.penup() #podnosi pisak
pad_a.goto(-338, -200) #ustawia paletke na danym punkcie

# paletka niebieska
pad_b = turtle.Turtle() #tworzy nowego żółwia
pad_b.speed(0) #ustawia prędkość żółwia na 0
pad_b.shape("square") #ustawia kształt żówia na kwadrat
pad_b.color("blue") #ustawia kolor żółwia na niebieski
pad_b.shapesize(stretch_wid=5.1,stretch_len=0.85) #ustawia szerokość i wysokość żówia
pad_b.penup() #podnosi pisak
pad_b.goto(338, 250) #ustawia paletke na danym punkcie

# piłka
ball = turtle.Turtle() #tworzy nowego żółwia
ball.speed(0) #ustawia prędkość żółwia na 0
ball.shape("circle") #ustawia kształt żówia na koło
ball.color("white") #ustawia kolor żółwia na biały
ball.penup() #podnosi pisak
ball.goto(0, 0) #ustawia piłke na srodku ekranu po uruchomieniu gry
ball.dx = 0.42 #ile jednostek przesunie sie piłka na osi x jeśli wykona krok
ball.dy = 0.42 #ile jednostek przesunie sie piłka na osi y jeśli wykona krok

# tekst
pen = turtle.Turtle() #tworzy nowego żółwia
pen.speed(0) #ustawia prędkość żółwia na 0
pen.shape("square") #ustawia kształt żówia na kwadrat
pen.color("white") #ustawia kolor żółwia na biały
pen.penup() #podnosi pisak
pen.hideturtle() #ukrywa żółwia
pen.goto(0, 260) #ustawia tekst na danym punkcie
pen.write("gracz czerwony: 0  gracz niebieski: 0", align="center", font=("Courier", 16, "normal")) #pisze tekst w wybranym miejscu, wybraną czcionnką i wielkościa liter

# Poruszanie sie platform
def pad_a_up():
    y = pad_a.ycor() #przy naciśnięciu "w" czerwona platworma porusza sie w góre
    y += 55
    pad_a.sety(y)

def pad_a_down():
    y = pad_a.ycor() #przy naciśnięciu "s" czerwona platworma porusza sie w dół
    y -= 55
    pad_a.sety(y)

def pad_b_up():
    y = pad_b.ycor() #przy naciśnięciu strzałki w góre czerwona platworma porusza sie w góre
    y += 55
    pad_b.sety(y)

def pad_b_down():
    y = pad_b.ycor() #przy naciśnięciu strzałki w dół czerwona platworma porusza sie w dół
    y -= 55
    pad_b.sety(y)
 

# Klawisze
wn.listen()
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")

# pętla
while True:
    wn.update()
    
    # ruch piłki
    ball.setx(ball.xcor() + ball.dx) #ustaw kordynat x piłki dodając dynamikę piłki do jego kordynatu x
    ball.sety(ball.ycor() + ball.dy) #ustaw kordynat y piłki dodając kierunek piłki do jego kordynatu y


       #zablokowanie paletek w ekranie
    if pad_a.ycor() > 255:  #lewa w górę
        pad_a.sety(255)

    elif pad_a.ycor() < -255:  #lewa w dół
        pad_a.sety(-255)
      
    if pad_b.ycor() > 255:  #prawa w górę
        pad_b.sety(255)

    elif pad_b.ycor() < -255:  #prawa w dół
        pad_b.sety(-255)

    # granice mapy

    # górna ściana i dolna ściana
    if ball.ycor() > 290:  
        ball.sety(290) #jeśli piłka dotknie wysokości 290 jednostek na osi y odbije sie
        ball.dy *= -1
    
    elif ball.ycor() < -290:
        ball.sety(-290) #jeśli piłka dotknie wysokości -290 jednostek na osi y odbije sie
        ball.dy *= -1

    # lewa ściana i prawa ściana
    if ball.xcor() > 350:  #jeśli przekroczy 350 jednostkę w lewo gracz niebieski dostaje punkt
        score_a += 1
        pen.clear()
        pen.write("gracz czerwony: {}  gracz niebieski: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1 #jeśli przekroczy 350 jednostkę w prawo gracz czerwony dostaje punkt
        pen.clear()
        pen.write("gracz czerwony: {}  gracz niebieski: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # zderzanie sie piłki z paletką
    if ball.xcor() < -337.2 and ball.ycor() < pad_a.ycor() + 60 and ball.ycor() > pad_a.ycor() - 60: #jeśli piłka dotknie środka paletki i obszaru bliskiego od niej o 60 jednostek odbije sie
        ball.dx *= -1 
    
    elif ball.xcor() > 338.85 and ball.ycor() < pad_b.ycor() + 60 and ball.ycor() > pad_b.ycor() - 60: #jeśli piłka dotknie środka paletki i obszaru bliskiego od niej o 60 jednostek odbije sie
        ball.dx *= -1
        
    #wygrana graczy
    if score_a == 10:
        pen.showturtle()
        pen.goto(0, 0) 
        pen.write("RED WON!", align="center", font=("Courier", 60, "normal")) 
        pen.hideturtle()
        ball.hideturtle()

    if score_b == 10:
        pen.showturtle()
        pen.goto(0, 0) 
        pen.write("BLUE WON!", align="center", font=("Courier", 60, "normal")) 
        pen.hideturtle()
        ball.hideturtle()
