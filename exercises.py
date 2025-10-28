def isPositiveNumber(n):
  return n > 0

def requestNumber(text = 'give me a number', onlyPositive = False):
  while True:
    n = input(f'{text} ')

    try:
      n = int(n)

      if onlyPositive and not isPositiveNumber(n):
        print(f'{n} less or equal 0, this time I need a positive number')
        continue

      return n
    except ValueError:
      print(f'I expect to have a number! {n} is not a number.')

# 1. Räkna uppåt
# Be användaren om ett tal och skriv ut alla tal från 1 upp till det talet

def countUp():
  n = requestNumber('I need a number in order to count from 1 to this number', True)

  for i in range(1, n + 1):
    print(i)

# countUp()

# 2. Multiplikationstabell
# Be användaren om ett tal och visa multiplikationstabellen för det talet (1–10).

def printMultiplicationTable():
  a = requestNumber('Give me a number in order tov print a multiplication table for this number')

  for n in range(1, 11):
    print(f'{n} x {a} = {n * a}')

# printMultiplicationTable()

# 3. Upprepa en text
# Be användaren om en text och ett antal gånger. Skriv ut texten så många gånger.

def repeatText():
  text = input('Give me a text which I can repeat ')
  n = requestNumber('Give me the number of repetition', True)

  for i in range(1, n + 1):
    print(text)

# repeatText()

# 4. Summera tal
# Be användaren skriva hur många tal som ska adderas. Ta in varje tal och skriv ut summan

def getOrdinalNumber(num):
  lastDigit = int(str(num)[-1])
  postfix = ''

  match lastDigit:
    case 1:
      postfix = 'st'
    case 2:
      postfix = 'nd'
    case 3:
      postfix = 'rd'
    case _:
      postfix = 'th'
    
  return f'{num}{postfix}'

def getSetNumbers(amount):
  numbers = []

  for i in range(amount):
    numbers.append(
      requestNumber(f'Give me the {getOrdinalNumber(i + 1)} number')
    )
  
  return numbers

def sumArray(numbers):
  sum = 0
  for i in numbers:
    sum += i
  return sum

def sumNumbers():
  amount = requestNumber('Give me how many number would you like to add up', True)
  numbers = getSetNumbers(amount)
  sum = sumArray(numbers)

  print(f'The sum of the numbers is {sum}')
  return sum


# sumNumbers()

# Beräkna medelvärde
# Be användaren skriva in flera tal och räkna ut medelvärdet.

def getAverageValue():
  amount = requestNumber('Of how many numbers I should count average value', True)
  numbers = getSetNumbers(amount)
  sum = sumArray(numbers)
  average = sum / amount

  print(f'The average value of the numbers is {average}')

# getAverageValue()

# 6. Rita en triangel
# Be användaren om en höjd och rita en triangel med stjärnor (*).

def createTriangleLine(num,):
  line = ''
  for i in range(num):
    line += '* '

  return line + '\n'

def printTriangle():
  space = ' '
  height = requestNumber('How high triangle should I print', True)
  triangle = ''

  for i in range(1, height + 1):
    triangle += f'{space * (height - i)}{createTriangleLine(i)}'
  
  print(triangle)

# printTriangle()

# 7. Räkna ner
# Be användaren om ett startvärde och räkna ner till 0.
def countDown():
  n = requestNumber('I need a number in order to count down from the number to 0', True)

  for i in range(n + 1):
    print(n - i)

# countDown()


import random

n = random.randint(1, 10)  # includes both 1 and 10
print(n)

def guessNumber():
  secretNumber = random.randint(1, 1000)
  print('I have a secret number in the range from 1 to 1000.')

  while True:
    guess = requestNumber('Guess the number', True)

    if secretNumber == guess:
      print(f'Correct, the number is {guess}')
      return
    
    comparison = 'less' if secretNumber > guess else 'more'

    print(f'{guess} is {comparison} than the number')

# guessNumber()

def guessNumber2():
  secretNumber = random.randint(1, 10)
  attempt = requestNumber('I have a secret number in range from 1 to 10. How many attempt do you need to guess the number?')

  for i in range(attempt):
    guess = requestNumber('Guess the number!')

    if guess == secretNumber:
      print(f'Correct the number is {guess}')
      return
    
    print(f'Incorrect! You have {attempt - (i + 1)} attempts')

  print('Game over you have not guessed')

# guessNumber2()
