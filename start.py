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

  

  
