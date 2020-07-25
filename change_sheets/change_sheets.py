import random
import time


N = int(input('Enter number of students: '))
students = list(range(1, N+1))

random.shuffle(students)

for i in range(len(students)):
    if i % 7 == 1 and i != 1:
        print("")
    print("  " + str(students[i]) + " |", end='', flush = True)
    time.sleep(1)

