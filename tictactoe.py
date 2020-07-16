#!/usr/bin/python
# Author: sgrmshrsm7

from tkinter import *

window = Tk()
window.minsize(400, 480)
window.maxsize(400, 480)
positionRight = int(window.winfo_screenwidth() / 2 - 200)
positionDown = int(window.winfo_screenheight() / 2 - 240)
window.geometry('+{}+{}'.format(positionRight, positionDown))
window.configure(background='#ffd2a5')
window.title('TicTacToe')

gridcolor = '#a5d2ff'
gridtxt = '#000000'
btncolor = '#d2a5ff'
name = 'Player1'
name1 = 'Player1'
name2 = 'Player2'
char = 'O'
turn = 0

vslabel = Label(window, text = name1 + ' vs ' + name2, font = 'Helvetica 22 bold', bg = '#ffd2a5', fg = '#222222')
vslabel.place(relx = 0.5, y = 25, anchor = CENTER)

grid = [[0 for x in range(3)] for y in range(3)]
label = Label(window, text = name + '\'s turn', font = 'Helvetica 22 bold', bg = '#ffd2a5', fg = '#222222')
label.place(relx = 0.5, y = 375, anchor = CENTER)

def playagain():
        global turn
        global char
        global name
        turn = 0
        char = 'O'
        name = name1
        for i in range(3):
                for j in range(3):
                        grid[i][j]['text'] = ' '
                        grid[i][j]['bg'] = gridcolor
        label['text'] = name + '\'s turn'

playagainbutton = Button(window, text = ' Play Again ', fg = '#ffffff', bg = '#0080ff', command = playagain, font = 'Helvetica 20', borderwidth = 0)
playagainbutton.place(x = 50, y = 400, height = 50, width = 140)
exitbutton = Button(window, text = ' Exit ', fg = '#ffffff', bg = '#0080ff', command = window.destroy, font = 'Helvetica 20', borderwidth = 0)
exitbutton.place(x = 210, y = 400, height = 50, width = 140)

def wincheck():
        win = False
        if grid[0][0]['text'] != ' ' and grid[0][0]['text'] == grid[0][1]['text'] == grid[0][2]['text']:
                grid[0][0]['bg'] = '#ee9090'
                grid[0][1]['bg'] = '#ee9090'
                grid[0][2]['bg'] = '#ee9090'
                win = True
        elif grid[1][0]['text'] != ' ' and grid[1][0]['text'] == grid[1][1]['text'] == grid[1][2]['text']:
                grid[1][0]['bg'] = '#ee9090'
                grid[1][1]['bg'] = '#ee9090'
                grid[1][2]['bg'] = '#ee9090'
                win = True
        elif grid[2][0]['text'] != ' ' and grid[2][0]['text'] == grid[2][1]['text'] == grid[2][2]['text']:
                grid[2][0]['bg'] = '#ee9090'
                grid[2][1]['bg'] = '#ee9090'
                grid[2][2]['bg'] = '#ee9090'
                win = True
        elif grid[0][0]['text'] != ' ' and grid[0][0]['text'] == grid[1][0]['text'] == grid[2][0]['text']:
                grid[0][0]['bg'] = '#ee9090'
                grid[1][0]['bg'] = '#ee9090'
                grid[2][0]['bg'] = '#ee9090'
                win = True
        elif grid[0][1]['text'] != ' ' and grid[0][1]['text'] == grid[1][1]['text'] == grid[2][1]['text']:
                grid[0][1]['bg'] = '#ee9090'
                grid[1][1]['bg'] = '#ee9090'
                grid[2][1]['bg'] = '#ee9090'
                win = True
        elif grid[0][2]['text'] != ' ' and grid[0][2]['text'] == grid[1][2]['text'] == grid[2][2]['text']:
                grid[0][2]['bg'] = '#ee9090'
                grid[1][2]['bg'] = '#ee9090'
                grid[2][2]['bg'] = '#ee9090'
                win = True
        elif grid[0][0]['text'] != ' ' and grid[0][0]['text'] == grid[1][1]['text'] == grid[2][2]['text']:
                grid[0][0]['bg'] = '#ee9090'
                grid[1][1]['bg'] = '#ee9090'
                grid[2][2]['bg'] = '#ee9090'
                win = True
        elif grid[0][2]['text'] != ' ' and grid[0][2]['text'] == grid[1][1]['text'] == grid[2][0]['text']:
                grid[0][2]['bg'] = '#ee9090'
                grid[1][1]['bg'] = '#ee9090'
                grid[2][0]['bg'] = '#ee9090'
                win = True
        return win

def updategrid(a, b):
        global char
        global turn
        global name
        if grid[a][b]['text'] == ' ' and not wincheck():
                grid[a][b]['text'] = char
                if wincheck():
                        label['text'] = name + ' won the match !!!'
                else:
                        if turn < 8:
                                if char == 'O':
                                        char = 'X'
                                        name = name2
                                else:
                                        char = 'O'
                                        name = name1
                                turn += 1
                                label['text'] = name + '\'s turn'
                        else:
                                label['text'] = 'Match Drawn!!!'

grid[0][0] = Button(window, text = ' ', fg = gridtxt, bg = gridcolor, font = 'Helvetica 40 bold', borderwidth = 0, command = lambda: updategrid(0, 0))
grid[0][1] = Button(window, text = ' ', fg = gridtxt, bg = gridcolor, font = 'Helvetica 40 bold', borderwidth = 0, command = lambda: updategrid(0, 1))
grid[0][2] = Button(window, text = ' ', fg = gridtxt, bg = gridcolor, font = 'Helvetica 40 bold', borderwidth = 0, command = lambda: updategrid(0, 2))
grid[1][0] = Button(window, text = ' ', fg = gridtxt, bg = gridcolor, font = 'Helvetica 40 bold', borderwidth = 0, command = lambda: updategrid(1, 0))
grid[1][1] = Button(window, text = ' ', fg = gridtxt, bg = gridcolor, font = 'Helvetica 40 bold', borderwidth = 0, command = lambda: updategrid(1, 1))
grid[1][2] = Button(window, text = ' ', fg = gridtxt, bg = gridcolor, font = 'Helvetica 40 bold', borderwidth = 0, command = lambda: updategrid(1, 2))
grid[2][0] = Button(window, text = ' ', fg = gridtxt, bg = gridcolor, font = 'Helvetica 40 bold', borderwidth = 0, command = lambda: updategrid(2, 0))
grid[2][1] = Button(window, text = ' ', fg = gridtxt, bg = gridcolor, font = 'Helvetica 40 bold', borderwidth = 0, command = lambda: updategrid(2, 1))
grid[2][2] = Button(window, text = ' ', fg = gridtxt, bg = gridcolor, font = 'Helvetica 40 bold', borderwidth = 0, command = lambda: updategrid(2, 2))

for a in range(3):
        for b in range(3):
                grid[a][b].place(x = (50 + 100 * b), y = (50 + 100 * a), height = 100, width = 100)

window.mainloop()