file = open('input.txt','r')
lines = file.readlines()

valid_set = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
valid_ecl = {'amb','blu','brn','gry','grn','hzl','oth'}

def valid_byr(val):
    if val >= 1920 and val <= 2020:
        return 1
    return 0

def valid_iyr(val):
    if val >= 2010 and val <= 2020:
        return 1
    return 0

def valid_eyr(val):
    if val >= 2020 and val <= 2030:
        return 1
    return 0

def valid_hgt(val):
    if 'cm' in val:
        hgt = int(val.split('cm')[0])
        if hgt < 150 or hgt > 193:
            return 0
        return 1
    
    elif 'in' in val:
        hgt = int(val.split('in')[0])
        if hgt < 59 or hgt > 76:
            return 0
        return 1
    
    else:
        return 0

def valid_hcl(val):
    if val[0] != '#' or len(val) !=7:
        return 0
    for value in val[1:]:
        if not((value >= '0' and value <= '9') or (value >='a' and value <='f')):
            return 0
    return 1

def validecl(val):
    if val in valid_ecl:
        return 1
    return 0

def valid_pid(val):
    if len(val) != 9:
        return 0
    for i in val:
        if i < '0' or i > '9':
            return 0
    return 1
def validate_1(passport):
    for key in valid_set:
        if not(key in passport):
            return 0
    return 1

def validate_2(passport):
    
    for key in valid_set:
        if not (key in passport):
            return 0
        if (key == 'byr' and not(valid_byr(int(passport[key]))) or
            key == 'iyr' and not(valid_iyr(int(passport[key]))) or
            key == 'eyr' and not(valid_eyr(int(passport[key]))) or
            key == 'hgt' and not(valid_hgt(passport[key])) or
            key == 'hcl' and not(valid_hcl(passport[key])) or
            key == 'ecl' and not(validecl(passport[key])) or
            key == 'pid' and not(valid_pid(passport[key]))):
            return 0
        
    return 1
            
            

#Day - 4, Part 2
ans1 = 0
ans2 = 0
passport = {}
for line in lines:
    if line == "\n":
        ans1 = ans1 + validate_1(passport)
        ans2 = ans2 + validate_2(passport)
        passport = {}
    else:
        i = line.split(' ')
        for s in i:
            k = s.split(':')
            passport[k[0]] = k[1].split('\n')[0]

if passport != {}:
    ans1 = ans1 + validate_1(passport)
    ans2 = ans2 + validate_2(passport)

print("Part-1: ",ans1)
print("Part-2: ",ans2)




        
