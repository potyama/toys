import random
import time


N = int(input('Enter number of students: '))
students = list(range(1, N+1))

random.shuffle(students)

for i, student in enumerate(students):
    if i % 7 == 0 and i != 0:
        print()
    print(" {} |".format(student), end='', flush = True)
    time.sleep(0.1)

