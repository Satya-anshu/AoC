lines = open('in.txt','r').read()

'''
8 possible orientation for the tiles...
'''
class Tile:
    def __init__(self, id, tile):
        self.id = id
        self.tile = tile
        self.edge_match = 0
    
    def flip(self):
        self.tile = [t[::-1] for t in self.tile]

    def rotate(self):
        self.tile = [list(reversed(x)) for x in zip(*self.tile)]

def parse(lines):
    tiles_str = lines.split('\n\n')
    t = []
    for tiles in tiles_str:
        tile_id = int(tiles.splitlines()[0].split(':')[0].split()[1])
        tiles = [t for t in tiles.splitlines()[1:]]
        t.append(Tile(tile_id,tiles))
    return t

def is_match2(tile1,tile2):
    for j in range(4):
        if tile1.tile[0] == tile2.tile[0]:
            return True
        tile2.rotate()
    tile2.flip()
    for j in range(4):
        if tile1.tile[0] == tile2.tile[0]:
            return True
        tile2.rotate()
    return False

def is_match(tile1, tile2):
    for i in range(4):
        if is_match2(tile1,tile2):
            return True
        tile1.rotate()
    tile1.flip()
    for i in range(4):
        if is_match2(tile1,tile2):
            return True
        tile1.rotate()
    return False

def solve(tiles_list):
    #Find 4 corners...basically 2 edges should match...
    for i in range(len(tiles_list)):
        #Try all 8 configuration of i
        #Try all 8 configuration of j
        #If there is a match, increase edge count by 1 for both the tiles
        for j in range(len(tiles_list)):
            if i == j:
                continue
            if is_match(tiles_list[i],tiles_list[j]):
                tiles_list[i].edge_match += 1
                tiles_list[j].edge_match += 1

    ans = 1
    for tile in tiles_list:
        if tile.edge_match == 4:
            ans = ans * tile.id
    print("Part 1: ",ans)
tiles_list = parse(lines)
solve(tiles_list)

