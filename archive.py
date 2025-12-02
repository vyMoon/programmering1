# while True:
#   stopWord = 'stop'
#   text = input(f'Write smth in order to repeat it, or write {stopWord} to stop the programme.')

#   if text != stopWord:
#     print('The programme is stopped')
#     break

#   print(text)


# text = 'jensens'
# sCount = 0
# for i in range(0, len(text)):
  
#   if (text[i] == 's'):
#     sCount += 1

# print(sCount)


# i  = 0 
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# def vowelCounter():
#   vowels = ['a', 'i', 'e', 'o', 'u', 'y', 'å', 'ö', 'ä']
#   text = input('write a text in order to count vowels')
#   vowelCounter = 0

#   for text in text:
#     print(text)
#   #   if text[i].lower() in vowels:
#   #     vowelCounter += 1
#   # print(vowelCounter)
#   print(text)

# vowelCounter()

# it = 'string'.__iter__()
# print(it.__repr__())


# while it.__length_hint__():
#   print(it.__length_hint__())
#   print('next', it.__next__())
#   print(it.__length_hint__())
# print('the string is over')




def requestPass():
  pas = 'python123'

  while True:
    inpt = input('write the password ')

    if inpt == pas:
      print('You have the access')
      break

    print('password is incorrect')

# requestPass()

from tools import requestNumber

def gasConsum():
  distance = requestNumber('How many kilometers have you driven', True)
  gasConsummation = requestNumber('HOw much gas have been used', True)

  consummationPerMil = round((gasConsummation / distance) * 10, 2 )
  print(consummationPerMil)
  if consummationPerMil > 1:
    print('Bilen drar mycket bränsle')
  else:
    print('Bra bränsleekonomi')


# gasConsum()

def speedComparison():
  maxSpeed = requestNumber('What is allowed speed?', True)
  speed = requestNumber('What is your speed', True)
  diff = speed - maxSpeed

  if diff > 0 :
    print('Du kör för fort!')
    if diff >= 30:
      print('Du riskerar böte!')
  else:
    print('Du hller hastighetsgränsen')

# speedComparison()


from tools import requestNumber
import random

# arr = ['Ford', 'Volvo', 'BMW']

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

# numbers = [1,2,3]

# print(f'{'number found in the list' if 24 in numbers else 'number does not exist in the list'}')

# users = ['user1', 'user2', 'user3', 'user4', 'user5']

# def findUserIndex(user):
#   for i in range(len(users)):
#     if users[i] == user:
#       return i
#   return False
    

# index = findUserIndex('user1')


# for user in users:
#   if  index:
#     if user == users[index]:
#       continue
#   print(user)

menu = {
  'add': 1,
  'remove': 2,
  'stop': 3
}

def choseAction(menu):
  availableOptions = []
  for key, value in menu.items():
    print(f'{key} - {value}')
    availableOptions.append(value)
  while True:
    chosen = requestNumber('Which action, you chose. chose a number above', True)
    if chosen in availableOptions:
      return chosen
    else:
      print(f'Option {chosen} does not exist, try again')

def append(arr):
  arr.append(
    input('What should I add? ')
  )

def remove(arr):
  if len(arr) == 0:
    print('In the list there is nothing')
    return
  
  while True:
    el = input('what should I remove? ')
    if el in arr:
      arr.remove(el)
      print(f'{el} removed')
      return
    else:
      print(f'{el} does not exist in list, try again')

def listEditor():
  arr = []
  while True:
    chosen = choseAction(menu)
    print(chosen)

    if chosen == menu['add']:
      append(arr)
    elif chosen == menu['remove']:
      remove(arr)
    elif chosen == menu['stop']:
      return
    
    print(arr)
# listEditor()

# name = input('Provide your name ')
# surname = input('Provide your surname ')

# for i in range(20):
#   if i < 15:
#     print(name)
#   print(surname)

# cities = ['Stockholm', 'Sundsvall', 'Göteborg']

# cities.append('Motala')
# print(1, cities)

# vesterosIndex = 2
# cities.insert(vesterosIndex, 'Vestrås')
# print(2, cities)

# cities.pop(0)
# print(3, cities)

# cities.remove('Motala')
# print(4, cities)

# cities.clear()
# print(1, cities)
# print(len(cities))


fruits = ['Apple', 'Orange', 'Banana']

def checkEl(el, arr):
  for e in arr:
    if e == el:
      print(f'{el} exist in listan')
      return
  print(f'{el} does not exist')

# checkEl('Apple', fruits)

def getIndex(el, arr):
  for i in range(len(arr)):
    if el == arr[i]:
      return i
  return False

def removeListEl(el, arr):
  index = getIndex(el, arr)
  if not(index is False):
    arr.remove(el)
  print(f'Error, there is no {el} in the list')


# subjects = ['matte', 'datortecnik', 'nätverksteknik']

# print(1, len(subjects))

# subjects.append('programmering')
# print(2, subjects)

# subjects.insert(1, 'natverksteknologier')
# print(3, subjects)

# subjects.pop(2)
# print(4, subjects)

# elToRemove = 'matte'
# removeListEl(elToRemove, subjects)
# print(5, subjects)

# print(5)
# for i in range(len(subjects)):
#   print(subjects[i])

# subjects.clear()
# print(6, subjects, f'Subject\'s length is s{len(subjects)}')

# arr = [1,2,3,4,5,6]

# print(arr[3:5])



# def vowelCounter(word):
#   vowel = 'aeiouyåöä'
#   counter = 0
#   for letter in word.lower():
#     if letter in vowel:
#       counter += 1
  
#   return counter

# print(vowelCounter('realisationsvinstbeskattning'))

# Hitta det största talet
# Facit: Byt `>` till `<` för att hitta det minsta talet.

def getBiggest(arr):
  if len(arr) == 0:
    raise ValueError('The list is empty')
  
  if len(arr) == 1:
    return arr [0]

  res = arr[0]

  for index in range(1, len(arr)):
    if arr[index] > res:
      res = arr[index]
  
  return res
  
def getSmallest(arr):
  if len(arr) == 0:
    raise ValueError('The list is empty')
  
  if len(arr) == 1:
    return arr [0]
  
  res = arr[0]

  for index in range(1, len(arr)):
    if res > arr[index]:
      res = arr[index]
  return res

tal = [-40, 9, -1, 7, 3, 10]

# print("Det största talet är:", getBiggest(tal))
# print('The smallest is ', getSmallest(tal))

num = [1, 5, -29, 86, 7, -8]

# print(1, min(num))
# print(2, max(num))
# print(3, sum(num))
# newArr = num[:]
# print(4, newArr)


from tools import requestNumber
import random
import math

def getNumber(text, onlyPositive = False):
  while True:
    inp = input(f'{text} ')

    try:
      num = int(inp)

      if onlyPositive and num <= 0:
        print('This time I expect tot se only positive numbers. Try one more time')
        continue

      return num
    
    except ValueError:
      print(f'You should provide a number. {inp} is not a number')
      continue


def getWeekdayName(index):
  weekDays = ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lördag', 'Söndag']
  
  return weekDays[index]


def tvWatchCounter():
  time = 0
  
  for index in range(7):
    while True:
      minuter = getNumber(f'Hur många minuter har du tittatt TV på {getWeekdayName(index)}')

      if minuter < 0:
        print('Antal minuter måste vara mer eller lika med 0 ')
        continue

      time += minuter
      break

  return round(time / 60)

# print(tvWatchCounter())

def getAudience():
  amount = getNumber('Hur Många manniskor är i gruppen?', True)

  group = []

  for i in range(amount):
    group.append(
      input(f'Vad hetter {i + 1} person')
    )
  
  return group

def printStudents(message, people):
  print(message)

  for person in people:
    print(person)


def attendanceAccounting():
  yes = 'ja'
  no = 'nej'
  group = getAudience()
  present = []
  absent = []

  for person in group:
    while True:
      presence = input(f'Har {person} varit med? (ja/nej)')
      
      if presence == yes:
        present.append(person)
        break
      elif presence == no:
        absent.append(person)
        break
      else:
        print('Du kan svara bara ja eller nej. Försök igen')
        continue

  printStudents('De som har varit med ör:', present)
  printStudents('De som inte har varit med ör:', absent)

  
# attendanceAccounting()

def evenNumber(n):
  return n / 2

def oddNumber(n):
  return n * 3 + 1

def collatzSequence(number):
  # number = getNumber('Provide a number', True)
  steps = 0

  while number != 1:
    if number % 2 == 0:
      number = evenNumber(number)
    else:
      number = oddNumber(number)
    steps += 1
  
  return steps

# print(collatzSequence(15708356))

def сontrolPin():
  pin = "1234"
  for i in range(3):
    inp = input('Provide pin (digits only)')
    if pin == inp:
      print('Opened')
      return i + 1
  print('Closed')
  return False


# number = 1

# while number <= 10:
#   print(number)
#   number += 1
# print('stop')

# n = 5

# while n >= 1:
#   print(n)
#   n -= 1
# print('stop')

def pn(message = 'Provide a number', onlyPositive = False):
  while True:
    inp = input(f'{message} ')

    try:
      num = int(inp)

      if onlyPositive and num < 1:
        print('This time i need a positive number. Try one more time')
        continue

      return num
    except:
      print(f'I need a number. {inp} is not a number. Try one more time')
      continue


def guessNumber():
  secret = random.randint(1, 100)
  print('Guess the number in range from 1 to 100')

  while True:
    n = pn('Guess the number', True)

    if secret == n:
      print("Correct")
      return
    elif secret > n:
      print('secret number is more than your guess')
    elif secret < n:
      print('secret number is less than your guess')
    
    print('Try one more time')


# guessNumber()

def isPositive():
  number = pn('Provide a number')
  
  if number == 0:
    return 0
  elif number > 0:
    return True
  
  return False

# print(isPositive())

def countPositiveNumbers():
  sum = 0

  while True:
    number = pn()

    if number == 0:
      return sum
    
    if number > 0:
      sum += number

# print(countPositiveNumbers())

def getGroupsGrades(amount):
  grades = []
  for i in range(1, amount + 1):
    message = f'What grade has student {i}'
    grades.append(pn(message, True))
  return grades

def countAverageGrade():
  amount = pn('How many students in the group?', True)
  grades = getGroupsGrades(amount)

  return sum(grades) / len(grades)

# print(countAverageGrade())

days = ['Monday', 'Tuesday', 'Wednesday ', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def printMaxTemperature(temperature):
  maximum = max(temperature)
  day = days[temperature.index(maximum)]

  print(f'Tha max temperature ({maximum} was on {day})')

def printMinTemperature(temperature):
  minimum = min(temperature)
  day = days[temperature.index(minimum)]

  print(f'Tha max temperature ({minimum} was on {day})')

def printAverageTemp(temperature):
  print(f"Average temperature is {sum(temperature) / len(temperature)}")

def TemperatureReport():
  temperature = []

  for day in days:
    temperature.append(
      pn(f'What temperature wa on {day}?')
    )

  printAverageTemp(temperature)
  printMaxTemperature(temperature)
  printMinTemperature(temperature)

TemperatureReport()

  

  
