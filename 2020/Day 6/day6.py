lines = open('input.txt','r').readlines()

count1 = 0
count2 = 0
ques = {}
person = 0
for line in lines:
    if line == '\n':
        count1 += len(ques)
        for key, val in ques.items():
            if val == person:
                count2 += 1
        ques = {}
        person = 0
    else:
        person = person + 1
        questions = list(line.strip('\n'))
        for question in questions:
            if question not in ques:
                ques[question] = 1
            else:
                ques[question] = ques[question] + 1
count1+= len(ques)
for key, val in ques.items():
    if val == person:
        count2 += 1
print("Puzzle 1: ", count1)
print("Puzzle 2: ", count2)
