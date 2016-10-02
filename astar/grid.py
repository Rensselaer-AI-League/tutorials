from vector import Vector

def charToElevation(c):
    try:
        return int(c)
    except ValueError:
        numLetters = ord('Z') - ord('A')
        n = ord(c) - ord('A')
        if n >= 0 and n <= numLetters:
            return ord(c) - ord('A') + 10
        else:
            return ord(c) - ord('a') + 11 + (ord('Z') - ord('A'))
        
def elevationToChar(e):
    numLetters = ord('Z') - ord('A')
    if e < 10:
        return str(e)
    if e <= 10 + numLetters:
        return chr(e - 10 + ord('A'))
    return chr(e - 11 - numLetters + ord('a'))
        
def makeMap(width, height, roughness = 1.0):
    val = 0
    low = 0
    high = 0
    res = []
    for y in range(height):
        res.append([])
        for x in range(width):
            val += int(math.floor(r.gauss(0, roughness)+0.5))
            if val > high:
                high = val
            elif val < low:
                low = val
            res[-1].append(val)
    for y in range(height):
        for x in range(width):
            res[y][x] -= low
    high -= low
    string = '%s %s\n' % (width, height)
    for y in range(height):
        for x in range(width):
            string += elevationToChar(res[y][x])
        string += '\n'
    return string

class Grid:
    def __init__(self, filename):
        with open(filename) as f:
            self.width, self.height = map(int, f.readline().split())
            self.grid = [[None for j in range(self.height)] for i in range(self.width)]
            for y in range(self.height):
                row = f.readline()
                for x in range(self.width):
                    self.grid[x][y] = charToElevation(row[x])
    
    def __str__(self):
        gridStr = [''] * self.height
        
        for x, row in enumerate(self.grid):
            for y, val in enumerate(row):
                gridStr[y] += elevationToChar(val)
                
        res = ''
        for row in gridStr:
            res += row  + '\n'  
        return res
    
    def __call__(self, x, y = None):
        if y is None:
            y = x[1]
            x = x[0]
        if x < 0 or y < 0:
            raise IndexError()
        return self.grid[x][y]
    
    def size(self):
        return (self.width, self.height)
    
    def cost(self, loc, direction):
        end = Vector(loc) + Vector(direction)
        return abs(self(loc) - self(end))
    
    def validDirs(self, loc):
        validDirs = set([])
        for direction in [(1,0), (-1,0), (0,1), (0,-1)]:
            end = Vector(loc) + Vector(direction)
            try:
                val = self(end)
                validDirs.add(direction)
            except IndexError:
                pass
        return validDirs
    
    def greedyPathTo(self, start, end):
        pass
    
    def pathTo(self, start, end):
        pass
        

if __name__ == "__main__":
    import math
    import random as r
    
    filename = 'map3.txt'
    
    grid = Grid(filename)
    
    print grid
        
    #print makeMap(30,30)
    #print makeMap(30,30, 1.5)