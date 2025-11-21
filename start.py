from tools import requestNumber
import random
import math

def getN(text, onlyPositive = False):
  while True:
    inp = input(f'{text} ')

    try:
      num = int(inp)
      if onlyPositive and num <=0:
        print('This time  I expect tot se only positive numbers. Try one more time')
        continue

      return num
    except ValueError:
      print(f'You should provide a number. {inp} is not a number')

# print(math.pi)

def getCircleArea(r):
  return math.pi * (r * r)

def getCircleLength(r):
  return 2 * math.pi * r

def circleCounter():
  rad = requestNumber('Provide the length of the radius', True)
  print(f' The area is {getCircleArea(rad)}')
  print(f' The length of te circle is {getCircleArea(rad)}')

# circleCounter()


def frunc():
  stopWord = 'stop'

  print('Provide a number in order to process this number')
  print(f'or provide the stop word: \'{stopWord}\'')

  while True:
    inp = input('What is the next ')

    if inp == stopWord:
      return
    
    try:
      num = int(inp)

      if num > 20:
        print(f'Square root of {num} is {math.sqrt(num)}')
      else:
        print(f'The square of {num} is {pow(num , 2)}')

    except ValueError:
      print(f'In order to operate with the value I need a number. {inp} is not a number')

# frunc()

def add(num1, num2):
  return num1 + num2

def substraction(minuend, subtrahend):
  return minuend - subtrahend

def multiplication(num1, num2):
  return num1 * num2

# print(add(2,3))
# print(add(5,6))

def getTriangleArea(base, hight):
  return base * hight / 2

# print(getTriangleArea(5, 7))

def getRadius():
  return getN('Provide radius', True)

def getCircleArea(radius):
  return math.pi * pow(radius, 2)

# print(getCircleArea(getRadius()))

# 10. Skapa en rekursiv funktion fakultet(n) som beräknar n!.

def factorial(n):
  if n < 1:
    raise ValueError('It is not possible to count factorial of a not positive number')

  if n == 1:
    return 1
  
  return n * factorial(n-1)

print(factorial(3))