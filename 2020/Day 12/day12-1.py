import math
lines = open('in.txt','r').readlines()

class Ship:
    def __init__(self):
        self.angle = 0
        self.x = 0
        self.y = 0
        
    def move(self, direction):
        num = int(direction[1:])
        if direction[0] == 'N':
            self.y += num
        elif direction[0] == 'S':
            self.y -= num
        elif direction[0] == 'E':
            self.x += num
        elif direction[0] == 'W':
            self.x -= num
        elif direction[0] == 'L':
            self.angle += (num * math.pi) / 180
        elif direction[0] == 'R':
            self.angle -= (num * math.pi) / 180
        else:
            self.x += num*math.cos(self.angle)
            self.y += num*math.sin(self.angle)

def main():
    ship = Ship()
    for line in lines:
        line = line.strip('\n')
        ship.move(line)
    print("Part 1: ", round(abs(ship.x) + abs(ship.y),0))
main()
