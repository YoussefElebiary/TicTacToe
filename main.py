'''
* Name           :    TicTacToe
* Description    :    This is a simple TicTacToe game
* Author         :    Youssef Elebiary
* Version        :    1.0
'''



# === Imports ===
from tkinter import *
from os import path
from sys import executable



# === Game Class ===
class TicTacToe(Tk):
    # Initializing the GUI
    def __init__(self):
        super().__init__()
        # Main Window
        self.title("TicTacToe")
        self.geometry("300x300")
        self.resizable(0, 0)
        self.iconbitmap("icon.ico")
        print(path.join(path.dirname(executable), "icon.ico"))

        self.paper = Canvas(self)
        self.paper.pack(fill=BOTH, expand=True)
        self.paper.bind("<Button-1>", self.get_pos)
        self.draw_grid()
        # Setting The Variables
        self.turn = 0
        self.isWinner = False
        self.played = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    # Drawing the Grid
    def draw_grid(self):
        self.paper.create_line(100, 0, 100, 300, fill="black", width=5)
        self.paper.create_line(200, 0, 200, 300, fill="black", width=5)
        self.paper.create_line(0, 100, 300, 100, fill="black", width=5)
        self.paper.create_line(0, 200, 300, 200, fill="black", width=5)

    # Draw X
    def draw_x(self, corner: tuple):
        x = corner[0]
        y = corner[1]
        self.paper.create_line((100 * x + 10), (100 * y + 10), ((100 * (x + 1)) - 10), ((100 * (y + 1)) - 10), width = 5, fill = "red")
        self.paper.create_line(((100 * (x + 1)) - 10), (100 * y + 10), (100 * x  + 10), ((100 * (y + 1)) - 10), width = 5, fill = "red")
        self.paper.update()

    # Draw O
    def draw_y(self, corner: tuple):
        x = corner[0]
        y = corner[1]
        self.paper.create_oval((100 * x + 10), (100 * y + 10), ((100 * (x + 1)) - 10), ((100 * (y + 1)) - 10), width = 5, outline = "lime")
        self.paper.update()

    # Get Position
    def get_pos(self, event):
        x_cord = event.x
        y_cord = event.y
        self.get_corner((x_cord, y_cord))

    # Get Cell Number
    def get_corner(self, pos: tuple):
        x = pos[0]
        y = pos[1]
        x_corner = 0 if x == 300 else (x // 100)
        y_corner = 2 if y == 300 else (y // 100)

        self.corners = (x_corner, y_corner)
        self.player_turn()
        
    # Get Player Turn
    def player_turn(self):
        want_to_play = self.played[self.corners[1]][self.corners[0]]
        if (self.turn == 0 and want_to_play != 0 and want_to_play != 1 and not self.isWinner):
            self.draw_x(corner=self.corners)
            self.played[self.corners[1]][self.corners[0]] = 0
            self.check_winner()
            self.turn = 1
        elif (self.turn == 1 and want_to_play != 0 and want_to_play != 1 and not self.isWinner):
            self.draw_y(self.corners)
            self.played[self.corners[1]][self.corners[0]] = 1
            self.check_winner()
            self.turn = 0

    # Check Winner
    def check_winner(self):
        # Check Left Column
        if (self.played[0][0] == self.played[1][0] == self.played[2][0] != None):
            self.paper.create_line(50, 10, 50, 290, fill='blue', width=7)
            self.isWinner = True
        # Check Middle Column
        elif (self.played[0][1] == self.played[1][1] == self.played[2][1] != None):
            self.paper.create_line(150, 10, 150, 290, fill='blue', width=7)
            self.isWinner = True
        # Check Right Column
        elif (self.played[0][2] == self.played[1][2] == self.played[2][2] != None):
            self.paper.create_line(250, 10, 250, 290, fill='blue', width=7)
            self.isWinner = True
        # Check Top Row
        elif (self.played[0][0] == self.played[0][1] == self.played[0][2] != None):
            self.paper.create_line(10, 50, 290, 50, fill='blue', width=7)
            self.isWinner = True
        # Check Middle Row
        elif (self.played[1][0] == self.played[1][1] == self.played[1][2] != None):
            self.paper.create_line(10, 150, 290, 150, fill='blue', width=7)
            self.isWinner = True
        # Check Bottom Row
        elif (self.played[2][0] == self.played[2][1] == self.played[2][2] != None):
            self.paper.create_line(10, 250, 290, 250, fill='blue', width=7)
            self.isWinner = True
        # Check Left To Right Diagonal
        elif (self.played[0][0] == self.played[1][1] == self.played[2][2] != None):
            self.paper.create_line(10, 10, 290, 290, fill='blue', width=7)
            self.isWinner = True
        # Check Right To Left Diagonal
        elif (self.played[2][0] == self.played[1][1] == self.played[0][2] != None):
            self.paper.create_line(10, 290, 290, 10, fill='blue', width=7)
            self.isWinner = True
        # Check Draw
        elif (all(i != None for row in self.played for i in row)):
            print("THE GAME IS DRAW")

        # Display Winner GUI if a player won
        if (self.isWinner):
            self.winner_gui()

    # Winner GUI
    def winner_gui(self):
        self.root = Toplevel(self)
        winner = "X" if self.turn == 0 else "O"
        Label(self.root, text=f"Congratulations! {winner} won the game!", font=('bold', 14),).pack(side=TOP)
        Button(self.root, text="Play Again!", font=('bold', 12), command=self.play_again).pack(side=BOTTOM)

    # Play Again
    def play_again(self):
        # Resetting The Variables
        self.turn = 0
        self.isWinner = False
        self.played = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        # Redrawing The Canvas
        self.paper.delete("all")
        self.draw_grid()
        self.root.destroy()



# Calling the class
if __name__ == "__main__":
    TicTacToe().mainloop()
