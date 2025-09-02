from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align= "center", font= ("Arial", 14))
        self.increment()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align = 'center', font= ('Arial', 20))
   
    def increment(self):
        self.score += 1
    
        
        

