import random

rolls = []
count_6 = 0
count_1 = 0
count_double_6 = 0

for i in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)
    if roll == 6:
        count_6 += 1
    if roll == 1:
        count_1 += 1
    if i > 0 and rolls[i] == 6 and rolls[i-1] == 6:
        count_double_6 += 1

print("Rolls:", rolls)
print("Number of times 6 was rolled:", count_6)
print("Number of times 1 was rolled:", count_1)
print("Number of times two 6s in a row were rolled:", count_double_6)
