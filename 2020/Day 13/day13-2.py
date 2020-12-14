import helpers

def part2(ids):
    ids = ids.split(',')
    remainders = []
    mods = []
    prod = 1
    for idx, val in enumerate(ids):
        if val == 'x':
            continue
        val = int(val)
        remainders.append((-idx) % val)
        mods.append(val)
        prod *= val
    total = 0
    print(remainders, mods)
    for i in range(len(mods)):
        # b_i * n_i * x_i
        total += remainders[i] * int(prod/mods[i]) * pow(int(prod/mods[i]), -1, mod=mods[i])
    return total % prod

with open("in.txt", "r") as file:
    lines = file.read().splitlines()
    file.close()

print("Part 2: ", part2(lines[1]))
