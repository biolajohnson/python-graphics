import turtle
import random
import time

class Node:
    def __init__(self, val, x, y) -> None:
        self.val = val
        self.x = x
        self.y = y
        self.next = None


def start_graphics():
    player_one = turtle.Turtle()
    player_two = player_one.clone()
    referee = turtle.Turtle()
    referee.shape("turtle")
    player_one.shape("turtle")
    player_two.shape("turtle")
    player_one.color("blue")
    player_two.color("red")
    player_one.penup()
    player_two.penup()
    player_one.goto(-300, 200)
    player_two.goto(-300, -200)
    referee.penup()
    referee.goto(300, -250)
    referee.pendown()
    referee.color("black")
    referee.left(90)
    referee.forward(500)
    return player_one, player_two
   
def get_move():
    move = random.randint(1, 7)
    return move * 15


def start_game(player_one, player_two):
    while True:
        move = get_move()
        player_one.forward(move)
        time.sleep(1)
        second_move = get_move()
        player_two.forward(second_move)

        if player_one.pos() >= (300, 250) or player_two.pos() >= (300, -200):
            break

    

   
  

def main():
   screen = turtle.Screen()
   screen.bgcolor("lightblue")
   player_one, player_two = start_graphics()
   start_game(player_one, player_two)
   turtle.done()




if __name__ == "__main__":
    main()


