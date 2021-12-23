# Thanks to https://github.com/anthonywritescode/aoc2021/tree/main/day22 for his solution!

from functools import partial
import os
import copy
import collections
from typing import NamedTuple
import pytest
import numpy as np

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10
'''

test_input_2 = \
'''on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682
'''
class Cube(NamedTuple):
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

    @property
    def size(self) -> int:
        return (
            (self.x2 - self.x1) *
            (self.y2 - self.y1) *
            (self.z2 - self.z1)
        )
    
    def intersects(self, other) -> bool:
        return (
            self.x1 <= other.x2 - 1 and
            self.x2 - 1 >= other.x1 and
            self.y1 <= other.y2 - 1 and
            self.y2 - 1 >= other.y1 and
            self.z1 <= other.z2 - 1 and
            self.z2 - 1 >= other.z1
        )

    def contains(self, other) -> bool:
        return (
            self.x1 <= other.x1 and
            self.x2 >= other.x2 and
            self.y1 <= other.y1 and
            self.y2 >= other.y2 and
            self.z1 <= other.z1 and
            self.z2 >= other.z2
        )
    
    def subtract(self, other):
        if not self.intersects(other):
            return [self]
        elif other.contains(self):
            return []
        
        xs = sorted((self.x1, self.x2, other.x1, other.x2))
        ys = sorted((self.y1, self.y2, other.y1, other.y2))
        zs = sorted((self.z1, self.z2, other.z1, other.z2))

        ret = []
        for x1, x2 in zip(xs, xs[1:]):
            for y1, y2 in zip(ys, ys[1:]):
                for z1, z2 in zip(zs, zs[1:]):
                    cube = Cube(x1, x2, y1, y2, z1, z2)
                    if self.contains(cube) and not cube.intersects(other):
                        ret.append(cube)
        return ret
    
    @classmethod
    def parse(cls, x: str, y: str, z: str):
        x1_s, x2_s = x.split('..')
        y1_s, y2_s = y.split('..')
        z1_s, z2_s = z.split('..')
        return cls(
            int(x1_s), int(x2_s) + 1,
            int(y1_s), int(y2_s) + 1,
            int(z1_s), int(z2_s) + 1,
        )

class Cuboid_2(NamedTuple):
    on: bool
    cube: Cube
    
    @classmethod
    def parse(cls, line:str):
        ins, xyz_s = line.split(" ")
        x_s,y_s,z_s = xyz_s.split(",")
        return cls(
            ins == 'on',
            Cube.parse(x_s[2:],y_s[2:],z_s[2:])
        )

class Cuboid(NamedTuple):
    on: bool
    x: tuple[int,int]
    y: tuple[int,int]
    z: tuple[int,int]
    
    @classmethod
    def parse(cls, line:str):
        ins, xyz_s = line.split(" ")
        x_s,y_s,z_s = xyz_s.split(",")
        x1,x2 = map(int,x_s.split("=")[1].split(".."))
        y1,y2 = map(int,y_s.split("=")[1].split(".."))
        z1,z2 = map(int,z_s.split("=")[1].split(".."))
        return cls(
            ins == 'on',
            (int(x1), int(x2)),
            (int(y1), int(y2)),
            (int(z1), int(z2)),
        )

def solve_1(lines):
    cuboids = [Cuboid.parse(line) for line in lines.splitlines()]
    coords = set()
    for ins in cuboids:
        new_coords = {
            (x,y,z)
            for x in range(max(ins.x[0],-50), min(ins.x[1],50) + 1)
            for y in range(max(ins.y[0],-50), min(ins.y[1],50) + 1)
            for z in range(max(ins.z[0],-50), min(ins.z[1],50) + 1)
        }
        if ins.on:
            coords |= new_coords
        else:
            coords -= new_coords
    return len(coords)

def solve_2(lines):
    cuboids = [Cuboid_2.parse(line) for line in lines.splitlines()]
    
    cubes: list[Cube] = []
    for step in cuboids:
        cubes = [
            part
            for cube in cubes
            for part in cube.subtract(step.cube)
        ]
        if step.on:
            cubes.append(step.cube)
    
    return sum(cube.size for cube in cubes)

def test(input_s, expected):
    assert(solve_1(input_s) == expected)

if __name__ == "__main__":
    lines = open("input.txt","r").read()
    print('Part 1: ',solve_1(lines))
    print('Part 2: ',solve_2(lines))