import collections
import copy
import os
import numpy as np

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''

def solve_1(energies,steps):
    total_flashes = 0
    energies = np.pad(energies, (1,1), 'constant', constant_values = np.iinfo(np.int32).min)
    for step in range(steps):
        energies += 1
        flashes = np.any(energies > 9)
        while flashes:
            total_flashes += np.count_nonzero(energies > 9)
            flash_points = np.where(energies > 9)
            energies[energies > 9] = 0
            for point in zip(flash_points[0],flash_points[1]):
                adjacent_points = energies[point[0]-1:point[0]+2, point[1]-1:point[1]+2]
                adjacent_points[adjacent_points != 0] += 1
                energies[point[0]-1:point[0]+2, point[1]-1:point[1]+2] = adjacent_points
            flashes = np.any(energies > 9)
    print(total_flashes)

def solve_2(energies):
    energies = np.pad(energies, (1,1), 'constant', constant_values = np.iinfo(np.int32).min)
    step = 1
    while True:
        energies += 1
        flashes = np.any(energies > 9)
        while flashes:
            flash_points = np.where(energies > 9)
            energies[energies > 9] = 0
            for point in zip(flash_points[0],flash_points[1]):
                adjacent_points = energies[point[0]-1:point[0]+2, point[1]-1:point[1]+2]
                adjacent_points[adjacent_points != 0] += 1
                energies[point[0]-1:point[0]+2, point[1]-1:point[1]+2] = adjacent_points
            flashes = np.any(energies > 9)
        
        if np.all(energies[1:-1, 1:-1] == 0):
            break
        step += 1
    print(step)

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    part1 = np.array([list(energy) for energy in lines]).astype(np.int32)
    part2 = np.array([list(energy) for energy in lines]).astype(np.int32)
    solve_1(part1,100)
    solve_2(part2)
