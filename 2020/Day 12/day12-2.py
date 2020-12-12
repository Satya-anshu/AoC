import math
lines = open('sample.txt','r').readlines()

class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.wayX = 10
        self.wayY = 1
    
    def move(self, direction):
        num = int(direction[1:])
        if direction[0] == 'N':
            self.wayY += num
        elif direction[0] == 'S':
            self.wayY -= num
        elif direction[0] == 'E':
            self.wayX += num
        elif direction[0] == 'W':
            self.wayX -= num
        elif direction[0] == 'L':
            for i in range(num // 90):
                self.wayX, self.wayY = self.wayY, self.wayX
                self.wayX *= -1
        elif direction[0] == 'R':
            for i in range(num // 90):
                self.wayY, self.wayX = self.wayX, self.wayY
                self.wayY *= -1
        else:
            self.x += self.wayX * num
            self.y += self.wayY * num   
        print(direction,self.x, self.y, self.wayX, self.wayY)
        
def main():
    ship = Ship()
    for line in lines:
        line = line.strip('\n')
        ship.move(line)
    print("Part 2: ", abs(ship.x) + abs(ship.y),0)
main()
