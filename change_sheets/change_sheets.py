import random
import time


N = int(input('Enter number of students: '))
students = list(range(1, N+1))

random.shuffle(students)
for i, student in enumerate(students):
    if i % 7 == 0:
        print()

    print("{0:3d}|".format(student), end='', flush = True)
    time.sleep(random.random())

print()
