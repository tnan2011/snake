from tkinter import *
import random

from characters import Snake, Food

H = 800 # chiều cao của màn hình 
W = 1000 # chiều rộng của màn hình
BG = 'black' # màu nền
SPEED = 100 # tốc độ của con rắn
DEFAULT_CHARACTER_SIZE = 25  # kích thước của hình vuông

squares = []
score = 0
direction = 'down'

def change_direction(new_direction):
    global direction 
    # print(new_direction)

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction 
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction 
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction 
    elif direction != 'up':
            direction = new_direction 
        
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text='GAME OVER', fill='red')

def next_turn(snake, food):
    if direction == 'up':
        snake.up()
    elif direction == 'down':
        snake.down()
    elif direction == 'left':
        snake.left()
    else:
        snake.right()
    
    x, y = snake.coordinates[0] # head of the snake

    square = canvas.create_rectangle(x, y, x+DEFAULT_CHARACTER_SIZE, y+DEFAULT_CHARACTER_SIZE, fill='green', tag='snake')
    squares.insert(0, square)
    
    
    if snake.eatFood(food):
        global score
        score += 1
        label['text'] = f"Score: {score}"
        print(score)
        canvas.delete('food')
        food = Food()
        canvas.create_oval(food.x, food.y, food.x+DEFAULT_CHARACTER_SIZE, food.y+DEFAULT_CHARACTER_SIZE, fill='red', tag='food')
    
    else:
        snake.delete_tail()
        canvas.delete(squares[-1])
        squares.pop()

    if snake.byteItself() or snake.hittingWall():
        game_over()
    else: 
        window.after(SPEED, next_turn, snake, food)


window = Tk()
window.title("Snake game")
window.resizable(False, False)

label = Label(window, text=f"Score: {score}", font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BG, height=H, width=W)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

s = Snake()
f = Food()

for x, y in s.coordinates:
    square = canvas.create_rectangle(x, y, x+DEFAULT_CHARACTER_SIZE, y+DEFAULT_CHARACTER_SIZE, fill='green', tag='snake')
    squares.append(square)

canvas.create_oval(f.x, f.y, f.x+DEFAULT_CHARACTER_SIZE, f.y+DEFAULT_CHARACTER_SIZE, fill='red', tag='food')

next_turn(s, f)

window.mainloop()

