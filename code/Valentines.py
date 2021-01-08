import tkinter as tk
import turtle
from tkinter import *
import math

curveSize = .5
forwardBot = 55.825
turtleGoto = -100
                  
def curve(forward):
    turtle.speed(0)
    j = forward
    for i in range(200):
        turtle.right(1)
        turtle.forward(j)

def drawHeart(curveSize, forwardBot, turtleGoto):
    curveSize = curveSize
    forwardBot = forwardBot
    turtleGoto = turtleGoto
    
    turtle.penup()
    turtle.goto(0,turtleGoto)
    turtle.pendown()
    turtle.hideturtle()
    turtle.bgcolor("light green")
    turtle.pensize(2)
    turtle.speed(1)
    turtle.color("red","pink")
    
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(forwardBot)
    curve(curveSize)

    turtle.speed(1)
    
    turtle.left(120)
    curve(curveSize)
    
    turtle.speed(1)
    
    turtle.forward(forwardBot)
    turtle.end_fill()
    turtle.right(220)
    
    curveSize *= 1.2
    forwardBot *= 1.2
    turtleGoto -= 20
    drawHeart(curveSize,forwardBot,turtleGoto)
def drawHappyVal():

    turtle.bgcolor("light green")

    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-225,250)
    turtle.color("deep pink")
    style = ('Rosalinda', 30)
    turtle.write('Happy Valentines Day Beautiful!',font = style)

    turtle.goto(-250,-300)
    turtle.write('My love for you never stops growing', font = style)

def quit():
    turtle.bye()
    main.destroy()

def main():

    main = tk.Tk()
    main.iconbitmap('code\heart.ico')
    main.configure(bg ='light blue')
    main.title("Happy Valentines Day <3")

    frame1 = tk.Frame(main).pack(side = 'left')
    frame2 = tk.Frame(main).pack(side = 'left')
    frame3 = tk.Frame(main).pack(side = 'right')
    frame4 = tk.Frame(main).pack(side = 'right')

    def draw():
        drawHappyVal()
        drawHeart(1,111.65,-100)

    def quit():
        turtle.bye()
        main.destroy()
        
    
    button1 = tk.Button(frame4, text = 'Heart', command = draw, fg = 'purple', bg = 'dark grey')
    quitButton = tk.Button(frame4, text = 'Quit', command = quit, fg = 'red', bg = 'dark grey')

    label1 = tk.Label(frame1, text = "I just wanted to make you \nsomething special, I really hope you like it.", bg = 'light blue').pack(side='left')
    
    
    scroll = tk.Scrollbar(frame4).pack(side = tk.RIGHT, fill = tk.Y)
    text2 = tk.Text(frame4, height = 25, width = 80)
    text2.insert(tk.END, """Spider-Man is a fictional superhero created by writer-editor Stan Lee and writer-artist Steve Ditko. He first appeared in the anthology comic book
Amazing Fantasy #15 (Aug. 1962) in the Silver Age of Comic Books. He appears in American comic books published by Marvel Comics, as well as in a number of movies, television
shows, and video game adaptations set in the Marvel Universe. In the stories, Spider-Man is the alias of Peter Parker, an orphan raised by his Aunt May and Uncle Ben in New York
City after his parents Richard and Mary Parker died in a plane crash. Lee and Ditko had the character deal with the struggles of adolescence and financial issues, and accompanied
him with many supporting characters, such as J. Jonah Jameson, Harry Osborn, Max Modell, romantic interests Gwen Stacy and Mary Jane Watson, and foes such as Doctor Octopus, the
Green Goblin and Venom. His origin story has him acquiring spider-related abilities after a bite from a radioactive spider; these include clinging to surfaces, superhuman strength
and agility, and detecting danger with his "spider-sense." He then builds wrist-mounted "web-shooter" devices that shoot artificial spider-webbing of his own design.""")

    
    
    def pack():
        answer = tk.messagebox.askquestion(title = "Forever.", message = "I love you the most.")
        while answer == 'no':
            wrong = tk.messagebox.showinfo(title = 'Never.', message = 'Wrong. Press again :)')
            answer = tk.messagebox.askquestion(title = "Forever.", message = "I love you the most.")
            if answer == 'yes':
                text2.pack(side = 'top')

            
        

    
        
                                  
                                  
    loveMessageButton = tk.Button(frame4, text = 'Press Me First', command = pack, fg = 'yellow', bg ='dark grey')
    loveMessageButton.pack()
    button1.pack()
    quitButton.pack()

    tk.mainloop()

main()
    

