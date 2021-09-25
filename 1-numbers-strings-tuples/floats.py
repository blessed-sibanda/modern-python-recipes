import math 
import cmath

answer = (19/155) * (155/19)
print(answer)

print(round(answer, 3))

error = 1 - answer
print(error)

print(answer == 1.0)

print('is answer nearly equal to 1')
print(math.isclose(answer, 1))

print('Square root of negative 2 =', cmath.sqrt(-2))