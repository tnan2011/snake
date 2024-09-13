import random

# Các bạn không thay đổi gì ở các dòng bên dưới này nha
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
DEFAULT_CHARACTER_SIZE = 25


# Các bạn bắt đầu lập trình bên dưới


class Food:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH // DEFAULT_CHARACTER_SIZE) * DEFAULT_CHARACTER_SIZE
        self.y = random.randint(0, SCREEN_HEIGHT // DEFAULT_CHARACTER_SIZE) * DEFAULT_CHARACTER_SIZE

class Snake:
    def __init__(self):
        self.body_sizes = 3
        self.coordinates = []

        for i in range(self.body_sizes):
            self.coordinates.append([0, 0])

    def get_head_coordinates(self):
        return self.coordinates[0]

    def up(self):
        x, y = self.get_head_coordinates()
        y = y - DEFAULT_CHARACTER_SIZE
        self.coordinates.insert(0, [x, y])

    def down(self):
        x, y = self.get_head_coordinates()
        y = y + DEFAULT_CHARACTER_SIZE
        self.coordinates.insert(0, [x, y])

    def left(self):
        x, y = self.get_head_coordinates()
        x = x - DEFAULT_CHARACTER_SIZE
        self.coordinates.insert(0, [x, y])

    def right(self):
        x, y = self.get_head_coordinates()
        x = x + DEFAULT_CHARACTER_SIZE
        self.coordinates.insert(0, [x, y])

    def delete_tail(self):
        self.coordinates.pop()

    def eatFood(self, food):
        x_snake_head, y_snake_head = self.get_head_coordinates()

        if x_snake_head == food.x and y_snake_head == food.y:
            return True
        
        return False