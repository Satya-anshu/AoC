lines = open('sample2.txt','r').readlines()
bagMap = {}
bagCountMap = {}
shinygold = 'shiny gold'

for line in lines:
    bags = line.strip('\n').strip('.').split('contain')
    ''' Left side => Outer Bag
        Rest = Inner Bag'''
    outer_bag = ' '.join(bags[0].split(' ')[:2])
    outer_bag = outer_bag.rstrip()
    inner_bags = bags[1].split(',')
    inner_bag = []
    bagDict = {}
    for i in inner_bags:
        i = i.lstrip().rstrip().strip('bag').strip('bags')
        i = i.rstrip()
        ib = ' '.join(i.split(' ')[1:])
        if ib != 'other':
            num_ib = int(i.split(' ')[0])
            bagDict[ib] = num_ib
            if ib not in bagMap:
                bagMap[ib] = []
            bagMap[ib].append(outer_bag)
    bagCountMap[outer_bag] = bagDict

'''
Find shiny gold and count bags
'''
def findBags(bag, bagMap, bagSeen):
    if bag in bagSeen:
        return
    elif bag not in bagMap:
        '''Leaf node'''
        bagSeen.add(bag)
        return
    bagSeen.add(bag)
    for each_bag in bagMap[bag]:
        findBags(each_bag,bagMap,bagSeen)
    

bagSeen = set()
if shinygold in bagMap:
    for i in bagMap[shinygold]:
        findBags(i, bagMap,bagSeen)
print("Part1 Puzzle: ",len(bagSeen))

'''
Find Count of Inner Bags
'''
def findInnerBags(key, bagCountMap):
    count = 0
    for key,value in bagCountMap[key].items():
        count += value + value * findInnerBags(key,bagCountMap)
    return count

count = 0
for key,value in bagCountMap[shinygold].items():
    count += value + value * findInnerBags(key,bagCountMap)

print("Part2 Puzzle: ", count)
