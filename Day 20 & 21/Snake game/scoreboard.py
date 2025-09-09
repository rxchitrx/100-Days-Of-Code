from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.highscore = 0
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", False, align= "center", font= ("Arial", 14))
        

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
   
    def increment(self):
        self.score += 1
        self.update_scoreboard()
    
        
        

