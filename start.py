arr = ['Ford', 'Volvo', 'BMW']

# print(arr)
# print(type(arr))
# print(type(arr) == list)
# print(len(arr))

# arr[2] = 'Saab'
# arr.insert(10, 'Random car')
# # arr.remove('Saab')
# print(arr)

# print(arr.pop(2))
# print(arr)

# arr.extend('abc')
# arr.extend(['x', 'y', 'z'])
# print(arr)

# # print(max(arr))
# # print(sum(arr))

# print(arr.remove('a'))
# print(arr)

# cities = [
#   'Stockholm', 'Sundsvall', "Göteborg"
# ]
# cities.append('Motala')
# cities.insert(2, 'Västerås')
# cities.pop(0)
# cities.remove('Motala')
# cities[cities.index('Västerås')] = 'Eskilstuna'
# cities.clear()

# print(cities)

# arr = ['Orange', 'Apple', 'Banana']

# def findEl(el, arr):
#   for e in arr:
#     if e == el:
#       return f'{el} is exist'
#   return f'{el} not exist'
  
# print(findEl('Orange', arr))



# subjects = [
#   'matte', 'datorteknik', "nätverksteknik"
# ]

# print(1, len(subjects))

# subjects.append('programmering')
# print(2, subjects)

# subjects.insert(1, 'natverksteknologier')
# print(3, subjects)

# subjects.pop(2)
# print(4, subjects)

# subjects.remove('matte')
# print(5, subjects)

# print(6)
# for i in subjects:
#   print(i)

# subjects.clear()
# print(7, subjects)




# def kassa(): 
#   products = []
#   while True:
#     next = input('What is the nex product? ')

#     try:
#       num = int(next)
#       if num == 0:
#           print(f'The amount of products is {len(products)}')
#           return
#       print(f'{num} is not a correct product. It is not accepted.')
#     except ValueError:
#        products.append(next)

# kassa()

import random
from tools import requestNumber

def guessNumber():
  secret = random.randint(1, 100)
  print('I have a secret number in range from 1 to 100.')

  while True:
    input = requestNumber('Guess the number', True)

    if input == secret:
      print(f'Correct the secret number equals {input}')
      break
    else:
      comparison = 'more' if input > secret else 'less'
      print(f'{input} is not a correct, it is {comparison} than the secret number')

# guessNumber()

adj = ['red', 'big', 'tasty']
friuts = ['apple', 'banana', 'cherry']

# for prop in adj:
#   for frut in friuts:
#     print(f'{prop} {frut}')

numbers = [1,2,3]

print(f'{'present' if 2 in numbers else 'is not present'}')

