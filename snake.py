import keyboard
import time
import os
import random
from dataclasses import dataclass

@dataclass
class pos:
    dim0: int
    dim1: int


os.system('cls' if os.name == 'nt' else 'clear')

current = "s"
snakeLen = 1

#Sets the current key to dictate snake movement
def setKey(key: keyboard.KeyboardEvent):
    global current
    current = key.name

def printField(map):
    for string in map:
        print("".join(string))


def playfieldTemplate(length: int, width: int):

    map = []

    for i in range(length):

        if i == 0 or i == length - 1:
            string = []

            for j in range(width + 4):
                string += "█"
            
            map.append(string)
        else:
            string = ["██"]

            for j in range(width):
                string += "•"
            
            string += "██"

            map.append(string)
    
    return map

def applePos(snake, length, width):
    position = snake[0]

    while position in snake:
        position = pos(random.randrange(start=1, stop=length - 1, step=1), random.randrange(start=2, stop=width + 1, step=1))
    
    return position





keyboard.on_press_key("w", setKey)
keyboard.on_press_key("a", setKey)
keyboard.on_press_key("s", setKey)
keyboard.on_press_key("d", setKey)
keyboard.on_press_key("up arrow", setKey)
keyboard.on_press_key("down arrow", setKey)
keyboard.on_press_key("left arrow", setKey)
keyboard.on_press_key("right arrow", setKey)

if __name__ == "__main__":
    length = int(input("Enter length of playfield (5-30): "))
    width = int(input("Enter width of playfield (5-30): "))

    snake = [pos(width // 2, length // 2)]
    apple = applePos(snake, length, width)

    print(apple)

    os.system('cls' if os.name == 'nt' else 'clear')

    while True:

        start = time.time()

        if snake[0].dim0 <= 2 or snake[0].dim0 >= length - 1 or snake[0].dim1 <= 0 or snake[0].dim1 >= width + 1:
            exit()

        playfield = playfieldTemplate(length, width)

        for coord in snake:
            playfield[coord.dim0][coord.dim1] =  '#'

        os.system('cls' if os.name == 'nt' else 'clear')

        playfield[apple.dim0][apple.dim1] = 'O'

        printField(playfield)

        if apple == snake[0]:
            snakeLen += 1
            apple = applePos(snake, length, width)

        if snakeLen == length * width:
            print("Game over! You win!")
            break

        if current == 'up' or current == 'w':
            snake[0].dim0 -= 1
        elif current == 'down' or current == 's':
            snake[0].dim0 += 1
        elif current == 'left' or current == 'a':
            snake[0].dim1 -= 1
        elif current == 'right' or current == 'd':
            snake[0].dim1 += 1

        end = time.time()
        dur = end - start

        time.sleep(0 if dur >= 0.15 else 0.15 - dur)





    
