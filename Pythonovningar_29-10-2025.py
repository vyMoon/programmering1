import random
from tools import requestNumber
from tools import getOrdinalNumber
from tools import getSetNumbers
from tools import getOperatorCalc
from tools import getCalcResult

# Beskrivning: Skriv ett program som ber användaren ange ett startvärde och ett slutvärde.
# Programmet ska skriva ut alla jämna tal mellan dessa värden (inklusive gränserna om de är
# jämna).

def printEven():
  start = requestNumber('Give start value')
  end = requestNumber('Give end value')

  for i in range(start, end + 1):
    if i % 2 == 0:
      print(i)

# printEven()

# Beskrivning: Skapa ett gissningsspel där programmet har ett förutbestämt hemligt tal.
# Användaren får tre försök att gissa talet. Programmet berättar om gissningen var korrekt.
# Instruktioner: Använd en for-loop som itererar tre gånger, läs in användarens gissning och jämför
# med hemligt tal. Avsluta tidigt om användaren gissar rätt.

def guessNumber3():
  secret = random.randint(1, 10)
  print('I have a number in range from 1 to 10. You have 3 attempt to guess it')

  for i in range(3):
    guess = requestNumber(f'Guess the number. The {getOrdinalNumber(i + 1)} attempt')

    if guess == secret:
      print(f'Correct! the secret number is {guess}'),
      return
    else:
      if i != 2:
        print('IT is not correct. Try one more time')
  
  print('This was the last attempt. You have not guesses')

# guessNumber3()

# Beskrivning: Skriv ett program som frågar användaren att mata in fem tal, ett i taget. Programmet
# ska räkna och skriva ut hur många av talen som är positiva (>0), negativa (<0) och noll.
# Instruktioner: Använd en for-loop som körs fem gånger och if/elif/else för att klassificera varje tal.

def numberTypesCounter():
  print('I need 5 numbers in order to count negative numbers, positive number and 0')

  nums = getSetNumbers(5)
  amount0 = 0
  amountNegative = 0
  amountPositive = 0

  for i in nums:
    print(i > 0, i < 0,)
    if i > 0:
      amountPositive += 1
    elif i < 0:
      amountNegative +=1
    else:
      amount0 += 1

  print(f'Amount positive numbers is {amountPositive}')
  print(f'Amount zeros is {amount0}')
  print(f'Amount neNegative numbers is {amountNegative}')

# numberTypesCounter()

# Beskrivning: Skapa ett program som frågar användaren om två tal och en operator (låtsas att
# operatorn väljs som en av '+', '-', '*', '/'). Programmet ska skriva ut resultatet av operationen.
# Instruktioner: Hantera division med noll genom att ge ett felmeddelande. Använd if/elif/else för att
# välja operation.

def calculator():
  num1 = requestNumber('Give the fist number')
  operator = getOperatorCalc()
  num2 = requestNumber('Give the second number')

  if operator == '/' and num2 == 0:
    print('You are going to divide by 0, which is forbidden')
    return
  
  result = getCalcResult(num1, num2, operator)

  if type(result) == int or type(result) == float:
    print(f'The result is {result}')
  else:
    print('Error: unknown operator')

# calculator()

# Beskrivning: Skriv ett program som ber användaren ange ett lösenord. Om lösenordet matchar
# det förväntade, skriv ut 'Åtkomst beviljad!'. Användaren får tre försök innan programmet avslår.
# Instruktioner: Använd en for-loop med tre iterationer och break för att avsluta om korrekt lösen
# anges.

def autenthification():
  pas = '1234'
  amountAttempts = 3
  print('Provide password, You have 3 attempts')

  for i in range(amountAttempts):
    candidate = input(f'Provide tha password. The {getOrdinalNumber(i + 1)} attempt ')
    if candidate == pas:
      print('The password is correct. You have an access')
      return
    elif amountAttempts == i + 1:
      break
    else:
      print('Provided password is incorrect')
  
  print('You have spent your last attempt. Access denied')

# autenthification()

#   Beskrivning: Skriv ett program som går igenom talen 1–50. För varje tal, skriv ut 'Fizz' om talet är
# delbart med 3, 'Buzz' om det är delbart med 5, och 'FizzBuzz' om det är delbart med både 3 och
# 5. Annars skriv ut talet. Instruktioner: Använd modulus-operatorn (%) och if/elif/else i rätt ordning (kontrollera både 3 och 5 först).

def fizzBuzz():
  fizz = 'Fizz'
  buzz = 'Buzz'

  for i in range(1, 51):
    text = ''
    if i % 3 == 0:
      text += fizz
    if i % 5 == 0:
      text += buzz
    if text == '':
      text = i
    
    print(text)

# fizzBuzz()

# Beskrivning: Låt användaren ange ett startvärde och ett slutvärde. Programmet ska beräkna
# summan av alla udda tal i intervallet (inklusive gränserna om de är udda) och skriva ut summan.
# Instruktioner: Iterera med range() och kontrollera udda tal med %2 != 0.

def oddSumm():
  start = 0
  end = 0
  sum = 0

  while True:
    start = requestNumber('provide the strat value')
    end = requestNumber('Provide end value')

    if end <= start:
      print('Strart value should be lower and not equal end value. Try  again')
      continue

    break

  for i in range(start, end + 1):
    if i % 2 != 0:
      sum += i
  
  print(f'The summ of all odd numbers between {start} and {end} = {sum}')

# oddSumm()

# Beskrivning: Skriv ett program som läser in ett poängtal mellan 0 och 100 och omvandlar det till
# ett betyg enligt skalan A–F:
# 90–100:A, 80–89:B, 70–79:C, 60–69:D, 50–59:E, 0–49:F.
# Instruktioner: Hantera ogiltiga poäng (exempelvis under 0 eller över 100) med ett felmeddelande.

def getGrade(points):
  if points < 50:
    return 'F'
  elif 49 < points < 60:
    return 'E'
  elif 59 < points < 70:
    return "D"
  elif 69 < points < 80:
    return "c"
  elif  79 < points < 90:
    return "B"
  elif 89 < points <=100:
    return "A"
  
  return False

def gradeCounter():
  points = 0

  while True:
    pointsCandidate = requestNumber('How much pointss have you got? (in range between 0 and 100)')
    print(pointsCandidate > 100)
    if 0 > pointsCandidate or pointsCandidate > 100:
      print('Possible amount of points should be between 0 and 100. Try again')
      continue

    points = pointsCandidate
    print (points)
    break

  grade = getGrade(points)

  if grade:
    print(f'Grade is {grade}')
  else:
    print('Error. Incorrect amount of points')

# gradeCounter()

# Beskrivning: Skapa ett program som visar en meny med tre alternativ (Hälsa, Räkna till 10,
# Avsluta). Programmet ska utföra vald funktion.
# Instruktioner: Läs in användarens val och använd if/elif/else för att välja rätt åtgärd.

def printMenu(menu):
  print('Menu options')
  for key, value in menu.items():
    print(f'{key} - {value}')

def getMenuName(menu, chosen):
  for key, value in menu.items():
    if value == chosen:
      return key
  return ''

def choseMenuOption(menu):
  printMenu(menu)

  while True:
    chosenCandidate = requestNumber('Chose a menu option')

    if chosenCandidate in menu.values():
      return chosenCandidate
    else:
      print('You can chose only from menu options')
      printMenu(menu)

def countTo10():
  for i in range(1, 11):
    print(i)

def greeting():
  name = input('Who should I greet? ')

  print(f'Hi, {name}!')

def menu():
  menu = {
    'greetirng': 1,
    'count from 1 to 10': 2, 
    'close': 3
  }

  while True:
    chosen = choseMenuOption(menu)

    print(f'You have chosen option number {chosen}, whic is {getMenuName(menu, chosen)}')

    if chosen == menu['greetirng']:
      greeting()
    elif chosen == menu['count from 1 to 10']:
      countTo10()
    elif chosen == menu['close']:
      print('The end of the prgramme')
      return

# menu()

# Beskrivning: Skriv ett program som ber användaren ange tre tal. Programmet ska bestämma och
# skriva ut vilket tal som är störst.

def getNumString(nums):
  text = ''

  for i in nums:
    add =''
    if text == '':
      text += f'{i}'
    else:
      text += f', {i}'

def biggestNumber():
  nums = getSetNumbers(3)
  biggest = None

  for i in nums:
    if biggest == None or biggest < i:
      biggest = i

  print(f'{biggest} is the biggest value out of {getNumString(nums)}')

# biggestNumber()

# Beskrivning: Skriv ett program som läser in ett ord och räknar antalet vokaler (a, e, i, o, u, y, å, ä, ö)
#. Programmet ska skriva ut hur många vokaler ordet innehåller.

def countVovwels():
  vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']
  word = input('Give me a word in order to count vovewl ')
  amountVovwels = 0

  for i in range(len(word)):
    if word[i].lower() in vowels:
      amountVovwels += 1
  
  print(f'Word \'{word}\' contains {amountVovwels} vowels')

# countVovwels()
