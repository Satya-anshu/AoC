import os
import copy
import collections
from itertools import permutations

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def extract_info(lines):
    scanner = []
    pos = []
    for line in lines:
        if line == '':
            scanner.append(pos)
            pos = []
            continue
        if '---' in line:
            continue
        else:
            x,y,z = map(int,line.split(","))
            pos.append((x,y,z))
    scanner.append(pos)
    return scanner

orientations = set()
for X in (-1,1):
    for Y in (-1,1):
        for Z in (-1,1):
            orientations.add((X,Y,Z))

def check_overlap(scanner, beacon_location,N):
    # Get all possible orientations for scanner and try to map it per beacon. Atleast 12 should be matching
    # Get current position in beacon_location
    new_beacon = copy.deepcopy(beacon_location)
    for beacon in beacon_location:
        # Try to map every beacon of this scanner to this beacon
        # Try all 8*6 orientations of the scanner
        for o in orientations:
            z = permutations(list([0,1,2]))
            for k in list(z):
                new_scanner = set()
                temp = copy.deepcopy(scanner)
                temp = list(scanner)
                for i in range(len(temp)):
                    w = list(temp[i])
                    w[0] *= o[0]
                    w[1] *= o[1]
                    w[2] *= o[2]
                    tt = [0,0,0]
                    tt[k[0]] = w[0]
                    tt[k[1]] = w[1]
                    tt[k[2]] = w[2]
                    new_scanner.add((tt[0],tt[1],tt[2]))
                new_scanner = list(new_scanner)
                for i in range(len(new_scanner)):
                    dx = beacon[0] - new_scanner[i][0]
                    dy = beacon[1] - new_scanner[i][1]
                    dz = beacon[2] - new_scanner[i][2]
                    pos = set()
                    # Find all other positions
                    for j in range(len(new_scanner)):
                        x = new_scanner[j][0] + dx
                        y = new_scanner[j][1] + dy
                        z = new_scanner[j][2] + dz
                        pos.add((x,y,z))
                    # If intersection gets me 12 beacons in place, add these new positions to beacon_location
                    if len(new_beacon.intersection(pos)) >= 12:
                        new_beacon = new_beacon.union(pos)
                        print("Found!",N)
                        scan_pos = (dx,dy,dz)
                        #print(beacon_location.intersection(pos))
                        return True,new_beacon,scan_pos
    return False,None,None

def solve(lines):
    scanner = extract_info(lines)
    # Consider scanner 0 positioned at (0,0,0)
    # Everything else is positioned relative to this.
    # For any 2 scanners, atleast 12 beacons should overlap
    # Each scanner can have 24 orientations
    # (x,y,z) => 8, (y,z,x) => 8, (z,x,y) => 8
    found_beacon_locations = set()

    # Fix locations of scanner 0
    for x,y,z in scanner[0]:
        found_beacon_locations.add((x,y,z))
    
    # Now try to find overlaps for remaining beacons
    vis = set()
    vis.add(0)
    i = 1
    scanner_pos = set()
    scanner_pos.add((0,0,0,0))
    while len(vis) != len(scanner):
        if i not in vis:
            found,pos,scan_pos = check_overlap(scanner[i],found_beacon_locations,i)
            if found:
                vis.add(i)
                found_beacon_locations = copy.deepcopy(pos)
                scan_pos = list(scan_pos)
                scanner_pos.add((i,scan_pos[0],scan_pos[1],scan_pos[2]))
        i+=1
        if i == len(scanner):
            i = 1
    print("Part 1: ",len(found_beacon_locations))
    max_dist = -1
    scanner_pos = list(scanner_pos)
    for i in range(len(scanner_pos)):
        for j in range(i+1,len(scanner_pos)):
            dist_x = abs(scanner_pos[i][1]-scanner_pos[j][1])
            dist_y = abs(scanner_pos[i][2]-scanner_pos[j][2])
            dist_z = abs(scanner_pos[i][3]-scanner_pos[j][3])
            max_dist = max(max_dist, dist_x + dist_y + dist_z)
    print("Part 2: ",max_dist)


if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = open("test.txt","r").read().splitlines()
    solve(lines)